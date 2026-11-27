--- antes_rodada2/Capitulos/04_metodologia.tex
+++ unificado_rodada2/Capitulos/04_metodologia.tex
@@ -60,6 +60,11 @@
 
 As tabelas de sessões foram analisadas por ação e por fase do software. As contagens de testes de regressão são fotografias de versões, não amostras independentes a somar. A telemetria de aproximadamente 30 minutos foi mantida separada do histórico de comandos e das observações com motor. Os intervalos sem relatórios foram interpretados considerando os desligamentos intencionais e as trocas de ambiente. Os planos de campanhas ainda não executadas não foram convertidos em resultados.
 
+\section{Contribuição de aplicativo e protocolo proposto}
+A entrega de 27 de novembro acrescenta oito registros do fluxo de dispensação vinculada no Oficial e sete no Simulado, em CSVs com identificadores de operação. Esses recortes foram confrontados linha a linha com os resumos e mantidos separados dos 12 ciclos por cavidade do pacote anterior; não são amostras independentes a somar. Campo ausente não foi convertido em zero, sucesso ou estoque físico verificado. \cite{DC_NICOLAS2026}
+
+O fluxo vincula paciente, medicamento e posição e distingue pedido, retorno do aparelho e observação humana. A campanha prospectiva proposta utiliza esse fluxo e o Apêndice~\ref{ap:ensaios}; os blocos, tamanhos e critérios ainda dependem de aprovação. Os registros históricos não foram produzidos sob esse protocolo, e sua existência não demonstra execução da campanha. \cite{DC_NICOLAS2026}
+
 \section*{\textcolor{DCPendente}{Complementações necessárias}}
 \pendencia{MET01-ACEITE}{Identificar executores e revisores dos ensaios, instrumentos, condições e evidências por frente.}
 \pendencia{MET03-IA}{Completar a declaração por integrante: Copilot (especificar produto), Copilot Studio, OpenAI (produto/API e modelo), Claude e demais ferramentas efetivamente usadas; tarefas, datas/versões quando disponíveis, partes aproveitadas e revisão humana realizada.
@@ -69,4 +74,4 @@
 \pendencia{MET02-PROTOCOLO}{Fechar com a orientação o protocolo final, repetições, amostragem, instrumentos e critérios quantitativos.
 Não há base documental suficiente para inventar tolerâncias de taxa de erro, corrente, latência ou desempenho.}
 \pendencia{MET-ETICA}{Informar se haverá participantes, coleta de imagens ou dados pessoais; documentar autorizações, consentimento e avaliação institucional aplicáveis.
-Não inserir número de parecer ou dispensa não fornecidos.}+Não inserir número de parecer ou dispensa não fornecidos.}
--- antes_rodada2/Capitulos/06_arquitetura.tex
+++ unificado_rodada2/Capitulos/06_arquitetura.tex
@@ -64,6 +64,9 @@
 
 O controlador escreve um comando DC1 e consulta o resultado enquanto a ESP32 gera o movimento localmente. Assim, não mantém o barramento reservado durante todo o giro. A serialização de um único giro por vez é uma política do runtime, que também reduz a sobreposição de picos de corrente e mantém a rastreabilidade; não é uma impossibilidade elétrica de um barramento atender mais de um endereço. A expansão para vários submódulos permanece sem aceite físico. \cite{DC_VALIDACAO2026}
 
+\section{Divergência de versão na entrega de 27 de novembro}
+O LEIA-ME da frente de aplicativo indica runtime 0.8.0 como instalado, enquanto o relatório anterior identifica uma leitura de 26 de novembro, 22h10, com 0.9.2 e release \texttt{2026.11.25-cam-3}. A nova entrega não inclui manifesto do aparelho que demonstre alteração posterior. Assim, mantém-se a referência de leitura datada, registra-se a divergência e solicita-se confirmação final. Não se retrocede a versão por simples substituição textual. \cite{DC_NICOLAS2026,DC_VALIDACAO2026}
+
 \section*{\textcolor{DCPendente}{Complementações necessárias}}
 \pendencia{ARQ01}{Conferir os diagramas inseridos com a configuração final; atualizar módulos, interfaces e versões que tenham sido alterados desde o desenho de referência.}
 \pendencia{ARQ02}{Fornecer esquema da montagem pós-reparos, orientação de cada pogo, continuidade e fotografias identificadas. O mapa funcional disponível não comprova ordem física nem estado atual de todos os módulos.}
--- antes_rodada2/Capitulos/10_backend.tex
+++ unificado_rodada2/Capitulos/10_backend.tex
@@ -91,6 +91,8 @@
 
 A documentação de segurança registra ainda o uso, pela API, de papel que pode ignorar as políticas RLS e a autenticação do MCP por chave estática. Assim, a proteção efetiva depende de validação no servidor e de controle dos segredos; a existência de RLS no banco não autoriza afirmar segregação de ponta a ponta. Os testes de recusa de token inválido e os testes locais não equivalem a auditoria de todas as permissões em produção. Retenção, restauração, privacidade e acesso a observações reservadas continuam sujeitos à verificação específica. \cite{DC_VALIDACAO2026}
 
+\input{Capitulos/10b_dados_rastreabilidade}
+
 \section*{\textcolor{DCPendente}{Complementações necessárias}}
 \pendencia{BE01-RUNTIME}{Versão e configuração de 26/11 incorporadas; complementar hash, manifesto e dependências da apresentação, sem atribuir a essa configuração todos os ensaios históricos.}
 \pendencia{BE02-AGENDA}{Fornecer evidência de comissionamento, tempo confiável sem rede, calibração, associação e pré-condições da agenda. Manter a declaração de operação automática pendente até ensaio de perda de rede, reinício e recuperação.}
--- antes_rodada2/Capitulos/11_aplicativo.tex
+++ unificado_rodada2/Capitulos/11_aplicativo.tex
@@ -1,109 +1,193 @@
 \chapter{Aplicativo Care}\label{cap:aplicativo}
-O Care reúne configuração e acompanhamento da rotina de cuidado. Seu desenvolvimento buscou manter as tarefas principais acessíveis pela interface, sem tornar cadastro, consulta ou registro dependentes da conversação com o agente. A aplicação se comunica com a API e apresenta os estados recebidos, preservando a diferença entre planejamento e ocorrência. \cite{DC_APP}
+O Care é a interface web pela qual cuidadores, familiares e a própria pessoa em tratamento configuram e acompanham a rotina de cuidado. O aplicativo concentra o cadastro de medicamentos e horários, o registro de tomadas e observações, a consulta ao estado do aparelho e o acesso ao assistente de inteligência artificial. As regras de negócio permanecem na API; o aplicativo apresenta os estados recebidos e preserva a diferença entre o que foi planejado e o que de fato ocorreu. \cite{DC_APP}
+
+\section{Um aplicativo, três perfis}
+O mesmo código-fonte é compilado em três perfis, definidos no momento do empacotamento. O perfil \emph{oficial} atende ao uso real, com todas as travas do sistema e sem funções de simulação. O perfil \emph{simulado} conversa com uma instância separada do servidor e do banco de dados, destinada a apresentações e ensaios com o protótipo, e acrescenta uma área de testes do aparelho. O perfil \emph{demonstração} roda inteiramente no navegador, com uma paciente fictícia, sem acesso ao servidor nem ao aparelho; foi o perfil publicado para o público da feira por meio de um código QR.
+
+A separação por perfis busca manter as funções de teste fora do uso real e permite apresentar a interface com dados fictícios. As diferenças entre os perfis estão reunidas em um único módulo de configuração; as telas são as mesmas. As capturas utilizam dados fictícios: o login foi obtido no perfil Oficial; as demais telas usam a Demonstração ou uma cópia local de apresentação. Os três prints do assistente têm respostas roteirizadas, como explicitado na legenda, e não comprovam execução do agente. \cite{DC_NICOLAS2026}
 
 \section{Da referência visual ao protótipo navegável}
-A primeira etapa utilizou o Google Stitch para elaborar a composição visual. A Figura~\ref{fig:app_stitch} apresenta essa referência, com destaque para próxima dose e indicadores do painel. Os nomes, estoques e percentuais exibidos pertencem ao desenho demonstrativo, não aos resultados de uso.
+A primeira etapa utilizou o Google Stitch para elaborar a composição visual, apresentada na Figura~\ref{fig:app_stitch}, com destaque para a próxima dose e os indicadores do painel. Em seguida, o Google AI Studio foi utilizado para experimentar navegação, animações e alertas com relógio acelerado e ocorrências simuladas. A sequência da Figura~\ref{fig:app_etapas} resume a passagem do desenho à aplicação integrada, na qual os estados em memória foram substituídos por operações autenticadas na API.
 
 \begin{figure}[htbp]
 \centering
 \caption{Referência inicial de interface criada no Google Stitch}\label{fig:app_stitch}
-\includegraphics[width=0.94\textwidth,height=0.66\textheight,keepaspectratio]{Figuras/SharePoint/app_stitch.png}
+\includegraphics[width=0.94\textwidth,height=0.6\textheight,keepaspectratio]{Figuras/SharePoint/app_stitch.png}
 \fonte{Acervo dos autores. Protótipo visual com nomes, estoque e indicadores demonstrativos.}
 \end{figure}
-
-
-Em seguida, o Google AI Studio foi utilizado para experimentar navegação, animações e respostas da interface. A sequência da Figura~\ref{fig:app_etapas} resume a passagem do desenho à aplicação integrada. O piloto permitiu discutir alertas e estados antes da implementação da persistência e das regras no servidor.
 
 \begin{figure}[htbp]
 \centering
 \caption{Evolução do desenvolvimento: desenho, navegação e implementação}\label{fig:app_etapas}
-\includegraphics[width=0.98\textwidth,height=0.66\textheight,keepaspectratio]{Figuras/SharePoint/app_etapas.png}
+\includegraphics[width=0.98\textwidth,height=0.6\textheight,keepaspectratio]{Figuras/SharePoint/app_etapas.png}
 \fonte{Elaboração dos autores (2026).}
 \end{figure}
 
-
-A Figura~\ref{fig:app_piloto} mostra a experimentação dos alertas e da próxima dose. O relógio acelerado e as ocorrências simuladas serviram ao desenvolvimento da interação. A implementação posterior precisou substituir os estados em memória por operações autenticadas e tratar os casos de falha de rede e ausência de dados.
-
-\begin{figure}[htbp]
-\centering
-\caption{Experimentação da navegação e dos alertas no Google AI Studio}\label{fig:app_piloto}
-\includegraphics[width=0.98\textwidth,height=0.66\textheight,keepaspectratio]{Figuras/SharePoint/app_piloto.png}
-\fonte{Acervo dos autores. Doses, relógio e alertas de simulação.}
-\end{figure}
-
-
-\section{Implementação e autenticação}
-O frontend foi implementado em React e TypeScript. A interface organiza componentes e estados de apresentação, enquanto a API FastAPI concentra as regras e a persistência. A Figura~\ref{fig:app_camadas} apresenta a separação entre essas responsabilidades e as interfaces do aparelho e do assistente. \cite{DC_VISUAL}
+\section{Arquitetura do frontend}
+O frontend foi implementado em React com TypeScript, empacotado com Vite e estilizado com Tailwind CSS. A interface organiza componentes e estados de apresentação, enquanto a API FastAPI concentra validação, autorização e persistência. A Figura~\ref{fig:app_camadas} apresenta essa separação e as interfaces com o aparelho e com o assistente. \cite{DC_VISUAL}
 
 \begin{figure}[htbp]
 \centering
 \caption{Responsabilidades da interface, da API e da persistência}\label{fig:app_camadas}
-\includegraphics[width=0.98\textwidth,height=0.66\textheight,keepaspectratio]{Figuras/SharePoint/app_camadas.png}
+\includegraphics[width=0.98\textwidth,height=0.6\textheight,keepaspectratio]{Figuras/SharePoint/app_camadas.png}
 \fonte{Elaboração dos autores (2026).}
 \end{figure}
 
