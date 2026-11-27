# DoseCerta — revisão integral de 27/11/2026

Projeto completo para substituição em um novo projeto do Overleaf. O ZIP contém os fontes, a classe, a bibliografia, as figuras, os desenhos V75, os dados de apoio e os controles de revisão. Não aplique os ZIPs antigos antes deste.

## Situação da entrega

A checagem estática passou sem erros ou avisos nos controles implementados: 36 arquivos TeX ativos, 102 rótulos, 121 referências internas, 59 inclusões de figuras e 15 chaves bibliográficas citadas. Há 87 pendências abertas, conservadas em vermelho e extraídas para arquivos separados.

Não há pdfLaTeX neste ambiente. Não foi gerado nem revisado visualmente um PDF atualizado. As listas têm seus comandos no documento, mas seu preenchimento e a paginação só podem ser confirmados após compilar. A verificação estática não certifica ausência de extravasamentos, posicionamento das figuras ou conformidade integral com a norma institucional. Não entregar à banca sem compilar e conferir o PDF.

## Abrir no Overleaf

1. Crie um projeto a partir do ZIP completo; os arquivos principais ficam na raiz do arquivo compactado.
2. Escolha `main.tex` como documento principal e pdfLaTeX como compilador.
3. Use a opção de recompilar do zero. Aguarde a estabilização do sumário, das listas e das referências; recompile se ainda houver avisos de referências alteradas.
4. Confira visualmente todos os capítulos, listas, chamadas, fontes das figuras, tabelas, margens e quebras. Não aceite referências `??` nem avisos de citações indefinidas.
5. Não execute BibTeX/Biber: a bibliografia autor-data já está em `referencias.tex`.

## Compilar localmente

Com Python 3 e TeX Live/MiKTeX instalados, execute na raiz:

```sh
python3 gerar_referencias.py
python3 validar_integracao.py
python3 compilar_banca.py
```

No Windows, use `python` se necessário. Os atalhos `compilar_banca.bat` e `compilar_banca.sh` executam o último passo. Os três scripts de geração/validação usam apenas a biblioteca padrão de Python; não instalam programas. O compilador precisa dos pacotes LaTeX usados pela classe FEI/abnTeX2 e pelo documento.

`compilar_banca.py` faz até seis passagens de pdfLaTeX, exige auxiliares estáveis, procura entradas nas listas/sumário e sinaliza referências indefinidas e caixas com extravasamento. Seu sucesso também exige revisão visual posterior. Se houver erro fatal, consulte `ULTIMA_COMPILACAO.txt` e `main.log`. O relatório final de uma execução concluída é `CHECAGEM_COMPILACAO.json`.

Se alterar citações ou a base `.bib`, regenere `referencias.tex`. A bibliografia é gerada somente a partir das citações na árvore ativa de `main.tex`.

## Estrutura ativa

* Pré-textuais: capa, folha de rosto, aprovação, textos preliminares, resumos, listas de figuras/tabelas, siglas, símbolos e sumário.
* Capítulos: introdução; fundamentação/estado da arte; metodologia de desenvolvimento, integração e testes; resultados/discussão; considerações finais.
* Referências e dois apêndices, incluindo desenhos técnicos V75.
* `Capitulos/03_metodo_integrado.tex` organiza as seções técnicas e o método de testes. Os resultados ficam em `Capitulos/15_resultados.tex`, seguido da discussão.
* `Documentacao/` conserva a ficha técnica e os desenhos V75. As dimensões são nominais; a inclinação do eixo é de 30 graus da vertical.

Arquivos de capítulos preservados por compatibilidade, mas não incluídos por `main.tex`, não determinam a estrutura compilada. Não os inclua adicionalmente: isso pode duplicar capítulos ou rótulos.

## Arquivos para a revisão

* `PENDENCIAS_ABERTAS.txt`: lista legível atual, com ID e arquivo de localização.
* `PENDENCIAS_ABERTAS.json`: os mesmos itens com o texto TeX exato. Ambos são regenerados por `validar_integracao.py`.
* `PENDENCIAS_ENCERRADAS.json`: encerramento de MEC01, APP03 e AG05 e seus fundamentos; outras limitações dessas frentes permanecem abertas.
* `CHECAGEM_ESTATICA.json` e `VALIDACAO_E_COMPILACAO.md`: controles atuais e limites.
* `REVISAO_INTEGRAL_20261127.txt`: mudanças e roteiro de conferência.
* `dosecerta_pedidos_finais_grupo.md`: edição da autora, preservada sem alteração nesta finalização.
* `ARQUIVOS_ALTERADOS_REVISAO.json` e `REVISAO_INTEGRAL.patch`: comparação com o backup anterior à revisão integral; não são instruções para sobrepor ao ZIP completo.
* `MANIFESTO_REVISAO_SHA256.json`: integridade dos arquivos da entrega, exceto o próprio manifesto.

## Escopo e limites de evidência

O protótipo considera um paciente por cadastro e identidade fixa no MCP. Ampliação multipaciente e testes de isolamento ficam nas considerações finais como trabalhos futuros. O inventário distingue componentes identificados dos que ainda exigem confirmação física; dados ausentes não foram estimados como se medidos.

Resultados de testes automatizados, diálogos, chamadas de ferramentas e respostas do firmware não equivalem a dispensação contada no coletor nem a validação clínica. A explicação da contagem independente está no método de testes. A avaliação textual do agente separa versões, configuração avaliada e caminho usado pelo Care; não comprova avaliação de voz ou da integração completa.

Os dados anteriores e arquivos de proveniência foram mantidos. Relatórios antigos, patches anteriores, `pendencias.json`, `validacao_estatica.json`, `manifesto_sha256.json` e perguntas históricas não descrevem o estado atual: prevalecem os controles em maiúsculas e esta documentação. Nenhum ensaio físico, chamada ao produto ou gravação em serviço foi executado nesta revisão editorial.
