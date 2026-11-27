"""Compila main.tex repetidamente e bloqueia entrega com referências/listas inconsistentes.
Requer Python 3 e TeX Live/MiKTeX com pdfLaTeX. Não instala programas.
"""
from pathlib import Path
import hashlib,json,re,shutil,subprocess,sys
P=Path(__file__).resolve().parent

def problemas(log,folder):
 errors=[];notes=[]
 for pat,msg in [
  (r'(?m)^!|Fatal error occurred|Emergency stop','Erro fatal do LaTeX'),
  (r'(?mi)(?:LaTeX|Package [^\n]+) Warning:[^\n]*(?:undefined|multiply defined)|There were undefined (?:references|citations)','Referência ou citação indefinida/duplicada'),
  (r'LaTeX Warning: Label\(s\) may have changed|Rerun to get|Rerun to get /PageLabels','Referências ainda pedem recompilação'),
 ]:
  if re.search(pat,log):errors.append(msg)
 over=re.findall(r'Overfull \\[hv]box[^\n]*',log)
 if over:errors.append(f'{len(over)} caixa(s) com extravasamento: conferir o relatório e o PDF')
 for ext,kind in [('toc','SUMÁRIO'),('lof','LISTA DE FIGURAS'),('lot','LISTA DE TABELAS')]:
  p=folder/f'main.{ext}'
  if not p.exists() or r'\contentsline' not in p.read_text(errors='replace'):errors.append(kind+' ausente ou sem entradas')
  else:notes.append(kind+': entradas presentes no arquivo auxiliar')
 if not (folder/'main.pdf').exists():errors.append('main.pdf não gerado')
 return errors,notes,over

def state():
 files=sorted(P.rglob('*.aux'))+[P/f'main.{ext}' for ext in ['toc','lof','lot','out']]
 return {str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files if f.exists()}

def main():
 engine=shutil.which('pdflatex')
 if not engine:
  print('NÃO COMPILADO: pdfLaTeX indisponível. Use Overleaf ou instale TeX Live/MiKTeX.');return 2
 # Bibliografia já está em referencias.tex. Não executar BibTeX/Biber.
 old=None;stable=False;runs=0
 for runs in range(1,7):
  print(f'pdfLaTeX: passagem {runs}/6',flush=True)
  cmd=[engine,'-interaction=nonstopmode','-halt-on-error','-file-line-error','main.tex']
  result=subprocess.run(cmd,cwd=P,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,errors='replace')
  (P/'ULTIMA_COMPILACAO.txt').write_text(result.stdout,encoding='utf-8')
  if result.returncode:
   print('COMPILAÇÃO INTERROMPIDA. Consulte ULTIMA_COMPILACAO.txt e main.log.');return result.returncode
  current=state()
  if runs>=3 and current==old:stable=True;break
  old=current
 log=(P/'main.log').read_text(errors='replace')
 errors,notes,over=problemas(log,P)
 if not stable:errors.append('Arquivos auxiliares não estabilizaram após seis passagens')
 report={'passagens':runs,'auxiliares_estaveis':stable,'erros_de_entrega':errors,'verificacoes':notes,'extravasamentos':over,'limite':'Exige revisão visual do PDF: não atesta ABNT integral, recortes, legibilidade ou colocação de cada figura.'}
 (P/'CHECAGEM_COMPILACAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))
 if errors:return 1
 print('Checagens automáticas de compilação aprovadas. Revise main.pdf visualmente antes de entregar.');return 0
if __name__=='__main__':sys.exit(main())