+A implementação descrita associa às operações de escrita uma chave de idempotência gerada no navegador. Se a resposta se perde e a solicitação é reenviada, o servidor reconhece a chave e devolve o resultado original, em vez de criar um segundo registro. O mesmo princípio, descrito no Capítulo~\ref{cap:backend}, busca impedir duplicação quando o reenvio mantém a mesma identidade; não prova por si que duas solicitações independentes não produzam dois comandos. A conversa com o assistente utiliza um canal WebSocket com a API, que atua como intermediária entre o aplicativo e o serviço de voz; o aplicativo nunca recebe as credenciais do serviço de IA.
 
-O acesso ao cuidado exige login. A sessão fornece o token utilizado nas solicitações à API, mas não substitui a autorização de cada ação. A interface precisa tratar sessão expirada, recusa de acesso e falha de conexão de forma explícita, sem apresentar dados antigos como confirmação de uma operação atual.
+O aplicativo é responsivo. No celular, a navegação fica em abas no topo e o assistente em um botão flutuante; em telas largas, as mesmas funções se reorganizam em uma barra horizontal, como na Figura~\ref{fig:app_desktop}.
 
-Nas operações de escrita, a identificação da tentativa permite reconhecer reenvios. Quando uma resposta se perde, a aplicação deve acompanhar o estado da solicitação antes de criar outra. Essa relação entre interface e servidor aplica ao uso cotidiano o tratamento de idempotência descrito no Capítulo~\ref{cap:backend}.
+\section{Autenticação, visões e pacientes}
+O acesso exige login com e-mail e senha (Figura~\ref{fig:app_login_painel}). O serviço de identidade emite um token de sessão, enviado em cada solicitação à API; a API valida o token e decide, a cada operação, se aquele usuário pode agir sobre aquele paciente. A sessão identifica a conta autenticada, não necessariamente a pessoa física em uma conta compartilhada. A autorização descrita deve ser confirmada por testes negativos por paciente e interface. \cite{DC_NICOLAS2026,DC_VALIDACAO2026}
 
-\section{Organização dos dados}
-O modelo preserva o vínculo entre paciente, medicamento, agenda e evento. Atividades e observações do cuidado possuem registros próprios, e o inventário associa medicamento e compartimento. A Figura~\ref{fig:app_dados} apresenta um recorte conceitual dessa organização, sem representar todas as relações físicas do banco.
+\begin{figure}[htbp]
+\centering
+\caption{Tela de entrada do perfil oficial e painel inicial do cuidador}\label{fig:app_login_painel}
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/00_login.jpg}\par\small (a) Login
+\end{minipage}\hfill
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/02_painel.jpg}\par\small (b) Painel
+\end{minipage}
+\fonte{Capturas do aplicativo Care, perfis oficial (a) e demonstração (b), com dados fictícios (nov. 2026).}
+\end{figure}
+
+A interface oferece três visões: cuidador, familiar e paciente (Figura~\ref{fig:app_visoes}). Cada visão ajusta a linguagem e as funções disponíveis; na visão do paciente, por exemplo, o painel passa a tratar a rotina como ``Seu dia''. Quando um mesmo aparelho atende mais de um paciente, o aplicativo exige a escolha explícita do paciente antes de exibir dados ou abrir o assistente, e a API recusa operações sem essa seleção. A entrega registra essa seleção como resposta ao risco de contexto incorreto, mas também aponta que o caminho MCP pode continuar usando um paciente fixo. A seleção na tela e a validação de abertura da conversa não comprovam o isolamento do assistente de ponta a ponta. Ver Capítulo~\ref{cap:agente}. \cite{DC_NICOLAS2026}
+
+\begin{figure}[htbp]
+\centering
+\caption{Visões do aplicativo: seleção da visão e painel na visão do paciente}\label{fig:app_visoes}
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/13_visoes_cuidador_familiar_paciente.jpg}\par\small (a) Seleção da visão
+\end{minipage}\hfill
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/14_painel_visao_paciente.jpg}\par\small (b) Visão do paciente
+\end{minipage}
+\fonte{Capturas do aplicativo Care no perfil de demonstração, com dados fictícios (nov. 2026).}
+\end{figure}
+
+\section{Organização dos dados de cuidado}
+O modelo preserva o vínculo entre paciente, medicamento, horário e evento. Atividades do dia a dia e observações possuem registros próprios, e o inventário associa cada medicamento a um compartimento do aparelho. A Figura~\ref{fig:app_dados} apresenta um recorte conceitual dessa organização; a estrutura completa do banco é descrita na Seção~\ref{sec:dados_rastreabilidade}.
 
 \begin{figure}[htbp]
 \centering
 \caption{Organização conceitual dos dados de cuidado}\label{fig:app_dados}
-\includegraphics[width=0.98\textwidth,height=0.66\textheight,keepaspectratio]{Figuras/SharePoint/app_dados.png}
+\includegraphics[width=0.98\textwidth,height=0.6\textheight,keepaspectratio]{Figuras/SharePoint/app_dados.png}
 \fonte{Elaboração dos autores. Agrupamento conceitual, não diagrama completo de chaves estrangeiras.}
 \end{figure}
 
+A distinção entre planejar e registrar evita que uma alteração de horário seja interpretada como tomada realizada. Cada registro conserva sua origem (o aparelho, uma pessoa ou o sistema) e seu autor. O mesmo princípio orienta a apresentação do histórico e das notificações.
 
-A distinção entre planejar e registrar evita que uma alteração de horário seja interpretada como tomada realizada. Também permite conservar a autoria de um relato e a origem de uma verificação do aparelho. O mesmo princípio é utilizado na apresentação do histórico.
-
-\section{Painel e rotina diária}
-A evolução do painel priorizou próxima dose, resumo dos horários e observações. Recursos complementares foram distribuídos entre rotinas, relatos, manual e configurações. A Figura~\ref{fig:app_evolucao} apresenta etapas dessa reorganização e o guia de primeiro acesso.
+\section{Funções principais}
+\subsection{Painel e rotinas}
+O painel (Figura~\ref{fig:app_login_painel}b) prioriza a próxima dose, com tempo restante, o resumo das tomadas do dia, o último registro, a próxima atividade e a última observação. A aba Rotinas separa os medicamentos das atividades do dia a dia, navegáveis por data (Figura~\ref{fig:app_rotinas}). Cada horário mostra um de oito estados: programada, tomada registrada, não tomada, não administrada, horário perdido, verificação inconclusiva, sem atualização e resultado a conferir. Um horário vencido nunca é convertido em tomada; a ausência de informação aparece como tal.
 
 \begin{figure}[htbp]
 \centering
-\caption{Reorganização do painel e introdução do guia de primeiro acesso}\label{fig:app_evolucao}
-\includegraphics[width=0.98\textwidth,height=0.66\textheight,keepaspectratio]{Figuras/SharePoint/app_evolucao.png}
-\fonte{Acervo dos autores. A e B: reconstruções e simulações; C: captura do guia publicado em 12 out. 2026.}
+\caption{Rotinas: horários de medicamentos e atividades do dia a dia}\label{fig:app_rotinas}
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/03_rotinas_medicamentos.jpg}\par\small (a) Medicamentos
+\end{minipage}\hfill
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/04_rotinas_dia_a_dia.jpg}\par\small (b) Dia a dia
+\end{minipage}
+\fonte{Capturas do aplicativo Care no perfil de demonstração, com dados fictícios (nov. 2026).}
 \end{figure}
 
-
-A simplificação visual buscou reduzir a concentração de informações na abertura. Essa escolha de projeto não é apresentada como melhora quantitativa de usabilidade, pois exige avaliação própria. O guia introduz a navegação e orienta o acesso às funções, sem substituir mensagens de estado durante a operação.
-
-O plano diário apresenta as atividades programadas, enquanto o histórico reúne ocorrências com resultado e origem. A Figura~\ref{fig:app_rotina_historico} mostra essas duas tarefas com dados fictícios. Um resultado inconclusivo permanece identificado como tal, sem ser convertido em dose confirmada.
+\subsection{Observações e notificações}
+As observações registram relatos do cuidado, com autor, horário e visibilidade (compartilhada ou reservada). As notificações reúnem registros e avisos recentes; limpar a lista afeta apenas a visualização de quem limpou e não apaga os registros (Figura~\ref{fig:app_notas}).
 
 \begin{figure}[htbp]
 \centering
-\caption{Plano diário e histórico com identificação da origem dos registros}\label{fig:app_rotina_historico}
-\includegraphics[width=0.88\textwidth,height=0.70\textheight,keepaspectratio]{Figuras/SharePoint/app_rotina_historico.png}
-\fonte{Acervo dos autores. Capturas de demonstração com dados fictícios.}
+\caption{Observações do cuidado e central de notificações}\label{fig:app_notas}
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/05_observacoes.jpg}\par\small (a) Observações
+\end{minipage}\hfill
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/09_notificacoes.jpg}\par\small (b) Notificações
+\end{minipage}
+\fonte{Capturas do aplicativo Care no perfil de demonstração, com dados fictícios (nov. 2026).}
 \end{figure}
 
-
-\section{Manual e assistente}
-O manual tridimensional relaciona a representação do aparelho aos componentes e à manutenção. O carregamento dos recursos é separado da abertura do painel, evitando associar toda a navegação inicial à carga do modelo. A Figura~\ref{fig:app_manual_assistente} apresenta o manual e uma conversa de demonstração. \cite{DC_VISUAL}
+\subsection{Aparelho e estoque}
+A janela do aparelho informa o último retorno recebido da central, permite verificar a conexão e lista os medicamentos por posição com a quantidade em estoque (Figura~\ref{fig:app_aparelho}). A reposição é registrada pelo usuário; a baixa automática ocorre apenas quando a saída de uma unidade é confirmada, como descrito na Seção~\ref{sec:app_dispensacao}.
 
 \begin{figure}[htbp]
 \centering
-\caption{Manual tridimensional e interface de conversa}\label{fig:app_manual_assistente}
-\includegraphics[width=0.88\textwidth,height=0.69\textheight,keepaspectratio]{Figuras/SharePoint/app_manual_assistente.png}
-\fonte{Acervo dos autores. Manual reconstruído e conversa identificada como demonstração.}
+\caption{Janela do aparelho e controle de estoque por posição}\label{fig:app_aparelho}
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/07_aparelho.jpg}\par\small (a) Aparelho
+\end{minipage}\hfill
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/08_estoque_reposicao.jpg}\par\small (b) Estoque e reposição
+\end{minipage}
+\fonte{Capturas do aplicativo Care no perfil de demonstração, com dados fictícios (nov. 2026).}
 \end{figure}
 
+\subsection{Manual tridimensional e guia de primeiro acesso}
+O manual apresenta a montagem do aparelho em 16 etapas sobre um modelo tridimensional que pode ser girado, além de uma tabela dos sinais luminosos e sonoros e das instruções de conexão. O guia de primeiro acesso percorre as funções do aplicativo e pode ser reaberto pelas configurações (Figura~\ref{fig:app_manual}). O carregamento do modelo 3D é feito apenas quando o manual é aberto, para não atrasar a abertura do painel.
 
