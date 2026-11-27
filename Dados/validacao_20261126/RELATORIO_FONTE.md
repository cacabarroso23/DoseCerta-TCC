# Relatório de validação do DoseCerta · insumos para a monografia

**Data:** 26/11/2026. **Preparado por:** frente de mecânica, elétrica, arquitetura e programação (Rafael), com apoio de agentes de IA. **Para:** consolidação da monografia (Caroline).

Este relatório responde às perguntas feitas no grupo: **qual o cenário de teste, qual a métrica, quantos testes, que dados foram anotados em cada teste, qual critério prova que funciona e qual o nível de acerto**. Todos os números vêm de registros do próprio aparelho, do servidor ou de testes rodados hoje. Nada foi estimado à mão.

## Como ler os níveis de evidência


| Nível                      | Significado                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------- |
| **Aceito fisicamente**     | Executado no protótipo real e conferido por uma pessoa ou por uma prova física                    |
| **Registrado no hardware** | Executado no protótipo real; o resultado vem do registro do aparelho (sensor, placa, banco local) |
| **Observado em produção**  | Medido no servidor com o aparelho real conectado                                                  |
| **Testado em software**    | Testes automatizados, sem o hardware                                                              |
| **Não medido**             | Não há dado; está no plano do fim de semana (seção 7)                                             |


Uma contagem só vira taxa quando o denominador está na tabela.

---

## 1. Resumo em números


| Indicador                                                            | Valor                                                                                                                                                   | Amostra / período                        | Nível                  | Arquivo                                                                         |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ---------------------- | ------------------------------------------------------------------------------- |
| Comandos I²C (protocolo DC1) registrados e reconhecidos pelas placas | **3\.430 de 3.430** (100%)                                                                                                                              | 17/10 a 26/11, 17 dias de uso            | Registrado no hardware | `06_.../ledger_dc1_*.csv`                                                       |
| Identificadores de comando repetidos ou pulados                      | **0** (INT01: 2.669 seguidos; SUB01: 761 seguidos)                                                                                                      | mesmo período                            | Registrado no hardware | `resumo_aparelho.json`                                                          |
| Pedidos de parada (ABORT) que pararam o motor                        | **39 de 39**                                                                                                                                            | idem                                     | Registrado no hardware | `ledger_dc1_comandos_por_tipo.csv`                                              |
| Movimentos do motor com resultado reconhecido pela central           | **359 de 359**                                                                                                                                          | idem                                     | Registrado no hardware | idem                                                                            |
| Fases executadas em giros concluídos                                 | **139\.244** (≈34 voltas do disco) em 303 giros                                                                                                         | idem                                     | Registrado no hardware | idem                                                                            |
| Passo medido entre bolsos do disco                                   | **819,2 ± 10,8 fases** (mín. 806, máx. 846); nominal 819,2                                                                                              | 15 intervalos de 3 calibrações           | Registrado no hardware | `calibracoes_do_disco.csv`                                                      |
| Separação do sensor entre bolso vazio e ocupado                      | vazio ≥ 1.556; ocupado ≤ 1.139 (margem ≥ 417 contagens do ADC de 12 bits)                                                                               | 3 calibrações                            | Registrado no hardware | idem                                                                            |
| Ruído do sensor com o disco parado (1 leitura/s)                     | **média 143,4; desvio 1,2** contagens                                                                                                                   | 1\.724 leituras em 29 min (hoje)         | Registrado no hardware | `07_.../telemetria_i2c_*`                                                       |
| Leituras de estado das duas placas sem erro                          | **3\.228 de 3.228** (0 falhas, 0 reinícios)                                                                                                             | hoje, 29 min                             | Registrado no hardware | idem                                                                            |
| Localização do disco que deu certo                                   | antes da correção: **1 de 12**; depois: **5 de 9** (2 de 2 na versão atual)                                                                             | 21 tentativas                            | Registrado no hardware | `sessoes_do_disco_por_fase.csv`                                                 |
| Ciclos de dispensação conferidos pelo sensor                         | **12 ciclos**: 4 bolsos esvaziados, 2 saídas com reabastecimento, 4 comprimidos retidos, 2 sem releitura                                                | 15 sessões, 21 unidades pedidas          | Registrado no hardware | `dispensacao_ciclos_por_bolso.csv`                                              |
| Atualizações das ESP32 pelo I²C                                      | **4 aceitas**; 3 tentativas iniciais canceladas com a imagem antiga preservada                                                                          | 7 tentativas                             | Aceito fisicamente     | `05_Dados_historicos`                                                           |
| Releases instaladas na Raspberry                                     | **46** releases de 21/07 a 25/11; desde 24/10, **27** instaladas pelo atualizador com pacote assinado, 3 recusadas antes da troca e 1 revertida sozinha | —                                        | Registrado no hardware | `releases_instaladas_raspberry.csv`, `05_.../instalacoes_runtime_raspberry.csv` |
| Disponibilidade do enlace aparelho–servidor (Simulado)               | **98,9%** do tempo (29 lacunas &gt; 60 s, 3,2 h em 293,6 h)                                                                                             | 98\.722 relatórios de estado, 14 a 26/11 | Observado em produção  | `servidor_simulado_*`                                                           |
| Intervalo entre relatórios de estado                                 | mediana **10,5 s**; 99% abaixo de 11,5 s                                                                                                                | idem                                     | Observado em produção  | idem                                                                            |
| Tempo do pedido até o aparelho reconhecer (LEDs)                     | mediana **1,26 s**; máx. 12,5 s                                                                                                                         | 40 comandos, 18 a 24/10                  | Observado em produção  | `servidor_oficial_comandos_ao_aparelho.csv`                                     |
| Testes automatizados do runtime da Raspberry                         | **824** testes na versão 0.9.2; 13 rodadas completas (612 a 824 testes) sem falha nova                                                                  | 03/11 a 25/11                            | Testado em software    | `05_.../testes_software_por_rodada.csv`                                         |
| Outras suítes (rodadas independentes, não se somam)                  | API 297 (25/11); provisionamento 227 de 227 (03/11); app 293 (07/11)                                                                                    | —                                        | Testado em software    | idem                                                                            |
| Executor da campanha de caixa preta                                  | **42 de 42** testes passando                                                                                                                            | rodado hoje, 26/11                       | Testado em software    | `07_.../executor_caixa_preta_42_testes.log`                                     |
| Taxa de acerto da dispensação (pedido = saída)                       | **não medida** com contagem humana                                                                                                                      | —                                        | Não medido             | seção 7                                                                         |
| Precisão e recall da visão computacional                             | **não medidos** (não há conjunto rotulado)                                                                                                              | —                                        | Não medido             | seção 4.6                                                                       |


