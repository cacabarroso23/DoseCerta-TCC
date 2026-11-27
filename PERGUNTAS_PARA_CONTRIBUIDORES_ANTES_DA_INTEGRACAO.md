# DoseCerta — roteiro atualizado de pendências

## Decisões incorporadas

* Monografia em português do Brasil, com abstract em inglês e modelo FEI fornecido pela equipe.
* Nick/Nicolas: aplicativo Care; Vini/Vinicius: visão computacional; Thi/Thiago: agente de IA; Toca/Rafael: elétrica e mecânica; Caroline: revisão bibliográfica e consolidação.
* Inclinação de projeto: 35°. Não é necessário reconfirmar a decisão; a comprovação da peça fabricada continua pendente.
* Login do aplicativo obrigatório. Versão, telas e evidências de autenticação ainda devem ser fornecidas.
* Aplicativo, visão e agente pertencem ao escopo formal, sem atendimento presumido dos requisitos.
* Resultados, discussão e conclusão aguardam dados; não foram inventados métodos, medições ou resultados.
* Elementos pré-textuais não preenchidos foram mantidos com marcação vermelha. Somente a ficha catalográfica foi omitida.

## Como responder

Esta lista corresponde aos 87 campos de `pendencias.json` e às chamadas de `\pendencia{ID}{texto}` no projeto. A macro define texto vermelho para a futura compilação. O PDF integral ainda não foi compilado nem inspecionado visualmente.

Para cada ID, informar resposta, responsável, data/versão e arquivo de evidência. Ensaios devem registrar condições, instrumentos, repetições, denominadores e falhas. Não enviar credenciais nem dados identificáveis de pacientes. Na ausência de evidência, manter a pendência.

Os responsáveis acima são a divisão confirmada pela autora. Para firmware, servidor, integração e ensaios, a equipe deve identificar o responsável técnico; não foi presumida atribuição individual.

## Campos por arquivo

### `Capitulos/01_introducao.tex`

* `EA04` — Definir população, amostra, contexto de avaliação e desfechos do estudo empírico. Não há dados finais para afirmar melhora de adesão, usabilidade, segurança clínica ou redução de erros.

### `Capitulos/03_estado_da_arte.tex`

* `EA02-REV` — Caroline: concluir a revisão bibliográfica, registrar bases, datas, expressões de busca, critérios e referências adicionais. Se for adotado um método sistemático, executar e documentar o protocolo antes de assim denominar o levantamento.

* `EA03-COMP` — Completar o quadro comparativo com modelos específicos e fontes primárias: capacidade, autonomia, dimensões, preço com data/região, reabastecimento e mecanismo. Não preencher parâmetros comerciais ausentes por analogia nem afirmar vantagem sem ensaio comparável.

* `EA04-COMP` — Inserir comparação empírica somente após definição de população, cenário, desfechos e dados. Deixar explícitos os parâmetros ainda não medidos e as diferenças entre as soluções comparadas.

### `Capitulos/04_metodologia.tex`

* `MET01-ACEITE` — Cada responsável deverá fornecer os instrumentos, condições, calibração, protocolo e evidências da sua frente. Identificar quem executou e quem conferiu os ensaios; não inferir autoria ou aceite apenas da divisão de tarefas.

* `MET03-IA` — Completar a declaração por integrante: Copilot (especificar produto), Copilot Studio, OpenAI (produto/API e modelo), Claude e demais ferramentas efetivamente usadas; tarefas, datas/versões quando disponíveis, partes aproveitadas e revisão humana realizada. Não atribuir uso a uma pessoa sem confirmação.

* `MET02-VERSOES` — Informar software e revisão CAD final, impressora/fatiador, versões das bibliotecas, compiladores, dependências e releases efetivamente apresentados. Distinguir ambiente de desenvolvimento, teste e produção.

* `MET02-PROTOCOLO` — Fechar com a orientação o protocolo final, repetições, amostragem, instrumentos e critérios quantitativos. Não há base documental suficiente para inventar tolerâncias de taxa de erro, corrente, latência ou desempenho.