-O acesso ao assistente complementa as funções manuais. Sua presença na interface não significa que todas as ferramentas do agente de teste estejam disponíveis na conversa publicada. A separação entre voz e MCP é apresentada no Capítulo~\ref{cap:agente}, juntamente com o fluxo de aprovação das escritas.
+\begin{figure}[htbp]
+\centering
+\caption{Manual tridimensional e guia de primeiro acesso}\label{fig:app_manual}
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/06_manual_3d.jpg}\par\small (a) Manual 3D
+\end{minipage}\hfill
+\begin{minipage}[t]{0.42\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.55\textheight,keepaspectratio]{Figuras/App/01_guia_primeiro_acesso.jpg}\par\small (b) Guia
+\end{minipage}
+\fonte{Capturas do aplicativo Care no perfil de demonstração, com dados fictícios (nov. 2026).}
+\end{figure}
+
+\section{Assistente no aplicativo}
+O assistente abre em tela própria e mantém o paciente selecionado como contexto da conversa. A pessoa pode escrever, ditar a mensagem pelo microfone ou iniciar uma conversa por voz em tempo real, na qual a transcrição aparece enquanto se fala. Cada resposta pode ser copiada ou ouvida novamente. A Figura~\ref{fig:app_assistente} mostra uma consulta à rotina e o envio de uma receita.
+
+O anexo aceita foto da câmera, imagem da galeria ou arquivo PDF. Antes de sair do aparelho, toda imagem é reduzida para no máximo 1600 pixels no lado maior; um PDF tem suas primeiras páginas (até quatro) desenhadas como imagens no próprio navegador. Dessa forma, receitas digitais e fotografadas são lidas da mesma maneira, e o tamanho transmitido fica limitado. A API repassa as imagens ao agente, que as interpreta junto com o contexto do paciente. Segundo o relato da entrega, um teste exploratório com receita fictícia retornou quatro medicamentos, doses e horários em cerca de 15~s. Não há nesta entrega uma série independente que permita estimar precisão ou latência típica. \cite{DC_NICOLAS2026} A leitura da receita produz uma resposta em texto; qualquer alteração no cadastro continua sujeita às regras descritas no Capítulo~\ref{cap:agente}.
+
+\begin{figure}[htbp]
+\centering
+\caption{Assistente: consulta à rotina, menu de anexo e leitura de uma receita fictícia}\label{fig:app_assistente}
+\begin{minipage}[t]{0.31\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.5\textheight,keepaspectratio]{Figuras/App/10_assistente_conversa.jpg}\par\small (a) Consulta
+\end{minipage}\hfill
+\begin{minipage}[t]{0.31\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.5\textheight,keepaspectratio]{Figuras/App/11_assistente_menu_anexo.jpg}\par\small (b) Anexo
+\end{minipage}\hfill
+\begin{minipage}[t]{0.31\textwidth}\centering
+\includegraphics[width=\textwidth,height=0.5\textheight,keepaspectratio]{Figuras/App/12_assistente_receita.jpg}\par\small (c) Receita
+\end{minipage}
+\fonte{Capturas do aplicativo Care em ambiente local de demonstração, com dados e receita fictícios (nov. 2026). As respostas foram roteirizadas para a captura; a de (c) reproduz o texto obtido do agente real em teste de 17 nov. 2026.}
+\end{figure}
+
+\section{Integração com o aparelho: dispensação vinculada}\label{sec:app_dispensacao}
+Para os ensaios com o protótipo, o aplicativo oferece um fluxo de dispensação vinculada a um paciente, a um medicamento e a uma posição do aparelho. O fluxo separa quatro momentos, cada um com registro próprio no banco de dados:
+\begin{enumerate}
+\item \textbf{Pedido}: o usuário escolhe a quantidade; a API registra o início do ensaio com o estoque naquele instante.
+\item \textbf{Comando}: a API cria um comando para a central, que o executa no submódulo e devolve o resultado do motor e as leituras do sensor óptico antes e depois do giro.
+\item \textbf{Observação}: uma pessoa informa quantas unidades viu sair no copo coletor, ou registra que não observou.
+\item \textbf{Baixa}: o estoque é reduzido somente pela quantidade observada; sem confirmação de saída, nada é debitado.
+\end{enumerate}
+
+Essa separação permite comparar, em cada ensaio, o que foi pedido, o que o aparelho relatou e o que a pessoa observou. Quando o resultado do motor é incerto, o aplicativo bloqueia um novo pedido até que a situação seja reconciliada. Os mesmos registros formam a ficha de cada ensaio utilizada no Capítulo~\ref{cap:resultados}. No perfil simulado, uma área de testes reúne ainda o teste das ligações (LEDs, buzzer, motor e sensor), a calibração e a localização do disco, a câmera e o modo de apresentação.
 
 \section{Tratamento de falhas e acessibilidade}
-A interface deve indicar carregamento, conclusão, recusa e resultado desconhecido. Uma consulta vazia não é equivalente à comprovação de estoque físico zero; uma resposta de texto não é confirmação de alteração persistida. Essas distinções mantêm o usuário informado sobre o alcance de cada retorno.
+A interface distingue carregamento, conclusão, recusa e resultado desconhecido. Uma consulta vazia não é tratada como estoque zero, e uma resposta do assistente não é tratada como alteração gravada. Mensagens de erro da API e do aparelho são traduzidas para frases curtas, com orientação sobre o que fazer; por exemplo, a perda de comunicação com o submódulo durante um giro gera a orientação de verificar energia e contatos.
 
-A avaliação de acessibilidade considera contraste, identificação dos controles, navegação e compreensão das confirmações, tomando as WCAG 2.2 como referência. O uso de texto junto às cores também é aplicado à comunicação dos estados do dispositivo. \cite{WCAG22}
+A interface adota as WCAG 2.2 como referência: controles identificados por texto e por rótulo acessível, estados comunicados por texto além da cor, contraste elevado nos elementos principais e áreas de toque amplas. A conformidade com as diretrizes depende de avaliação específica, ainda não realizada. \cite{WCAG22}
+
+\begin{figure}[htbp]
+\centering
+\caption{Painel em tela larga, com a navegação reorganizada em barra horizontal}\label{fig:app_desktop}
+\includegraphics[width=0.9\textwidth,keepaspectratio]{Figuras/App/15_painel_desktop.jpg}
+\fonte{Captura do aplicativo Care no perfil de demonstração, com dados fictícios (nov. 2026).}
+\end{figure}
+
+\section{Verificação do aplicativo}
+O aplicativo possui testes automatizados com Vitest e Testing Library, que cobrem componentes, estados e a comunicação com a API simulada. A entrega menciona rodadas históricas de 27 arquivos e 359 casos no Care e de 43 arquivos e 240 casos na suíte geral. Esses recortes não substituem a rodada posterior de 25 de novembro e não são somados a ela. \cite{DC_NICOLAS2026,DC_VALIDACAO2026} A verificação de tipos é feita pelo compilador TypeScript. Os resultados da versão final estão consolidados no Capítulo~\ref{cap:resultados}.
 
 \section*{\textcolor{DCPendente}{Complementações necessárias}}
-\pendencia{APP01}{Nicolas: a autora enviará a versão e as telas do aplicativo. Inserir release/hash, ambiente, navegação e tarefas efetivamente disponíveis, além de capturas sanitizadas.}
-\pendencia{APP02}{Login obrigatório confirmado: inserir telas e evidências do fluxo real, emissão/validação e renovação de sessão, expiração, logout, acesso negado e mensagens de erro, sem expor credenciais.}
-\pendencia{APP03}{Conferir a autorização na versão final, especialmente se as visões de paciente/cuidador usam conta única. Não declarar isolamento de dados sem teste.}
-\pendencia{APP04}{Fornecer resultados próprios da suíte Care, integração autenticada, estados de erro/sem rede, atualização de histórico e comunicação com o aparelho. Identificar o que foi simulado.}
-\pendencia{APP05}{Inserir fotos/capturas atualizadas das tarefas principais e avaliação de acessibilidade/usabilidade: método, participantes quando houver, critérios, problemas e correções. Não inferir qualidade de uso pelo desenho das telas.}
+\pendencia{APP01}{Dezesseis capturas incorporadas com identificação de perfil, dados fictícios e respostas roteirizadas. Confirmar release/hash publicado do webapp e da API. A entrega cita webapp 2aa391ad e API 2d07bd78 em 18/11 e republicação posterior; não assumir esses hashes como finais.}
+\pendencia{APP02}{Login fotografado sem credenciais. Completar evidências autenticadas de emissão, validação, renovação, expiração, logout e acesso negado; os prints da Demonstração não comprovam esses caminhos.}
+\pendencia{APP03}{Conferir autorização final com dois pacientes no mesmo aparelho e conta operadora compartilhada. Testar telas, observações reservadas e assistente; a entrega aponta paciente fixo no MCP apesar da seleção na interface.}
+\pendencia{APP04}{Corrigir ou justificar as falhas remanescentes e registrar versão/log final. Não substituir 363 casos de 25/11 por 359 de um recorte anterior nem somar suítes com escopos sobrepostos. Completar integração autenticada e falhas de rede.}
+\pendencia{APP05}{Capturas das funções principais incorporadas; permanecem a avaliação de usabilidade/acessibilidade com método, autorizações, tarefas e achados, e a eventual captura de voz real sem roteirização.}
--- antes_rodada2/Capitulos/12_visao_computacional.tex
+++ unificado_rodada2/Capitulos/12_visao_computacional.tex
@@ -72,6 +72,11 @@
 
 Os riscos identificados na análise do método incluem confirmação em um único quadro, oclusão dos lábios pela mão, contornos sem identidade farmacológica, limiares fixos em pixels e perda de movimentos rápidos. Ausência de pontos faciais não deve ser confundida com boca fechada. São limitações e hipóteses para ensaio, não frequências de falha já medidas. \cite{DC_VISAO2026}
 
+\subsection{Registro histórico da versão 2}
+A base remetida em 27 de novembro descreve testes exploratórios de 28 de outubro com webcam e uma pessoa. Na primeira rodada, três de quatro sequências simuladas receberam escore de 0,946 a 0,992 e uma, 0,884, ficou inconclusiva. Em outra, seis sessões receberam rótulo positivo, incluindo mão apoiada na bochecha com cabeça inclinada, um falso positivo identificado no próprio desenvolvimento. Um gesto de espreguiçar também levou a escore positivo e à revisão das regras. \cite{DC_NICOLAS2026}
+
+Esse histórico descreve ajuste de uma versão anterior, não teste independente da vision-v3. Os limiares da versão 2 (positivo a partir de 0,90, negativo até 0,15 e permanência mínima de 0,4 s) e sua janela de 20 s não foram transferidos para a máquina de estados com janela de 30 s do memorial do responsável. É necessário vincular cada registro a código, configuração e modelo antes de comparar resultados; um escore não calibrado não é probabilidade clínica. \cite{DC_NICOLAS2026,DC_VISAO2026}
+
 \section*{\textcolor{DCPendente}{Complementações necessárias}}
 \pendencia{VIS01}{Confirmar com o responsável a correspondência entre vision-v3 3.0.0, código, release instalada e método ativo. Resolver a divergência com a regressão logística de 16 medidas do pacote.}
 \pendencia{VIS02}{Anexar figuras reais da aquisição, landmarks, ROI e interface; conferir versões das bibliotecas e execução dos mecanismos de câmera/cancelamento no aparelho. O DOCX não possui imagens incorporadas.}
--- antes_rodada2/Capitulos/13_agente_ia.tex
+++ unificado_rodada2/Capitulos/13_agente_ia.tex
@@ -1,32 +1,44 @@
 \chapter{Agente de inteligência artificial}\label{cap:agente}
-O agente oferece uma forma de consultar informações e solicitar ações do cuidado em linguagem natural. Sua função é complementar o aplicativo, não prescrever, escolher doses ou substituir o responsável pelo tratamento. A execução das solicitações permanece sujeita às regras da API e às permissões do contexto.
+O agente oferece uma forma de consultar informações e solicitar ações do cuidado em linguagem natural, por texto ou por voz. Sua função é complementar o aplicativo, não prescrever, escolher doses ou substituir o responsável pelo tratamento. As operações passam pela API, que aplica as regras de negócio e as permissões do contexto.
+
+\section{Situação documental e revisão por frente}
+O texto a seguir incorpora uma proposta de atualização enviada pela frente de aplicativo e dados em 27 de novembro, ainda sujeita à conferência do responsável pelo agente. A documentação de 3 de novembro registrava agente de conversa v5 separado de um agente de teste MCP v8. O pacote anterior relatava migração para Voice Live com contexto de leitura e desligamento do MCP dedicado; a nova entrega relata MCP de leitura e escrita no agente do aplicativo. São descrições de épocas e origens distintas; sem exportação sanitizada da configuração, não se presume que todas descrevam a implantação atual. \cite{DC_FOUNDRY,DC_VALIDACAO2026,DC_NICOLAS2026}
 
 \section{Evolução e organização}