---

## 2. Cenário de teste: o que foi avaliado

**Bancada (configuração lida no aparelho hoje, 26/11, 22h10):**


| Item                | Valor                                                                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Central             | Raspberry Pi Zero 2 W, runtime **0\.9.2** (release `2026.11.25-cam-3`), sem subtensão (`throttled=0x0`), 53,7 °C                                                  |
| Intermediário INT01 | ESP32, endereço 0x20, firmware **0\.3.1**, gravado pelo I²C e verificado (`i2c_ota_verified`)                                                                     |
| Submódulo SUB01     | ESP32, endereço 0x30, firmware **0\.6.1**, gravado pelo I²C e verificado (`i2c_ota_verified`)                                                                     |
| Barramento          | I²C compartilhado, linhas SDA e SCL em repouso no nível alto, as duas placas presentes e válidas                                                                  |
| Disco e sensor      | disco de 5 bolsos, TCRT5000 sob o disco, silo com fita preta na face inferior (correção de 07/11), calibração ativa de 07/11 23h24                                |
| Servidor            | ambiente **Simulado** (`simulado.tcc.stacklab.dev`), aparelho pareado e on-line, relógio confiável por NTP                                                        |
| Política de travas  | `apresentacao`: um giro por vez, botão Parar e limites de giro ativos                                                                                             |
| Agenda automática   | **desligada** (bloqueios: agendas não mapeadas, comissionamento manual pendente, localização do SUB01 pendente)                                                   |
| RTC                 | módulo HW-084 (DS3231M) montado, **não ativado no Linux** (`rtc_device_present = false`); na foto da central aberta o suporte da bateria parece vazio, a conferir |


**Fotos:** 35 fotos do protótipo real, tiradas hoje, em `04_Fotos_do_prototipo`: conjunto (3), central (10), intermediário (7) e submódulo (15, com detalhes do disco, do silo e do sensor). O catálogo traz legenda pronta no padrão FEI e a pendência que cada foto atende. Sugestões: foto 01 para a vista geral (MEC06-FOTO1), 40 para o disco com o sensor (MEC06-FOTO2), 35 para a vista explodida do submódulo, 26 para os quatro contatos do encaixe (ARQ02), 16 para a central aberta (ELE02, ELE06) e 23 para os LEDs acesos (ELE05).

