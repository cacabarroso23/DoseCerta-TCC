# Validação da revisão integral — 27/11/2026

## Controles executados

* Regeneração das referências a partir da árvore ativa: 15 entradas citadas; nenhuma chave citada ausente.
* Checagem estática: 36 arquivos TeX ativos, 102 rótulos, 121 referências internas, 59 inclusões de figuras e 87 pendências abertas; zero erros e zero avisos nos controles implementados.
* Conferência de caminhos de imagens e PDFs incluídos, chaves, ambientes, rótulos duplicados, referências sem rótulo, citações sem entrada e comandos de listas/sumário.
* Conferência de que as figuras possuem chamada fora de seu ambiente. Isso não comprova adequação visual de cada chamada.
* Expansão da árvore ativa para conferir a sequência das figuras 7–10: `fig:prototipo_montado`, `fig:cad_v75`, `fig:dosador_explodido`, `fig:montagem_2026`.
* Soma das larguras proporcionais declaradas das tabelas `longtable`: nenhuma acima da largura disponível. Isso não avalia palavras ou conteúdo que possam extravasar dentro de uma célula.
* Conferência de cinco capítulos principais e dois apêndices na árvore ativa; numeração corrida para figuras e tabelas.
* Regeneração de `PENDENCIAS_ABERTAS.json` e `.txt` a partir dos mesmos comandos que produzem os marcadores vermelhos. IDs encerrados não se repetem na lista aberta.
* Verificação de sintaxe Python dos scripts de bibliografia e validação.

## Compilação não realizada

A tentativa de `python3 compilar_banca.py` terminou com código 2 e a mensagem de pdfLaTeX indisponível. Não foi produzido PDF atualizado. Não há certificação de paginação, margens, conteúdo efetivamente gerado nas listas, ausência de `??` no PDF, recortes finais, legibilidade ou ausência de caixas com extravasamento.

Os comandos de listas e sumário estão presentes nos fontes. As referências internas têm rótulos correspondentes, mas precisam das passagens de compilação para serem resolvidas no PDF. As imagens foram limitadas à área útil e as tabelas receberam larguras declaradas; essas alterações não substituem a revisão visual.

## Validação a executar antes da banca

1. Importe o ZIP completo em um projeto novo do Overleaf e selecione `main.tex` e pdfLaTeX.
2. Recompile do zero; aguarde a estabilização das referências e listas.
3. Verifique sumário, listas de figuras/tabelas e ordem de capítulos, referências e apêndices.
4. Confira as figuras 7–10 e todas as demais chamadas, legendas e fontes, a resolução das fotos e a ausência de figuras inseridas no meio de parágrafos.
5. Revise as tabelas, quebras e margens em todo o PDF e trate os avisos do log; não confunda larguras declaradas com resultado visual garantido.
6. Confirme dados institucionais e as 87 pendências. Só retire marcadores quando a informação ou evidência estiver disponível.

Localmente, `compilar_banca.py` executa até seis passagens e cria `CHECAGEM_COMPILACAO.json` após uma compilação concluída, sinalizando referências indefinidas, listas sem entradas e extravasamentos. Uma execução sem esses avisos ainda precisa de inspeção visual.

## Limites de evidência

Nenhum teste físico, integração em produção, reexecução das suítes do produto ou auditoria clínica/de segurança foi realizado nesta revisão. Números incorporados representam os registros disponíveis e preservam a distinção entre contagem física, observação humana, estado de software e resultado de teste automatizado. O escopo multipaciente não foi reaberto; é trabalho futuro.

Os relatórios com nomes em minúsculas e os documentos de rodadas anteriores são históricos. O controle estático atual é `CHECAGEM_ESTATICA.json`; a lista atual é `PENDENCIAS_ABERTAS.*`.
