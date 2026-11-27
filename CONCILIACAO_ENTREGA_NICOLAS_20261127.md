# Conciliação da entrega Nicolas — rodada 2, 27/11/2026

## Como esta versão foi feita

A base é a pasta de trabalho da rodada 1 com as edições locais da autora. Antes das alterações foi feito backup. O relatório-fonte e a conferência SharePoint editados foram preservados byte a byte; o histórico ALTERACOES foi preservado e recebeu uma seção nova no final. Nenhuma busca ou sincronização nova do GitHub/SharePoint foi feita nesta rodada; o material anterior foi usado como contexto e os quatro anexos novos como contribuição adicional.

O ZIP foi listado antes da leitura. A extração foi seletiva; não foram abertos arquivos compactados aninhados nem executados programas recebidos. Os 16 prints repetidos na pasta `prints/` não foram duplicados. O PDF externo é idêntico em SHA-256 ao PDF do ZIP; trata-se de uma única prévia recebida, não de duas verificações independentes.

## Decisões por contribuição

| Material | Decisão |
|---|---|
| Aplicativo | Capítulo novo incorporado, com as 16 capturas e ressalvas sobre login oficial, demonstração e resposta roteirizada. APP01–APP05 preservadas e atualizadas. |
| Dados e rastreabilidade | Nova seção no capítulo 10, com SQLite, PostgreSQL, volumes, ambientes e limites dos controles de segurança. Volumes de 26/11 identificados como estimativas de estatísticas, não contagens exatas. |
| Resultados | Conteúdo anterior preservado e ampliado com duas tabelas de registros e uma de qualidade da evidência. Não se somam recortes sobrepostos. |
| Visão | Mantido o método detalhado do DOCX da frente. A base v2 recebida acrescenta histórico de exploração, não substitui a vision-v3 nem prova sua implantação. |
| Agente | Proposta incorporada como relato a revisar com Thiago. Mantidos o registro histórico e os conflitos com a descrição anterior de Voice Live. Sem presumir implantação, modelo, autorização ou aprovação segura. |
| Apêndice | Matriz dos 25 requisitos mantida; protocolo A–F adicionado como proposta. Verbos no passado corrigidos para não afirmar campanha executada. |
| Segurança e armazenamento | Controles relatados diferenciados de auditoria. Evidenciados conta compartilhada, possibilidade de bypass de RLS, MCP e processamento externo de anexos. |
| Referências | URLs de contas corporativas removidas da base e do texto bibliográfico gerado; títulos e datas dos documentos mantidos. A base `dosecerta_adicionais.bib` mencionada no LEIA-ME não estava disponível aqui nem no ZIP recebido. |
| Folha de rosto | Corrigido no main o uso dos argumentos opcionais dos ambientes, sem mexer na classe. Sem compilação local, o resultado visual ainda precisa ser conferido. |

## Diferenças que não poderiam virar afirmações de resultado

### Oficial: oito registros não equivalem a oito ensaios válidos

- Linha 1: pedido de 29/10 com zero ciclos; saída informada em 07/11. Inconsistência temporal mantida, não usada como sucesso físico.
- Linha 5: `not_observed`, sem quantidade observada e sem estoque posterior. A célula vazia não virou zero nem comprovação de estoque.
- Linhas 2, 3, 4, 6, 7 e 8: têm quantidade e estoque antes/depois; a redução registrada corresponde à quantidade relatada em 6/6. Isso é consistência contábil, **não contagem independente do estoque físico**.
- Linhas 4 e 8: relatos unitários sem a inconsistência temporal da linha 1; a 8 ainda tem resultado do aparelho exigindo reconciliação.
- Linhas 2, 6 e 7: recusas antes do movimento com relato de zero saída. São recusas do desenvolvimento, não acertos de dispensação.
- Linhas 3 e 5: retenção indicada pelo sensor, mas somente a 3 tem relato humano de zero. Não são duas retenções fisicamente contadas.
- Não foram adotados como estimativas de segurança/eficácia: estoque físico 8/8, zero dose extra 0/8, sucesso físico 3/8 ou seus intervalos de confiança.

### Simulado: cinco sem contagem não são cinco fechamentos automáticos

O CSV tem quatro `presentation_policy`, dois `human_report` e um `sem fechamento`. Há cinco linhas sem quantidade humana porque a linha aberta também não tem quantidade. Nos dois relatos de demonstração constam duas unidades e estoque 10→10, sob política de apresentação. O conjunto não foi usado para inferir acurácia ou integridade de estoque da política rigorosa.

### Configuração e métricas

- Runtime: LEIA-ME novo cita 0.8.0; leitura datada anterior de 26/11, 22h10 cita 0.9.2 e release `2026.11.25-cam-3`. Mantida esta última como referência da coleta, com conflito explícito; não se presume atualização ou downgrade posterior.
- RTC: há evidência fotográfica de montagem, mas não estava habilitado no Linux. Não se adotou “não instalado” como explicação universal.
- Localização: 4/9 na proposta não foi intercambiado com os grupos 1/12, 3/7 e 2/2 do CSV anterior, sem IDs e filtros equivalentes.
- Sensor: faixas de capturas históricas não são faixas de todas as medições nem substituem calibração ativa. Medianas fracionárias 108,5; 1916,5; 220,5 e 125,5 foram preservadas nas tabelas.
- Disponibilidade: fração diária do total teórico de relatórios (91–94%) não é a mesma métrica que cálculo por lacunas (98,90%). Nenhuma equivale à taxa de eventos sincronizados corretamente.
- Testes: cópia de 18/11 não substitui as rodadas de 25/11; os totais não são somados. Não foram reexecutados testes do produto.
- Agente: v28, aprovação não imposta e paciente fixo são relatos do contribuinte, ainda a confirmar com o responsável. Rótulos internos divergentes de modelo não foram apresentados como especificação pública.

## Revisão sugerida

1. Abra `ALTERACOES_20261127.md` na seção Rodada 2.
2. Leia os capítulos 11 e 10b e confira as legendas dos 16 prints.
3. Leia as novas seções do capítulo 15 junto dos dois CSVs originais.
4. Passe a proposta do capítulo 13 ao Thiago e o histórico v2 ao Vinicius; não remova as ressalvas sem evidência.
5. Confira o apêndice com a orientação antes de qualquer campanha. Não apague tentativas desfavoráveis ao iniciar um bloco após correção.
6. Compile `main.tex` do zero e revise capa, folha de rosto, sumário, listas, referências e quebras das tabelas/figuras.

O PDF de 102 páginas enviado é a prévia do contribuinte. **Não foi gerado PDF desta versão unificada**, nem foram confirmados nela ausência de estouro de margem ou número final de páginas.
