
# DoseCerta — Trabalho de Conclusão de Curso

## Sobre o projeto

O **DoseCerta** é um projeto de Trabalho de Conclusão de Curso em Engenharia de Robôs do Centro Universitário FEI. Consiste no desenvolvimento de um dispenser inteligente de medicamentos voltado a idosos em regime de polifarmácia, com o objetivo de auxiliar na organização e no gerenciamento dos horários de administração dos medicamentos.

Este repositório reúne os arquivos relacionados à elaboração da monografia, incluindo textos, capítulos, referências bibliográficas, imagens, documentos técnicos e materiais auxiliares.

## Objetivo do repositório

O GitHub é utilizado como ambiente central de armazenamento, organização e controle de versões do trabalho.

Na prática, isso significa que os integrantes da equipe podem acessar os arquivos do projeto, acompanhar as alterações realizadas e compartilhar atualizações sem depender de diferentes cópias dos documentos.

O histórico de versões permite identificar o que foi alterado, quando a modificação ocorreu e quais arquivos foram atualizados. Dessa forma, o repositório contribui para a rastreabilidade do desenvolvimento da monografia e para a colaboração entre os integrantes.

Os arquivos-fonte permanecem disponíveis para edição, enquanto o PDF compilado permite consultar a versão mais recente do documento.

## Organização dos arquivos

A estrutura do repositório foi organizada para separar o documento principal, os capítulos e os materiais utilizados durante o desenvolvimento.

| Arquivo ou diretório | Descrição |
|---|---|
| `main.tex` | Arquivo principal da monografia. Organiza a estrutura do documento e inclui os capítulos e demais elementos. |
| `Capitulos/` | Contém os arquivos individuais dos capítulos da monografia. |
| `PreTextual/` | Reúne os elementos pré-textuais, como resumo, abstract e outros elementos iniciais. |
| `PosTextual/` | Contém os elementos pós-textuais, como apêndices e anexos. |
| `classe/` | Armazena a classe LaTeX e os arquivos de formatação utilizados no modelo acadêmico. |
| `FEI-pre-textual.tex` | Arquivo de configurações dos elementos pré-textuais. |
| `FEI-bib/` | Reúne os arquivos relacionados à base bibliográfica. |
| `Figuras/` | Armazena imagens, diagramas, fotografias e demais recursos visuais do trabalho. |
| `referencias.tex` | Contém as referências bibliográficas formatadas utilizadas no documento. |
| `gerar_referencias.py` | Script utilizado para gerar ou atualizar o arquivo de referências. |
| `pendencias_dosecerta.tex` | Define a formatação visual das pendências destacadas na monografia. |
| `pendencias.json` | Registra os identificadores e dados associados às pendências do documento. |
| `PERGUNTAS_PARA_CONTRIBUIDORES.md` | Reúne questões e informações que precisam ser confirmadas ou fornecidas pelos integrantes. |
| `VALIDACAO_E_COMPILACAO.md` | Documenta os procedimentos de validação e as instruções de compilação. |
| `main.pdf` | Versão compilada da monografia, disponibilizada para consulta. |

### Organização das figuras

O diretório `Figuras/` possui materiais separados por finalidade:

- `Figuras/SharePoint/`: reúne 37 figuras utilizadas na documentação e no desenvolvimento da monografia.
- `Figuras/Artigo/`: preserva sete imagens documentais utilizadas como material de apoio.

A inclusão de uma imagem no repositório não significa necessariamente que ela já esteja incorporada à versão final do documento.

## Diretrizes de desenvolvimento

Para manter a consistência e a rastreabilidade do trabalho, são adotadas as seguintes diretrizes:

- Os capítulos são mantidos em arquivos separados, facilitando a edição, revisão e divisão de responsabilidades.
- Informações ainda não confirmadas são identificadas como pendências.
- Especificações técnicas devem ser verificadas antes de serem apresentadas como definições consolidadas.
- Resultados experimentais devem corresponder aos testes efetivamente realizados.
- Decisões de projeto devem ser diferenciadas de resultados de implementação e validação.
- Elementos institucionais, como aprovação e informações da banca, não devem ser preenchidos com dados fictícios.

### Decisões de projeto documentadas

Entre as definições registradas até o momento estão:

- Inclinação de projeto de 35°.
- Autenticação obrigatória para acesso ao sistema.
- CARE documentado em capítulo próprio.
- Capítulo de visão computacional reservado ao conteúdo sob responsabilidade de Vini.
- Ferramentas de desenvolvimento e inteligência artificial documentadas na metodologia.

As definições ainda sujeitas à confirmação permanecem identificadas como pendências.

## Situação atual

A monografia encontra-se em desenvolvimento. O repositório contém a estrutura do documento, os capítulos elaborados, os materiais técnicos e os arquivos necessários à compilação.

Ainda existem informações que dependem de confirmação dos integrantes, validações do protótipo, realização de testes, análise de resultados e revisão acadêmica.

As pendências são identificadas ao longo do documento para facilitar seu acompanhamento. Atualmente, os arquivos de controle preservam 87 identificadores de pendências.

O arquivo `main.pdf` corresponde à versão compilada disponibilizada no repositório. Os arquivos `.tex` são os documentos-fonte utilizados para sua elaboração.

## Como colaborar

Os integrantes podem acessar o repositório, consultar os documentos e contribuir com as partes sob sua responsabilidade.

O fluxo recomendado para atualização é:

1. Atualizar a cópia local do repositório antes de começar a trabalhar.
2. Editar os arquivos correspondentes à sua responsabilidade.
3. Salvar as alterações e verificar se o documento continua compilando corretamente.
4. Registrar as modificações utilizando um commit com uma mensagem que descreva o que foi alterado.
5. Enviar as atualizações ao GitHub por meio do comando `git push`.

É importante evitar alterações simultâneas no mesmo arquivo sem alinhamento prévio entre os integrantes, reduzindo a possibilidade de conflitos durante a integração.

## Como compilar a monografia

O documento utiliza LaTeX e pode ser compilado localmente com MiKTeX ou TeX Live, desde que os pacotes necessários estejam instalados.

O arquivo de entrada é `main.tex`.

No terminal, dentro da pasta raiz do projeto, executar:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

As três passagens permitem atualizar elementos como sumário, referências cruzadas e paginação.

Na configuração atual, as referências são incorporadas por meio do arquivo `referencias.tex`, sem necessidade de executar BibTeX ou Biber.

Caso seja necessário atualizar as referências bibliográficas, executar:

```bash
python gerar_referencias.py
```

Após a compilação, recomenda-se conferir o PDF gerado, especialmente a organização dos capítulos, as figuras, as tabelas, as referências e as pendências destacadas.

---

**Este repositório é a base compartilhada de desenvolvimento e documentação do TCC DoseCerta, permitindo que a equipe mantenha o trabalho organizado, atualizado e rastreável durante todas as etapas do projeto.**