-A proposta inicial utilizou Microsoft Copilot Studio. O desenvolvimento posterior passou a utilizar Microsoft Foundry, com um agente de conversa e uma configuração separada de teste para ferramentas MCP. Essa evolução alterou o modo de integrar voz, contexto e operações de escrita. \cite{DC_ARTIGO,DC_FOUNDRY}
+A proposta inicial utilizou Microsoft Copilot Studio. O desenvolvimento posterior passou a utilizar Microsoft Foundry, com um agente versionado (\texttt{tcc-agent}) acessado pela API do projeto por meio do serviço Azure Voice Live, que oferece conversa por texto e por voz em tempo real. \cite{DC_ARTIGO,DC_FOUNDRY}
 
-Na configuração de referência de 3 de novembro de 2026, o aplicativo utilizava o agente de conversa na versão 5, sem MCP. A configuração de teste utilizava \texttt{tcc-agent-mcp-teste} na versão 8. A Figura~\ref{fig:agente_arquitetura} apresenta os dois caminhos. A separação evita atribuir à interface de voz funções disponíveis apenas no ambiente de teste.
+A Tabela~\ref{tab:13-versoes} reproduz a sequência de versões relatada pela frente de aplicativo, ainda não conferida por exportação do serviço nesta consolidação. Até 12 de novembro, o aplicativo usava a versão 5, que apenas pesquisava em arquivos de referência e não acessava os dados do paciente. A partir da versão 21, o agente passou a usar um servidor MCP próprio, que expõe ferramentas de leitura e escrita sobre os dados do cuidado. A configuração de teste com MCP, apresentada na Figura~\ref{fig:agente_arquitetura}, foi portanto incorporada ao agente do aplicativo.
+
+{\small\setlength{\tabcolsep}{3pt}\begin{longtable}{p{0.1\textwidth}p{0.17\textwidth}p{0.63\textwidth}}
+\caption{Versões do agente utilizadas pelo aplicativo}\label{tab:13-versoes}\\
+\hline\textbf{Versão} & \textbf{Uso no app} & \textbf{Características}\\\hline\endfirsthead
+\hline\textbf{Versão} & \textbf{Uso no app} & \textbf{Características}\\\hline\endhead
+5 & até 12/11 & Pesquisa em arquivos de referência; sem acesso aos dados do paciente\\\hline
+21 & 12/11 & Pesquisa em arquivos e servidor MCP com consulta ao contexto de cuidado; respostas curtas\\\hline
+24 e 25 & 12/11 a 25/11 & Ferramentas de escrita descritas nas instruções, com regra de confirmar em dois turnos\\\hline
+28 & desde 25/11 & Responde somente sobre o DoseCerta; esforço de raciocínio baixo; escolha automática de ferramentas\\\hline
+\end{longtable}}{\small\noindent Fonte: proposta de atualização recebida em 27 nov. 2026; confirmação da frente pendente. \cite{DC_NICOLAS2026}\par}
 
 \begin{figure}[htbp]
 \centering
-\caption{Separação entre o assistente do aplicativo e o agente de teste com MCP}\label{fig:agente_arquitetura}
+\caption{Organização do agente com servidor MCP, na configuração de teste de 3 nov. 2026}\label{fig:agente_arquitetura}
 \includegraphics[width=0.98\textwidth,height=0.66\textheight,keepaspectratio]{Figuras/SharePoint/agente_arquitetura.png}
-\fonte{Elaboração dos autores. Configuração de referência de 3 nov. 2026.}
+\fonte{Elaboração dos autores. A partir de 12 nov. 2026, o agente do aplicativo passou a usar o mesmo servidor MCP.}
 \end{figure}
 
+\section{Contexto e recuperação de informações}
+O agente combina duas fontes. A pesquisa em arquivos recupera conhecimento de referência, como o funcionamento do aparelho; as ferramentas MCP consultam os dados atuais do paciente. A utilidade da primeira depende do conteúdo carregado e de sua atualização; a existência do índice não garante que o manual esteja completo.
 
-\section{Contexto e recuperação de informações}
-Na configuração de referência de 3 de novembro, o agente de conversa utilizava pesquisa em arquivos para recuperar contexto. A utilidade desse recurso depende da seleção, da revisão e da atualização do conteúdo disponibilizado. A existência de um índice não garante que o manual esteja completo ou que os registros atuais do cuidado sejam consultados.
-
-As respostas devem distinguir conhecimento de referência e dados obtidos por ferramenta. Quando uma consulta falha ou retorna informação parcial, o agente precisa informar esse limite antes de afirmar rotina, estoque ou histórico. Textos recuperados são tratados como dados de contexto, não como instruções para alterar a política de operação.
+As respostas devem distinguir conhecimento de referência e dados obtidos por ferramenta. Quando uma consulta falha ou retorna informação parcial, o agente precisa informar esse limite antes de afirmar rotina, estoque ou histórico. Textos recuperados são tratados como dados de contexto, não como instruções.
 
 \section{Ferramentas e operações}
-A configuração MCP de referência de 3 de novembro reunia duas ferramentas de leitura e seis de escrita. As leituras consultam contexto e registros; as escritas alteram cadastros, rotinas, atividades ou observações. A Tabela~\ref{tab:13-1} apresenta os identificadores da configuração de referência. \cite{DC_FOUNDRY}
+O servidor MCP reúne duas ferramentas de leitura e seis de escrita (Tabela~\ref{tab:13-1}). As leituras consultam contexto e registros; as escritas alteram cadastros, rotinas, atividades ou observações. A disponibilidade no serviço final depende da conferência de configuração. \cite{DC_FOUNDRY,DC_NICOLAS2026}
 
-{\small\setlength{\tabcolsep}{3pt}\begin{longtable}{p{0.44\textwidth}p{0.12\textwidth}p{0.32\textwidth}}\caption{Ferramentas da cópia MCP do agente, documentadas em novembro}\label{tab:13-1}\\
+{\small\setlength{\tabcolsep}{3pt}\begin{longtable}{p{0.44\textwidth}p{0.12\textwidth}p{0.32\textwidth}}\caption{Ferramentas do servidor MCP do agente}\label{tab:13-1}\\
 \hline
-\textbf{Ferramenta documental} & \textbf{Tipo} & \textbf{Papel}\\\hline
+\textbf{Ferramenta} & \textbf{Tipo} & \textbf{Papel}\\\hline
 \endfirsthead\hline
-\textbf{Ferramenta documental} & \textbf{Tipo} & \textbf{Papel}\\\hline
+\textbf{Ferramenta} & \textbf{Tipo} & \textbf{Papel}\\\hline
 \endhead
 \texttt{get\_care\_context} & Leitura & Contexto de cuidado\\\hline
 \texttt{list\_care\_records} & Leitura & Registros de cuidado e histórico\\\hline
@@ -36,48 +48,37 @@
 \texttt{add\_care\_observation} & Escrita & Registro de observação\\\hline
 \texttt{create\_daily\_activity} & Escrita & Criação de atividade\\\hline
 \texttt{update\_daily\_activity} & Escrita & Alteração de atividade\\\hline
-\end{longtable}}{\small\noindent Fonte: Configuração do agente em 3 nov. 2026.\par}
+\end{longtable}}{\small\noindent Fonte: configuração do servidor MCP, nov. 2026.\par}
 
-As operações de escrita requerem esclarecimento dos dados necessários e aprovação antes da execução. Uma frase ambígua sobre dosagem ou horário não deve ser convertida diretamente em alteração. A confirmação apresenta a ação e seus argumentos, permitindo ao usuário revisar o pedido.
-
-\section{Aprovação e segurança}
-O fluxo da Figura~\ref{fig:agente_aprovacao} começa pela consulta do contexto e pela verificação da clareza do pedido. A negação da aprovação encerra a ação sem escrita. A aprovação, por sua vez, permite prosseguir para o servidor, mas não elimina a validação das regras de negócio e das permissões.
+\section{Aprovação das escritas e segurança}
+O fluxo projetado para as escritas, apresentado na Figura~\ref{fig:agente_aprovacao}, começa pela consulta do contexto e pela verificação da clareza do pedido, apresenta a ação e seus argumentos e só prossegue após aprovação explícita.
 
 \begin{figure}[htbp]
 \centering
-\caption{Solicitação, esclarecimento, aprovação e execução de uma operação de escrita}\label{fig:agente_aprovacao}
+\caption{Fluxo projetado de solicitação, esclarecimento, aprovação e execução de uma escrita}\label{fig:agente_aprovacao}
 \includegraphics[width=0.98\textwidth,height=0.66\textheight,keepaspectratio]{Figuras/SharePoint/agente_aprovacao.png}
 \fonte{Elaboração dos autores (2026).}
 \end{figure}
 
+Segundo a proposta recebida, a aprovação não seria imposta pela infraestrutura no caminho de integração então descrito. Nesse relato, o servidor MCP estaria configurado sem exigência de aprovação, e o relay de voz não trataria pedidos de aprovação do serviço. A única proteção é a instrução no prompt, que pede confirmação em dois turnos antes de qualquer escrita. A proposta relata uma gravação de atividade pela versão 24 sem confirmação; não acompanha o diálogo e o registro primário desse caso. O relato exige tratamento como risco e verificação em ambiente autorizado, não como teste repetido nesta revisão. Se confirmada essa configuração, a aprovação depende do comportamento do modelo e não de um controle verificável, contrariando RF15-AG; até a reconciliação, a garantia de aprovação não está demonstrada. \cite{DC_NICOLAS2026}
 
-A segurança é distribuída entre identificação do usuário, autorização do serviço e validação na API. Instruções no prompt complementam esses controles, mas não os substituem. Chaves e credenciais não integram o texto nem as capturas públicas.
+Uma segunda limitação relatada refere-se ao paciente consultado. O aplicativo exige a escolha do paciente e a API valida essa escolha ao abrir a conversa, mas, segundo a proposta, o identificador não seria repassado ao servidor MCP, que usaria o contexto de um paciente fixo configurado no servidor. Com um único paciente ativo, o efeito não aparece; com dois, o agente pode responder sobre o paciente errado. \cite{DC_NICOLAS2026}
 
-Quando o retorno de uma ferramenta é incerto, o agente deve consultar o estado antes de solicitar repetição. O mesmo cuidado se aplica à comunicação do resultado: preparar uma chamada, obter aprovação, persistir a alteração e produzir eventual efeito físico são etapas diferentes.
+A correção proposta, a verificar e testar, é: exigir aprovação nas ferramentas de escrita, tratar o pedido de aprovação no relay e no aplicativo com um botão de confirmar ou recusar, e repassar o paciente selecionado ao servidor MCP.
 
-\section{Voz e integração com o Care}
-A interface de voz utiliza um relay no backend. Na configuração histórica de 3 de novembro, esse caminho não processa as aprovações exigidas pelas ferramentas MCP, motivo pelo qual foi mantido separado do agente de teste. A resposta conversacional disponível no Care não é, portanto, apresentada como execução automática das oito ferramentas. \cite{DC_FOUNDRY,DC_ANALISE}
+\section{Voz, anexos e integração com o Care}
+O assistente do Care usa o mesmo agente por texto e por voz. Na conversa por voz em tempo real, a transcrição aparece durante a fala; quando a resposta exige consulta aos dados, a entrega relata cerca de 11~s até a primeira palavra em uma condição de consulta; não apresenta amostra de latências. O aplicativo também envia fotos e PDFs de receitas, convertidos em imagens no próprio celular; a entrega relata um teste com receita fictícia, quatro medicamentos e resposta em cerca de 15~s (Capítulo~\ref{cap:aplicativo}). \cite{DC_NICOLAS2026}
 