**Gráficos prontos:** `06_Dados_do_aparelho_e_servidor/graficos` (PNG e SVG): sessões do disco por versão, resultado dos ciclos de dispensação e passo entre bolsos.

**Três ambientes do servidor:** Oficial (uso real), Simulado (bancada e banca) e Demonstração (público). O aparelho ficou no Oficial até 14/11 e está no Simulado desde então.

---

## 3. Critérios de validação e resultado

As metas abaixo são as **propostas** no plano da campanha de caixa preta (25/11), a confirmar com o orientador. A coluna "situação" compara com o que já foi medido.


| Requisito                       | Critério proposto                                                    | O que foi medido                                                                                                                         | Situação                                            |
| ------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| RNF02 · não repetir movimento   | Nenhum identificador reutilizado; nenhum resultado incerto reenviado | 3\.430 comandos, 0 repetidos, 0 saltos; 0 execuções incertas no estado atual                                                             | **Atingido** (registro do hardware)                 |
| RNF03 · limites locais          | 100% dos pedidos de Parar efetivos                                   | 39 de 39 ABORT pararam o motor                                                                                                           | **Atingido** (amostra de 39)                        |
| Comunicação                     | Até 1 erro de I²C por 1.000 transações                               | 3\.430 comandos reconhecidos; 3.228 leituras de estado sem erro hoje                                                                     | **Atingido** (0 erros na amostra)                   |
| RF05 · calibração               | Desvio do passo entre bolsos até 15 fases                            | σ = 10,8 fases em 15 intervalos                                                                                                          | **Atingido** (amostra pequena)                      |
| RF05 · localização              | Pelo menos 98% de localizações corretas                              | 5 de 9 depois das correções de 07–08/11; 2 de 2 na versão atual                                                                          | **Não atingido / amostra insuficiente**             |
| RF01 · dispensação              | Pedido = saída em pelo menos 95%, com 60 pedidos ou mais             | 12 ciclos pelo sensor, sem contagem humana por ciclo                                                                                     | **Amostra insuficiente** (ensaio no fim de semana)  |
| RF01 · segurança                | 0 dose dupla                                                         | Não há registro de dose dupla; também não houve contagem de saída                                                                        | **Não medido**                                      |
| RF10 · atualização pelo I²C     | Toda tentativa termina em imagem válida                              | 4 aceitas + 3 canceladas com a imagem antiga ativa: 7 de 7 seguras                                                                       | **Atingido**; reversão provocada ainda não ensaiada |
| RF11 · atualização da Raspberry | Pacote assinado, com volta automática                                | 27 releases instaladas pelo atualizador desde 24/10; 3 pacotes recusados antes de trocar o serviço e 1 revertido sozinho (`rolled_back`) | **Atingido**                                        |
| RNF01 · operação sem rede       | Agenda roda sem servidor quando há relógio confiável                 | Agenda automática desligada; RTC não ativado                                                                                             | **Não atingido** (declarar como limite)             |
| Enlace com o servidor           | Pelo menos 99% de eventos sincronizados                              | 98,9% do tempo on-line no Simulado; filas vazias e 0 falhas de envio na amostra de hoje                                                  | **Quase atingido** (inclui desligamentos manuais)   |
| RF14 · visão                    | Precisão, recall e F1 com referência humana                          | Não há conjunto rotulado; a central processa ≈1,3 quadro/s                                                                               | **Não medido**                                      |


---

## 4. Resultados por frente

### 4.1 Comunicação I²C e protocolo DC1

O registro de comandos da central (`dc1.sqlite`) guarda cada comando enviado às placas, com o identificador, o código da operação e o estado devolvido pela placa. Entre 17/10 e 26/11:


| Placa         | Operação                                 | Quantidade | Estado devolvido                                                   |
| ------------- | ---------------------------------------- | ---------- | ------------------------------------------------------------------ |
| INT01         | SET_SLOT_LED (acender LED de encaixe)    | 1\.701     | 1\.701 concluídos                                                  |
| INT01         | ALL_LEDS_OFF                             | 894        | 894 concluídos                                                     |
| INT01 e SUB01 | PING                                     | 78         | 78 prontos                                                         |
| SUB01         | BENCH_JOG (giro finito)                  | 350        | 303 concluídos, 37 parados por ABORT, 10 ainda girando no registro |
| SUB01         | ACK_RESULT (reconhecer resultado retido) | 359        | 359 prontos                                                        |
| SUB01         | ABORT                                    | 39         | 39 parados                                                         |
| SUB01         | INDEX_NEXT_HOLE                          | 9          | 7 girando no registro, 2 parados                                   |


Os identificadores são contíguos e únicos por placa (INT01 de 4.714 a 7.382; SUB01 de 116 a 876), o que prova que nenhum comando foi duplicado ou reaproveitado depois de reinícios, quedas de rede ou atualizações. Hoje a coleta passiva de 29 minutos leu o estado das duas placas 3.228 vezes, sem nenhuma leitura inválida e sem reinício.

### 4.2 Mecanismo e sensor

**Calibrações salvas (3):** os centros dos bolsos ficaram em 0, 814, 1.639, 2.451 e 3.266 fases na calibração ativa. O passo médio é de 819,2 fases, igual ao nominal (4.096 fases por volta ÷ 5 bolsos), com desvio de 10,8 fases. As faixas do detector separam vazio (≥ 1.556) de ocupado (≤ 1.139) com margem de pelo menos 417 contagens.

**Sessões do disco (101), antes e depois das correções:**


| Ação              | Até a dc8-3 (antes de 07/11 20h37) | dc8-4 e dc8-5 | dc8-6 em diante                                |
| ----------------- | ---------------------------------- | ------------- | ---------------------------------------------- |
| Calibração        | 1 de 18                            | 2 de 5        | 0 de 3 (2 disco obstruído, 1 captura instável) |
| Localização       | 1 de 12                            | 3 de 7        | 2 de 2                                         |
| Teste de ligações | 20 de 22                           | —             | —                                              |


**Sessões de dispensação (15, com 21 unidades pedidas: 9 pedidos de 1 e 6 de 2):** 4 terminaram com a quantidade pedida; 4 pararam com comprimido retido; 3 pararam antes de girar porque a leitura do bolso estava ambígua; 1 parou por silo sem comprimido disponível; 3 falharam por dado do sensor desatualizado ou calibração liberada. Em todas o aparelho parou e registrou o motivo, sem girar além do pedido.

As falhas têm causa registrada: lacunas na varredura óptica (9), calibração liberada pelo operador (7), contraste insuficiente (4), disco obstruído (4). As correções de 07 e 08/11 atacaram cada uma: ritmo de amostragem da varredura (dc8-4), referência parada e fita preta sob o silo (dc8-5), posição guardada sem nova localização (dc8-6).

**Dispensação conferida pelo sensor (12 ciclos, 08 a 15/11):**


| Resultado do ciclo                        | Quantidade | Leitura do bolso antes → depois                             |
| ----------------------------------------- | ---------- | ----------------------------------------------------------- |
| Bolso esvaziado (comprimido saiu)         | 4          | ocupado (108 a 272) → vazio (1.646 a 1.917)                 |
| Saiu e o bolso foi reabastecido pelo silo | 2          | ocupado → ambíguo/ocupado                                   |
| Comprimido retido no bolso                | 4          | ocupado → ocupado, mesmo com até 2 tentativas de desprender |
| Interrompido antes da releitura           | 2          | —                                                           |


**Leitura honesta:** o mecanismo libera o comprimido, mas a retenção apareceu em 4 de 10 ciclos completos. A causa provável, registrada na bancada, é o desvio de posição do disco e a geometria do bolso com o comprimido de teste. Isso entra na discussão como limite do protótipo e como ponto de melhoria (geometria da cavidade, inclinação, raspador).

### 4.3 Atualizações sem cabo

* **ESP32 pelo I²C:** 4 atualizações aceitas no hardware (SUB 0.5.0→0.5.1, INT 0.3.0→0.3.1, SUB 0.5.1→0.6.0, SUB 0.6.0→0.6.1), com partições A/B, manifesto vinculado ao MAC, ao site e ao boot, e verificação por SHA-256. As 3 primeiras tentativas falharam no apagamento e foram canceladas com prova de que a imagem antiga continuava ativa. Hoje as duas placas rodam firmware com origem `i2c_ota_verified`.
* **Raspberry:** 46 releases instaladas entre 21/07 e 25/11. Desde 24/10, 27 foram instaladas pelo atualizador com pacote assinado e verificação de saúde; os recibos com tempo registram de 97 a 316 s por instalação, sem nenhum comando de motor e sem mudar o firmware das placas. Três pacotes foram recusados antes de trocar o serviço (trava de manutenção ocupada, manifesto com fim de linha CRLF e placas ausentes) e um foi revertido sozinho depois de falhas de comunicação.