* `MET-ETICA` — Informar se haverá participantes, coleta de imagens ou dados pessoais; documentar autorizações, consentimento e avaliação institucional aplicáveis. Não inserir número de parecer ou dispensa não fornecidos.

### `Capitulos/05_requisitos.tex`

* `REQ02` — Definir os limites quantitativos de aceitação: taxa de separação correta e dose extra, tempo por unidade, capacidade útil, repetibilidade, tensão mínima em carga, correntes, latência, disponibilidade, número de ciclos e critérios de visão/agente. Registrar justificativa e unidade; não inventar metas.

* `REQ03-MATRIZ` — Preencher a matriz final requisito--teste--evidência--resultado após a campanha. Todas as frentes permanecem no escopo; o estado de atendimento continua pendente.

### `Capitulos/06_arquitetura.tex`

* `ARQ01` — A autora enviará o subspace de arquitetura. Incorporar o diagrama da configuração final e confrontá-lo com esquema, versões e montagem real; não substituir o material prometido por inferência.

* `ARQ02` — Fornecer esquema da montagem pós-reparos, orientação de cada pogo, continuidade e fotografias identificadas. O mapa funcional disponível não comprova ordem física nem estado atual de todos os módulos.

* `ARQ04` — Confirmar a configuração na data de fechamento: hashes, versões, boot IDs, módulos montados, provisionamento e pré-condições de operação. Registrar RTC, agenda e comissionamento com evidências primárias.

### `Capitulos/07_projeto_mecanico.tex`

* `MEC01` — Inserir CAD e desenho técnico finais, revisão, cotas e relação das peças fabricadas com o modelo. A inclinação adotada é 35°; fornecer a evidência de fabricação e a medição do conjunto montado.

* `MEC03` — Conferir as dimensões da peça fabricada com instrumento, revisão e incerteza apropriados. Medir disco, cavidades, folgas, aberturas, oscilação e trajeto até o coletor. Não converter cotas do V75 em valores medidos do protótipo.

* `MEC04` — Inserir a ficha de fabricação por peça: material/marca/lote, impressora, fatiador, revisão, bico, temperaturas, camada, perímetros, preenchimento, orientação, suportes, tempo e massa. A lista de compra já foi recebida; falta a fabricação efetiva.

* `MEC05` — Completar a lista técnica instalada: parafusos por posição, ímãs e polaridade, acoplamentos, pogo, retenção, ajustes e eventual uso de adesivo. Incorporar o material complementar a ser fornecido pela autora.

* `MEC06-FOTO1` — INSERIR FOTO: vista geral do protótipo físico final, identificando revisão, módulos presentes e data. A figura CAD do artigo não substitui a fotografia.

* `MEC06-FOTO2` — INSERIR FOTOS: disco, cavidades, reservatório, placa de apoio, saída, coletor, fixação do motor e contatos. Incluir escala e legenda, sem dados pessoais.

* `MEC07` — Registrar massas, inclinação medida, atrito/ângulo de deslizamento, retenção desenergizada, folgas após impressão, desgaste e ciclos de encaixe. Para cada tipo de comprimido de teste, registrar captura simples/dupla, retenção, travamento, tentativas e falhas com denominador. Não há resultados finais fornecidos.

### `Capitulos/08_projeto_eletronico.tex`

* `ELE01` — Informar marca/modelo da fonte instalada, etiqueta, regulação, fusíveis, aterramento, proteção e cabeamento. Medir tensão na Pi e nos módulos, queda de tensão, corrente em repouso/atuação e aquecimento. Não tratar 10 A como consumo.

* `ELE02` — Conferir ordem, orientação e continuidade real de cada pogo, comprimentos, bitolas e retornos. Completar esquema elétrico pós-reparos e identificar conectores por modelo ou desenho cotado.

* `ELE03` — Medir pull-ups equivalentes, capacitância/tempos de subida e níveis do I²C com os módulos e os motores; verificar colisão de endereços, taxas de erro e comportamento no encaixe/retirada energizados. O mapa funcional não atesta integridade elétrica.

* `ELE04` — Conferir pinagem do TCRT5000 físico, resistores, alimentação e faixa ADC; obter leituras em cavidade vazia/ocupada e sob diferentes condições. Medir comportamento do motor, driver e sensor em conjunto, sem confundir leitura da cavidade com sensor de saída.

