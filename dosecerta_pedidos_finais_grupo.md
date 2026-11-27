"""Converte a base .bib do projeto em referencias.tex, sem dependências externas.
Executar com Python 3 depois de editar a bibliografia ou as citações.
Saída autor-data compatível com abntex2cite do modelo FEI.
"""
from pathlib import Path
import re,unicodedata,collections
ROOT=Path(__file__).resolve().parent
BIB=ROOT/'FEI-bib/dosecerta-referencias.bib'
def braced(s,i):
    assert s[i]=='{'
    depth=1;j=i+1
    while j<len(s) and depth:
        if s[j]=='{' and s[j-1]!='\\':depth+=1
        elif s[j]=='}' and s[j-1]!='\\':depth-=1
        j+=1
    if depth:raise ValueError('Chaves não balanceadas na base bibliográfica')
    return s[i+1:j-1],j

def parse(s):
    out={};pos=0
    while (m:=re.search(r'@(\w+)\s*\{\s*([^,]+),',s[pos:])):
        start=pos+m.start();body,end=braced(s,start+s[start:].index('{'));pos=end
        key=body.split(',',1)[0].strip();d={'type':m[1].lower()};rest=body.split(',',1)[1];i=0
        while (f:=re.search(r'(\w+)\s*=\s*',rest[i:])):
            name=f[1].lower();a=i+f.end()
            if rest[a]!='{':raise ValueError('Usar campos entre chaves: '+key+':'+name)
            value,i=braced(rest,a);d[name]=value.strip()
        if key in out:raise ValueError('Chave duplicada '+key)
        out[key]=d
    return out

def unbrace(s):return s.replace('{','').replace('}','')
def author_info(d):
    if 'author' not in d:return d.get('organization','Autoria não informada'),d.get('organization','AUTORIA NÃO INFORMADA').upper()
    a=d['author']
    if a.startswith('{'):return unbrace(a),unbrace(a).upper()
    names=a.split(' and ');short=[n.split(',')[0].strip() for n in names];full=[]
    for n in names:
        bits=n.split(',',1)
        full.append(bits[0].strip().upper()+(', '+bits[1].strip() if len(bits)>1 else ''))
    if len(short)>3:label=short[0]+r' \textit{et al.}'
    elif len(short)==3:label=', '.join(short[:2])+' e '+short[2]
    elif len(short)==2:label=' e '.join(short)
    else:label=short[0]
    return label,'; '.join(full)

def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',unbrace(s)) if not unicodedata.combining(c)).casefold()

def generate():
    entries=parse(BIB.read_text(encoding='utf-8'));cited=set()
    queue=[ROOT/'main.tex']; seen=set()
    while queue:
        f=queue.pop()
        if f in seen:continue
        seen.add(f)
        content=f.read_text(encoding='utf-8')
        content=re.sub(r'(?<!\\)%[^\n]*','',content)
        for name in re.findall(r'\\(?:input|include)\{([^}]+)\}',content):
            target=ROOT/(name if Path(name).suffix else name+'.tex')
            if target.name!='referencias.tex':queue.append(target)
        for m in re.finditer(r'\\cite\w*\*?(?:\[[^]]*\])*\{([^}]+)\}',content):cited.update(k.strip() for k in m[1].split(','))
    missing=cited-set(entries)
    if missing:raise ValueError('Referências ausentes: '+', '.join(sorted(missing)))
    keys=sorted(cited,key=lambda k:(norm(author_info(entries[k])[0]),entries[k].get('year',''),norm(entries[k]['title'])))
    groups=collections.defaultdict(list)
    for k in keys:groups[(author_info(entries[k])[0],entries[k].get('year','[s.d.]'))].append(k)
    years={}
    for (author,year),ks in groups.items():
        for i,k in enumerate(ks):years[k]=year+(chr(97+i) if len(ks)>1 else '')
    text=r'''% Gerado por gerar_referencias.py a partir de FEI-bib/dosecerta-referencias.bib.
% Não requer main.bbl. Recompilar o LaTeX pelo menos duas vezes após alterações.
\begingroup
\setlength{\labelsep}{0pt}
\begin{thebibliography}{99}
\providecommand{\abntrefinfo}[3]{}
\providecommand{\abntbstabout}[1]{}
'''
    for k in keys:
        d=entries[k];label,author=author_info(d);year=years[k]
        text+='\n'+r'\bibitem['+label+' '+year.replace('[','').replace(']','')+']{'+k+'}\n'+r'\abntrefinfo{'+label+'}{'+label+'}{'+year+'}\n'
        title=d['title'];parts=[author+'.']
        if d['type']=='article':
            parts.append(title+'.');parts.append(r'\textbf{'+d['journal']+'},')
            if 'volume' in d:parts.append('v. '+d['volume']+',')
            if 'number' in d:parts.append('n. '+d['number']+',')
            if 'pages' in d:parts.append(('art. ' if k=='MASNOON2017' else 'p. ')+d['pages']+',')
            parts.append(year+'.')
        else:parts.extend([r'\textbf{'+title+'}.',year+'.'])
        if 'doi' in d:parts.append(r'DOI: \nolinkurl{'+d['doi']+'}.')
        if 'note' in d:parts.append(d['note'])
        if 'url' in d:parts.append(r'Disponível em: \url{'+d['url']+'}.')
        if 'urlaccessdate' in d:parts.append('Acesso em: '+d['urlaccessdate']+'.')
        text+=' '.join(parts)+'\n'
    text+='\n'+r'\end{thebibliography}'+'\n'+r'\endgroup'+'\n'
    (ROOT/'referencias.tex').write_text(text,encoding='utf-8')
    print(f'{len(keys)} entradas autor-data geradas; nenhuma chave citada ausente.')
    return entries,keys

if __name__=='__main__':generate()
