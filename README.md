# Validação da rodada 2 — 27/11/2026

## Executado nesta rodada

- Inventário do ZIP antes da leitura e extração seletiva; nenhum script recebido executado.
- Identidade SHA-256 entre a prévia PDF externa e a interna do ZIP: confirmada.
- Preservação byte a byte do relatório-fonte e da conferência SharePoint editados; histórico de alterações anterior mantido como prefixo.
- `python3 gerar_referencias.py`: 19 entradas citadas geradas, nenhuma chave ausente.
- `python3 validar_integracao.py`: 34 fontes LaTeX percorridas, 95 rótulos, 111 chamadas internas, 59 inclusões de figuras.
- Caminhos, balanço de chaves, ambientes, rótulos duplicados, referências sem rótulo, citações, chaves bibliográficas e imagens: nenhum erro nos controles implementados.
- 88 IDs de pendência anteriores preservados; matriz dos 25 requisitos mantida.
- 35 fotos únicas no mapa anterior; 16 novas capturas de aplicativo verificadas em pranchas de contato. Inspeção visual das pranchas não é revisão de paginação integral.
- CSV Oficial: oito linhas, uma sem quantidade/estoque posterior e uma temporalmente inconsistente; seis linhas restantes com consistência aritmética do estoque registrado. Não equivale a estoque físico medido.
- CSV Simulado: sete linhas; quatro fechamentos automáticos, dois relatos de demonstração e uma sem fechamento; cinco sem quantidade humana.
- URLs corporativas ausentes de `referencias.tex` gerado. Documentos de proveniência internos podem conservar seus links de origem.
- Contagens/calibrações da rodada anterior continuam verificadas; não foram somadas a recortes sobrepostos.

## Não executado

- Compilação pdfLaTeX, indisponível neste ambiente.
- Revisão visual do PDF unificado, certificação de margens ou número final de páginas.
- Validação de comandos/serviços em produção ou reexecução das suítes do produto.
- Campanha física, auditoria de segurança, autorização por paciente ou confirmação da configuração atual do agente.

O relatório de máquina é `validacao_estatica.json`; os controles são reproduzíveis. Nenhum erro estático não significa compilação aprovada, conformidade, eficácia clínica ou segurança demonstrada. O PDF de 102 páginas recebido não é o resultado desta integração.