-A integração deve conservar os caminhos manuais do aplicativo e informar o que foi efetivamente realizado. O agente pode esclarecer uma solicitação, consultar e apresentar um retorno, mas não deve transformar uma falha de acesso em afirmação de ausência de dados.
+A integração conserva os caminhos manuais do aplicativo: tudo o que o agente faz pode ser feito pelas telas, e o resultado de uma escrita aparece nas mesmas listas.
 
 \section{Avaliação}
-A avaliação diferencia recuperação de contexto, escolha da ferramenta, argumentos, confirmação, autorização e efeito persistido. Também considera respostas a ambiguidades, recusa de pedidos clínicos e tratamento de falhas. O teste funcional do servidor MCP avalia uma parte dessa cadeia; não representa, isoladamente, a qualidade do modelo ou da experiência de voz.
-
-Os procedimentos são relacionados à estratégia de integração do capítulo seguinte. Os resultados do agente devem manter a versão, o ambiente e os casos utilizados, permitindo interpretar o alcance de cada evidência.
-
-\section{Estado da integração e alcance da evidência}
-Os novos insumos não apresentam uma campanha de interações do modelo que permita estimar precisão de seleção de ferramenta, frequência de falso sucesso ou segurança de escritas em contexto real. A suíte do MCP verifica componentes de software, não corresponde ao mesmo número de conversas avaliadas. A conversa de leitura documentada e a configuração de aprovação são evidências distintas de uma alteração aprovada, persistida e conferida no cuidado correto. \cite{DC_VALIDACAO2026}
-
-A aprovação do Foundry é uma política do caminho do agente, não uma trava universal de toda chamada ao MCP. Quem detiver a chave do serviço pode estar fora desse caminho; por isso, controle de segredo, autorização na API e registro da origem permanecem necessários. A monografia não presume que a integração entre voz, MCP e Care esteja validada apenas porque cada parte responde isoladamente. \cite{DC_VALIDACAO2026}
-
-\section{Relatos posteriores à configuração de referência}
-O pacote de novembro relata migração do agente para Azure Voice Live, desligamento do MCP dedicado anterior e consulta somente de leitura ao contexto do paciente por \texttt{GET /v1/care/assistant\_context}; as alterações permaneceriam no aplicativo. Essas informações são relatos de integração de outra frente, não uma atualização confirmada da configuração do agente neste capítulo. Não se apresentam a leitura de receita nem a redução de latência de 94,5 s para 11,0 s como métricas verificadas sem versão, cenário, repetição e registro primário. \cite{DC_VALIDACAO2026}
+A avaliação diferencia recuperação de contexto, escolha da ferramenta, argumentos, confirmação, autorização e efeito persistido. Também considera respostas a ambiguidades, recusa de pedidos clínicos, perguntas fora do tema e tratamento de falhas. O teste funcional do servidor MCP avalia uma parte dessa cadeia; não representa, isoladamente, a qualidade do modelo ou da experiência de voz.
 
 \section*{\textcolor{DCPendente}{Complementações necessárias}}
-\pendencia{AG01}{Confirmar modelo, parâmetros e versões finais do agente publicado e do agente chamado pelo aplicativo. O rótulo interno gpt-5.6-luna precisa de identificação verificável e não deve ser tratado como especificação pública do modelo.}
-\pendencia{AG02}{Fornecer evidências das oito ferramentas, aprovação e recusa de escritas, validação do servidor, tratamento de duplicatas e falhas ambíguas. Não executar gravações de teste em dados reais.}
+\pendencia{AG01}{Confirmar com Thiago modelo, parâmetros, exportação sanitizada e versão efetivamente chamada pelo aplicativo. A proposta cita v28 desde 25/11 e usa rótulo interno gpt-6-luna, diferente de gpt-5.6-luna no registro anterior; nenhum deles foi promovido a identificação pública de modelo sem comprovação.}
+\pendencia{AG02}{Conferir as oito ferramentas e o caminho de aprovação: proposta de 27/11 relata escrita sem confirmação na v24 e relay sem tratamento de aprovação. Obter evidências de aprovação/recusa e autorização no servidor; usar apenas dados fictícios em ambiente autorizado.}
 \pendencia{AG03}{Inventariar o conteúdo efetivo do armazenamento vetorial: fontes, revisão, atualização e avaliação da recuperação, incluindo manual atual. Não assumir base atualizada por existir \texttt{file\_search}.}
 \pendencia{AG04}{Anexar diálogos sanitizados e registros de chamadas/efeitos persistidos em ambiente de teste; identificar resultado parcial, erro, restauração e limpeza dos dados de teste.}
 \pendencia{AG05}{Definir e executar conjunto de avaliação do agente: casos, repetições, referência humana, critérios, falhas clínicas e resultados. Contagens de testes do MCP não são desempenho do modelo.}
 \pendencia{AG06}{Documentar permissões, rotação de chaves, limites de acesso, retenção e proteção contra instruções maliciosas em dados. Distinguir controles verificáveis de orientações do prompt.}
-\pendencia{AG07}{Reconciliar a configuração histórica de 03/11 com o relato posterior de Voice Live e ferramenta de contexto somente de leitura; identificar versão ativa, protocolo, permissões e evidência no Care antes de afirmar a integração atual.}
+\pendencia{AG07}{Revisar a proposta recebida com Thiago: reconciliar configuração de 03/11, relato anterior de Voice Live somente de leitura e nova indicação de v28 com MCP. Conferir encaminhamento do paciente selecionado, paciente fixo no MCP e correções implantadas, sem presumir que o risco foi resolvido.}
--- antes_rodada2/Capitulos/15_resultados.tex
+++ unificado_rodada2/Capitulos/15_resultados.tex
@@ -63,6 +63,22 @@
 \fonte{Elaboração a partir das tabelas do pacote de validação. \cite{DC_VALIDACAO2026}}
 \end{figure}
 
+\section{Dispensação vinculada: registros acrescentados em 27 de novembro}
+O novo CSV do Oficial contém oito registros iniciados entre 29 de outubro e 8 de novembro, não oito execuções homogêneas bem-sucedidas. Três pedidos (2, 6 e 7) foram recusados antes de mover e têm relato de zero saída. Há três ciclos completos com veredito: no 3, o sensor indica retenção e o relato é zero; no 4, leitura vazia e relato de uma unidade; no 5, retenção e resposta ``não observado''. O 8 requer reconciliação, com relato de uma unidade. O 1 recebe relato de saída cerca de nove dias depois do pedido, apesar de zero ciclos associados; permanece identificado como inconsistente. \cite{DC_NICOLAS2026}
+
+\input{Capitulos/tabela_ensaios}
+
+Não se adota a síntese ``estoque correto em 8/8'': a linha 5 não tem estoque posterior nem quantidade observada, e a linha 1 não serve como correspondência temporal confiável. Nas seis linhas restantes, a redução registrada corresponde à quantidade relatada, mas isso comprova apenas consistência contábil dos registros. Não há contagem física independente do reservatório que demonstre integridade em todas as linhas. Da mesma forma, a ausência de unidade extra nos relatos completos não é garantia de ausência de dose dupla nos oito casos. As proporções 3/8, 8/8 e 0/8 da proposta não são usadas como estimativas de eficácia ou segurança. \cite{DC_NICOLAS2026}
+
+A Tabela~\ref{tab:ensaios-simulado} contém sete linhas de 14 de novembro. O campo \texttt{fechamento} registra quatro encerramentos automáticos, dois relatos humanos de demonstração e uma linha sem fechamento. Portanto, cinco casos estão sem quantidade humana, mas apenas quatro estão explicitamente encerrados automaticamente. Nos dois relatos de demonstração, foram informadas duas unidades, com retenção indicada pelo sensor e estoque registrado 10 para 10. Não se mistura essa política com as travas do Oficial. \cite{DC_NICOLAS2026}
+
+\input{Capitulos/tabela_ensaios_simulado}
+
+Esses registros não se somam às 15 sessões nem aos 12 ciclos apresentados anteriormente: há sobreposição temporal e funcional entre as extrações. O novo CSV acrescenta identificação de operação e observação humana a parte do histórico, não uma campanha independente. Os intervalos de ADC das capturas históricas (vazio 2.755--2.952; ocupado 104--157), citados no memorial, também não substituem as faixas do perfil ativo nem incorporam as leituras intermediárias de todos os ciclos. \cite{DC_NICOLAS2026,DC_VALIDACAO2026}
+
+\subsection{Contagens e critérios que permanecem divergentes}
+A proposta resume localização em 4/9, enquanto a extração por fase do pacote anterior contém 1/12, 3/7 e 2/2; sem filtro e conjunto de identificadores equivalentes, essas proporções não foram intercambiadas. O resumo 3/26 de calibração refere-se à operação \texttt{calibrate\_slot}; a sessão distinta \texttt{calibrate\_five} continua separada. Indicadores de disponibilidade derivados de número de sinais por dia (91--94\% na entrega) não são a mesma métrica que a estimativa por lacunas de 98,90\% do relatório anterior. Nenhum deles mede acurácia física. \cite{DC_NICOLAS2026,DC_VALIDACAO2026}
+
 \section{Telemetria passiva da central}
 A janela das 22h11 às 22h40 contém 1.725 tentativas de consulta e uma falha HTTP do runtime, restando 1.724 amostras válidas por placa. As 1.614 leituras distintas por placa totalizam 3.228 sem indicação de erro ou troca de boot nas amostras válidas. A latência da consulta local foi mediana 183,4 ms, percentil 95 de 277,7 ms e máximo de 7.932,1 ms; não se trata da latência de uma dose ou de um comando remoto. \cite{DC_VALIDACAO2026}
 
@@ -91,10 +107,12 @@
 O erro do runtime pertence ao teste legado \texttt{test\_can\_hardware}; a API registra dois erros antigos de ambiente. O app de 25 de novembro apresenta 12 falhas e quatro ignorados mesmo na execução isolada; ``nenhuma falha nova'' não significa aprovação integral. A rodada de provisionamento é dc8, não demonstra por si a validação completa da versão instalada dc9. Os testes não foram reexecutados nesta consolidação. \cite{DC_VALIDACAO2026}
 \pendencia{RES04}{Vincular versões e logs completos do servidor e aplicativo apresentados na defesa; resolver ou justificar erros e falhas remanescentes. Completar testes autenticados de ponta a ponta e tarefas, sem somar rodadas.}
 
+A entrega de aplicativo também menciona a cópia de 18 de novembro, com 224/240 casos aprovados na suíte geral e 341/359 no Care, incluindo quatro ignorados. Não se trata de reexecução posterior à rodada de 25 de novembro; por isso, esses valores são históricos e não substituem a tabela de rodadas acima. As capturas demonstram a interface, não a aprovação dos testes ou o isolamento do paciente. \cite{DC_NICOLAS2026}
+
 \section{Visão, agente e avaliação de uso}
 O DOCX de visão fornece método, parâmetros e limites, não métricas experimentais. Os cinco eventos históricos originados pelo dispositivo e o evento manual de demonstração não compõem um conjunto de referência independente. A divergência entre regressão logística e vision-v3 está preservada no Capítulo~\ref{cap:visao}. \cite{DC_VALIDACAO2026,DC_VISAO2026}
 
