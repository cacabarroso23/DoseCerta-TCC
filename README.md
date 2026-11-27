# DoseCerta — versão integrada para revisão, 27/11/2026

Esta é uma versão de trabalho, não a monografia final nem a validação do produto.

## Abrir e compilar

Importe o ZIP completo em um projeto separado do Overleaf. Selecione `main.tex` como principal e pdfLaTeX. Compile do zero e repita até estabilizar sumário, listas e referências. Não execute BibTeX/Biber: `referencias.tex` já está incluído. Se alterar citações ou a base `.bib`, execute `python3 gerar_referencias.py` antes de recompilar.

Localmente, com TeX Live/MiKTeX, execute três vezes:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

**Não foi possível compilar neste ambiente. Não há PDF novo neste pacote.** Não confundir `main.pdf` enviado com um PDF desta revisão. A inspeção visual das pranchas e gráficos não é revisão da paginação integral.

## O que mudou

- Metodologia, autoria das frentes e declaração de apoio de IA do GitHub preservadas/conciliadas.
- Arquitetura e configuração de 26/11; Oficial, Simulado com aparelho real e Demonstração sem hardware separados.
- Erratas da mecânica, inclinação 30/35 graus não resolvida, leitura com reservatório e posição persistida.
- RTC não ativo, alimentação sob carga, L4 18/17/16, LEDs comuns versus item WS2812B do orçamento e hash versus assinatura nas atualizações ESP32.
- Trinta e cinco fotos em oito pranchas, com mapa dos arquivos de origem; dois gráficos a partir dos CSVs.
- Visão com aquisição, landmarks, ROI, equações, limiares, máquina de estados e protocolo. Divergência com regressão logística mantida em aberto; sem métricas inventadas.
- Conta compartilhada, privilégios/RLS e diferença entre aprovação do Foundry e autorização do serviço explicitadas.
- Agente: arquitetura histórica preservada; relatos posteriores de Voice Live identificados como sujeitos à confirmação da frente.
- Resultados, discussão e conclusão agora têm redação baseada nos dados disponíveis, não apenas campos vazios.
- Resumo/abstract atualizados, matriz dos 25 requisitos e fontes de dados no apêndice.
- Os 87 IDs de pendência anteriores foram preservados e delimitados; ARM01 acrescentado para conservação fora do blister. São 88 pendências, não 88 ausências de implementação.

## Roteiro da sua leitura

1. Leia `ALTERACOES_20261127.md` e as ressalvas de compilação.
2. Confira primeiro os capítulos 12, 15, 16 e 17, depois os capítulos técnicos 4–10 e 13.
3. Verifique com os responsáveis a inclinação, o método de visão instalado e o agente atual.
4. Confira as fontes e notas de cada tabela. Sessão concluída, ACK, leitura vazia e contagem física não são equivalentes.
5. Revise as fotos/legendas, a macro vermelha, capa, folha de rosto, sumário, listas e quebras após compilar.
6. Use `PERGUNTAS_PARA_CONTRIBUIDORES.md` para resolver as lacunas; não remova o vermelho sem evidência.

## Organização

`Capitulos/`, `PreTextual/`, `PosTextual/`, `classe/` e `FEI-pre-textual.tex` compõem o modelo. A classe foi preservada nesta integração. `FEI-bib/dosecerta-referencias.bib` e `referencias.tex` guardam as referências. `Dados/validacao_20261126/` contém tabelas e documentos-fonte selecionados, não bancos brutos ou scripts do ZIP recebido. `Figuras/Validacao20261126/` contém os novos elementos. `mapa_fotos_20261126.json` vincula os painéis aos originais.

A conferência SharePoint fornecida pela autora foi preservada em `CONFERENCIA_SHAREPOINT_REFERENCIA.md`; o guia antigo em `PERGUNTAS_PARA_CONTRIBUIDORES_ANTES_DA_INTEGRACAO.md` é histórico. O guia atual é gerado do inventário de pendências desta versão.

Nenhum teste físico ou suíte do produto foi executado, nenhum comando foi enviado ao aparelho e nenhum commit/push foi feito. Os testes estáticos locais não provam compilação, aceite, conformidade ou completude bibliográfica.
