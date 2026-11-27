# Pacote para a Carol (27/11/2026)

Parte do Nicolas (aplicativo, dados e integração) e material de apoio para os resultados.
Tudo foi testado dentro de uma cópia atualizada do repositório `DoseCerta-TCC`: **compila com pdfLaTeX sem erro, sem referência quebrada e sem estouro de margem (102 páginas)**. A prévia está em `PREVIA_monografia_com_as_alteracoes.pdf`.

## O que tem aqui

| Pasta ou arquivo | O que é | Como usar |
|---|---|---|
| `PREVIA_monografia_com_as_alteracoes.pdf` | A monografia inteira já com tudo abaixo aplicado | Só para ler e conferir |
| `monografia/Capitulos/11_aplicativo.tex` | **Capítulo 11 reescrito** com 16 prints novos | Substitui o original |
| `monografia/Capitulos/10b_dados_rastreabilidade.tex` | **Seção nova**: camada de dados e rastreabilidade (SQLite da Pi, PostgreSQL, dois ambientes, volumes) | Acrescentar `\input{Capitulos/10b_dados_rastreabilidade}` no fim do `10_backend.tex`, logo antes de "Complementações necessárias" |
| `monografia/Capitulos/15_resultados.tex` | **Capítulo 15** com todos os dados reais que existem hoje, mais as seções reservadas para a campanha | Substitui o original |
| `monografia/Capitulos/tabela_ensaios.tex` e `tabela_ensaios_simulado.tex` | Tabelas usadas pelo capítulo 15 | Copiar para `Capitulos/` |
| `monografia/Capitulos/13_agente_ia.tex` | **Proposta** de correção do capítulo 13 (versões atuais do agente e a limitação da aprovação) | Revisar com o Thi antes de substituir |
| `monografia/Capitulos/12_visao_computacional.tex` | **Base** do capítulo 12 para o Vini (pipeline v2 documentado, pendências da v3) | Passar para o Vini completar |
| `monografia/PosTextual/apendices.tex` | **Apêndice A**: protocolo de ensaio, ficha e matriz requisito × ensaio | Substitui o original |
| `monografia/Figuras/App/` | 16 prints do app (dados fictícios) | Copiar para `Figuras/App/` |
| `protocolo/PROTOCOLO_CAMPANHA.md` | Protocolo operacional da campanha (para a bancada) | Levar para o orientador aprovar os critérios |
| `protocolo/ficha_ensaio.csv` | Modelo da ficha por ensaio | Abre no Excel |
| `dados/` | CSVs com os ensaios reais (ambiente oficial e simulado) | Evidência do capítulo 15 |
| `ferramentas/exportar_campanha.py` | Gera a ficha, a tabela LaTeX e as taxas com IC direto do banco, depois da campanha | Nicolas roda |
| `prints/` | Os mesmos 16 prints, para usar em slides | — |

## Correções pontuais em outros capítulos (não incluídas como arquivo)

1. **Versão do runtime da Pi:** onde aparece 0.7.12 (pendência ARQ04 no cap. 6) e 0.7.7 (fonte da Figura de serviços no cap. 10), a versão instalada hoje é **0.8.0**.
2. **Cap. 6 e cap. 10:** citar que existem **dois ambientes** (oficial e simulado), detalhados na nova Seção 10.x.
3. **Cap. 4 (Metodologia):** dizer que os ensaios usam o fluxo de dispensação vinculada do app e o protocolo do Apêndice A.
4. **Referências:** os links internos apontam para um OneDrive corporativo da General Motors (`generalmotors-my.sharepoint.com/...`). A banca não abre esses links e eles expõem a conta de alguém. Trocar por "documento interno do projeto" (sem URL) ou colocar o material no apêndice.
5. **Referências não citadas:** `FEI-bib/dosecerta_adicionais.bib` tem 13 referências acadêmicas boas que nunca entram no PDF, porque o `gerar_referencias.py` só lê `dosecerta-referencias.bib`. Exemplos: OMS (2003) sobre adesão, Paterson (2017) e Faisal (2021) sobre dispensadores, Patel (2020) sobre usabilidade com idosos, Kopetz e Lee & Seshia sobre sistemas embarcados.
6. **Folha de rosto:** aparece o rótulo solto "Folha de rosto" no topo da página 2. Vem da redefinição de `\imprimirfolhaderosto` no `main.tex`.

## Sobre os prints

- Todos usam a paciente fictícia **Helena Martins** (perfil de demonstração do app, que roda só no navegador). Nenhum dado real aparece.
- O login (`00_login.jpg`) é a tela real do perfil oficial, sem nada digitado.
- Os prints do assistente (`10`, `11`, `12`) foram feitos com um servidor local que responde no mesmo protocolo do app. As respostas são roteirizadas; a da receita (`12`) reproduz o texto que o agente real deu em 17/11 para a mesma receita fictícia. A legenda da figura diz isso.
- Na demo pública o botão de anexo fica desligado. Para o print `11`/`12` ele foi ligado numa cópia local, igual ao app oficial.
- A tela de conversa por voz não pôde ser capturada (o navegador usado bloqueia o microfone). Se quiser, tirar no celular.

## Números principais (para conferir)

- **Ambiente oficial (18/10 a 09/11):** 8 dispensações integradas: 3 saídas confirmadas, 3 recusas seguras antes de mover, 2 comprimidos retidos. Nenhuma dose extra; estoque coerente 8/8.
- **Sensor:** vazio 2755–2952, ocupado 104–157 (ADC de 12 bits).
- **Calibração:** 3/26; localização 4/9 (principal gargalo).
- **Comandos:** 207 até 12/11, 205 em estado final, nenhum reexecutado; LEDs 40/40 + 18/18 (26/11).
- **Ambiente simulado (desde 14/11):** 7 dispensações, 5 fechadas automaticamente sem contagem humana. Não servem como acurácia.
- **Telemetria:** a Pi ficou conectada 91–94% do tempo entre 15 e 25/11.

## O que ainda falta (não depende de texto)

1. **Aprovar os critérios** do protocolo com o orientador, **antes** dos ensaios.
2. **Rodar a campanha** (blocos A a F) com contagem humana e foto de cada ensaio, de preferência no ambiente **oficial**.
3. Vini: exportar os resultados da visão da Pi e avaliar contra referência.
4. Thi: conjunto de casos de teste do agente; decidir se corrige a aprovação das escritas.
5. Nicolas: corrigir as falhas dos testes do app e registrar a contagem final; conferir a versão publicada.
