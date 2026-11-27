# Alterações da integração — 27/11/2026

## Base e fontes
Comparação contra o backup local anterior à integração, não contra hash/commit remoto certificado. A versão de trabalho foi conciliada com os textos do GitHub já lidos e os arquivos main.tex e metodologia foram reconferidos nesta rodada. Foram consultados o compilado e documentos de segurança/agente do SharePoint, a conferência atualizada da autora e os três anexos. O PDF enviado é referência anterior; não é PDF desta entrega.

## Decisões de evidência
- runtime 0.9.2 e release 2026.11.25-cam-3: não promovidos a 0.9.3 por suposição.
- perfil ativo de 4.096 fases; três perfis mantidos separados de precisão angular medida.
- dispersão amostral calculada dos CSVs: 11,2 fases; 10,8 corresponde aproximadamente à dispersão populacional.
- 12 sessões encerradas não viram 12 dispensações corretas: há retenções e encerramentos por impedimentos.
- telemetria sem motor não vira ensaio de alimentação sob carga.
- regressão logística e vision-v3 não foram equiparadas.
- arquitetura histórica do agente e relato posterior de Voice Live permanecem distintos até confirmação.
- armazenamento: nenhum prazo do pacote foi transformado em validade farmacêutica do protótipo.

## Arquivos LaTeX e bibliografia modificados
- `Capitulos/01_introducao.tex`
- `Capitulos/02_fundamentacao.tex`
- `Capitulos/03_estado_da_arte.tex`
- `Capitulos/04_metodologia.tex`
- `Capitulos/05_requisitos.tex`
- `Capitulos/06_arquitetura.tex`
- `Capitulos/07_projeto_mecanico.tex`
- `Capitulos/08_projeto_eletronico.tex`
- `Capitulos/09_embarcados.tex`
- `Capitulos/10_backend.tex`
- `Capitulos/11_aplicativo.tex`
- `Capitulos/12_visao_computacional.tex`
- `Capitulos/13_agente_ia.tex`
- `Capitulos/14_testes.tex`
- `Capitulos/15_resultados.tex`
- `Capitulos/16_discussao.tex`
- `Capitulos/17_conclusao.tex`
- `FEI-bib/dosecerta-referencias.bib`
- `PosTextual/apendices.tex`
- `PreTextual/abstract.tex`
- `PreTextual/resumo.tex`
- `PreTextual/simbolos.tex`
- `main.tex`
- `pendencias_dosecerta.tex`
- `referencias.tex`

## Verificação e limites
Os controles estáticos não apontaram erro; 88 pendências permanecem explícitas. Compilação e revisão visual integral do PDF não executadas. O arquivo `alteracoes_base_local.patch` contém o diff textual; dados, figuras e documentos de apoio novos constam em `arquivos_alterados.json`. Nenhum push foi feito.
