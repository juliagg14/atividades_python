import mysql.connector as mysql

database = input("Digite um database que você deseja conectar: ")
cursorx = mysql.connect(
host ='127.0.0.1',
port=3306,
database = database,
user = 'root',
password=''
)

 
if cursorx.is_connected():
    db_info = cursorx.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = cursorx.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    
    tabela1 = input("digite o nome do seu registro: ")
    
def criar_registro():
    
    cursor.execute("create table if not exists " + (tabela1) + "(`id` int not null auto_increment primary key, `nome` varchar(50), `idade` int not null);")
    
def adicionar_dados():
    adicionar_dados = f"INSERT INTO {tabela1} (id, nome, idade) VALUES (%s, %s, %s)"
    id= int(input("digite seu id: "))
    nome= input("digite seu nome: ")
    idade= int(input("digite sua idade: "))
    
    cursor.execute(adicionar_dados, (id, nome, idade))
    cursorx.commit()   

        