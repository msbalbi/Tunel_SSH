# Tunel_SSH
Projeto referente a realizar um tunel ssh usando uma vpc em cloud


O código fornecido é um script Python que demonstra como estabelecer uma conexão com um servidor SQL Server através de um túnel SSH usando as bibliotecas `pyodbc` e `paramiko`. Abaixo, vou explicar cada parte do código em detalhes:

1. Importação de bibliotecas:
   - `pyodbc`: É uma biblioteca Python para acesso a bancos de dados via ODBC (Open Database Connectivity).
   - `paramiko`: É uma biblioteca Python que fornece suporte SSH para a criação de túneis e execução de comandos remotos.

2. Parâmetros de conexão SSH:
   - `ssh_host`: O endereço IP do servidor SSH com o qual você deseja estabelecer uma conexão.
   - `ssh_port`: A porta do servidor SSH (geralmente a porta padrão é 22).
   - `ssh_username`: O nome de usuário que será usado para autenticar na conexão SSH.
   - `ssh_private_key_path`: O caminho para a chave RSA privada que será usada para autenticação SSH.

3. Parâmetros de conexão SQL Server:
   - `sql_server_host`: O endereço IP do servidor SQL Server que você deseja acessar.
   - `sql_server_port`: A porta usada pelo servidor SQL Server (a porta padrão é 1433).
   - `sql_server_database`: O nome do banco de dados que você deseja acessar.
   - `sql_server_username`: O nome de usuário para autenticação no SQL Server.
   - `sql_server_password`: A senha do usuário para autenticação no SQL Server.

4. Carregando a chave privada RSA:
   - A biblioteca `paramiko` é usada para carregar a chave privada RSA a partir do caminho especificado.

5. Estabelecendo a conexão SSH:
   - Um objeto `SSHClient` é criado.
   - O método `set_missing_host_key_policy` é usado para aceitar automaticamente as chaves do host.
   - A conexão SSH é estabelecida com o servidor SSH usando as informações fornecidas (endereço IP, porta, nome de usuário e chave privada).

6. Criando um túnel SSH:
   - Um túnel SSH é criado para encaminhar a porta do SQL Server através do servidor SSH.
   - A função `get_transport()` obtém o canal de transporte SSH.
   - `open_channel('direct-tcpip', ...)` cria o túnel SSH.

7. Construindo a string de conexão SQL Server:
   - A string de conexão é montada usando informações do servidor SSH e do SQL Server.
   - O servidor SQL é definido como "localhost" e a porta é obtida dinamicamente do túnel SSH.
   - Outros parâmetros, como banco de dados, nome de usuário e senha, são definidos na string de conexão.

8. Conectando-se ao SQL Server:
   - A biblioteca `pyodbc` é usada para estabelecer uma conexão com o SQL Server usando a string de conexão.
   - Um cursor é criado para executar consultas SQL.

9. Exemplo de consulta SQL:
   - O código executa uma consulta SQL simples que retorna a data e hora do servidor SQL.
   - Os resultados da consulta são impressos na tela.

10. Fechando a conexão e o cursor:
   - Após a execução da consulta, o cursor e a conexão são fechados para liberar recursos.

11. Tratamento de exceções:
   - O código inclui um bloco `try...except` para lidar com exceções que possam ocorrer durante a conexão ou consulta SQL. Qualquer erro é impresso na tela.

12. Fechando o túnel SSH e a conexão SSH:
   - No final do script, o túnel SSH e a conexão SSH são fechados para liberar os recursos e encerrar a conexão com o servidor SSH.

Este código permite que você acesse um servidor SQL Server através de uma conexão SSH segura, usando uma chave privada RSA para autenticação. Certifique-se de fornecer os valores corretos para os parâmetros de conexão SSH e SQL Server antes de executar o código.