-Para o agente, os novos relatos de integração e latência ainda exigem confirmação da frente responsável. Não foi localizada, nos materiais conferidos, campanha com casos, denominadores e efeitos persistidos que permita calcular desempenho do modelo. Não se infere ausência de testes do agente pela falta dessa campanha.
+Para o agente, a proposta de 27 de novembro detalha versões até v28, latências exploratórias de cerca de 11 s em voz e 15 s na leitura de receita e riscos de aprovação e contexto do paciente. São relatos ainda sujeitos à conferência da frente, não uma série de desempenho. \cite{DC_NICOLAS2026} Não foi localizada, nos materiais conferidos, campanha com casos, denominadores e efeitos persistidos que permita calcular desempenho do modelo. Não se infere ausência de testes do agente pela falta dessa campanha.
 \pendencia{RES05}{Completar os resultados de visão e agente separadamente, com método/versionamento reconciliados, conjunto de referência, falhas e denominadores.}
 \pendencia{RES06}{Inserir avaliação de usabilidade e acessibilidade, caso realizada: protocolo, autorizações aplicáveis, participantes, tarefas e achados. Não há base para afirmar melhoria de adesão ou eficácia clínica.}
 
--- antes_rodada2/Capitulos/16_discussao.tex
+++ unificado_rodada2/Capitulos/16_discussao.tex
@@ -5,6 +5,9 @@
 A leitura com o reservatório montado alterou substancialmente a referência óptica e motivou uma intervenção física e ajustes de amostragem. O caso evidencia que um limiar adequado sem o reservatório não é automaticamente transferível à montagem completa. As quatro retenções nos dez ciclos com releitura também mostram que reconhecer ocupação e transportar a unidade são problemas distintos. \cite{DC_VALIDACAO2026}
 
 A coincidência da média dos intervalos com o nominal decorre do fechamento dos perfis em uma volta de 4.096 fases. Sem referência angular independente, a dispersão desses intervalos descreve a distribuição no modelo, mas não demonstra precisão mecânica ou repetibilidade entre ensaios controlados. Uma amostra de duas localizações posteriores bem-sucedidas é um indício exploratório, não comprovação estatística de 98\% de acerto.
+
+\subsection{O que muda com os registros vinculados}
+O novo material acrescenta relatos humanos e identificadores a oito casos do Oficial, mas revela uma observação muito tardia e outra não realizada. Há saídas relatadas e recusas antes do movimento; os campos de estoque permitem verificar consistência contábil em seis linhas sem a inconsistência temporal. Isso melhora a rastreabilidade, sem sustentar ``estoque físico correto em 8/8'' ou taxa final de acerto. Os sete casos do Simulado têm quatro fechamentos automáticos, dois relatos de apresentação e um caso aberto; não substituem contagem independente. \cite{DC_NICOLAS2026}
 
 \section{Comparação com a literatura}
 A literatura discutida no Capítulo~\ref{cap:estadoarte} situa a integração de organização, dispensação e acompanhamento; os achados deste protótipo não permitem afirmar superioridade em adesão, segurança clínica, autonomia ou exatidão de dose. Comparações quantitativas exigem método, unidade experimental, amostra e condições equivalentes.
@@ -17,6 +20,8 @@
 
 Na visão, a divergência de versões impede combinar escores históricos com o método vision-v3. Mesmo após reconciliá-la, a identificação de uma sequência visual não comprova deglutição. Na segurança dos dados, conta operadora compartilhada, privilégios que contornam RLS e limites da aprovação no caminho do agente impedem afirmar isolamento individual ou conformidade integral apenas pela existência de autenticação. \cite{DC_VISAO2026,DC_COMPILADO,DC_VALIDACAO2026}
 
+A proposta do agente descreve aprovação dependente de instrução e possível uso de paciente fixo no MCP. Enquanto a configuração não for reconciliada e testada, as funções de escrita devem ser apresentadas como risco a controlar, não como benefício seguro comprovado. A síntese de armazenamento também evidencia que anexos e conversas podem ser processados no Azure, embora os resultados detalhados da câmera permaneçam locais; isso exige políticas distintas de finalidade e retenção. \cite{DC_NICOLAS2026,DC_SEGURANCA2026}
+
 \section{Implicações e continuidade}
 A prioridade é fechar o vínculo entre configuração, pedido, movimento, contagem física e registro. A campanha deve manter falhas e interrupções no denominador, caracterizar retenção e unidade extra, medir energia durante movimento e verificar recuperação sem repetir o efeito. Depois do comissionamento, cabem ensaios sem rede e sem NTP com RTC, avaliação rotulada da visão e do agente e tarefas de uso autorizadas. Esses itens são validação ainda necessária, não benefícios já entregues.
 \pendencia{DIS01}{Revisar a interpretação com a orientação e os responsáveis após a campanha final; conservar o recorte exploratório dos resultados atuais.}
--- antes_rodada2/Capitulos/17_conclusao.tex
+++ unificado_rodada2/Capitulos/17_conclusao.tex
@@ -2,7 +2,7 @@
 \section{Resposta aos objetivos}
 O trabalho resultou na construção e documentação de um protótipo modular que integra mecanismo de disco, ESP32, Raspberry Pi, comunicação I²C, serviços de aplicação e interface de cuidado. Os materiais recebidos permitem demonstrar montagem física, operações registradas entre central e placas, atualização de software e evidências parciais de transporte de unidades. O capítulo de visão passa a explicitar aquisição, processamento e decisão temporal, mantendo a divergência de implantação em aberto. \cite{DC_VALIDACAO2026,DC_VISAO2026}
 
-Esses resultados não encerram o objetivo de dispensação autônoma confiável. Ainda não há taxa pedido = saída por contagem humana em série, houve retenção em ciclos registrados, o RTC não está ativo e a agenda automática permanece desligada. Também não se dispõe de avaliação rotulada da visão, campanha completa do agente ou avaliação de uso que sustente melhoria de adesão ou eficácia clínica. \cite{DC_VALIDACAO2026,DC_VISAO2026}
+Esses resultados não encerram o objetivo de dispensação autônoma confiável. Os registros vinculados acrescentam observações humanas parciais, mas não uma campanha independente que estime a taxa pedido = saída; houve retenção em ciclos registrados, o RTC não está ativo e a agenda automática permanece desligada. Também não se dispõe de avaliação rotulada da visão, campanha completa do agente ou avaliação de uso que sustente melhoria de adesão ou eficácia clínica. \cite{DC_VALIDACAO2026,DC_VISAO2026}
 
 \section{Contribuições e continuidade}
 As contribuições demonstradas concentram-se na integração tecnológica, na rastreabilidade das operações e na identificação de condições que exigem intervenção humana. A distinção entre comando reconhecido, sessão encerrada, leitura da cavidade e quantidade coletada é necessária para que o acompanhamento não transforme incerteza em sucesso aparente.
--- antes_rodada2/FEI-bib/dosecerta-referencias.bib
+++ unificado_rodada2/FEI-bib/dosecerta-referencias.bib
@@ -3,8 +3,6 @@
   title = {DoseCerta: compilado interno da monografia},
   year = {2026},
   note = {Memorial técnico do projeto. Documento interno de desenvolvimento.},
-  url = {https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/_layouts/15/Doc.aspx?sourcedoc=%7BCB1B745D-0CDE-46E6-AF6E-A0CFFA7C3A2A%7D&file=DoseCerta_Monografia_Compilado.docx&action=default&mobileredirect=true&web=1},
-  urlaccessdate = {25 nov. 2026}
 }
 
 @misc{DC_CIRCUITOS,
@@ -12,8 +10,6 @@
   title = {HANDOFF DOSECERTA CIRCUITOS FINAL},
   year = {2026},
   note = {Memorial de circuitos. Revisão de 27 de setembro de 2026.},
-  url = {https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/DoseCerta_Compilado_Monografia/DoseCerta_Compilado_Monografia/05_Fontes_do_projeto/02_Projeto/Eletrica_e_Circuitos/Circuitos_2026-09-27/HANDOFF_DOSECERTA_CIRCUITOS_FINAL.md?web=1},
-  urlaccessdate = {25 nov. 2026}
 }
 
 @misc{DC_FOUNDRY,
@@ -21,8 +17,6 @@
   title = {Agentes no Foundry: configuração documentada},
   year = {2026},
   note = {Especificação técnica. Revisão de 3 de novembro de 2026.},
-  url = {https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/documenta%C3%A7%C3%A3o/documenta%C3%A7%C3%A3o/10-agentes-foundry.md?web=1},
-  urlaccessdate = {25 nov. 2026}
 }
 
 @misc{DC_ANALISE,
@@ -30,8 +24,6 @@
   title = {DoseCerta: análise do servidor e do aparelho},
   year = {2026},
   note = {Registro técnico de configuração. 12 de novembro de 2026.},
-  url = {https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/DoseCerta_Acervo_Completo_20261112/03_historico_e_analises/manual-agente-20261112/ANALISE_SERVIDOR_20261112.md?web=1},
-  urlaccessdate = {25 nov. 2026}
 }
 
 @misc{DC_ARTIGO,
@@ -157,3 +149,16 @@
  year = {2026},
  note = {Memorial da frente de visão fornecido pelos autores em formato DOCX. Descreve processamento local, rastreamento e máquina de estados; não apresenta conjunto experimental rotulado nem métricas finais.}
 }
+
+@misc{DC_NICOLAS2026,
+ author = {Kuhnast, Nicolas},
+ title = {DoseCerta: entrega de aplicativo, dados e integração de 27 de novembro de 2026},
+ year = {2026},
+ note = {Documento interno do projeto. Pacote com capítulos propostos, dezesseis capturas demonstrativas, CSVs de oito registros do Oficial e sete do Simulado e protocolo de campanha ainda proposto. Divergências entre resumo e linhas dos CSVs identificadas na consolidação.}
+}
+@misc{DC_SEGURANCA2026,
+ author = {{Equipe DoseCerta}},
+ title = {DoseCerta: segurança dos dados e armazenamento},
+ year = {2026},
+ note = {Síntese técnica interna recebida em 27 de novembro de 2026. Controles declarados e locais de processamento; não é laudo de auditoria ou comprovação de isolamento.}
+}
--- antes_rodada2/PosTextual/apendices.tex
+++ unificado_rodada2/PosTextual/apendices.tex
@@ -7,7 +7,7 @@
 \caption{Requisitos, evidências recebidas e aceite ainda necessário}\label{tab:ap-matriz}\\
 \hline\textbf{ID} & \textbf{Evidência disponível} & \textbf{Lacuna de aceite}\\\hline\endfirsthead
 \hline\textbf{ID} & \textbf{Evidência disponível} & \textbf{Lacuna de aceite}\\\hline\endhead
-RF01 & Disco, sensor e 12 ciclos registrados & Contagem independente, unidade extra e retenção\\\hline
+RF01 & Disco, 12 ciclos e oito registros vinculados, com lacunas & Campanha independente, unidade extra e retenção\\\hline
 RF02 & Associação e sinais descritos; montagem fotografada & Conferência física de cada posição e associação\\\hline
 RF03 & Fluxo e sinais documentados & Agenda real desligada; falta comissionamento e sequência automática\\\hline
 RF04 & Dez ciclos com releitura, de 12 registrados & Confrontar leitura com inspeção do disco e contagem no copo\\\hline
@@ -27,15 +27,59 @@
 RNF06 & Inventário de releases e versões & Manifesto sanitizado da configuração final e dependências\\\hline
 RNF07 & Fotos dos encaixes e quatro contatos & Inserção energizada, continuidade e integridade do barramento\\\hline
 RNF08 & Interface Care e sinais com apoio de texto & Tarefas autorizadas, acessibilidade e compreensão\\\hline
-RF13-APP & Care implementado e suítes registradas & Sessão válida/expirada e tarefas autenticadas por tela\\\hline
+RF13-APP & Care, suítes históricas e 16 capturas demonstrativas & Sessão válida/expirada, versão e tarefas autenticadas\\\hline
 RF14-VIS & Método de visão documentado & Reconciliar versões e avaliar sequências rotuladas\\\hline
