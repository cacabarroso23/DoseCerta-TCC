# Protocolo da campanha de validação do DoseCerta

**Status: PROPOSTA.** Os critérios de aceitação precisam ser aprovados pelo orientador antes do primeiro ensaio. Se forem mudados depois de ver os resultados, a validação perde valor.

---

## 1. Objetivo

Medir, com dados contáveis e anotados um a um, se o DoseCerta:

1. libera a quantidade pedida (acurácia da dispensação);
2. nunca libera unidade a mais (segurança);
3. mantém o estoque do app igual ao estoque físico (integridade dos dados);
4. não repete movimento depois de falha de rede ou de energia (recuperação);
5. distingue cavidade vazia de ocupada pelo sensor óptico;
6. acende o LED certo em cada posição.

## 2. Configuração do ensaio (registrar ANTES de começar)

| Item | O que anotar |
|---|---|
| Ambiente | **Oficial** (`dosecerta-ambiente oficial`, política `rigoroso`). Se for usar o Simulado, fechar TODO ensaio com a contagem humana |
| Versões | Runtime da Pi, firmware INT-01 e SUB-01, webapp e API (o app mostra; conferir também no servidor) |
| Submódulo e posição | Ex.: SUB-01 na posição 1 do INT-01 |
| Comprimido de teste | Nome ou tipo, diâmetro e espessura medidos com paquímetro, massa. **Um único tipo por bloco** |
| Disco | Revisão do disco e inclinação montada (medir) |
| Estoque inicial | Contar à mão quantas unidades foram colocadas no reservatório e registrar no app |
| Pessoas | Quem opera o app, quem conta o copo, quem fotografa |
| Data, hora e local | Bancada, iluminação (afeta o sensor) |

Fotografar a montagem completa, com régua ou escala, antes do primeiro ensaio.

## 3. Preparação

1. Ligar o aparelho e conferir no app: aparelho conectado, submódulo vinculado à posição certa.
2. Rodar o **teste de ligações** na área de testes e confirmar visualmente LEDs, buzzer e motor.
3. Com o disco **vazio**, rodar **calibração** e **localização** até concluírem. Anotar quantas tentativas foram necessárias, porque isso também é dado.
4. Abastecer o reservatório com a quantidade contada e registrar a reposição no app.
5. Copo coletor vazio.

## 4. Procedimento de cada ensaio (dispensação vinculada)

1. Escrever num papel o número do ensaio (ex.: `A-07`) e deixar visível perto do copo.
2. No app: **dispensação vinculada**, escolher paciente, medicamento e quantidade.
3. Aguardar o resultado do aparelho na tela. **Não repetir o pedido** enquanto ele não terminar.
4. Contar as unidades que caíram no copo. Essa contagem é a **referência** do ensaio.
5. **Foto 1**: copo de cima, mostrando as unidades e o papel com o número do ensaio.
6. **Foto 2**: tela do app com o resultado e o identificador da operação.
7. No app, registrar a observação: quantas unidades saíram, ou "não observado".
8. Anotar na ficha qualquer coisa estranha: travou, fez barulho, comprimido preso, unidade quebrada.
9. Esvaziar o copo e guardar as unidades **fora** do reservatório (não devolver durante o bloco).
10. A cada 10 ensaios, contar o estoque físico restante e comparar com o app.

Nome das fotos: `A-07_1.jpg` e `A-07_2.jpg`, todas numa pasta por bloco.

## 5. Blocos de ensaio

| Bloco | O que | N | Critério de aceitação (proposta) |
|---|---|---|---|
| **A** | Dispensar 1 unidade | **50** | ≥ 90% com exatamente 1 unidade no copo; **0 doses extras** |
| **B** | Dispensar 2 unidades | 20 | ≥ 85% com exatamente 2; 0 doses extras |
| **C** | Falha forçada durante o giro: 10× desligar o Wi-Fi, 5× reiniciar a Pi, 5× tirar a energia do SUB | 20 | **0 movimentos repetidos**; o app mostra "incerto" e pede reconciliação |
| **D** | Sensor: 30 leituras com cavidade vazia e 30 com cavidade ocupada | 60 | Faixas sem sobreposição; ≥ 95% classificadas corretamente |
| **E** | LEDs: 4 posições × 3 cores, com observação visual | 12 | 12/12 acendem a posição e a cor pedidas |
| **F** | Agenda sem internet (só se houver RTC instalado) | 5 | 5/5 executadas no horário. Sem RTC: declarar "não testado" |

Em todos os blocos:
- **Estoque:** 100% de coincidência entre o estoque do app e a contagem física.
- **Tempo:** registrar do pedido ao resultado (o banco grava sozinho).

### Regras de parada
- Três travamentos seguidos: parar, anotar, corrigir. O bloco **recomeça do zero** depois de qualquer ajuste mecânico.
- Não mudar o comprimido nem o disco no meio de um bloco.
- Ensaio em que alguém esqueceu de contar ou fotografar: **conta como inválido**, não vira sucesso.

## 6. Como reportar (para o capítulo 15)

Para cada bloco: N, acertos, taxa e **intervalo de confiança de 95% (Wilson)**. Exemplos:

| Resultado | Taxa | IC 95% |
|---|---|---|
| 47/50 | 94,0% | 83,8% a 97,9% |
| 48/50 | 96,0% | 86,5% a 98,9% |
| 50/50 | 100% | 92,9% a 100% |
| 0 doses extras em 50 | 0% | a taxa real fica abaixo de ~6% (regra dos três) |

O script `ferramentas/exportar_campanha.py` gera a ficha e as tabelas direto do banco, a partir da data e hora de início do bloco.

## 7. Matriz requisito × ensaio

| Requisito | Ensaio | Evidência |
|---|---|---|
| RF01 liberar quantidade programada | A, B | Ficha + fotos + banco |
| RF02 indicar posição por luz | E | Ficha + foto |
| RF04 reler a cavidade após liberar | A, D | Leituras antes/depois no banco × contagem humana |
| RF05 calibrar e localizar | Preparação (tentativas) | Banco |
| RF06 registrar com origem e sincronizar | A–C | `domain_event` / `device_command` |
| RNF01 operar sem rede | F | Ficha (ou "não testado") |
| RNF02 não repetir movimento | C | Banco + ficha |
| RNF03 limites locais | C | Banco |
| RF13-APP login e acompanhamento | Todos | Fluxo usado em todos os ensaios |
