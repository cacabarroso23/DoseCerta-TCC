"""Compila com pdfLaTeX até estabilizar listas e referências; não aceita PDF parcial."""
from pathlib import Path
import subprocess,sys,shutil,re,hashlib,json
P=Path(__file__).resolve().parent

def run(cmd):
 r=subprocess.run(cmd,cwd=P)
 if r.returncode:raise SystemExit(r.returncode)

def check_log(log):
 patterns=[r'LaTeX Warning: (?:Reference|Citation) .*? undefined',r'There were undefined references',r'Label\(s\) may have changed',r'Rerun to get cross-references right',r'LaTeX Warning: Label .* multiply defined']
 return [m.group(0) for pat in patterns for m in re.finditer(pat,log)]

def main():
 compiler=shutil.which('pdflatex')
 if not compiler:raise SystemExit('pdfLaTeX indisponível. Instale TeX Live/MiKTeX ou abra no Overleaf e selecione main.tex e pdfLaTeX. Não foi gerado PDF.')
 run([sys.executable,'gerar_referencias.py'])
 previous=None
 for i in range(1,7):
  run([compiler,'-interaction=nonstopmode','-halt-on-error','-file-line-error','main.tex'])
  files=[P/('main.'+ext) for ext in ['aux','toc','lof','lot']]+list((P/'Capitulos').glob('*.aux'))+list((P/'PosTextual').glob('*.aux'))
  digest=hashlib.sha256(b''.join(p.read_bytes() for p in sorted(files) if p.exists())).hexdigest()
  log=(P/'main.log').read_text(errors='replace');issues=check_log(log)
  if i>=3 and digest==previous and not issues:break
  previous=digest
 else:raise SystemExit('Compilação não estabilizou ou contém referências indefinidas. Consulte main.log; não entregar este PDF.')
 for ext in ['toc','lof','lot']:
  p=P/('main.'+ext)
  if not p.exists() or '\\contentsline' not in p.read_text(errors='replace'):raise SystemExit('Lista/sumário vazio: '+p.name)
 overflows=re.findall(r'Overfull \\[hv]box[^\n]*',log)
 report={'rodadas':i,'referencias_indefinidas':issues,'sumario_e_listas_preenchidos':True,'extravasamentos':overflows,'revisao_visual_ainda_necessaria':True}
 (P/'CHECAGEM_PDF.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 if overflows:raise SystemExit('PDF compilado, mas há extravasamentos de margem. Revise main.log/CHECAGEM_PDF.json antes de entregar.')
 print('PDF compilado; listas preenchidas e referências estabilizadas. Conferir visualmente paginação, figuras e tabelas antes de entregar à banca.')
if __name__=='__main__':main()