-RF15-AG & Configuração histórica e relatos posteriores & Confirmar agente atual, ferramentas e aprovação de escrita\\\hline
+RF15-AG & Histórico e proposta v28 ainda a confirmar & Aprovação técnica, paciente correto e efeitos persistidos\\\hline
 RNF09-IA & Limites de finalidade descritos & Casos adversariais e avaliação humana do agente e da visão\\\hline
 RNF10-DADOS & Registros locais e centrais com origem & Matriz de acesso, retenção e auditoria de todas as observações\\\hline
 \end{longtable}\noindent Fonte: elaboração dos autores a partir das evidências recebidas. \cite{DC_VALIDACAO2026}\par}
 
+\section{Situação do protocolo recebido}
+O protocolo de 27 de novembro é uma \textbf{proposta} a aprovar antes da coleta, não campanha executada. As metas abaixo pertencem à proposta do contribuinte e não são metas clínicas nem critérios já aprovados pela orientação. O PDF de prévia emprega em alguns trechos verbos no passado; a presente consolidação os corrige para evitar afirmar experimentos sem fichas. \cite{DC_NICOLAS2026}
+
+Não se deverão realizar ensaios de ingestão com medicamentos ou participantes a partir deste plano de bancada. Unidades de ensaio, montagem segura e autorizações devem ser definidos previamente. Interrupções de alimentação ou rede exigem procedimento supervisionado e aprovado; a proposta não é autorização para intervenção em produção.
+
+\section{Proposta de campanha: configuração antes de cada bloco}
+Antes do primeiro ensaio de cada bloco deverão ser registrados: o ambiente do servidor e a política de travas da central; as versões do runtime, dos firmwares do intermediário e do submódulo, do aplicativo e da API; o submódulo e a posição utilizados; o comprimido de teste (tipo, diâmetro, espessura e massa medidos); a revisão do disco e a inclinação montada; o estoque inicial contado manualmente; os responsáveis pela operação, pela contagem e pelas fotografias. A montagem deverá ser fotografada com escala; não há fichas preenchidas dessa campanha no pacote.
+
+\section{Procedimento de um ensaio de dispensação}
+\begin{enumerate}
+\item Identificação do ensaio em papel visível junto ao copo coletor.
+\item Pedido pelo fluxo de dispensação vinculada do aplicativo, com a quantidade definida para o bloco.
+\item Espera pelo resultado do aparelho, sem repetir o pedido.
+\item Contagem manual das unidades no copo, adotada como referência.
+\item Fotografia do copo com a identificação do ensaio e fotografia da tela com o resultado e o identificador da operação.
+\item Registro da observação no aplicativo, que debita o estoque somente pela quantidade observada.
+\item Separação das unidades liberadas, sem devolvê-las ao reservatório durante o bloco.
+\item Conferência do estoque físico com o estoque do aplicativo a cada dez ensaios.
+\end{enumerate}
+
+Três travamentos consecutivos interrompem o bloco; após qualquer ajuste mecânico, inicia-se novo bloco identificado, preservando todos os resultados e motivos de interrupção do anterior. Reiniciar não autoriza apagar as tentativas desfavoráveis. Ensaios sem contagem ou sem fotografia são considerados inválidos e reportados como tal.
+
+\section{Blocos e critérios de aceitação}
+{\small\setlength{\tabcolsep}{3pt}\begin{longtable}{p{0.06\textwidth}p{0.4\textwidth}p{0.07\textwidth}p{0.37\textwidth}}
+\caption{Blocos e critérios propostos, ainda não aprovados nem executados}\label{tab:ap-blocos}\\
+\hline\textbf{Bloco} & \textbf{Ensaio} & \textbf{N} & \textbf{Critério}\\\hline\endfirsthead
+\hline\textbf{Bloco} & \textbf{Ensaio} & \textbf{N} & \textbf{Critério}\\\hline\endhead
+A & Dispensação de uma unidade & 50 & Pelo menos 90\% com exatamente uma unidade; nenhuma dose extra\\\hline
+B & Dispensação de duas unidades & 20 & Pelo menos 85\% com exatamente duas; nenhuma dose extra\\\hline
+C & Falhas controladas, com procedimento seguro aprovado (rede, reinício e alimentação) & 20 & Nenhum movimento repetido; estado incerto sinalizado\\\hline
+D & Leitura do sensor com cavidade vazia e ocupada & 60 & Faixas sem sobreposição; pelo menos 95\% corretas\\\hline
+E & Sinalização luminosa por posição e cor & 12 & Todas corretas\\\hline
+F & Agenda sem internet (RTC ativo, energia de retenção e comissionamento) & 5 & Todas no horário\\\hline
+\end{longtable}}{\small\noindent Fonte: proposta de campanha recebida em 27 nov. 2026. \cite{DC_NICOLAS2026}\par}
+
+Em todos os blocos, o estoque do aplicativo deve coincidir com a contagem física. Caso a amostragem e a independência sejam justificadas, as proporções deverão ser acompanhadas de intervalo de Wilson de 95\%, com numerador, denominador, exclusões e inconclusivos explícitos. Esses intervalos não corrigem viés de seleção, ajuste durante o teste ou repetição dependente no mesmo conjunto. Zero eventos observados não significa risco nulo.
+
+\section{Ficha de ensaio}
+Cada ensaio gera uma linha com: bloco, número, data e hora, identificador da operação, quantidade pedida, quantidade contada no copo, resultado do aparelho, leituras do sensor antes e depois do giro, estoque do aplicativo antes e depois, estoque físico contado, tempo de resposta, nomes das fotografias, responsável pela contagem, validade e observações. Os campos de operação, resultado, sensor, estoque e tempo poderão ser extraídos do banco de dados; a contagem, as fotografias e as observações são preenchidas manualmente.
+
+
+\section{Vínculo entre blocos e requisitos}
+Os blocos A e B fornecem dados para RF01 e RF04; D complementa RF04; E verifica RF02 e parte de RF12. As tentativas da preparação caracterizam RF05. C informa RNF02 e RNF03; F se refere à continuidade de RNF01, condicionada ao comissionamento temporal. RF06 e RF13-APP requerem também registros de origem, autenticação e acompanhamento. Os demais requisitos da matriz permanecem sujeitos a ensaios específicos; a campanha não encerra automaticamente todos os 25 requisitos.
+
 \section{Inventário e integridade}
-O diretório \texttt{Dados/validacao\_20261126} conserva tabelas de sessões, ciclos, calibração, comunicação, servidor e software. O histórico de observações foi preservado com sua proveniência; o projeto distribuído não inclui bancos brutos nem scripts executáveis do arquivo recebido. O mapa \texttt{mapa\_fotos\_20261126.json} relaciona cada painel às imagens de origem. As pranchas fotográficas foram compostas e redimensionadas para a monografia, sem reconstrução de conteúdo.
+O diretório \texttt{Dados/validacao\_20261126} conserva tabelas de sessões, ciclos, calibração, comunicação, servidor e software. O histórico de observações foi preservado com sua proveniência; o projeto distribuído não inclui bancos brutos nem scripts executáveis do arquivo recebido. O diretório \texttt{Dados/entrega\_Nicolas\_20261127} conserva os CSVs e o protocolo proposto, além da síntese de segurança. As tabelas-fonte recebidas não foram alteradas. O mapa \texttt{mapa\_fotos\_20261126.json} relaciona cada painel às imagens de origem. As pranchas fotográficas foram compostas e redimensionadas para a monografia, sem reconstrução de conteúdo.
 
 \section{Protocolos ainda não executados}
 O plano de caixa preta recebido propõe blocos de localização com disco vazio, dispensação com contagem independente e comunicação/energia. Seu executor aprovado em testes de software não transforma o plano em experimento executado. A ficha de referência, versões e condições devem acompanhar cada tentativa; falhas e interrupções precisam permanecer no denominador. \cite{DC_VALIDACAO2026}
--- antes_rodada2/PreTextual/abstract.tex
+++ unificado_rodada2/PreTextual/abstract.tex
@@ -1,6 +1,6 @@
 \begin{resumo}[Abstract]\begin{otherlanguage*}{english}
 Managing a treatment involving multiple medications requires coordinating schedules, quantities, and availability while monitoring daily care events. This work presents DoseCerta, a modular prototype for unit-dose medication dispensing and care monitoring intended for older adults with polypharmacy. The system combines removable reservoirs, a rotating disc with five cavities, a stepper motor, and optical sensing, with distributed control provided by a Raspberry Pi Zero 2 W and ESP32 microcontrollers. The modules communicate over a four-contact interface carrying power and a shared I²C bus. The central unit maintains a local schedule and operational records and synchronizes information with an API and a central database. The Care application provides authenticated configuration, a daily plan, a history, and a user manual, while the computer vision and artificial intelligence agent components support observation and interaction. Development was organized around requirements, incremental construction, and verification of components and interfaces. The evaluation strategy distinguishes software behavior, physical execution, and interpretation of events.
-The received records contain 3,430 DC1 commands and 12 dispensing cycles, including four classified as retained units. These records do not establish dispensing accuracy without independent physical counts. The real scheduled dispensing function remained disabled, and vision accuracy was not measured. 
+The received records contain 3,430 DC1 commands and 12 dispensing cycles, including four classified as retained units. Eight linked records from the Official environment add partial human observations, including one missing response and one inconsistent late entry. These overlapping extracts do not establish dispensing accuracy or replace a campaign with independent reference counts. The real scheduled dispensing function remained disabled, and vision accuracy was not measured. 
 \pendencia{PRE-ABS}{Complete this abstract with the main quantitative results and conclusions after the experimental campaign. Match the final method and the institutional word limit.}
 \vspace{\onelineskip}\noindent\textbf{Keywords}: medication dispensing; embedded systems; polypharmacy; systems integration; care support.
 \end{otherlanguage*}\end{resumo}
--- antes_rodada2/PreTextual/resumo.tex
+++ unificado_rodada2/PreTextual/resumo.tex
@@ -1,6 +1,6 @@
 \begin{resumo}
 A organização de tratamentos com vários medicamentos exige controlar horários, quantidades e disponibilidade, além de acompanhar os eventos da rotina de cuidado. Este trabalho apresenta o DoseCerta, um protótipo modular de dispensação unitária e acompanhamento de medicamentos voltado a pessoas idosas em regime de polifarmácia. O sistema integra reservatórios removíveis, disco rotativo de cinco cavidades, motor de passo e leitura óptica, com controle distribuído entre uma Raspberry Pi Zero 2 W e microcontroladores ESP32. A comunicação dos módulos utiliza uma interface de quatro vias, com alimentação e barramento I²C compartilhado. A central mantém agenda e registros locais e sincroniza as informações com uma API e um banco de dados central. O aplicativo Care reúne configuração autenticada, plano diário, histórico e manual, enquanto as frentes de visão computacional e agente de inteligência artificial complementam a observação e a interação. O desenvolvimento foi organizado por requisitos, construção incremental e verificação das partes e de suas interfaces. A estratégia de avaliação distingue comportamento de software, execução física e interpretação dos eventos.
-Os registros recebidos contêm 3.430 comandos DC1 e 12 ciclos de dispensação, incluindo quatro classificados como retenção. Sem contagem física independente, esses dados não estabelecem taxa de acerto da dose. A dispensação agendada real permanecia desligada e o desempenho da visão não foi medido. 
+Os registros recebidos contêm 3.430 comandos DC1 e 12 ciclos de dispensação, incluindo quatro classificados como retenção. Oito registros vinculados no ambiente Oficial acrescentam observações humanas parciais, com uma resposta ausente e uma anotação tardia inconsistente. Esses recortes sobrepostos não estabelecem taxa de acerto da dose nem substituem campanha com referência independente. A dispensação agendada real permanecia desligada e o desempenho da visão não foi medido. 
 \pendencia{PRE-RES}{Completar o resumo com os principais resultados quantitativos e a conclusão após a campanha experimental. Ajustar o texto ao método final e ao limite institucional de palavras.}
 \vspace{\onelineskip}\noindent\textbf{Palavras-chave}: dispensação de medicamentos; sistemas embarcados; polifarmácia; integração de sistemas; assistência ao cuidado.
 \end{resumo}
