# Verificação estática e compilação

## Executado

* Verificação de 30 arquivos `.tex`: balanço de chaves e correspondência de ambientes.
* Conferência dos caminhos de `\include` e `\input` presentes nos `.tex`; todos os destinos encontrados.
* Conferência das quatro chamadas de imagem; todos os arquivos encontrados. As sete imagens preservadas também passaram pela verificação de integridade do decodificador Pillow.
* Conferência das 16 chaves de citação no arquivo bibliográfico ativo; nenhuma ausente e nenhuma entrada ativa não citada.
* Conferência de rótulos duplicados e referências internas sem rótulo: nenhum caso encontrado pelos controles executados.
* Inventário de 87 IDs de pendência, sem duplicação, associados aos arquivos atuais.
* Oito tabelas `longtable` com legenda e indicação de fonte.
* Comparação da classe com o original enviado: somente troca de `\include` por `\input` no carregamento de `FEI-pre-textual`.
* Nenhum erro ou aviso remanescente nos controles estáticos implementados.

## Não executado

* Compilação pdfLaTeX/BibTeX: compilador indisponível neste ambiente.
* Revisão visual do PDF integral: depende da compilação.
* Ensaios físicos, testes de integração ou aceite dos requisitos: dependem de evidências da equipe.
* Conferência final da exatidão e completude de todos os dados bibliográficos: requer revisão acadêmica.

O relatório de máquina está em `validacao_estatica.json`. Os controles são limitados e não constituem prova de compilação ou de conformidade institucional.

## Compilar e conferir

Usar `main.tex` como principal, na raiz, com pdfLaTeX e BibTeX. Executar pdfLaTeX, BibTeX e mais duas passagens de pdfLaTeX. No Overleaf, selecionar pdfLaTeX e recompilar do zero. Consultar o roteiro completo em `README.md`.

* Resolver erros de compilação e referências indefinidas antes de revisar a aparência.
* Conferir paginação, acentos, legendas, fontes, sumário e listas.
* Confirmar que os 87 campos permanecem vermelhos enquanto não forem resolvidos.
* Manter os elementos pré-textuais pendentes; não reinserir a ficha catalográfica nesta cópia sem nova decisão.
* Preencher resultados, discussão e conclusão somente com os dados finais.
