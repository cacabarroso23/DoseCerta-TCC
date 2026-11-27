# Alterações da integração — 27/11/2026

## Base e fontes

Comparação contra o backup local anterior à integração, não contra hash/commit remoto certificado. A versão de trabalho foi conciliada com os textos do GitHub já lidos e os arquivos main.tex e metodologia foram reconferidos nesta rodada. Foram consultados o compilado e documentos de segurança/agente do SharePoint, a conferência atualizada da autora e os três anexos. O PDF enviado é referência anterior; não é PDF desta entrega.

## Decisões de evidência

* runtime 0.9.2 e release 2026.11.25-cam-3: não promovidos a 0.9.3 por suposição.
* perfil ativo de 4.096 fases; três perfis mantidos separados de precisão angular medida.
* dispersão amostral calculada dos CSVs: 11,2 fases; 10,8 corresponde aproximadamente à dispersão populacional.
* 12 sessões encerradas não viram 12 dispensações corretas: há retenções e encerramentos por impedimentos.
* telemetria sem motor não vira ensaio de alimentação sob carga.
* regressão logística e vision-v3 não foram equiparadas.
* arquitetura histórica do agente e relato posterior de Voice Live permanecem distintos até confirmação.
* armazenamento: nenhum prazo do pacote foi transformado em validade farmacêutica do protótipo.

## Arquivos LaTeX e bibliografia modificados

* `Capitulos/01_introducao.tex`
* `Capitulos/02_fundamentacao.tex`
* `Capitulos/03_estado_da_arte.tex`
* `Capitulos/04_metodologia.tex`
* `Capitulos/05_requisitos.tex`
* `Capitulos/06_arquitetura.tex`
* `Capitulos/07_projeto_mecanico.tex`
* `Capitulos/08_projeto_eletronico.tex`
* `Capitulos/09_embarcados.tex`
* `Capitulos/10_backend.tex`
* `Capitulos/11_aplicativo.tex`
* `Capitulos/12_visao_computacional.tex`
* `Capitulos/13_agente_ia.tex`
* `Capitulos/14_testes.tex`
* `Capitulos/15_resultados.tex`
* `Capitulos/16_discussao.tex`
* `Capitulos/17_conclusao.tex`
* `FEI-bib/dosecerta-referencias.bib`
* `PosTextual/apendices.tex`
* `PreTextual/abstract.tex`
* `PreTextual/resumo.tex`
* `PreTextual/simbolos.tex`
* `main.tex`
* `pendencias_dosecerta.tex`
* `referencias.tex`

## Verificação e limites

Os controles estáticos não apontaram erro; 88 pendências permanecem explícitas. Compilação e revisão visual integral do PDF não executadas. O arquivo `alteracoes_base_local.patch` contém o diff textual; dados, figuras e documentos de apoio novos constam em `arquivos_alterados.json`. Nenhum push foi feito.

---

# Rodada 2 — integração da entrega Nicolas (27/11/2026)

A seção anterior foi preservada como histórico da rodada 1. Esta rodada parte da pasta local com as edições da autora; não é sincronização nova do GitHub nem sobrescrita da entrega anterior.

## Incorporado

- Capítulo Care reescrito, com 16 capturas do pacote e legenda que separa demonstração, login oficial e respostas roteirizadas.
- Nova seção `10b_dados_rastreabilidade.tex`, incluída no capítulo 10: SQLite, PostgreSQL, volumes por data, ambientes, controles declarados e processamento no Azure.
- Tabelas dos oito registros do Oficial e sete do Simulado adicionadas aos resultados, sem somá-las aos ciclos/sessões anteriores.
- Protocolo A–F adicionado ao apêndice como PROPOSTA, nunca como campanha executada. Matriz dos 25 requisitos mantida.
- Proposta do agente incorporada como relato a revisar com Thiago, com divergências de configuração, aprovação e paciente explícitas. IDs AG01–AG07 preservados.
- Capítulo detalhado vision-v3 do memorial do responsável preservado; base v2 recebida incorporada como histórico exploratório, não como substituição.
- Links corporativos retirados das referências compiladas; fontes internas mantidas por título. Bibliografia adicional mencionada no LEIA-ME não estava no pacote nem na base local e não foi inventada.
- Corrigida a passagem do argumento do ambiente da folha de rosto no `main.tex`, sem modificar a classe; depende de conferência visual após compilar.
- Resumo/abstract, discussão e conclusão ajustados à evidência nova; todos os 88 IDs de pendência anteriores preservados, com textos atualizados quando cabível.

## Divergências tratadas

- Oficial: não se afirma estoque correto 8/8, pois há linha sem quantidade e estoque posterior, além de anotação humana nove dias depois sem ciclo associado. Seis linhas restantes têm consistência contábil, não aferição independente do estoque físico.
- Simulado: quatro fechamentos automáticos, dois relatos de demonstração e um sem fechamento. Cinco SEM quantidade humana não são cinco fechamentos automáticos.
- Runtime 0.8.0 no LEIA-ME não substitui leitura datada de 26/11 que informa 0.9.2; falta manifesto de alteração posterior.
- RTC fotografado/montado não é RTC habilitado. Mantida a distinção; não foi adotado “não instalado”.
- Disponibilidade por contagem diária de sinais não é disponibilidade por lacunas nem sincronização por evento.
- Aprovação de escrita e seleção de paciente na tela não garantem aprovação técnica ou contexto correto no MCP.

Ver `CONCILIACAO_ENTREGA_NICOLAS_20261127.md` para o detalhamento dos recortes e `VALIDACAO_E_COMPILACAO.md` para o que foi efetivamente verificado. O PDF de 102 páginas é a prévia recebida, não PDF desta rodada unificada.