* `ELE05` — Confirmar LED adquirido/instalado, terminais A/K, corrente e brilho por cor, resistores e dissipação dos drivers. Fornecer fotos e testes de todas as posições; não assumir funcionamento dos dois intermediários a partir de uma unidade.

* `ELE06` — Identificar RTC e bateria realmente instalados; conferir carga e compatibilidade da placa, habilitação no Linux, leitura de /dev/rtc0 e teste após desligamento sem rede. A bateria do RTC não alimenta a Pi.

* `ELE07` — Fechar ensaios de buzzer, LEDs centrais, chaveamento, aquecimento, reinício e interferência em conjunto. Inserir esquema final, registros dos instrumentos e condições; confirmar capacitores/proteções acrescentados nos reparos.

* `BOM01` — Conciliar lista XLSX, proposta/contrato e eventual registro de R$ 2.512,55: revisão, data, aprovação, compras, doações, fretes e comprovantes. Não preencher custo realizado com orçamento ou campo vazio.

* `BOM02` — Completar a lista técnica instalada com sensores, conectores pogo, resistores, drivers de LEDs, buzzer/MOSFET, RTC, bateria, cabos, proteções e demais itens. Conferir a troca de WS2812B cotado pelo RGB comum documentado.

### `Capitulos/09_embarcados.tex`

* `EMB01` — Fornecer código/release final, hashes, dependências e manifesto de gravação por placa; papel, instância, endereço, site, boot ID e versão lida após reinício.

* `EMB02` — Completar tabela de estados, operações, códigos de erro e limites efetivamente ativos na versão final. Relacionar cada estado às saídas seguras e condições de recuperação.

* `EMB03` — Anexar parâmetros e registros de calibração e localização do disco utilizado: fases por volta, intervalo, leituras, limiares, dispersão, falhas e restauração após desligamento.

* `EMB04` — Fornecer relatórios de bancada de motor/sensor, duplicatas, perda de comunicação, reinício durante movimento, falha de persistência e recuperação. Separar teste simulado de execução física e identificar denominadores.

* `EMB05` — Comprovar atualização pelo barramento e recuperação de interrupção/corrupção com logs sanitizados. Não assumir assinatura, rollback ou persistência preservada sem evidência da versão.

### `Capitulos/10_backend.tex`

* `BE01-RUNTIME` — Confirmar release e hash instalados na data de fechamento, manifesto, dependências, serviços e configuração efetiva. Documentar o provisionamento ativo e a diferença entre fonte no servidor e instalação local.

* `BE02-AGENDA` — Fornecer evidência de comissionamento, tempo confiável sem rede, calibração, associação e pré-condições da agenda. Manter a declaração de operação automática pendente até ensaio de perda de rede, reinício e recuperação.

* `BE03-REDE` — Anexar roteiros e logs de pareamento, configuração/troca de Wi-Fi, senha incorreta, perda de conexão, reset e recadastramento, sem expor segredos.

* `BE04-LOCAL` — Comprovar persistência de filas e idempotência, tratamento de resultado incerto, sincronização após falha e atualização segura da Pi com interrupção controlada.

* `BE01-API` — Fornecer versão e hash da API, migrações aplicadas, esquema do banco, configuração sanitizada e manifesto dos serviços na versão final. Não atribuir versão do runtime à API.

* `BE02-CONTRATO` — Conferir os contratos atuais API--Pi, normalização de payload/hash, estados, paginação e migrações. O compilado indica uso de cancelled em fluxos de demonstração; confirmar que o tipo/coluna de produção o aceita e registrar a migração.

* `BE03-SEGURANCA` — Documentar autorização real por usuário/paciente, expiração/renovação de sessão, rotação de segredos, retenção e purga. Fornecer teste de backup/restauração e política para imagens/eventos.

* `BE04-TESTES` — Anexar resultados próprios do servidor, migrações e integração autenticada: data, ambiente, versões, comandos, aprovados, falhas e limites de simulação. Não converter relatórios históricos em aceite final.