### 4.4 Servidor e enlace


| Ambiente | Período       | Relatórios de estado | Intervalo mediano | Disponibilidade                                                                                                                 |
| -------- | ------------- | -------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Oficial  | 18/10 a 14/11 | 183\.254             | 10,45 s           | 82,2% bruto; inclui 93 h com o aparelho desligado (29/10 a 02/11) e 9,2 h do domínio vencido (04/11). Sem o desligamento: 95,9% |
| Simulado | 14/11 a 26/11 | 98\.722              | 10,53 s           | **98,9%**                                                                                                                       |


**Comandos do servidor ao aparelho (Oficial, 215):** LEDs 40 de 40 aplicados (mediana de 1,26 s até o reconhecimento); motor 56 aplicados e 34 terminados em falha com motivo registrado (os mesmos da seção 4.2); configuração 36 aplicadas, 21 falhas `config_not_available`, 19 expiradas e 7 na fila. No Simulado: 13 comandos, entre eles 6 de 7 dispensações aplicadas.

Depois do domínio vencido em 04/11, o aparelho ressincronizou sozinho, sem intervenção.

### 4.5 Software

A suíte do runtime da Raspberry passou de 100 testes (runtime 0.1.2, 18/10) para 824 (runtime 0.9.2, 25/11). Treze rodadas completas, de 03 a 25/11, têm a saída arquivada, com 612 a 824 testes cada; o único erro em todas é o antigo `test_can_hardware`, ligado ao código CAN legado. A API passou de 42 para 297 testes, e o provisionamento teve 227 de 227 aprovados na integração da dc8. Os testes criados para cada correção foram rodados também na versão antiga, para provar que detectam o defeito: dos 18 testes de ritmo da varredura, 15 falharam no runtime 0.7.9 e os 18 passaram no 0.7.10. As rodadas são independentes e não se somam; o total de 1.611 citado no pacote de 24/11 junta rodadas de datas diferentes e não deve aparecer como uma rodada só. O executor da campanha de caixa preta tem 42 testes e passou em todos hoje.

### 4.6 Visão computacional e agente (interfaces)

* A visão roda na central com MediaPipe e decide por uma regressão logística de 16 medidas. A central processa cerca de 1,3 quadro por segundo. Num teste com um gesto sintético perfeito, a confiança chega a 0,99 a partir de 4 quadros/s, mas fica entre 0,78 e 0,81 abaixo de 2,5 quadros/s; por isso a central hoje não chega a "tomada observada". A aba "Validação ao vivo" do Simulado roda o mesmo cálculo no navegador a até 8 quadros/s.
* O Oficial registra 5 eventos de tomada feitos pelo aparelho, com confiança média de 0,924, e 1 feito pela equipe. São registros de demonstração, não uma medida de acerto.
* O agente responde pelo Azure AI Foundry, lê receita por foto ou PDF e consulta o contexto do cuidado; a resposta completa caiu de 94,5 s para 11,0 s. Esses fatos são das outras frentes e devem ser confirmados pelos responsáveis.

### 4.7 Segurança


| Risco                       | Controle                                                                                                                                              | Evidência                                                                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Dose dupla por reenvio      | Identificador único e crescente; resultado incerto nunca é reenviado; um giro por vez                                                                 | 3\.430 comandos sem repetição (4.1)                                                                                 |
| Motor girando sem controle  | Limite local de fases e de tempo na ESP32 (até 4.096 fases e 30 s, corte independente aos 31 s); botão Parar                                          | 39 de 39 paradas efetivas                                                                                           |
| Dose fora de hora           | Nenhuma dose sem relógio confiável; após queda de energia, execução incerta bloqueia novas doses; dose atrasada só dentro da tolerância, sem acumular | políticas lidas no aparelho hoje: `uncertain_execution_blocks_new_doses`, `within_grace_only_no_backlog_dispensing` |
| Comprimido saiu ou não      | Confirmação humana da saída (`human_exit_count`); o sensor só confere o bolso                                                                         | dispensação agendada desligada até o comissionamento                                                                |
| Acesso indevido ao aparelho | Canal BLE com ECDH, HKDF-SHA256 e AES-256-GCM; senha do Wi-Fi só depois da autenticação mútua                                                         | seções 4.10 e 2.15 do material entregue                                                                             |
| Acesso indevido aos dados   | Login com JWT validado; credencial própria do aparelho                                                                                                | limite: conta única, as visões não isolam dados                                                                     |
| Atualização maliciosa       | Release da Raspberry assinada; imagem da ESP32 conferida por SHA-256                                                                                  | limite: a imagem da ESP32 não tem assinatura                                                                        |


