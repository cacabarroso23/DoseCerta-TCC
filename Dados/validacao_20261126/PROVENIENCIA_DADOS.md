# Dados do aparelho e do servidor (coleta de 26/11/2026)

Coletados hoje, só por leitura, no protótipo real e no servidor. Nenhum comando foi enviado às placas nem ao motor para gerar estes dados.

## De onde veio cada tabela

| Arquivo | O que tem | Origem |
|---|---|---|
| `ledger_dc1_comandos_por_tipo.csv` | Comandos I²C por placa e operação, com o estado devolvido pela placa | Registro de comandos da central (`dc1.sqlite`), 17/10 a 26/11 |
| `ledger_dc1_por_dia.csv` | Comandos por dia e movimentos do motor | idem |
| `sessoes_do_disco.csv` | As 101 sessões de calibração, localização, dispensação e teste de ligações, com versão do software, resultado e duração | Registro de sessões da central (`index_sessions.sqlite`), 18/10 a 15/11 |
| `sessoes_do_disco_por_fase.csv` | Sessões concluídas por fase do software (antes e depois das correções de 07–08/11) | idem |
| `sessoes_do_disco_motivos_de_falha.csv` | Código de cada falha e quantas vezes ocorreu | idem |
| `dispensacao_ciclos_por_bolso.csv` | Cada ciclo de dispensação: bolso antes e depois, leitura do sensor e resultado | idem |
| `calibracoes_do_disco.csv` | Centros dos 5 bolsos, intervalos e faixas do sensor (vazio × ocupado) das 3 calibrações | Modelos de calibração salvos |
| `releases_instaladas_raspberry.csv` | As 46 releases instaladas, com data e hora | Pasta de releases da central |
| `servidor_*_relatorios_de_estado_por_dia.csv` | Relatórios de estado enviados pelo aparelho, por dia | Banco do servidor (Oficial e Simulado) |
| `servidor_*_disponibilidade_do_enlace.csv` | Intervalo entre relatórios, lacunas acima de 60 s e disponibilidade | idem |
| `servidor_*_maiores_lacunas.csv` | As 12 maiores lacunas, com início e duração | idem |
| `servidor_*_comandos_ao_aparelho.csv` | Comandos por tipo e estado, com o tempo até o reconhecimento | idem |
| `servidor_oficial_motivos_de_falha_dos_comandos.csv` | Motivo de cada comando que falhou | idem |
| `servidor_*_comandos_de_motor_por_acao.csv` | Comandos de motor por ação e estado | idem |
| `servidor_oficial_registros_de_tomada.csv` | Registros de tomada por origem, com a confiança média | idem |
| `resumo_aparelho.json` | Os números consolidados | gerado das tabelas acima |
| `graficos/` | 3 gráficos (PNG e SVG) para o capítulo de resultados | gerado das tabelas acima |
| `brutos/` | Cópia dos dois bancos do aparelho (SQLite) e o estado lido hoje às 22h10, sem identificadores de paciente | aparelho |

## Cuidados ao usar

- **Estado no registro:** o estado gravado no registro de comandos é o da placa no momento do reconhecimento. "BUSY" quer dizer que o giro ainda estava em andamento; o resultado final vem do ACK_RESULT correspondente.
- **Sessão concluída × quantidade entregue:** "concluída" é a sessão que terminou sem erro de software. O resultado físico de cada ciclo está em `dispensacao_ciclos_por_bolso.csv`.
- **Contagem humana:** não houve contagem humana por ciclo. A taxa pedido = saída depende do ensaio do fim de semana.
- **Oficial:** os relatórios diários incluem 4 relatórios de um segundo aparelho de teste (ago–set). A disponibilidade foi calculada só para o aparelho principal, a partir de 18/10, quando o intervalo de 10 s passou a valer.
- **Lacunas:** as lacunas incluem os desligamentos feitos de propósito (por exemplo, 29/10 a 02/11 e a troca do LED da câmera em 25/11).