### `Capitulos/11_aplicativo.tex`

* `APP01` — Nicolas: a autora enviará a versão e as telas do aplicativo. Inserir release/hash, ambiente, navegação e tarefas efetivamente disponíveis, além de capturas sanitizadas.

* `APP02` — Login obrigatório confirmado: inserir telas e evidências do fluxo real, emissão/validação e renovação de sessão, expiração, logout, acesso negado e mensagens de erro, sem expor credenciais.

* `APP03` — Conferir a autorização na versão final, especialmente se as visões de paciente/cuidador usam conta única. Não declarar isolamento de dados sem teste.

* `APP04` — Fornecer resultados próprios da suíte Care, integração autenticada, estados de erro/sem rede, atualização de histórico e comunicação com o aparelho. Identificar o que foi simulado.

* `APP05` — Inserir fotos/capturas atualizadas das tarefas principais e avaliação de acessibilidade/usabilidade: método, participantes quando houver, critérios, problemas e correções. Não inferir qualidade de uso pelo desenho das telas.

### `Capitulos/12_visao_computacional.tex`

* `VIS01` — Texto a fornecer por Vinicius. Inserir objetivo específico, evento observado e limites; não preencher método por inferência de telas ou contratos de integração.

* `VIS02` — INSERIR arquitetura implementada, aquisição, preparação, algoritmo/modelo, saídas, erros, versões e evidência de implantação.

* `VIS03` — INSERIR origem e autorização dos dados, anonimização, classes, rotulagem, composição e separação dos conjuntos, protocolo e referência independente.

* `VIS04` — INSERIR métricas justificadas, limiares, cenários, repetições, condições e critérios de aceitação, distinguindo confiança do modelo de certeza clínica.

* `VIS05` — SEM DADOS FINAIS: inserir resultados reais somente após recebimento dos registros do responsável.

* `VIS06` — INSERIR limites observados e fatores de generalização, falhas e condições em que o sistema deve declarar inconclusão.

### `Capitulos/13_agente_ia.tex`

* `AG01` — Thiago: confirmar modelo/rótulo, versão publicada e versão efetivamente chamada, parâmetros, instruções e ambiente na data final. Anexar definição sanitizada e hashes quando aplicáveis.

* `AG02` — Fornecer evidências das oito ferramentas, aprovação e recusa de escritas, validação do servidor, tratamento de duplicatas e falhas ambíguas. Não executar gravações de teste em dados reais.

* `AG03` — Inventariar o conteúdo efetivo do armazenamento vetorial: fontes, revisão, atualização e avaliação da recuperação, incluindo manual atual. Não assumir base atualizada por existir file_search.

* `AG04` — Anexar diálogos sanitizados e registros de chamadas/efeitos persistidos em ambiente de teste; identificar resultado parcial, erro, restauração e limpeza dos dados de teste.

* `AG05` — Definir e executar conjunto de avaliação do agente: casos, repetições, referência humana, critérios, falhas clínicas e resultados. Contagens de testes do MCP não são desempenho do modelo.

* `AG06` — Documentar permissões, rotação de chaves, limites de acesso, retenção e proteção contra instruções maliciosas em dados. Distinguir controles verificáveis de orientações do prompt.

* `AG07` — Comprovar eventual integração posterior MCP--voz--Care e tratamento de aprovação na interface. Na ausência de prova, manter a distinção v5 sem MCP e agente de teste com ferramentas.

### `Capitulos/14_testes.tex`

* `TST01` — Inserir protocolo aprovado de bancada: instrumentos, revisão, condições, comprimidos de teste, repetições, referência independente, limites de parada e critérios de aceitação. Não usar amostra exploratória como campanha final.

* `TST02` — Fornecer relatórios completos por suíte: comando de execução, versão, ambiente, casos, aprovados, falhas/erros, data e arquivos de evidência. Não somar contagens de revisões sobrepostas nem atribuí-las ao Care, à visão ou ao agente.

* `TST03` — Executar e documentar a integração de ponta a ponta e os cenários sem rede/sem NTP, somente após comissionamento. Incluir RTC, reinício, reconexão, filas e correspondência entre eventos locais e centrais.

