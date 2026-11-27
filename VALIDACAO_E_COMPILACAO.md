# Validação da integração — 27/11/2026

## Executado

- `python3 gerar_referencias.py`: 18 referências autor-data geradas, nenhuma chave citada ausente.
- `python3 validar_integracao.py`: 31 fontes LaTeX percorridas (incluindo os metadados carregados pela classe), 81 rótulos, 93 chamadas internas e 47 inclusões de figuras.
- Caminhos, balanço de chaves, ambientes, rótulos duplicados, referências sem rótulo, citações, chaves bibliográficas e integridade de imagens: nenhum erro nos controles implementados.
- 88 IDs únicos; todos os 87 anteriores preservados, ARM01 acrescentado.
- Matriz confrontada com os 25 requisitos originais; mapa fotográfico com 35 imagens únicas.
- Conferência dos CSVs: 101 sessões, 15 simulações de quantidade, 12 ciclos e três perfis de cinco intervalos. Cada perfil fecha 4.096 fases. Desvio-padrão amostral dos 15 intervalos = 11,2135 (não 10,8 amostral; este último aproxima o populacional).
- Inspeção visual das oito pranchas e dos dois gráficos gerados.

## Não executado

- Compilação pdfLaTeX, indisponível neste ambiente.
- Revisão visual do PDF completo e análise de log de uma compilação nova.
- Ensaios físicos, testes do produto, integração em produção ou aceite acadêmico.

O relatório de máquina é `validacao_estatica.json`; os controles são reproduzíveis com `python3 validar_integracao.py` (Python 3 e Pillow). Não substituem a compilação. Seguir o README para Overleaf/pdfLaTeX; não executar BibTeX/Biber nesta versão.
