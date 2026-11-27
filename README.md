# DoseCerta — LaTeX unificado, rodada 2 (27/11/2026)

**Use este pacote completo em um projeto separado do Overleaf. Ele já inclui a rodada anterior: não precisa aplicar o ZIP antigo primeiro.**

Versão de trabalho para revisão da autora, não monografia final ou validação clínica. A base preserva as edições locais e integra a entrega Nicolas, os dados originais e a síntese de segurança. Não houve push nem sincronização nova com GitHub/SharePoint nesta rodada.

## Comece por aqui

1. `CONCILIACAO_ENTREGA_NICOLAS_20261127.md`: decisões, conflitos e roteiro da sua revisão.
2. `ALTERACOES_20261127.md`: histórico preservado; nova seção “Rodada 2” no final.
3. `VALIDACAO_E_COMPILACAO.md`: controles executados e limitações.
4. `PERGUNTAS_PARA_CONTRIBUIDORES.md`: 88 pendências atuais, incluindo confirmação de versão do agente, paciente correto e garantia técnica de aprovação.

## Abrir e compilar

Importe todo o ZIP, selecione `main.tex` como principal e pdfLaTeX. Compile do zero e repita até estabilizar sumário, listas e referências. Não execute BibTeX/Biber: o projeto inclui `referencias.tex`, gerado por `gerar_referencias.py`.

Se alterar citações ou a base principal `.bib`:

```sh
python3 gerar_referencias.py
python3 validar_integracao.py
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

As rotinas Python de validação exigem Python 3 e Pillow. pdfLaTeX exige TeX Live/MiKTeX ou Overleaf.

**Não há compilador LaTeX disponível neste ambiente. Não há PDF novo da rodada 2.** A prévia de 102 páginas foi recebida no pacote de Nicolas e não representa a versão unificada desta pasta. Não foram certificados paginação, margem e acabamento após a integração.

## Estrutura

- `main.tex`, `FEI-pre-textual.tex`, `classe/`, `PreTextual/`, `Capitulos/`, `PosTextual/`: fontes da monografia.
- `Capitulos/10b_dados_rastreabilidade.tex`: seção nova, incluída pelo capítulo 10.
- `Capitulos/tabela_ensaios*.tex`: tabelas adaptadas dos CSVs, com as lacunas preservadas.
- `FEI-bib/dosecerta-referencias.bib` e `referencias.tex`: base e saída bibliográfica sem URLs corporativas.
- `Figuras/Validacao20261126/`: pranchas das 35 fotos e dois gráficos anteriores.
- `Figuras/App/`: 16 capturas recebidas, uma cópia por imagem.
- `Dados/validacao_20261126/`: fontes anteriores, inclusive o relatório editado pela autora.
- `Dados/entrega_Nicolas_20261127/`: CSVs e protocolo recebidos, LEIA-ME, mensagem e síntese de segurança. São fontes originais; seus resumos contêm divergências apontadas na conciliação.
- `pendencias.json`, `validacao_estatica.json`, `manifesto_sha256.json`: inventário, verificação estática e integridade de arquivos.

As tabelas não demonstram uma campanha física concluída. Interface demonstrativa, resposta roteirizada, aprovação de prompt, comando reconhecido, sessão encerrada e quantidade contada são evidências distintas. Nenhum ensaio físico, comando de aparelho, teste do produto, gravação em serviço ou commit foi executado nesta rodada.
