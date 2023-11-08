import pyodbc
import paramiko


# Parâmetros para a conexão SSH
ssh_host = ip_do_servidor_ssh
ssh_port = 22
ssh_username = usuario_de_conexão
ssh_private_key_path =  Caminho para sua chave RSA privada
 
# Parâmetros para a conexão SQL Server
sql_server_host = ip do servidor (verifique se a maquina virtual consegue resolver hostname ou somente o ip)
sql_server_port = Porta padrão do SQL Server
sql_server_database = database
sql_server_username = usuario
sql_server_password = password

# Carregue a chave privada RSA
private_key = paramiko.RSAKey(filename=ssh_private_key_path)

# Estabeleça a conexão SSH
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ssh_host, ssh_port, ssh_username, pkey=private_key)
 
# Crie um túnel SSH para encaminhar a porta do SQL Server
ssh_tunnel = ssh_client.get_transport().open_channel('direct-tcpip', (sql_server_host, sql_server_port), ('localhost', 0))

stdin, stdout, stderr = ssh_client.exec_command('ls -l')
#print(stdout.read().decode())

#print({ssh_tunnel.getpeername()[1]})


# Construa a string de conexão para o SQL Server

sql_server_connection_string = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER=localhost,{ssh_tunnel.getpeername()[1]};"
    # f"SERVER=ipserver,porta do banco;" teste realizado forçando o ip do servidor
    f"DATABASE={sql_server_database};"
    f"UID={sql_server_username};"
    f"PWD={sql_server_password};"
    f"Trusted_Connection=yes;"
)
print(sql_server_connection_string)
try:
    # Conecte-se ao SQL Server através do túnel SSH
    conn = pyodbc.connect(sql_server_connection_string)
 
    # Crie um cursor para executar consultas SQL
    cursor = conn.cursor()
 
    # Exemplo: Execute uma consulta SQL
    cursor.execute('SELECT getdate();')
    rows = cursor.fetchall()
 
    for row in rows:
        print(row)
 
    # Feche o cursor e a conexão
    cursor.close()
    conn.close()
 
except pyodbc.Error as ex:
    print('Erro na conexão com o SQL Server:', ex)
 
# Feche o túnel SSH e a conexão SSH
ssh_tunnel.close()
ssh_client.close()
