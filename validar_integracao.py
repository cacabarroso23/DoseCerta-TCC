"""Checagens estáticas, não substitui compilação pdfLaTeX ou aceite físico."""
from pathlib import Path
import re,json,collections,csv,statistics
from PIL import Image
R=Path(__file__).resolve().parent
errors=[];warnings=[];labels={};refs=[];images=[];includes=[];cites=set();pending=[]
def clean(s):
 s=re.sub(r'(\\(?:no)?(?:link)?url\{)([^}]*)(\})',lambda m:m[0].replace('%','PERCENT'),s)
 return re.sub(r'(?<!\\)%[^\n]*','',s)
def unescaped(s,i):
 n=0;i-=1
 while i>=0 and s[i]=='\\':n+=1;i-=1
 return n%2==0
files=[R/'main.tex',R/'FEI-pre-textual.tex'];seen=set()
while files:
 p=files.pop()
 if p in seen:continue
 seen.add(p)
 if not p.exists():errors.append('Arquivo ausente: '+str(p));continue
 s=clean(p.read_text());depth=0
 for i,c in enumerate(s):
  if c in '{} ' and c!=' ' and unescaped(s,i):
   depth+=1 if c=='{' else -1
   if depth<0:errors.append(str(p.relative_to(R))+': chave fechada sem abertura');break
 if depth:errors.append(str(p.relative_to(R))+': balanço de chaves '+str(depth))
 stack=[]
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
  kind,env=m.groups()
  if kind=='begin':stack.append(env)
  elif not stack or stack.pop()!=env:errors.append(str(p.relative_to(R))+': ambiente divergente '+env)
 if stack:errors.append(str(p.relative_to(R))+': ambientes abertos '+str(stack))
 for name in re.findall(r'\\(?:input|include)\{([^}]+)\}',s):
  q=R/(name if Path(name).suffix else name+'.tex');includes.append(str(q.relative_to(R)));files.append(q)
 for lab in re.findall(r'\\label\{([^}]+)\}',s):
  if lab in labels:errors.append('Rótulo duplicado: '+lab)
  labels[lab]=str(p.relative_to(R))
 refs += [(r,str(p.relative_to(R))) for r in re.findall(r'\\(?:ref|pageref|eqref|autoref)\{([^}]+)\}',s)]
 for group in re.findall(r'\\cite\w*\*?(?:\[[^]]*\])*\{([^}]+)\}',s):cites.update(x.strip() for x in group.split(','))
 for im in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',s):
  q=R/im
  if not q.exists():errors.append('Figura ausente: '+im)
  else:
   try:
    with Image.open(q) as f:f.verify()
   except Exception as e:errors.append('Figura inválida: '+im+' '+str(e))
  images.append(im)
 for m in re.finditer(r'\\pendencia\{([^}]+)\}\{',s):
  i=m.end();j=i;d=1
  while j<len(s) and d:
   if s[j]=='{' and unescaped(s,j):d+=1
   if s[j]=='}' and unescaped(s,j):d-=1
   j+=1
  pending.append({'id':m[1],'arquivo':str(p.relative_to(R)),'texto':s[i:j-1]})
for lab,f in refs:
 if lab not in labels:errors.append('Referência sem rótulo: '+lab+' em '+f)
counts=collections.Counter(p['id'] for p in pending)
for id,n in counts.items():
 if n>1:errors.append('ID de pendência duplicado: '+id)
bib=(R/'FEI-bib/dosecerta-referencias.bib').read_text();keys=re.findall(r'@\w+\s*\{\s*([^,]+),',bib)
for k,n in collections.Counter(keys).items():
 if n>1:errors.append('Chave bibliográfica duplicada: '+k)
rendered=set(re.findall(r'\\bibitem(?:\[[^\n]*\])?\{([^}]+)\}',(R/'referencias.tex').read_text()))
for k in sorted(cites):
 if k not in keys:errors.append('Citação sem entrada na base: '+k)
 if k not in rendered:errors.append('Citação sem entrada gerada: '+k)
# Check independent source counts and arithmetic.
B=R/'Dados/validacao_20261126'
def csvrows(n):return list(csv.DictReader((B/n).open(encoding='utf-8-sig'),delimiter=';'))
cal=csvrows('calibracoes_do_disco.csv');intervals=[int(x) for r in cal for x in r['intervalos_fases'].split()]
assert len(intervals)==15 and all(sum(map(int,r['intervalos_fases'].split()))==4096 for r in cal)
cy=csvrows('dispensacao_ciclos_por_bolso.csv');assert len(cy)==12
co=collections.Counter(r['resultado_do_ciclo'] for r in cy);assert sorted(co.values())==[2,2,4,4]
ss=csvrows('sessoes_do_disco.csv');sim=[r for r in ss if r['acao']=='simulate_quantity'];assert len(ss)==101 and len(sim)==15
old=R/'historico_pendencias_pre_integracao.json'
if old.exists():
 baseline=json.loads(old.read_text());oldids={x['id'] for x in baseline};newids=set(counts)
 for id in sorted(oldids-newids):errors.append('Pendência anterior desapareceu sem baixa: '+id)
# Every requirement ID in the source must have exactly one evidence-matrix row.
requirements=(R/'Capitulos/05_requisitos.tex').read_text()
matrix=(R/'PosTextual/apendices.tex').read_text()
reqids=set(re.findall(r'^(R(?:F|NF)\d+(?:-[A-Z]+)?) &',requirements,re.M))
matrixids=re.findall(r'^(R(?:F|NF)\d+(?:-[A-Z]+)?) &',matrix,re.M)
if reqids!=set(matrixids) or len(matrixids)!=len(set(matrixids)):
 errors.append('Matriz de evidência divergente dos requisitos originais')
photos=json.loads((R/'mapa_fotos_20261126.json').read_text())
photo_names=[x['foto'] for group in photos.values() for x in group]
if len(photo_names)!=35 or len(set(photo_names))!=35: errors.append('Mapa fotográfico sem as 35 imagens únicas')
summary={'arquivos_tex_incluidos':len(seen),'rotulos':len(labels),'referencias_internas':len(refs),'figuras':len(images),'citacoes_distintas':len(cites),'pendencias':len(pending),'erros':errors,'avisos':warnings,'compilacao_pdf':'NAO_EXECUTADA_COMPILADOR_INDISPONIVEL','calibracao_media':statistics.mean(intervals),'calibracao_desvio_amostral':statistics.stdev(intervals),'ciclos_por_resultado':dict(co)}
(R/'pendencias.json').write_text(json.dumps(sorted(pending,key=lambda x:x['arquivo']),ensure_ascii=False,indent=2)+'\n')
(R/'validacao_estatica.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