--- antes_rodada2/main.tex
+++ unificado_rodada2/main.tex
@@ -20,11 +20,13 @@
 \usepackage{hyphenat}
 \input{pendencias_dosecerta}
 \makeatletter
+% Usar argumento opcional do ambiente; não imprimir o rótulo do marcador.
+\renewcommand{\imprimirfolhaderostostar}[1]{%
+\begin{folhaderosto*}[#1]\folhaderostocontent\end{folhaderosto*}}
+\renewcommand{\imprimirfolhaderostonostar}[1]{%
+\begin{folhaderosto}[#1]\folhaderostocontent\end{folhaderosto}}
 \renewcommand{\imprimirfolhaderosto}[1][\folhaderostoname]{%
-\@ifstar
-{\imprimirfolhaderostostar{#1}}
-{\imprimirfolhaderostonostar{#1}}%
-}
+\@ifstar{\imprimirfolhaderostostar{#1}}{\imprimirfolhaderostonostar{#1}}}
 \makeatother
 % A edição digital não insere páginas de paridade vazias.
 \let\cleardoublepage\clearpage
@@ -96,4 +98,4 @@
 \begin{anexosenv}
 \include{PosTextual/anexos}
 \end{anexosenv}
-\end{document}+\end{document}
--- antes_rodada2/referencias.tex
+++ unificado_rodada2/referencias.tex
@@ -12,7 +12,7 @@
 
 \bibitem[Equipe DoseCerta 2026a]{DC_FOUNDRY}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026a}
-EQUIPE DOSECERTA. \textbf{Agentes no Foundry: configuração documentada}. 2026a. Especificação técnica. Revisão de 3 de novembro de 2026. Disponível em: \url{https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/documenta%C3%A7%C3%A3o/documenta%C3%A7%C3%A3o/10-agentes-foundry.md?web=1}. Acesso em: 25 nov. 2026.
+EQUIPE DOSECERTA. \textbf{Agentes no Foundry: configuração documentada}. 2026a. Especificação técnica. Revisão de 3 de novembro de 2026.
 
 \bibitem[Equipe DoseCerta 2026b]{DC_VISUAL}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026b}
@@ -26,21 +26,21 @@
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026d}
 EQUIPE DOSECERTA. \textbf{Contrato/proposta de projeto do grupo 4}. 2026d. Proposta de projeto, grupo 4. Documento institucional assinado.
 
-\bibitem[Equipe DoseCerta 2026e]{DC_ANALISE}
+\bibitem[Equipe DoseCerta 2026e]{DC_APP}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026e}
-EQUIPE DOSECERTA. \textbf{DoseCerta: análise do servidor e do aparelho}. 2026e. Registro técnico de configuração. 12 de novembro de 2026. Disponível em: \url{https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/DoseCerta_Acervo_Completo_20261112/03_historico_e_analises/manual-agente-20261112/ANALISE_SERVIDOR_20261112.md?web=1}. Acesso em: 25 nov. 2026.
+EQUIPE DOSECERTA. \textbf{DoseCerta: aplicativo Care, levantamento documental e texto-base para a monografia}. 2026e. Memorial de desenvolvimento do aplicativo Care. Documento do projeto.
 
-\bibitem[Equipe DoseCerta 2026f]{DC_APP}
+\bibitem[Equipe DoseCerta 2026f]{DC_COMPILADO}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026f}
-EQUIPE DOSECERTA. \textbf{DoseCerta: aplicativo Care, levantamento documental e texto-base para a monografia}. 2026f. Memorial de desenvolvimento do aplicativo Care. Documento do projeto.
+EQUIPE DOSECERTA. \textbf{DoseCerta: compilado interno da monografia}. 2026f. Memorial técnico do projeto. Documento interno de desenvolvimento.
 
-\bibitem[Equipe DoseCerta 2026g]{DC_COMPILADO}
+\bibitem[Equipe DoseCerta 2026g]{DC_VALIDACAO2026}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026g}
-EQUIPE DOSECERTA. \textbf{DoseCerta: compilado interno da monografia}. 2026g. Memorial técnico do projeto. Documento interno de desenvolvimento. Disponível em: \url{https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/_layouts/15/Doc.aspx?sourcedoc=%7BCB1B745D-0CDE-46E6-AF6E-A0CFFA7C3A2A%7D&file=DoseCerta_Monografia_Compilado.docx&action=default&mobileredirect=true&web=1}. Acesso em: 25 nov. 2026.
+EQUIPE DOSECERTA. \textbf{DoseCerta: insumos de validação de 26 de novembro de 2026}. 2026g. Pacote técnico fornecido pelos autores: relatório, erratas, catálogo fotográfico, tabelas extraídas do aparelho e do servidor e telemetria. Ensaios de origem não repetidos na consolidação da monografia.
 
-\bibitem[Equipe DoseCerta 2026h]{DC_VALIDACAO2026}
+\bibitem[Equipe DoseCerta 2026h]{DC_SEGURANCA2026}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026h}
-EQUIPE DOSECERTA. \textbf{DoseCerta: insumos de validação de 26 de novembro de 2026}. 2026h. Pacote técnico fornecido pelos autores: relatório, erratas, catálogo fotográfico, tabelas extraídas do aparelho e do servidor e telemetria. Ensaios de origem não repetidos na consolidação da monografia.
+EQUIPE DOSECERTA. \textbf{DoseCerta: segurança dos dados e armazenamento}. 2026h. Síntese técnica interna recebida em 27 de novembro de 2026. Controles declarados e locais de processamento; não é laudo de auditoria ou comprovação de isolamento.
 
 \bibitem[Equipe DoseCerta 2026i]{DC_VISAO2026}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026i}
@@ -48,7 +48,7 @@
 
 \bibitem[Equipe DoseCerta 2026j]{DC_CIRCUITOS}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026j}
-EQUIPE DOSECERTA. \textbf{HANDOFF DOSECERTA CIRCUITOS FINAL}. 2026j. Memorial de circuitos. Revisão de 27 de setembro de 2026. Disponível em: \url{https://generalmotors-my.sharepoint.com/personal/cz3l6y_nam_corp_gm_com/Documents/tcc/DoseCerta_Compilado_Monografia/DoseCerta_Compilado_Monografia/05_Fontes_do_projeto/02_Projeto/Eletrica_e_Circuitos/Circuitos_2026-09-27/HANDOFF_DOSECERTA_CIRCUITOS_FINAL.md?web=1}. Acesso em: 25 nov. 2026.
+EQUIPE DOSECERTA. \textbf{HANDOFF DOSECERTA CIRCUITOS FINAL}. 2026j. Memorial de circuitos. Revisão de 27 de setembro de 2026.
 
 \bibitem[Equipe DoseCerta 2026k]{DC_LISTA}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026k}
@@ -57,6 +57,10 @@
 \bibitem[Equipe DoseCerta 2026l]{DC_PROPOSTA}
 \abntrefinfo{Equipe DoseCerta}{Equipe DoseCerta}{2026l}
 EQUIPE DOSECERTA. \textbf{Proposta de projeto, grupo 4}. 2026l. Proposta e orçamento do projeto. Planilha eletrônica.
+
+\bibitem[Kuhnast 2026]{DC_NICOLAS2026}
+\abntrefinfo{Kuhnast}{Kuhnast}{2026}
+KUHNAST, Nicolas. \textbf{DoseCerta: entrega de aplicativo, dados e integração de 27 de novembro de 2026}. 2026. Documento interno do projeto. Pacote com capítulos propostos, dezesseis capturas demonstrativas, CSVs de oito registros do Oficial e sete do Simulado e protocolo de campanha ainda proposto. Divergências entre resumo e linhas dos CSVs identificadas na consolidação.
 
 \bibitem[Masnoon \textit{et al.} 2017]{MASNOON2017}
 \abntrefinfo{Masnoon \textit{et al.}}{Masnoon \textit{et al.}}{2017}
--- antes_rodada2/validar_integracao.py
+++ unificado_rodada2/validar_integracao.py
@@ -85,7 +85,30 @@
 photos=json.loads((R/'mapa_fotos_20261126.json').read_text())
 photo_names=[x['foto'] for group in photos.values() for x in group]
 if len(photo_names)!=35 or len(set(photo_names))!=35: errors.append('Mapa fotográfico sem as 35 imagens únicas')
-summary={'arquivos_tex_incluidos':len(seen),'rotulos':len(labels),'referencias_internas':len(refs),'figuras':len(images),'citacoes_distintas':len(cites),'pendencias':len(pending),'erros':errors,'avisos':warnings,'compilacao_pdf':'NAO_EXECUTADA_COMPILADOR_INDISPONIVEL','calibracao_media':statistics.mean(intervals),'calibracao_desvio_amostral':statistics.stdev(intervals),'ciclos_por_resultado':dict(co)}
+# Round 2 evidence controls. CSVs are source data, never executed.
+N=R/'Dados/entrega_Nicolas_20261127'
+def incoming_csv(name):
+ with (N/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f,delimiter=';'))
+oficial=incoming_csv('ensaios_dispensacao.csv');simulado=incoming_csv('ensaios_dispensacao_simulado.csv')
+assert len(oficial)==8 and len(simulado)==7
+assert len({r['operation_id'] for r in oficial+simulado})==15
+assert sum(not r['qtd_observada'] for r in oficial)==1
+assert sum(not r['estoque_depois'] for r in oficial)==1
+eligible=[r for r in oficial if r['ensaio']!='1' and r['qtd_observada']!='' and r['estoque_depois']!='']
+assert len(eligible)==6
+assert all(int(r['estoque_antes'])-int(r['estoque_depois'])==int(r['qtd_observada']) for r in eligible)
+closures=collections.Counter(r['fechamento'] for r in simulado)
+assert closures=={'presentation_policy':4,'human_report':2,'sem fechamento':1}
+assert sum(not r['qtd_observada'] for r in simulado)==5
+for q in json.loads((R/'historico_pendencias_antes_rodada2.json').read_text()):
+ if q['id'] not in counts:errors.append('Pendência da rodada 1 desapareceu: '+q['id'])
+if len(list((R/'Figuras/App').glob('*.jpg')))<16:errors.append('Capturas incompletas')
+for f in seen:
+ if f.exists():
+  txt=f.read_text()
+  if any(ord(c)<32 and c not in '\n\r' for c in txt):errors.append('Controle inesperado no texto: '+str(f.relative_to(R)))
+if 'generalmotors-my.sharepoint.com' in (R/'referencias.tex').read_text():errors.append('URL corporativa exposta nas referências geradas')
+summary={'arquivos_tex_incluidos':len(seen),'rotulos':len(labels),'referencias_internas':len(refs),'figuras':len(images),'citacoes_distintas':len(cites),'pendencias':len(pending),'erros':errors,'avisos':warnings,'compilacao_pdf':'NAO_EXECUTADA_COMPILADOR_INDISPONIVEL','calibracao_media':statistics.mean(intervals),'calibracao_desvio_amostral':statistics.stdev(intervals),'ciclos_por_resultado':dict(co),'registros_vinculados_oficial':len(oficial),'registros_vinculados_simulado':len(simulado),'oficial_consistencia_contabil':{'linhas_elegiveis':len(eligible),'nao_equivale_a_estoque_fisico':True},'simulado_fechamentos':dict(closures)}
 (R/'pendencias.json').write_text(json.dumps(sorted(pending,key=lambda x:x['arquivo']),ensure_ascii=False,indent=2)+'\n')
 (R/'validacao_estatica.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(summary,ensure_ascii=False,indent=2))
