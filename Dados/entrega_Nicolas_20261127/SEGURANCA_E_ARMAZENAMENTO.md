# DoseCerta: segurança dos dados e armazenamento

## 1. Proteções em cada camada


| Camada             | Proteção                                                                                                                                                                         |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rede**           | Todo o tráfego passa por HTTPS, com certificado válido. O banco de dados não fica exposto: só a API conversa com ele.                                                            |
| **Usuário**        | Login com e-mail e senha, que gera um token de sessão enviado em cada pedido à API.                                                                                              |
| **Permissão**      | A API confere, a cada operação, se aquele usuário pode agir sobre aquele paciente. Quando um aparelho atende mais de um paciente, a escolha explícita do paciente é obrigatória. |
| **Banco de dados** | 40 políticas de acesso por linha, 62 regras de validação e 48 chaves estrangeiras garantem que só dados coerentes e autorizados sejam gravados e lidos.                          |
| **Aparelho**       | A Raspberry tem credencial própria e é pareada por um token de uso único, guardado só como hash. A Pi nunca acessa o banco diretamente: tudo passa pela API.                     |
| **Wi-Fi da Pi**    | A configuração é feita pelo celular, via Bluetooth, com um desafio de autenticação antes de a senha da rede ser enviada.                                                         |
| **Atualizações**   | Os pacotes de atualização da Pi chegam com hash e assinatura, conferidos antes da instalação.                                                                                    |
| **Integridade**    | Toda escrita leva uma chave de idempotência: se o pedido for reenviado, não duplica registro nem repete movimento do motor.                                                      |
| **Auditoria**      | Cada comando e evento registra quem fez, quando e a origem (aparelho, pessoa ou sistema), formando uma trilha de auditoria.                                                      |
| **Ambientes**      | Oficial e simulado usam bancos separados. A demonstração pública roda só no navegador, com dados fictícios, sem acesso ao servidor.                                              |


## 2. Onde os dados ficam


| Local                                    | O que fica armazenado                                                                                                           | Observação                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Servidor (VPS), PostgreSQL em Docker** | Cadastros de pacientes e responsáveis, medicamentos, horários, registros de tomada, observações, comandos, eventos e telemetria | Ambientes oficial e simulado em bancos separados                                                      |
| **Raspberry Pi, banco SQLite local**     | Agenda, decisões e execuções de dose, filas de entrada e saída                                                                  | Permite operar sem internet; grava cada transação de forma durável (modo WAL, sincronização completa) |
| **Raspberry Pi, pasta local da visão**   | Resultados das análises da câmera                                                                                               | Não são enviados ao servidor; ao servidor chegam só o pedido e o estado                               |
| **Azure (Microsoft Foundry)**            | Conversas com o assistente e fotos ou PDFs de receita enviados a ele                                                            | Dados de saúde processados por serviço externo                                                        |


