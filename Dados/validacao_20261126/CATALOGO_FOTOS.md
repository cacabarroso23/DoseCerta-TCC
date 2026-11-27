# Catálogo das fotos do protótipo real — DoseCerta (26/11/2026)

35 fotos tiradas pelo Rafael em 26/11/2026 (recebidas pelo WhatsApp em `WhatsApp Unknown 2026-11-26 at 22.03.31.zip`). Este catálogo descreve só o que aparece nas imagens; o que depende de interpretação está marcado como **provável** ou **conferir**. Nenhuma foto foi editada: os arquivos em `organizadas\` são cópias idênticas (mesmo SHA-256) dos de `originais\`, apenas renomeadas.

## Arquivos desta pasta

| Item | Conteúdo |
|---|---|
| `originais\` | os 35 JPEG como vieram do ZIP (739 × 1600 px; um em paisagem, 1600 × 739) |
| `organizadas\` | as mesmas fotos renomeadas em ordem de passo a passo (`01`–`03` conjunto, `10`–`19` central, `20`–`26` intermediário, `30`–`39` submódulo, `40`–`44` detalhes do submódulo) |
| `FOLHA_DE_CONTATO.jpg` | miniaturas numeradas (3000 × 4880 px), cor por módulo, selo TOP nas seis melhores |
| `FOLHA_DE_CONTATO.pdf` | a mesma folha em A4 paisagem (5 páginas, 8 fotos por página) com legenda e pendências |
| `catalogo_fotos.csv` | esta tabela completa (UTF-8 com BOM, separador `;`) |

A coluna **Oxx** é a ordem cronológica dos arquivos do WhatsApp (O01 = `22.02.51`, O02 = `22.02.51 (1)`, …, O35 = `22.03.10`). A resolução é a do WhatsApp (1600 px no lado maior): suficiente para figura de meia página, não para página inteira em alta qualidade. Se houver os originais da câmera do celular, prefira-os para as figuras finais.

## Como as fotos mostram o protótipo

- **Módulo central** (base): caixa com o conector de alimentação (jaque DC em caixinha parafusada), abertura frontal onde fica o **copinho coletor** removível, e face superior com **furo de passagem** e **4 contatos dourados em losango**. Por dentro (aberta pela tampa inferior): Raspberry Pi Zero 2 W, módulo RTC DS3231, cabo flat da câmera, porta USB-A traseira, jumpers e o tubo de queda que leva o comprimido ao copinho.
- **Módulo intermediário** (corpo alto com o logotipo e a tampa): por dentro tem **4 encaixes** para submódulos em volta de uma **coluna central em cruz** com furo de passagem; cada encaixe tem um contato circular concêntrico no fundo e uma janelinha translúcida de LED. A tampa inferior leva os 4 contatos que tocam a central.
- **Submódulo** (só um aparece nas fotos): base com face curva que se encaixa no quadrante, silo cilíndrico com tampa, anel interno com placa inclinada, disco de 5 cavidades sobre a placa de apoio, TCRT5000 sob o disco, canal de saída e, na base, ESP32, motor 28BYJ-48, placa de acionamento e um conector circular na face inferior.

Interpretações a confirmar com o Rafael: a foto 15 mostra a central **de cabeça para baixo** (os 8 parafusos da tampa inferior coincidem com os 8 ressaltos vistos na foto 16); a placa preta da foto 25 é **provavelmente** a ESP32 do intermediário; o componente redondo preto da central é **provavelmente** o buzzer; a câmera em si não aparece com nitidez.

## Tabela resumo

| Nº | Arquivo organizado | Oxx | Módulo | Vista | Estado | Qualidade | Pendências | TOP |
|---|---|---|---|---|---|---|---|---|
| 01 | `01_conjunto_frente.jpg` | O02 | conjunto | frente | montado e fechado (tampa do intermediário colocada; SUBs não visíveis) | boa: foco e luz bons, enquadramento central; fundo de plástico preto amassado e objeto metálico com fios à esquerda | MEC06-FOTO1 | TOP |
| 02 | `02_conjunto_tres_quartos_esquerda.jpg` | O01 | conjunto | perspectiva 3/4 frontal esquerda | montado e fechado | boa: foco e luz bons; fundo de plástico preto e objeto metálico com fios laranja à esquerda | MEC06-FOTO1 |  |
| 03 | `03_conjunto_sem_tampa_sub_encaixado.jpg` | O21 | conjunto | perspectiva 3/4 frontal superior | intermediário sem tampa; um SUB fechado encaixado no quadrante traseiro esquerdo; LEDs apagados | boa: foco bom, luz uniforme; fundo preto e cabo à esquerda | MEC06-FOTO1; ARQ02 |  |
| 10 | `10_central_tres_quartos_frente.jpg` | O03 | central | perspectiva 3/4 frontal | montado, sem o intermediário | boa: foco e luz bons; fundo de plástico preto e cabos | ARQ02; MEC06-FOTO2 (saída/coletor) |  |
| 11 | `11_central_retirando_copinho.jpg` | O05 | central | perspectiva 3/4 lateral superior | montado; copinho sendo retirado à mão | boa: foco bom; a mão ocupa cerca de um terço do quadro | MEC06-FOTO2 (saída/coletor) |  |
| 12 | `12_central_copinho_removido.jpg` | O06 | central | perspectiva 3/4 frontal superior | montado; copinho fora, seguro em primeiro plano | boa: foco no copinho e na central; dedos no canto inferior esquerdo | MEC06-FOTO2 (coletor) |  |
| 13 | `13_central_face_superior_contatos.jpg` | O23 | central | topo (face superior voltada para a câmera, peça na mão) | montado, fora do conjunto | boa: foco nos contatos; dedo à esquerda e hub USB ao fundo | ARQ02; ELE02 |  |
| 14 | `14_central_traseira_usb.jpg` | O22 | central | traseira (paisagem, peça na mão) | montado, fora do conjunto | foco bom, mas o fundo tem tela de computador com texto legível, teclado, frasco e doce | ELE02 |  |
| 15 | `15_central_invertida_tampa_inferior.jpg` | O04 | central | por baixo (módulo de cabeça para baixo — interpretação provável) | montado e fechado | boa: foco e luz bons | BOM02 (parafusos/insertos) |  |
| 16 | `16_central_aberta_raspberry_rtc.jpg` | O24 | central | interna/aberta (tampa inferior removida, módulo invertido) | aberto e energizado (LED verde da Raspberry aceso) | boa: visão geral nítida e bem iluminada; teclado e doce no canto inferior direito | ELE02; ELE06; BOM02 | TOP |
| 17 | `17_central_raspberry_detalhe.jpg` | O25 | central | interna, close | aberto e energizado (LED verde aceso) | boa: foco na placa; cabo flat desfocado no primeiro plano | ELE02; BOM02 |  |
| 18 | `18_central_cabo_camera.jpg` | O26 | central | interna, perspectiva | aberto e energizado | média: foco bom, mas teclado e doce no topo do quadro | ELE02 |  |
| 19 | `19_central_rtc_usb_contato.jpg` | O27 | central | interna, close da parede traseira | aberto | boa: foco bom, luz quente | ELE06; ARQ02; ELE02 |  |
| 20 | `20_intermediario_sem_tampa_encaixes.jpg` | O08 | intermediário | perspectiva 3/4 superior | montado sobre a central, sem tampa, encaixes vazios, LEDs apagados | boa: foco e luz bons | ARQ02; MEC06-FOTO1 |  |
| 21 | `21_intermediario_vista_superior_contatos.jpg` | O09 | intermediário | topo (ortogonal) | sem tampa, encaixes vazios, LEDs apagados | muito boa: vista ortogonal nítida; tampa na mesa e hub USB ao fundo | ARQ02; ELE05 (posição dos LEDs) |  |
| 22 | `22_intermediario_leds_verdes.jpg` | O07 | intermediário | perspectiva 3/4 superior | sem tampa, encaixes vazios, energizado | boa: foco bom; LEDs bem visíveis | ELE05 |  |
| 23 | `23_intermediario_sub_encaixado_leds_azuis.jpg` | O20 | intermediário | perspectiva 3/4 superior | sem tampa, um SUB fechado encaixado, energizado | boa: foco bom; ponta de dedo no canto inferior esquerdo e objetos à esquerda | ELE05; MEC06-FOTO1 | TOP |
| 24 | `24_intermediario_sub_aberto_no_encaixe.jpg` | O19 | intermediário | perspectiva 3/4 superior | sem tampa; SUB sem tampa e sem disco no encaixe traseiro esquerdo; LEDs apagados | boa: foco e luz bons | ARQ02; MEC06-FOTO1 |  |
| 25 | `25_intermediario_aberto_chicote.jpg` | O28 | intermediário | interna/aberta (tampa inferior removida, módulo invertido) | aberto | boa: foco bom; lâmpada de mesa e cabos no canto superior esquerdo | ELE02; ELE05; BOM02 |  |
| 26 | `26_intermediario_tampa_inferior_pogo_fios.jpg` | O29 | intermediário | interna/aberta (tampa inferior segurada ao lado do corpo) | aberto | boa no centro; fundo com bancada, lâmpada e objetos, mão segurando a tampa | ARQ02; ELE02 | TOP |
| 30 | `30_submodulo_frente.jpg` | O10 | submódulo | perspectiva 3/4 frontal | montado e fechado, fora do intermediário | boa: foco no SUB, conjunto desfocado ao fundo | MEC06-FOTO2; BOM02 |  |
| 31 | `31_submodulo_lateral.jpg` | O11 | submódulo | lateral, próxima | montado e fechado | boa; redundante com a foto 30 | MEC06-FOTO2 |  |
| 32 | `32_submodulo_reservatorio_comprimidos.jpg` | O12 | submódulo | topo inclinado | sem tampa; com comprimidos | boa: foco e luz bons, fundo limpo (mesa) | MEC06-FOTO2 |  |
| 33 | `33_submodulo_disco_vista_superior.jpg` | O14 | submódulo | topo | sem tampa e sem o anel interno; com comprimidos | boa: foco bom; sombra leve na parte de baixo | MEC06-FOTO2 |  |
| 34 | `34_submodulo_sem_disco_lateral.jpg` | O16 | submódulo | perspectiva 3/4 lateral | sem tampa e sem disco | média: peças ao fundo pequenas; conjunto ao fundo | MEC06-FOTO2 |  |
| 35 | `35_submodulo_vista_explodida.jpg` | O18 | submódulo | vista explodida (peças lado a lado, de cima) | desmontado | boa: todas as peças nítidas; borda de tampa e conjunto cortados no topo | MEC06-FOTO2; BOM02 | TOP |
| 36 | `36_submodulo_vista_explodida_b.jpg` | O17 | submódulo | vista explodida (perspectiva) | desmontado | boa; alternativa à foto 35 | MEC06-FOTO2 |  |
| 37 | `37_submodulo_invertido_conector.jpg` | O31 | submódulo | por baixo (SUB de cabeça para baixo) | fechado | boa: foco no conector; fundo com os outros módulos | ARQ02 |  |
| 38 | `38_submodulo_aberto_motor_driver.jpg` | O32 | submódulo | interna/aberta (tampa inferior removida) | aberto | boa: foco bom; dedo na borda esquerda e chave de fenda | ELE02; BOM02; MEC06-FOTO2 (fixação do motor) |  |
| 39 | `39_submodulo_aberto_esp32.jpg` | O33 | submódulo | interna/aberta (ESP32 levantada) | aberto | boa: componentes legíveis; mão segura a tampa no topo | BOM02; ELE02; ARQ02 |  |
| 40 | `40_detalhe_disco_cavidades_sensor.jpg` | O13 | submódulo (detalhe) | topo | sem tampa e sem o anel interno; com comprimidos | muito boa: foco e luz bons, fundo limpo | MEC06-FOTO2 | TOP |
| 41 | `41_detalhe_placa_apoio_eixo_sensor_saida.jpg` | O15 | submódulo (detalhe) | topo | sem tampa, sem anel e sem disco | muito boa: foco e luz bons, fundo limpo | MEC06-FOTO2 |  |
| 42 | `42_detalhe_motor_28byj48_driver.jpg` | O34 | submódulo (detalhe) | interna, close | aberto | boa: etiqueta nítida; dedos à esquerda | BOM02; MEC06-FOTO2 (fixação do motor) |  |
| 43 | `43_detalhe_fixacao_motor.jpg` | O35 | submódulo (detalhe) | interna, close | aberto | boa: foco no motor; dedo sobre a placa | MEC06-FOTO2 |  |
| 44 | `44_detalhe_conector_submodulo.jpg` | O30 | submódulo (detalhe) | por baixo (SUB de cabeça para baixo), perspectiva | fechado | boa: foco no conector; doce, frasco e teclado no canto superior direito | ARQ02; BOM02 (pogo) |  |

Contagem: conjunto 3 · central 10 · intermediário 7 · submódulo 10 + 5 detalhes = 35.

## As seis melhores para a monografia

1. **01** (`01_conjunto_frente.jpg`) — vista geral do protótipo montado (MEC06-FOTO1); combinar com a 03 para mostrar o submódulo dentro do intermediário.
2. **40** (`40_detalhe_disco_cavidades_sensor.jpg`) — disco de 5 cavidades com comprimidos e o TCRT5000 visível por baixo (MEC06-FOTO2).
3. **35** (`35_submodulo_vista_explodida.jpg`) — vista explodida real do submódulo, pedida em 4.2.7 (MEC06-FOTO2, BOM02).
4. **26** (`26_intermediario_tampa_inferior_pogo_fios.jpg`) — os 4 contatos da tampa inferior do intermediário, cada um com seu fio colorido (ARQ02, ELE02).
5. **16** (`16_central_aberta_raspberry_rtc.jpg`) — interior da central: Raspberry Pi Zero 2 W, RTC, cabo da câmera e tubo de queda (ELE02, ELE06, BOM02).
6. **23** (`23_intermediario_sub_encaixado_leds_azuis.jpg`) — submódulo encaixado e LEDs do intermediário acesos em azul (ELE05).

Reservas fortes: **03** (conjunto aberto com SUB), **21** (vista superior ortogonal dos encaixes), **39** (ESP32 e motor do SUB com etiquetas legíveis), **19** (RTC instalado), **41** (placa de apoio e saída).

## Passo a passo sugerido (para o pedido de "foto de cada etapa")

1. Protótipo montado — **01**, **02**
2. Retirar a tampa do intermediário: 4 encaixes e coluna de passagem — **20**, **21**
3. Encaixar o submódulo no quadrante — **24**, **03**
4. Ligar: LEDs indicadores acesos — **22**, **23**
5. Retirar o copinho coletor da central — **11**, **12**
6. Central isolada e seus contatos superiores — **10**, **13**
7. Central aberta: Raspberry, RTC, câmera e fiação — **16**, **17**, **18**, **19**
8. Intermediário aberto: chicote e contatos inferiores — **25**, **26**
9. Submódulo fechado — **30**
10. Abrir o reservatório: comprimidos — **32**
11. Retirar o anel interno: disco de 5 cavidades e sensor — **33**, **40**
12. Retirar o disco: placa de apoio, acoplamento, sensor e saída — **41**, **34**
13. Peças do submódulo separadas — **35**
14. Face inferior do submódulo: conector — **37**, **44**
15. Base do submódulo aberta: ESP32, driver e motor — **38**, **39**, **42**, **43**

## Fotos sugeridas para cada pendência

### MEC06-FOTO1 — vista geral do protótipo final, identificando módulos (4.2.1)

Usar **01** (fechado) e **03** (aberto, com o submódulo no encaixe) lado a lado, com rótulos "módulo central", "módulo intermediário" e "submódulo" desenhados sobre a figura. Alternativas: 02, 20, 24. Atenção: só um submódulo foi fotografado; a figura não deve sugerir quatro SUBs montados.

### MEC06-FOTO2 — disco, cavidades, reservatório, placa de apoio, saída, coletor, fixação do motor e contatos (4.2.7)

Disco e cavidades: **40**, 33. Reservatório: **32**. Placa de apoio e canal de saída: **41** (e a abertura lateral do silo em 30). Coletor: **12**, 11. Fixação do motor: **43**, 42, 38. Contatos: 37/44 (SUB), 21 (encaixes). Vista explodida: **35** (ou 36). **Não há escala** em nenhuma foto: os comprimidos servem só como referência informal; não deduzir medidas das fotos.

### ARQ02 — orientação de cada pogo/contato e fotos identificadas da montagem pós-reparos (4.1.1, 4.2.1, 4.3.9)

Central: **13** (4 contatos em losango ao redor do furo) e **19** (fio amarelo ligado a um contato por dentro). Intermediário: **26** (4 contatos da tampa inferior com fios preto, azul, amarelo e laranja), **21** (contatos dos encaixes e 4 pinos no topo da coluna). Submódulo: **37** e **44** (conector circular). Montagem pós-reparos: 03, 24. As cores são coerentes com a convenção documentada (preto GND, azul SDA, amarelo SCL, vermelho/laranja +5 V), mas a atribuição de cada via precisa de teste de continuidade antes de ir para a legenda.

### ELE02 — fiação e conectores

**16**, 17, 18, 19 (central), **25**, **26** (intermediário), **38**, **39** (submódulo), 14 (USB-A externa, só com recorte). Mostram jumpers Dupont, termorretrátil, abraçadeiras, cola quente na USB-A e o barramento de 4 fios do SUB; não mostram o modelo do pogo nem o esquema.

### ELE05 — LEDs do intermediário

**23** (azul) e **22** (verde) com os LEDs acesos; **21** para a posição das 4 janelas; 25 para o chicote (ligações prováveis dos LEDs). Faltam vermelho, cada LED isolado e a topologia (ânodo/cátodo comum).

### ELE06 — RTC instalado

**19** (RTC DS3231 parafusado junto à parede traseira) e 16 (posição na central). O suporte da bateria **parece vazio** na foto 19 — conferir antes de afirmar bateria instalada.

### BOM02 — itens instalados

Raspberry Pi Zero 2 W: 16, 17. RTC: 19. Cabo da câmera: 18. ESP32 do SUB: **39**. Motor 28BYJ-48: **42** (etiqueta legível). Placa de acionamento: 38, 42. TCRT5000: **40**, 41. Contatos/pogo: 13, 26, 37, 44. Parafusos, porcas e insertos: 15, 16, 43. Copinho: 12. Não aparecem com nitidez: módulo da câmera, buzzer e 2N7000, ULN2003A e resistores de 330 Ω do intermediário, LEDs 5050 em close, fonte de 5 V.

## O que ainda falta fotografar

- **Escala**: régua ou paquímetro ao lado do disco, do submódulo e do conjunto (MEC06-FOTO2 pede escala).
- **LEDs acesos em cada cor** (vermelho, verde, azul) em cada encaixe, com pouca luz ambiente, e o LED da central; um LED de cada vez para identificar a posição.
- **Copinho com comprimido dispensado** e, se possível, a sequência comprimido na cavidade → saída → copinho.
- **Câmera instalada**: o módulo e sua visada sobre o copinho (hoje só aparece o cabo flat).
- **Fita isolante preta sob o silo, acima do sensor** (correção de 07/11): não é identificável em nenhuma foto.
- **Buzzer e 2N7000** em close, com a ligação visível.
- **Interior do intermediário em close**: ESP32 identificável, ULN2003A, resistores de 330 Ω e LEDs 5050 (topologia para ELE05).
- **Faces externas dos contatos** (tampa inferior do intermediário, topo da coluna, encaixes) com rótulos +5 V / GND / SDA / SCL depois do teste de continuidade.
- **Bateria do RTC**: o suporte parece vazio; fotografar com a bateria colocada (ou registrar que não há).
- **Fonte de 5 V** e o cabo ligado ao jaque DC; conjunto completo ligado.
- **Vista geral padronizada** com fundo neutro (sem o plástico preto amassado, sem tela, teclado, frasco ou doce): frente, lateral, traseira e topo, mesma luz.
- Originais em resolução da câmera (as do WhatsApp têm 1600 px no lado maior).

## Cuidados antes de usar

- **14** (`14_central_traseira_usb.jpg`): o fundo tem uma tela de computador com mensagens legíveis. Só usar com recorte apertado na peça.
- Recortar mãos, dedos, teclado, doce, frasco e hub USB quando aparecem (ver coluna "Cuidados" no CSV).
- Não descrever as marcas de cola da face superior da central (13) como defeito sem confirmar com o Rafael.
- Itens marcados como provável/conferir não devem ir para a legenda como fato.

## Fichas por foto (com legenda pronta)

Na monografia, troque **N** pelo número da figura. Legenda acima da figura e fonte abaixo, conforme o padrão FEI.

### 01 — `01_conjunto_frente.jpg`  (TOP)

- **Original:** `WhatsApp Image 2026-11-26 at 22.02.51 (1).jpeg` (O02)
- **Módulo / vista / estado:** conjunto · frente · montado e fechado (tampa do intermediário colocada; SUBs não visíveis)
- **Componentes visíveis:** módulo central na base (caixa do jaque DC parafusada, abertura frontal com copinho coletor); módulo intermediário (corpo alto com logotipo DoseCerta em relevo e tampa)
- **Qualidade:** boa: foco e luz bons, enquadramento central; fundo de plástico preto amassado e objeto metálico com fios à esquerda
- **Para a banca:** empilhamento central + intermediário, frisos de junção, saída frontal com copinho, acabamento do PLA
- **Uso sugerido:** Cap. 4, seção 4.2.1 — vista geral do protótipo físico final — pendências: MEC06-FOTO1
- **Cuidados:** recortar a faixa esquerda (objeto metálico e fios)
- **Legenda (acima da figura):** Figura N – Protótipo DoseCerta montado: módulo central na base e módulo intermediário com tampa (vista frontal)
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 02 — `02_conjunto_tres_quartos_esquerda.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.02.51.jpeg` (O01)
- **Módulo / vista / estado:** conjunto · perspectiva 3/4 frontal esquerda · montado e fechado
- **Componentes visíveis:** módulo central (caixa do jaque DC, abertura com copinho, pequena janela translúcida acima da abertura — provável LED); módulo intermediário com logotipo e tampa
- **Qualidade:** boa: foco e luz bons; fundo de plástico preto e objeto metálico com fios laranja à esquerda
- **Para a banca:** profundidade do conjunto e posição lateral do conector de alimentação
- **Uso sugerido:** Cap. 4, seção 4.2.1 — alternativa à vista frontal — pendências: MEC06-FOTO1
- **Cuidados:** recortar a faixa esquerda
- **Legenda (acima da figura):** Figura N – Protótipo DoseCerta montado em perspectiva, com o conector de alimentação e a saída do copinho coletor
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 03 — `03_conjunto_sem_tampa_sub_encaixado.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.05 (2).jpeg` (O21)
- **Módulo / vista / estado:** conjunto · perspectiva 3/4 frontal superior · intermediário sem tampa; um SUB fechado encaixado no quadrante traseiro esquerdo; LEDs apagados
- **Componentes visíveis:** central (jaque DC, abertura do copinho); intermediário aberto com coluna central em cruz e pinos no topo; SUB com tampa no encaixe; contato de um encaixe vazio
- **Qualidade:** boa: foco bom, luz uniforme; fundo preto e cabo à esquerda
- **Para a banca:** como o SUB ocupa um quadrante e fica voltado para a coluna central de passagem
- **Uso sugerido:** Cap. 4, seção 4.2.1 — passo 'inserir o submódulo no intermediário' — pendências: MEC06-FOTO1; ARQ02
- **Legenda (acima da figura):** Figura N – Protótipo com a tampa do intermediário removida e um submódulo encaixado
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 10 — `10_central_tres_quartos_frente.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.02.52.jpeg` (O03)
- **Módulo / vista / estado:** central · perspectiva 3/4 frontal · montado, sem o intermediário
- **Componentes visíveis:** face superior com furo de passagem central e 4 contatos dourados em losango; caixa do jaque DC com 2 parafusos; abertura frontal com copinho coletor; pequena janela translúcida à direita da abertura (provável LED)
- **Qualidade:** boa: foco e luz bons; fundo de plástico preto e cabos
- **Para a banca:** interface de 4 contatos que recebe o intermediário; furo por onde o comprimido desce até o copinho
- **Uso sugerido:** Cap. 4, seções 4.1.1/4.2.1 — módulo central isolado — pendências: ARQ02; MEC06-FOTO2 (saída/coletor)
- **Legenda (acima da figura):** Figura N – Módulo central isolado: furo de passagem, contatos superiores, saída frontal e conector de alimentação
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 11 — `11_central_retirando_copinho.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.02.53.jpeg` (O05)
- **Módulo / vista / estado:** central · perspectiva 3/4 lateral superior · montado; copinho sendo retirado à mão
- **Componentes visíveis:** copinho coletor saindo pela abertura frontal; face superior com 4 contatos e furo; caixa do jaque DC
- **Qualidade:** boa: foco bom; a mão ocupa cerca de um terço do quadro
- **Para a banca:** retirada do copinho pelo usuário (ergonomia da saída)
- **Uso sugerido:** Cap. 4, seção 4.2.7 — passo 'retirar o copinho' — pendências: MEC06-FOTO2 (saída/coletor)
- **Cuidados:** mão em primeiro plano
- **Legenda (acima da figura):** Figura N – Retirada do copinho coletor pela abertura frontal do módulo central
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 12 — `12_central_copinho_removido.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.01.jpeg` (O06)
- **Módulo / vista / estado:** central · perspectiva 3/4 frontal superior · montado; copinho fora, seguro em primeiro plano
- **Componentes visíveis:** copinho coletor de formato esférico com boca; abertura frontal vazia; face superior com 4 contatos e furo; caixa do jaque DC
- **Qualidade:** boa: foco no copinho e na central; dedos no canto inferior esquerdo
- **Para a banca:** forma do copinho e da cavidade que o recebe
- **Uso sugerido:** Cap. 4, seção 4.2.7 — coletor — pendências: MEC06-FOTO2 (coletor)
- **Cuidados:** dedos no canto
- **Legenda (acima da figura):** Figura N – Copinho coletor removido do módulo central
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 13 — `13_central_face_superior_contatos.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.06 (1).jpeg` (O23)
- **Módulo / vista / estado:** central · topo (face superior voltada para a câmera, peça na mão) · montado, fora do conjunto
- **Componentes visíveis:** 4 pinos dourados em losango ao redor do furo de passagem (prováveis pinos pogo); porta USB-A e par trançado laranja/preto na borda traseira; marcas de cola/resíduo na superfície
- **Qualidade:** boa: foco nos contatos; dedo à esquerda e hub USB ao fundo
- **Para a banca:** posição física dos 4 contatos da central — base para indicar +5 V, GND, SDA e SCL na figura (atribuição não visível na foto)
- **Uso sugerido:** Cap. 4, seção 4.3.9 — orientação dos contatos da central — pendências: ARQ02; ELE02
- **Cuidados:** recortar dedo e fundo; as marcas de cola aparecem
- **Legenda (acima da figura):** Figura N – Face superior do módulo central com os quatro contatos ao redor do furo de passagem
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 14 — `14_central_traseira_usb.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.06.jpeg` (O22)
- **Módulo / vista / estado:** central · traseira (paisagem, peça na mão) · montado, fora do conjunto
- **Componentes visíveis:** porta USB-A fêmea embutida na parede (recorte com rebarbas); par trançado laranja/preto saindo por furo ao lado
- **Qualidade:** foco bom, mas o fundo tem tela de computador com texto legível, teclado, frasco e doce
- **Para a banca:** acabamento do recorte da USB-A e saída do cabo
- **Uso sugerido:** Cap. 4, seção 4.3 — conectores externos (só com recorte) — pendências: ELE02
- **Cuidados:** NÃO publicar sem recorte apertado: tela com mensagens legíveis no fundo
- **Legenda (acima da figura):** Figura N – Traseira do módulo central com porta USB-A e passagem de cabo
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 15 — `15_central_invertida_tampa_inferior.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.02.52 (1).jpeg` (O04)
- **Módulo / vista / estado:** central · por baixo (módulo de cabeça para baixo — interpretação provável) · montado e fechado
- **Componentes visíveis:** tampa inferior com parafusos no perímetro; caixa do jaque DC junto à mesa; copinho visível pela abertura
- **Qualidade:** boa: foco e luz bons
- **Para a banca:** fixação da tampa inferior por parafusos (coincide com os 8 ressaltos com insertos vistos na foto 16)
- **Uso sugerido:** uso secundário — fixação da carcaça — pendências: BOM02 (parafusos/insertos)
- **Cuidados:** confirmar a orientação com o Rafael antes de legendar
- **Legenda (acima da figura):** Figura N – Módulo central invertido, mostrando a tampa inferior parafusada
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 16 — `16_central_aberta_raspberry_rtc.jpg`  (TOP)

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.06 (2).jpeg` (O24)
- **Módulo / vista / estado:** central · interna/aberta (tampa inferior removida, módulo invertido) · aberto e energizado (LED verde da Raspberry aceso)
- **Componentes visíveis:** Raspberry Pi Zero 2 W; cabo flat da câmera ('Camera Ca…' impresso); módulo RTC DS3231 azul com suporte de bateria (HW-084, provável pelo formato); traseira da USB-A com 4 fios; jumpers Dupont laranja, preto, amarelo, azul, branco e verde; termorretrátil; cinta rosa prendendo fios; tubo de queda até a câmara do copinho; insertos roscados nos 8 ressaltos; componente redondo preto (provável buzzer)
- **Qualidade:** boa: visão geral nítida e bem iluminada; teclado e doce no canto inferior direito
- **Para a banca:** distribuição interna da central, roteamento dos fios, tubo de queda; a câmera em si não aparece
- **Uso sugerido:** Cap. 3/4, seção 4.3 — fiação e componentes instalados na central — pendências: ELE02; ELE06; BOM02
- **Cuidados:** recortar teclado e doce
- **Legenda (acima da figura):** Figura N – Interior do módulo central: Raspberry Pi Zero 2 W, módulo RTC, cabo da câmera e tubo de queda até o copinho
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 17 — `17_central_raspberry_detalhe.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.07.jpeg` (O25)
- **Módulo / vista / estado:** central · interna, close · aberto e energizado (LED verde aceso)
- **Componentes visíveis:** Raspberry Pi Zero 2 W (chip RP3A0, mini-HDMI, micro-USB, cartão microSD); fios ligados diretamente nos furos do GPIO (aparentemente soldados) em azul, laranja, verde-petróleo, branco e preto; termorretrátil; componente redondo preto (provável buzzer); placa preta junto ao tubo (provável módulo da câmera)
- **Qualidade:** boa: foco na placa; cabo flat desfocado no primeiro plano
- **Para a banca:** ligação direta no GPIO sem conector; organização dos jumpers
- **Uso sugerido:** Cap. 4, seção 4.3 — detalhe da Raspberry instalada — pendências: ELE02; BOM02
- **Legenda (acima da figura):** Figura N – Detalhe da Raspberry Pi Zero 2 W no módulo central e das ligações no barramento GPIO
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 18 — `18_central_cabo_camera.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.07 (1).jpeg` (O26)
- **Módulo / vista / estado:** central · interna, perspectiva · aberto e energizado
- **Componentes visíveis:** cabo flat com 'Raspberry Pi Came…' impresso chegando a uma placa preta junto à câmara do copinho (provável módulo da câmera); Raspberry Pi Zero 2 W; tubo de queda; insertos; termorretrátil; cinta rosa
- **Qualidade:** média: foco bom, mas teclado e doce no topo do quadro
- **Para a banca:** trajeto do cabo da câmera até a região do copinho
- **Uso sugerido:** Cap. 4, seção 4.3 — câmera e cabo — pendências: ELE02
- **Cuidados:** recortar teclado e doce
- **Legenda (acima da figura):** Figura N – Cabo flat da câmera e Raspberry Pi Zero 2 W ao lado da câmara do copinho coletor
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 19 — `19_central_rtc_usb_contato.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.07 (2).jpeg` (O27)
- **Módulo / vista / estado:** central · interna, close da parede traseira · aberto
- **Componentes visíveis:** módulo RTC DS3231 azul parafusado, com suporte de bateria que parece vazio (conferir); traseira da USB-A com 4 fios fixada com cola quente; par trançado laranja/preto entrando; fio amarelo ligado ao pino de um contato que atravessa a face superior; cinta rosa presa a uma peça cinza
- **Qualidade:** boa: foco bom, luz quente
- **Para a banca:** RTC instalado e fixado; ligação real de um contato superior (amarelo = SCL pela convenção documentada — conferir)
- **Uso sugerido:** Cap. 4, seção 4.3 — RTC instalado e contatos — pendências: ELE06; ARQ02; ELE02
- **Cuidados:** não afirmar bateria instalada a partir desta foto
- **Legenda (acima da figura):** Figura N – Módulo RTC instalado no módulo central e ligações do conector USB-A e de um contato superior
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 20 — `20_intermediario_sem_tampa_encaixes.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.01 (2).jpeg` (O08)
- **Módulo / vista / estado:** intermediário · perspectiva 3/4 superior · montado sobre a central, sem tampa, encaixes vazios, LEDs apagados
- **Componentes visíveis:** 4 encaixes de submódulo; contatos circulares concêntricos dourados no fundo dos encaixes (prováveis conectores pogo magnéticos); coluna central em cruz com furo de passagem e 4 pinos no topo; janelinhas translúcidas dos LEDs (prováveis); tampa sobre a mesa; central com jaque DC
- **Qualidade:** boa: foco e luz bons
- **Para a banca:** geometria dos encaixes e da coluna de passagem
- **Uso sugerido:** Cap. 4, seção 4.2.1 — intermediário aberto — pendências: ARQ02; MEC06-FOTO1
- **Legenda (acima da figura):** Figura N – Módulo intermediário sem tampa, com os quatro encaixes de submódulo e a coluna central de passagem
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 21 — `21_intermediario_vista_superior_contatos.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.02.jpeg` (O09)
- **Módulo / vista / estado:** intermediário · topo (ortogonal) · sem tampa, encaixes vazios, LEDs apagados
- **Componentes visíveis:** 4 quadrantes de encaixe, cada um com contato circular concêntrico (um com reflexo prateado); 4 janelas quadradas translúcidas (prováveis difusores dos LEDs RGB); coluna em cruz com 4 pinos dourados em losango no topo e furo central que desce até a central
- **Qualidade:** muito boa: vista ortogonal nítida; tampa na mesa e hub USB ao fundo
- **Para a banca:** orientação de cada contato e de cada janela de LED; base para numerar os encaixes 1–4 na figura
- **Uso sugerido:** Cap. 4, seções 4.2.1/4.3.9 — orientação dos contatos — pendências: ARQ02; ELE05 (posição dos LEDs)
- **Cuidados:** recortar hub USB e tampa
- **Legenda (acima da figura):** Figura N – Vista superior do módulo intermediário: encaixes, contatos e janelas dos LEDs
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 22 — `22_intermediario_leds_verdes.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.01 (1).jpeg` (O07)
- **Módulo / vista / estado:** intermediário · perspectiva 3/4 superior · sem tampa, encaixes vazios, energizado
- **Componentes visíveis:** 2 janelas de LED do intermediário acesas em verde; LED da central aceso em verde à direita da abertura do copinho; contatos dos encaixes; coluna central
- **Qualidade:** boa: foco bom; LEDs bem visíveis
- **Para a banca:** LEDs RGB funcionando na montagem real
- **Uso sugerido:** Cap. 4, seção 4.3 — sinalização luminosa — pendências: ELE05
- **Legenda (acima da figura):** Figura N – Módulo intermediário com LEDs indicadores acesos em verde
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 23 — `23_intermediario_sub_encaixado_leds_azuis.jpg`  (TOP)

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.05 (1).jpeg` (O20)
- **Módulo / vista / estado:** intermediário · perspectiva 3/4 superior · sem tampa, um SUB fechado encaixado, energizado
- **Componentes visíveis:** SUB com tampa no encaixe traseiro esquerdo; 2 janelas de LED acesas em azul nos encaixes vazios; LED da central aceso em azul; contatos dos encaixes; coluna central
- **Qualidade:** boa: foco bom; ponta de dedo no canto inferior esquerdo e objetos à esquerda
- **Para a banca:** LEDs em outra cor e SUB encaixado ao mesmo tempo
- **Uso sugerido:** Cap. 4, seção 4.3 — sinalização luminosa — pendências: ELE05; MEC06-FOTO1
- **Cuidados:** recortar dedo e borda esquerda
- **Legenda (acima da figura):** Figura N – Submódulo encaixado e LEDs indicadores acesos em azul
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 24 — `24_intermediario_sub_aberto_no_encaixe.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.05.jpeg` (O19)
- **Módulo / vista / estado:** intermediário · perspectiva 3/4 superior · sem tampa; SUB sem tampa e sem disco no encaixe traseiro esquerdo; LEDs apagados
- **Componentes visíveis:** SUB aberto com acoplamento do motor e sensor visíveis; 2 contatos de encaixes vazios; coluna central em cruz; central com jaque DC; comprimidos sobre a mesa
- **Qualidade:** boa: foco e luz bons
- **Para a banca:** relação entre o disco do SUB, a abertura lateral e a coluna de passagem
- **Uso sugerido:** Cap. 4, seção 4.2.1 — passo 'SUB no encaixe' — pendências: ARQ02; MEC06-FOTO1
- **Legenda (acima da figura):** Figura N – Submódulo aberto encaixado no intermediário, com o acoplamento do motor e o sensor visíveis
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 25 — `25_intermediario_aberto_chicote.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.08.jpeg` (O28)
- **Módulo / vista / estado:** intermediário · interna/aberta (tampa inferior removida, módulo invertido) · aberto
- **Componentes visíveis:** chicote com fios vermelho/laranja, preto, azul, amarelo e verde; abraçadeiras de nylon brancas e pretas; termorretrátil; placa preta com barra de pinos e fios encapados (provável ESP32 do INT01); barras de pinos com fios finos azul/laranja/verde perto das janelas (prováveis ligações dos LEDs RGB — conferir); costas metálicas dos contatos dos encaixes; tubo central de queda; insertos nos ressaltos; central ao fundo
- **Qualidade:** boa: foco bom; lâmpada de mesa e cabos no canto superior esquerdo
- **Para a banca:** organização do chicote entre os 4 encaixes; distribuição do barramento
- **Uso sugerido:** Cap. 4, seção 4.3 — fiação do intermediário — pendências: ELE02; ELE05; BOM02
- **Cuidados:** recortar lâmpada e cabos
- **Legenda (acima da figura):** Figura N – Interior do módulo intermediário aberto pela base: chicote de ligação dos encaixes e dos LEDs
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 26 — `26_intermediario_tampa_inferior_pogo_fios.jpg`  (TOP)

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.08 (1).jpeg` (O29)
- **Módulo / vista / estado:** intermediário · interna/aberta (tampa inferior segurada ao lado do corpo) · aberto
- **Componentes visíveis:** tampa inferior com 4 contatos em losango ao redor do furo central, em flange em estrela; um fio em cada contato: preto, azul, amarelo e laranja (termorretrátil no preto e no azul); chicote do intermediário; central ao fundo com 4 contatos
- **Qualidade:** boa no centro; fundo com bancada, lâmpada e objetos, mão segurando a tampa
- **Para a banca:** cores coerentes com a convenção documentada (preto GND, azul SDA, amarelo SCL, vermelho/laranja +5 V) — conferir continuidade antes de afirmar
- **Uso sugerido:** Cap. 4, seção 4.3.9 — ordem física das 4 vias — pendências: ARQ02; ELE02
- **Cuidados:** recortar mão, bancada e parte inferior
- **Legenda (acima da figura):** Figura N – Tampa inferior do módulo intermediário com os quatro contatos e seus fios de ligação
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 30 — `30_submodulo_frente.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.02 (1).jpeg` (O10)
- **Módulo / vista / estado:** submódulo · perspectiva 3/4 frontal · montado e fechado, fora do intermediário
- **Componentes visíveis:** base com face curva (encaixe no quadrante); silo cilíndrico com tampa; abertura lateral arredondada no silo (provável saída para a coluna central)
- **Qualidade:** boa: foco no SUB, conjunto desfocado ao fundo
- **Para a banca:** forma externa do SUB e janela de saída
- **Uso sugerido:** Cap. 4, seção 4.2.7 — submódulo — pendências: MEC06-FOTO2; BOM02
- **Legenda (acima da figura):** Figura N – Submódulo SUB01 fechado, fora do intermediário
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 31 — `31_submodulo_lateral.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.02 (2).jpeg` (O11)
- **Módulo / vista / estado:** submódulo · lateral, próxima · montado e fechado
- **Componentes visíveis:** silo com tampa e abertura lateral; base; parafuso no canto superior da base
- **Qualidade:** boa; redundante com a foto 30
- **Para a banca:** junção entre silo e base
- **Uso sugerido:** reserva — pendências: MEC06-FOTO2
- **Legenda (acima da figura):** Figura N – Submódulo em vista lateral, com a junção entre o silo e a base
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 32 — `32_submodulo_reservatorio_comprimidos.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.03.jpeg` (O12)
- **Módulo / vista / estado:** submódulo · topo inclinado · sem tampa; com comprimidos
- **Componentes visíveis:** reservatório com placa interna inclinada e cerca de 6 comprimidos amarelos na fenda de alimentação; 3 ressaltos circulares na placa; tampa ao lado com 3 rebaixos; parafuso Phillips na base
- **Qualidade:** boa: foco e luz bons, fundo limpo (mesa)
- **Para a banca:** reservatório em uso com medicamento real
- **Uso sugerido:** Cap. 4, seção 4.2.7 — reservatório — pendências: MEC06-FOTO2
- **Legenda (acima da figura):** Figura N – Reservatório do submódulo aberto, com comprimidos sobre a placa inclinada
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 33 — `33_submodulo_disco_vista_superior.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.03 (2).jpeg` (O14)
- **Módulo / vista / estado:** submódulo · topo · sem tampa e sem o anel interno; com comprimidos
- **Componentes visíveis:** disco de 5 cavidades: 3 com comprimidos, 2 vazias; parede do silo; parafuso Phillips na base
- **Qualidade:** boa: foco bom; sombra leve na parte de baixo
- **Para a banca:** cinco cavidades e assentamento dos comprimidos
- **Uso sugerido:** Cap. 4, seção 4.2.7 — disco e cavidades — pendências: MEC06-FOTO2
- **Legenda (acima da figura):** Figura N – Disco de cinco cavidades do submódulo com comprimidos (vista superior)
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 34 — `34_submodulo_sem_disco_lateral.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.04 (1).jpeg` (O16)
- **Módulo / vista / estado:** submódulo · perspectiva 3/4 lateral · sem tampa e sem disco
- **Componentes visíveis:** silo com abertura lateral; acoplamento do motor ao fundo; parafuso na base; disco de 5 cavidades, tampa e comprimidos sobre a mesa
- **Qualidade:** média: peças ao fundo pequenas; conjunto ao fundo
- **Para a banca:** passo intermediário da desmontagem
- **Uso sugerido:** reserva / passo a passo — pendências: MEC06-FOTO2
- **Legenda (acima da figura):** Figura N – Submódulo sem o disco, com o disco e a tampa ao lado
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 35 — `35_submodulo_vista_explodida.jpg`  (TOP)

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.04 (3).jpeg` (O18)
- **Módulo / vista / estado:** submódulo · vista explodida (peças lado a lado, de cima) · desmontado
- **Componentes visíveis:** corpo (silo + base) com placa de apoio e acoplamento; anel interno com placa inclinada e 3 furos; tampa com 3 rebaixos; disco de 5 cavidades; comprimidos ao fundo
- **Qualidade:** boa: todas as peças nítidas; borda de tampa e conjunto cortados no topo
- **Para a banca:** peças mecânicas do SUB e ordem de montagem
- **Uso sugerido:** Cap. 4, seção 4.2.7 — vista explodida real — pendências: MEC06-FOTO2; BOM02
- **Legenda (acima da figura):** Figura N – Peças do submódulo desmontadas: corpo com silo e base, anel interno, tampa e disco de cinco cavidades
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 36 — `36_submodulo_vista_explodida_b.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.04 (2).jpeg` (O17)
- **Módulo / vista / estado:** submódulo · vista explodida (perspectiva) · desmontado
- **Componentes visíveis:** mesmas peças da foto 35, em perspectiva mais baixa; sensor visível dentro do silo
- **Qualidade:** boa; alternativa à foto 35
- **Para a banca:** profundidade do anel interno
- **Uso sugerido:** reserva — pendências: MEC06-FOTO2
- **Legenda (acima da figura):** Figura N – Peças do submódulo desmontadas em perspectiva
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 37 — `37_submodulo_invertido_conector.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.09.jpeg` (O31)
- **Módulo / vista / estado:** submódulo · por baixo (SUB de cabeça para baixo) · fechado
- **Componentes visíveis:** tampa inferior da base com conector circular de pinos dourados ao centro; parafuso; abertura do silo; central e intermediário ao fundo
- **Qualidade:** boa: foco no conector; fundo com os outros módulos
- **Para a banca:** onde o SUB faz contato com o encaixe
- **Uso sugerido:** Cap. 4, seção 4.3.9 — contato do SUB — pendências: ARQ02
- **Legenda (acima da figura):** Figura N – Face inferior do submódulo com o conector circular de contato
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 38 — `38_submodulo_aberto_motor_driver.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.09 (1).jpeg` (O32)
- **Módulo / vista / estado:** submódulo · interna/aberta (tampa inferior removida) · aberto
- **Componentes visíveis:** motor de passo 28BYJ-48 (carcaça com '5V', tampa azul, fios azul/rosa/amarelo/laranja/vermelho); placa verde com conector branco de 5 vias (placa ULN2003, provável); placa ESP32 de lado com fios soldados e termorretrátil; barramento de 4 fios laranja, preto, azul e amarelo; parafusos do motor
- **Qualidade:** boa: foco bom; dedo na borda esquerda e chave de fenda
- **Para a banca:** arranjo compacto de motor, driver e ESP32 na base
- **Uso sugerido:** Cap. 4, seção 4.3 — eletrônica do SUB — pendências: ELE02; BOM02; MEC06-FOTO2 (fixação do motor)
- **Cuidados:** recortar dedo
- **Legenda (acima da figura):** Figura N – Interior da base do submódulo: motor de passo 28BYJ-48, placa de acionamento e ESP32
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 39 — `39_submodulo_aberto_esp32.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.09 (2).jpeg` (O33)
- **Módulo / vista / estado:** submódulo · interna/aberta (ESP32 levantada) · aberto
- **Componentes visíveis:** placa ESP32 DevKit (módulo ESP-WROOM-32 com blindagem, micro-USB, botões) ligada por 4 fios amarelo, azul, preto e laranja ao conector que atravessa a tampa inferior; motor com etiqueta 'STEP MOTOR 28BYJ-48 5V DC'; borda da placa verde do driver
- **Qualidade:** boa: componentes legíveis; mão segura a tampa no topo
- **Para a banca:** identificação inequívoca da ESP32 e do motor; ligação de 4 vias do SUB
- **Uso sugerido:** Cap. 3/4 — lista de materiais e eletrônica do SUB — pendências: BOM02; ELE02; ARQ02
- **Cuidados:** recortar mão
- **Legenda (acima da figura):** Figura N – ESP32 do submódulo e ligação de quatro fios ao conector da tampa inferior
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 40 — `40_detalhe_disco_cavidades_sensor.jpg`  (TOP)

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.03 (1).jpeg` (O13)
- **Módulo / vista / estado:** submódulo (detalhe) · topo · sem tampa e sem o anel interno; com comprimidos
- **Componentes visíveis:** disco de 5 cavidades: comprimidos em 3 (duas com pilha) e 2 vazias; por uma das vazias aparece, embaixo, o sensor TCRT5000 (corpo preto, emissor azul)
- **Qualidade:** muito boa: foco e luz bons, fundo limpo
- **Para a banca:** prova visual de que o sensor fica sob o disco e lê a cavidade
- **Uso sugerido:** Cap. 4, seção 4.2.7 — disco, cavidades e sensor — pendências: MEC06-FOTO2
- **Legenda (acima da figura):** Figura N – Disco de cinco cavidades com o sensor TCRT5000 visível através de uma cavidade
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 41 — `41_detalhe_placa_apoio_eixo_sensor_saida.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.04.jpeg` (O15)
- **Módulo / vista / estado:** submódulo (detalhe) · topo · sem tampa, sem anel e sem disco
- **Componentes visíveis:** placa de apoio com acoplamento branco do eixo do motor (fenda + 4 pontos metálicos, prováveis parafusos ou ímãs); TCRT5000 saindo por janela retangular; canal de saída semicircular; 2 parafusos de fixação da placa; parafuso na base
- **Qualidade:** muito boa: foco e luz bons, fundo limpo
- **Para a banca:** placa de apoio, saída e fixação; a fita isolante sob o silo não é identificável
- **Uso sugerido:** Cap. 4, seção 4.2.7 — placa de apoio, saída e acoplamento — pendências: MEC06-FOTO2
- **Legenda (acima da figura):** Figura N – Placa de apoio do submódulo sem o disco: acoplamento do eixo do motor, janela do sensor e canal de saída
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 42 — `42_detalhe_motor_28byj48_driver.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.09 (3).jpeg` (O34)
- **Módulo / vista / estado:** submódulo (detalhe) · interna, close · aberto
- **Componentes visíveis:** motor 28BYJ-48 com etiqueta legível ('STEP MOTOR 28BYJ-48 5V DC'); placa verde do driver com conector branco de 5 vias (provável ULN2003); verso da placa ESP32 com serigrafia 'ESP32 DEVKIT…'; parafusos Phillips e porcas sextavadas; fios com termorretrátil
- **Qualidade:** boa: etiqueta nítida; dedos à esquerda
- **Para a banca:** modelo do motor legível na peça instalada
- **Uso sugerido:** Cap. 4, seção 4.2.7/4.3 — motor e driver — pendências: BOM02; MEC06-FOTO2 (fixação do motor)
- **Cuidados:** recortar dedos
- **Legenda (acima da figura):** Figura N – Motor de passo 28BYJ-48 e placa de acionamento no interior do submódulo
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 43 — `43_detalhe_fixacao_motor.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.10.jpeg` (O35)
- **Módulo / vista / estado:** submódulo (detalhe) · interna, close · aberto
- **Componentes visíveis:** motor 28BYJ-48 de frente com etiqueta; flange parafusada (parafuso Phillips + porcas sextavadas); resistor em linha com termorretrátil (provável); placa do driver; chave de fenda e parafuso solto na mesa
- **Qualidade:** boa: foco no motor; dedo sobre a placa
- **Para a banca:** fixação mecânica do motor
- **Uso sugerido:** Cap. 4, seção 4.2.7 — fixação do motor — pendências: MEC06-FOTO2
- **Cuidados:** recortar dedo e metade superior
- **Legenda (acima da figura):** Figura N – Fixação do motor 28BYJ-48 por parafusos e porcas no submódulo
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

### 44 — `44_detalhe_conector_submodulo.jpg`

- **Original:** `WhatsApp Image 2026-11-26 at 22.03.08 (2).jpeg` (O30)
- **Módulo / vista / estado:** submódulo (detalhe) · por baixo (SUB de cabeça para baixo), perspectiva · fechado
- **Componentes visíveis:** conector circular com anel metálico e vários pinos dourados (provável conector pogo magnético que casa com o contato do encaixe); parafuso; abertura inferior do silo
- **Qualidade:** boa: foco no conector; doce, frasco e teclado no canto superior direito
- **Para a banca:** tipo de contato do SUB
- **Uso sugerido:** Cap. 4, seção 4.3.9 — contato do SUB — pendências: ARQ02; BOM02 (pogo)
- **Cuidados:** recortar canto superior direito
- **Legenda (acima da figura):** Figura N – Detalhe do conector circular na face inferior do submódulo
- **Fonte (abaixo da figura):** Fonte: Autores (2026)

> **Nota de privacidade (26/11, 22h45):** na foto 14 (`14_central_traseira_usb.jpg` e o original correspondente), a tela de computador ao fundo foi desfocada antes do envio, porque mostrava mensagens de outros projetos. A peça fotografada não foi alterada.