---

## 5. Problemas encontrados e correções

A tabela completa está em `05_Dados_historicos/ocorrencias_e_correcoes.csv`. Os principais:


| Problema                         | Causa encontrada                                                                   | Correção                                                       | Resultado                                             |
| -------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------- |
| Localização falhava 8 de 8 vezes | A varredura perdia amostras enquanto o barramento era usado para gravar o registro | Ritmo de amostragem preservado (runtime 0.7.10)                | 2 de 2 localizações na versão atual                   |
| Furo vazio lido como ocupado     | A base do silo refletia o infravermelho do sensor                                  | Fita isolante preta sob o silo                                 | Leitura do furo vazio voltou de 61 para 1.617 a 1.625 |
| Calibração falhava parada        | Referência de vazio montada só com o disco girando                                 | Referência parada (runtime 0.7.11)                             | Calibração com silo concluída em 07/11                |
| Placa reiniciou durante o giro   | Queda de tensão (brownout) no SUB01                                                | Sessão preservada como interrompida; capacitores propostos     | Estoque não mudou; nenhum giro duplicado              |
| Posição perdida ao reencaixar    | Nova localização com disco carregado                                               | Posição guardada, sem localizar ao reencaixar (runtime 0.7.12) | Regra em vigor desde 08/11                            |
| LED âmbar parece vermelho        | Vermelho domina nesses LEDs RGB                                                    | Decisão de cor pendente                                        | —                                                     |


---

## 6. Para a conclusão: o que os dados sustentam

**Sustentam:**

* A arquitetura distribuída funciona no hardware real: mais de 3 mil comandos pelo I²C sem perda nem duplicação, e placas atualizadas sem cabo.
* As travas de segurança agiram sempre que foram exigidas: paradas, resultados incertos, comandos recusados com motivo.
* O aparelho fica conectado ao servidor quase todo o tempo e se recupera sozinho de queda de rede.
* O sensor separa bolso vazio de ocupado com folga, e o passo do disco é repetível.

**Ainda não sustentam:**

* A taxa de acerto da dispensação, por falta de contagem humana em série; há retenção em 4 de 10 ciclos.
* A operação sem rede, porque o RTC não está ativado e a agenda automática está desligada.
* O acerto da visão computacional, porque falta um conjunto rotulado e a central processa poucos quadros.

---

## 7. Ensaios físicos para fechar no fim de semana

O executor da campanha (`06_Defesa_Final/campanha`) já está pronto e testado. Ele precisa da pessoa só nos pontos de parada.


| Ensaio                                   | O que mede                                              | Preparo                                       | Duração                       | Dados anotados                                   |
| ---------------------------------------- | ------------------------------------------------------- | --------------------------------------------- | ----------------------------- | ------------------------------------------------ |
| A · localização com disco vazio          | Localizações corretas, passo, parada no furo            | Esvaziar o disco e confirmar                  | 1 a 2 h, sem intervenção      | fases, leituras do sensor, código de resultado   |
| B · dispensação com comprimidos de teste | Pedido = saída, dose dupla, retenção, tempo por unidade | Carregar o silo; contar o copinho a cada lote | 1 a 2 h, contagem a cada lote | pedido, contagem humana, leituras antes e depois |
| C · comunicação e energia                | Erros de I²C, reinícios, subtensão, temperatura         | nenhum                                        | junto com A e B               | estado das placas a cada segundo                 |
| Fotos passo a passo                      | Sequência de uma dose                                   | celular                                       | 15 min                        | uma foto por etapa                               |


A ficha de ensaio está em `FICHA_DE_ENSAIO.csv`, ao lado deste relatório.