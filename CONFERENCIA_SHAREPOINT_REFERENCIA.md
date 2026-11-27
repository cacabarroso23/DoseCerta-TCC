# DoseCerta — conferência das evidências antes de cobrar a equipe

## Correção da solicitação anterior

A solicitação anterior era abrangente demais para ser tratada como lista de dados ausentes. Há resultados e medições no acervo. O pedido revisado distingue registro existente, divergência de versões, complemento necessário e ensaio ainda não localizado. Nenhuma ausência de evidência foi convertida em afirmação de que o responsável não trabalhou.

Conferi o compilado DOCX, documentação MD de agentes/MCP/segurança e relatórios do banco; inspecionei as 32 imagens incorporadas ao compilado em pranchas de conferência. Não afirmo que todo arquivo de toda a árvore do SharePoint foi examinado. O documento do usuário foi preservado em cópia anterior e substituído por uma solicitação focada nas quatro frentes pedidas, mais integração e ficha comum. Os arquivos LaTeX não foram alterados.

## O que já está documentado — e o que cobrar em vez disso


| Assunto                    | Registro existente                                                                                                                             | Limite e complemento específico                                                                                                                                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mecânica/modelos           | STL V75, 3MF V5, OBJ V15, foto do protótipo e medidas calculadas da malha.                                                                     | A seção 4.2 informa ausência de CAD nativo recuperado, desenho cotado e ficha de fabricação por peça. Pedir identificação da peça impressa, fabricação e conferência dimensional física, não novamente “o projeto mecânico”.       |
| Ângulo                     | O V75 mede 30°; o artigo informa 35°.                                                                                                          | Nenhum dos dois identifica sozinho o ângulo fabricado. Corrigir a premissa anterior de adotar 35° como montagem final confirmada.                                                                                                  |
| Motor/localização          | Seis buscas para cinco intervalos: 795, 845, 861, 798 e 801 fases, média 820.                                                                  | Um ciclo, sem encoder; não é erro angular medido nem demonstra repetibilidade. O perfil ativo posterior tem outros intervalos: 846, 806, 811, 811 e 853, soma 4.127. Não misturar campanhas/perfis.                                |
| Sensor sem silo            | Duas varreduras; vazio aproximadamente 2.800–2.900 contagens e ocupado 110–160.                                                                | Com silo, há faixa de 44–316. Confirmar perfil e geometria atuais e avaliar condições reais separadamente. A observação já existe; o que falta é alcance da avaliação e erros por condição.                                        |
| Dispensação                | Um ciclo 820+820 fases: avanço, queda e retorno observados.                                                                                    | Releitura ambígua: mediana \~2.864, com 7/20 amostras fora da faixa. Não reclassificar como confirmação automática; pedir repetições e contagem independente.                                                                      |
| Giro intermitente/brownout | Há vibração/giro alternantes com os mesmos parâmetros e brownout durante calibração; há uma medição estática de 5 V no driver.                 | A causa não foi isolada. A própria seção 4.2 propõe observação das linhas 5 V/3,3 V durante a atuação. Tensão estática não exclui queda transitória.                                                                               |
| Contatos                   | O SUB voltou a responder após ajuste; 20 leituras válidas e zero erros naquele reteste. Reparos de GND/curtos também estão registrados.        | Isso não identifica automaticamente a causa nem valida desgaste/encaixes/carga. Pedir condição pós-reparo, ordem física dos contatos e contagens por cenário; não negar o reteste existente.                                       |
| Medidas elétricas          | Há pranchas, pinagens, cores de fios e correções. A Tabela 4.3g mantém medições de tensão/corrente/contatos como dados a completar.            | Pedir medições pós-reparo sob carga, instrumentação, repetição e rastreabilidade; esquema não é medida, e fonte prevista não é fonte instalada.                                                                                    |
| API                        | Na dc8, 238 testes: 236 aprovados e dois erros antigos de importação; banco em memória.                                                        | Pedir correção/reexecução ou limitação explícita, casos autenticados com integração real e evidências por classe de falha. Não dizer que não existe teste de backend.                                                              |
| Runtime/provisionamento    | Na dc8, runtime com 712 testes, 711 aprovados e um erro antigo; provisionamento com 227/227.                                                   | Hardware/nuvem simulados no runtime. Aceite físico e configuração instalada são evidências diferentes. Não somar rodadas históricas ou subtestes para inflar cobertura.                                                            |
| Publicação/integridade     | Serviços saudáveis, rotas exigindo login e arquivos conferidos por manifesto.                                                                  | O compilado diz explicitamente que não foram ensaios funcionais autenticados, carga ou ausência de vulnerabilidades. Confirmar execução dessas avaliações, não cobrar novamente o manifesto.                                       |
| Care                       | O compilado exclui as suítes Care/painel das suas tabelas; os guias do app contêm registros em escopos diferentes.                             | Identificar relatório/versão do Care, casos sobrepostos e o que usa navegador simulado. Não concluir ausência de testes do app pela tabela de outra frente.                                                                        |
| Proteção de dados          | HTTPS, atores/tokens, idempotência, eventos e RLS constam da documentação; há casos de não registrar segredos e recusar contexto indevido.     | O relatório de 03/11 também aponta conta compartilhada, papel da API que ignora RLS, chave estática, retenção/privacidade e outros riscos. Confirmar mudanças e limites atuais; não afirmar conformidade ou isolamento por pessoa. |
| Agente                     | Duas configurações de agente, ferramentas e aprovação documentadas; MCP com suíte automatizada, indicada no seu guia como 763 testes sem rede. | Não são 763 interações avaliadas do modelo. Pedir resultados por interação e efeito persistido; conferir data/versão da contagem.                                                                                                  |
| Escrita pelo agente        | O guia registra conversa de ponta a ponta sem aprovar gravações.                                                                               | Não é prova de que não existam escritas em outro registro. Pedir localização das gravações de teste aprovadas e sua conferência, ou registrar não execução.                                                                        |
| Aprovação                  | Política no Foundry para seis ferramentas de escrita.                                                                                          | O guia explicita que quem possui a chave MCP pode chamar a escrita diretamente. Aprovação do agente não equivale a uma trava universal da API/MCP. Pedir limite de confiança e controle compensatório, nunca a chave.              |
| Versão instalada           | A dc8 aparece validada na Raspberry, mas ainda não instalada no momento do registro.                                                           | Não atribuir a essa entrega um ensaio físico feito em versão anterior. Solicitar manifesto/versão efetivamente instalada e data.                                                                                                   |


