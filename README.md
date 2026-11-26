# DoseCerta — entrega da versão de trabalho FEI

## Conteúdo do pacote

* `main.tex`: entrada principal da monografia, com 17 capítulos.
* `classe/`: classe e estilos fornecidos. Em `USPSC.cls`, a única alteração em relação ao original é `\include{FEI-pre-textual}` para `\input{FEI-pre-textual}`, evitando os efeitos de inclusão de páginas e auxiliares no carregamento dos metadados.
* `FEI-pre-textual.tex`, `PreTextual/` e `PosTextual/`: metadados e elementos de abertura/fechamento. Não foram produzidas aprovação, banca ou assinaturas fictícias.
* `FEI-bib/dosecerta-referencias.bib`: bibliografia ativa, com 16 chaves citadas.
* `FEI-bib/modelo-references.bib`: bibliografia original recebida, preservada sem inclusão automática das referências de exemplo no texto.
* `Figuras/Artigo/`: sete imagens documentais preservadas; quatro são incluídas no texto. As demais ficam como material de apoio, não como prova de implementação final.
* `pendencias_dosecerta.tex`, `pendencias.json` e `PERGUNTAS_PARA_CONTRIBUIDORES.md`: macro vermelha e roteiro dos 87 campos atuais.
* `VALIDACAO_E_COMPILACAO.md`: conferências executadas e instruções para compilar.

## Decisões respeitadas

* Português do Brasil, abstract em inglês e projeto no modelo FEI enviado.
* Care em capítulo próprio; visão computacional reservada para o conteúdo de Vini.
* Inclinação de projeto de 35° e login obrigatório, sem confundir decisão de projeto com comprovação experimental.
* Ferramentas de desenvolvimento e IA tratadas na metodologia, com confirmação pendente de produto, versão e uso por integrante quando faltam dados.
* Campos pré-textuais não preenchidos mantidos em vermelho. Somente a ficha catalográfica foi omitida.
* Resultados, discussão e conclusão continuam pendentes, em vermelho, sem afirmações antecipadas.

## Limite da entrega

Esta é uma versão de trabalho editável, não a versão acadêmica final. Não houve compilação LaTeX: nenhum executável pdfLaTeX, LuaLaTeX ou Tectonic foi encontrado. Não foi gerado PDF integral novo nem realizada revisão visual da paginação.

A checagem estática de arquivos incluídos, chaves/ambientes, figuras, citações, rótulos e IDs de pendência não encontrou erros nos controles executados. Ela não substitui compilação, leitura crítica, revisão de referências ou aprovação do orientador. Nenhum ensaio do protótipo foi executado nesta etapa.

## Compilar

No Overleaf, enviar o conteúdo completo do ZIP, selecionar `main.tex` como documento principal e usar pdfLaTeX. Confirmar que os arquivos de `classe/` e `FEI-bib/` estão no projeto. Compilar do zero e inspecionar o log.

Localmente, com TeX Live/MiKTeX e os pacotes usados pelo modelo, executar na pasta que contém `main.tex`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Antes de fechar, conferir o vermelho das pendências, capa/folha de rosto, lista de figuras e tabelas, sumário, legendas, quebras e referências. Corrigir erros e avisos relevantes do log. Após completar os dados, resolver cada ID; não ocultar pendências apenas para aparentar conclusão.

Os arquivos auxiliares de compilação não são necessários para importar esta entrega. O pacote não contém `.synctex.gz`, `.aux`, `.bbl`, `.loq` nem PDFs antigos apresentados como se fossem novos.