* `TST04` — Completar os protocolos e relatórios de visão e agente com versões, dados, métricas e falhas. Distinguir servidor MCP, seleção de ferramentas, qualidade de resposta, voz e integração com o Care.

* `TST05` — Consolidar a matriz final requisito--teste--evidência--resultado, incluindo itens não executados e falhas abertas. Vincular cada resultado ao capítulo 15; não antecipar discussão ou conclusão.

### `Capitulos/15_resultados.tex`

* `RES01` — SEM DADOS FINAIS: inserir configuração efetivamente avaliada, versões, montagem, data, instrumentos e condições.

* `RES02` — SEM DADOS: inserir dimensões medidas, alimentação, corrente, aquecimento e ensaios/fotografias finais.

* `RES03` — SEM DADOS: inserir tentativas, denominadores, saída observada, falhas, doses extras, repetibilidade e recuperação.

* `RES04` — SEM DADOS FINAIS: inserir resultados próprios de software, integração autenticada, latência e tarefas da versão avaliada.

* `RES05` — SEM DADOS: inserir avaliação real de cada módulo separadamente, método, conjunto, métricas, falhas e limites.

* `RES06` — SEM DADOS: inserir protocolo, autorizações aplicáveis, participantes, tarefas e achados, caso a avaliação seja realizada.

* `RES07` — SEM DADOS FINAIS: relacionar requisito, critério, teste, evidência, resultado e limitação; não marcar atendimento automaticamente.

### `Capitulos/16_discussao.tex`

* `DIS01` — PREENCHER APÓS OS RESULTADOS: analisar achados reais por objetivo e requisito, distinguindo software e evidência física.

* `DIS02` — PREENCHER APÓS OS RESULTADOS: comparar grandezas e contextos equivalentes, sem afirmar superioridade não demonstrada.

* `DIS03` — PREENCHER APÓS OS RESULTADOS: discutir falhas, incertezas, validade e limites da integração e das inferências.

* `DIS04` — PREENCHER APÓS OS RESULTADOS: derivar melhorias das evidências, separando requisito não concluído de evolução futura.

### `Capitulos/17_conclusao.tex`

* `CON01` — PREENCHER APÓS RESULTADOS E DISCUSSÃO: responder aos objetivos somente com base no que foi demonstrado.

* `CON02` — PREENCHER APÓS OS RESULTADOS: delimitar contribuições efetivas, limitações, pendências e possibilidades futuras. Não antecipar eficácia ou segurança clínica.

### `PosTextual/anexos.tex`

* `AN-A` — Selecionar os documentos externos estritamente necessários, com autoria, referência e autorização aplicável. Não anexar automaticamente contratos assinados ou dados pessoais; remover este campo apenas após decisão editorial.

### `PosTextual/apendices.tex`

* `AP-A` — Inserir manifestos de versões/hashes, protocolos aprovados, matriz de requisitos e fichas de ensaio, com identificação e vínculo com os resultados. Evitar repetir o corpo da monografia ou inserir credenciais.

### `PreTextual/abstract.tex`

* `PRE-ABS` — Update this abstract with the final method, quantitative results, and conclusions only after the experimental campaign and Chapters 15 to 17 are completed.

### `PreTextual/agradecimentos.tex`

* `PRE-AGR` — INSERIR o texto de agradecimentos aprovado pela equipe.

### `PreTextual/dedicatoria.tex`

* `PRE-DED` — INSERIR a dedicatória da equipe, se desejada na versão definitiva.

### `PreTextual/epigrafe.tex`

* `PRE-EPI` — INSERIR a citação escolhida com autoria e fonte, ou decidir pela retirada na versão definitiva.

### `PreTextual/folhadeaprovacao.tex`

* `PRE-APROV` — Inserir data de defesa/aprovação, composição da banca, titulação, afiliação e formalização/assinaturas conforme orientação da FEI. Não há aprovação presumida nesta cópia de leitura.

### `PreTextual/resumo.tex`

* `PRE-RES` — Atualizar o resumo com método final, principais resultados quantitativos e conclusão somente após o encerramento da campanha e dos capítulos 15 a 17.