## Leitura das imagens

As imagens foram usadas para distinguir desenho de projeto, foto da montagem, sinal medido e diagrama de comportamento. São tipos diferentes de evidência.

* A foto do protótipo demonstra uma montagem, mas a própria legenda ainda pede identificação dos módulos/peças. Não permite inferir dimensão, resistência, material ou versão exatos.
* A vista externa/interna e os modelos explodidos ajudam a identificar componentes. Não comprovam que a peça fabricada corresponde à revisão mostrada.
* As pranchas elétricas e de buzzer são referências de montagem; não demonstram queda de tensão, estabilidade de alimentação ou aquecimento medidos.
* A comparação das varreduras mostra duas execuções, condições explícitas e trecho ambíguo preservado. É evidência útil de bancada, não uma taxa final de acerto.
* A figura dos cinco intervalos informa que se trata de um ciclo sem encoder e que a média não é constante do mecanismo. Essa limitação deve permanecer no texto.
* Os diagramas de estados, atualização, provisionamento e publicação descrevem mecanismos esperados. Sem logs/observação do caso, não comprovam que cada transição foi exercitada fisicamente.

A prancha abaixo reúne quatro exemplos selecionados dessas diferenças; não substitui os arquivos originais nem acrescenta dados de ensaio.

![Conferência visual: foto do protótipo, modelo mecânico, esquema elétrico e varreduras do sensor](sandbox:/home/user/output/DoseCerta_conferencia_visual.png)

## Como usar a solicitação curta

1. Encaminhar somente as seções correspondentes e a ficha comum.
2. Começar perguntando onde o registro já existe; não impor repetição sem conferir sua adequação.
3. Se a condição/versão for diferente, registrar a diferença e decidir se é necessário reteste.
4. Se faltar registro, distinguir organização de documentação e ensaio a executar.
5. Definir critério/amostragem antes da avaliação final, sem propor um número mágico que sirva para todas as áreas.
6. Usar bancada segura, dados fictícios e ambiente autorizado. Não pedir falha perigosa, exposição de segredo ou teste invasivo em produção.
7. Cobrar o mesmo rigor de todas as frentes, com ênfase nas lacunas técnicas — não na pessoa nem no uso de IA.

## Fontes conferidas

* [DoseCerta — Monografia Compilado](https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/_layouts/15/Doc.aspx?sourcedoc=%7BCB1B745D-0CDE-46E6-AF6E-A0CFFA7C3A2A%7D&file=DoseCerta_Monografia_Compilado.docx&action=default&mobileredirect=true&web=1): seções 3.13, 4.2, 4.3, 4.8, 4.13 a 4.15.
* [Agentes no Foundry](https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/documenta%C3%A7%C3%A3o/documenta%C3%A7%C3%A3o/10-agentes-foundry.md?web=1): verificação de 03/11/2026, especialmente limites da voz, versão chamada e aprovação.
* [Segurança e privacidade](https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/documenta%C3%A7%C3%A3o/documenta%C3%A7%C3%A3o/12-seguranca-e-privacidade.md?web=1): controles, medições somente leitura, riscos aceitos e lacunas; não é auditoria nem parecer jurídico.
* [Servidor MCP](https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/documenta%C3%A7%C3%A3o/documenta%C3%A7%C3%A3o/09-mcp.md?web=1): ferramentas, testes automatizados e limites da integração.
* [Relatório Supabase](https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/DoseCerta_Acervo_Completo_20261112/03_historico_e_analises/analise_e_historico_do_app/supabase/RELATORIO_SUPABASE_DOSECERTA.md?web=1): modelo, papéis, RLS e rotinas operacionais.

Essas fontes já existentes sustentam os pedidos acima. “Não localizado” não significa “inexistente”; a primeira resposta deve apontar o registro, se houver. Valores e situações são históricos das fontes, não uma verificação nova do aparelho ou dos serviços. Testes externos não foram executados nesta conferência.