# Verificação estática e compilação

## Executado

* Verificação de 31 arquivos `.tex`: balanço de chaves e correspondência de ambientes.
* Conferência dos caminhos de `\include` e `\input` presentes nos `.tex`; todos os destinos encontrados.
* Conferência das 37 figuras incluídas: caminhos existentes, integridade verificada com Pillow, rótulos definidos e chamadas no texto.
* Conferência das 16 chaves citadas na base e em `referencias.tex`, com metadados autor-data; nenhuma ausente. A base contém ainda uma entrada de apoio não citada.
* Conferência de rótulos duplicados e referências internas sem rótulo: nenhum caso encontrado pelos controles executados.
* Inventário de 87 IDs de pendência, sem duplicação, associados aos arquivos atuais.
* Oito tabelas `longtable` com legenda e indicação de fonte.
* Comparação da classe com o original enviado: somente troca de `\include` por `\input` no carregamento de `FEI-pre-textual`.
* Conferência dos 14 itens do orçamento: soma XLSX de R$ 2.494,305 e soma XLSM de R$ 2.499,890, sem alterar os valores.
* Paginação configurada com `oneside`, `openany` e `\cleardoublepage` redirecionado para `\clearpage`, evitando páginas impostas pela paridade.
* Nenhum erro ou aviso remanescente nos controles estáticos implementados.

## Não executado

* Compilação pdfLaTeX: não executada; compilador indisponível neste ambiente. Nenhum PDF novo integra a entrega.
* Revisão visual do PDF integral: depende da compilação.
* Ensaios físicos, testes de integração ou aceite dos requisitos: dependem de evidências da equipe.
* Conferência final da exatidão e completude de todos os dados bibliográficos: requer revisão acadêmica.

O relatório de máquina está em `validacao_estatica.json`. Os controles são limitados e não constituem prova de compilação ou de conformidade institucional.

## Compilar e conferir

Usar `main.tex` como principal, na raiz, com pdfLaTeX. Executar três passagens ou repetir até estabilizar as referências e listas. No Overleaf, selecionar pdfLaTeX e recompilar do zero. Não executar BibTeX/Biber: `referencias.tex` já está incluído. Se alterar citações ou a base `.bib`, executar `python3 gerar_referencias.py` e depois recompilar. Consultar o roteiro completo em `README.md`.

* Resolver erros de compilação e referências indefinidas antes de revisar a aparência.
* Conferir paginação, acentos, legendas, fontes, sumário e listas.
* Confirmar que os 87 campos permanecem vermelhos enquanto não forem resolvidos.
* Manter os elementos pré-textuais pendentes; não reinserir a ficha catalográfica nesta cópia sem nova decisão.
* Preencher resultados, discussão e conclusão somente com os dados finais.
