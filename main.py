from funcoes import *
from tkinter import *
from PIL import Image
import os 

#aqui começo a fazer o meu porgrama das funções e organizar e desenvolver todas as opções do menu


#CADASTRAR DADOS:
def cadastrarDados():
    try:
        #criando um arquivo txt
        with open("Dados.txt","a") as arquivo:
            #solicitar ao usuário as opções que ele deseja 
            codigo = int(input("Código do atleta: "))
            nome = input("Nome do atleta: ")
            idade = int(input("Idade do atleta: "))
            telefone_atleta = int(input("Telefone do atleta: "))
            documento = int(input("Número do documento(RG): "))
            sexo = input("Sexo do atleta: ")

            #formatar os dados do aluno em uma string
            clientes = f"{codigo}, {nome}, {idade}, {telefone_atleta}, {documento}, {sexo}\n"
            print(clientes)

            #escrever os dados formatados no arquivo txt
            arquivo.write(clientes)

            #exibir uma mensagem de sucesso
            print("Ação realizada com sucesso!", f"Código do atleta: {codigo} | Nome do atleta: {nome} | Idade do alteta: {idade} | Telefone do atleta: {telefone_atleta} | Número do documento do atleta: {documento} | Sexo do atleta:  {sexo} .")
    except ValueError:
        #captar um erro, caso os dados informados pelo usuario não sejam condizentes com o input desejado
        print("Valor inválido! Certifique-se de digitar um valor condizente com o input desejado.")
    except Exception as e:
        #capturar qualquer outro erro que possa ecorre em algum momento da aplicação 
        print("Ocorreu um erro ao realizar a ação desejada",str(e))

 
#ALTERAR DADOS
def alterar_dados():
    try:
        # Abrir o arquivo 'Dados.txt' em modo de leitura 'r'
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("Nenhum dado de aluno cadastrado.")
            return

        # Aqui vai solicitar ao usuário o código do atleta que deseja alterar
        codigo_atleta = int(input("Digite o código do atleta que deseja alterar: "))
        encontrado = False

        for i in range(len(linhas)):
            # Dividir a linha em partes separadas por vírgulas e remover os espaços em branco
            dados = linhas[i].strip().split(', ')

            # Verificar se o código do atleta na linha atual corresponde ao código fornecido pelo usuário
            if int(dados[0]) == codigo_atleta:
                novo_codigo_atleta = int(input("Digite o novo código do atleta: "))
                novo_nome = input("Digite o novo nome do atleta: ")
                nova_idade = int(input("Digite a nova idade do atleta: "))
                novo_telefone = int(input("Digite o novo telefone do atleta: "))
                novo_documento = int(input("Digite o novo número de documento: "))
                novo_sexo = input("Digite o novo sexo do atleta: ")

                clientes = f"{novo_codigo_atleta}, {novo_nome}, {nova_idade}, {novo_telefone}, {novo_documento}, {novo_sexo}\n"

                print("Dados do atleta alterados com sucesso!")
                encontrado = True

                novo = f"Novo código do atleta: {novo_codigo_atleta} | Novo nome do atleta: {novo_nome} | Nova idade do atleta: {nova_idade} | Novo telefone do atleta: {novo_telefone} | Novo número de documento do atleta: {novo_documento} | Novo sexo do atleta:  {novo_sexo} "
                print(novo)

                # Substituir a linha no arquivo de dados velhos pelos dados novos
                linhas[i] = clientes

            if not encontrado:
                print("Nenhum atleta encontrado com o código fornecido.")

            # Abrir o arquivo 'Dados.txt' novamente em modo de escrita 'w', para conseguir alterar e substituir os dados velhos pelos novos dados
            with open('Dados.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            #aqui vou começar a definir os meus possíveis erros
    except ValueError:
        print("Valor inválido. Certifique-se de digitar um valor numérico para o código do atleta.")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao alterar os dados:", str(e))


#REALIZAR BACKUP
def realizarBackup():
    novo_dado = input("Digite o nome do arquivo que deseja fazer backup: ")
    try:
        with open(novo_dado, 'r') as arquivo_origem:
            with open(f"Backup_{novo_dado}", 'w') as arquvio_backup:
                conteudo = arquivo_origem.read()
                arquvio_backup.write(conteudo)
        print("Backup do arquvio realizado com sucesso!")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e: 
        print("Ocorreu um erro ao realizar o backup: ", str(e))



#EXCLUIR DADOS 
def excluirDados():
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("Nenhum dado de atleta cadastrado.")
            return
        
        codigo_atleta = int(input("Digite o código do atleta que deseja excluir: "))
        encontrado = False

        with open('Dados.txt', 'w') as arquivo:
            for linha in linhas:
                dados = linha.strip().split(', ')
                if int(dados[0]) == codigo_atleta:
                    encontrado = True #esse encontrado é para, se o dado nao foi encontrado Flase, e se for encontrado true
                    print("Dados do atleta excluído com sucesso!")
                else:
                    arquivo.write(linha)
        if not encontrado:
            print("Nenhum atleta encontrado com código fornecido.")
    except ValueError:
        print("Valor inválido. Certifique-se de digitar um valor número para o código do atleta.")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao excluir os dados:", str(e))

#LISTAR DADOS
def listar_dados():
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            print(linhas)

        if not linhas:
            print("Nenhum dado de atleta cadastrado.")
            return
        
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao executar a função desejada:", str(e))
listar_dados()


#AQUI COMEÇO A PROGRAMAÇÃO DO TKINTER ("front-end")
root = Tk()
root.title('Sistema de Cadastro')
root.geometry('500x420')
root.maxsize(700, 620)
root.minsize(500, 620)
root.configure(bg='#1d1d1d')

# Carrega a imagem do favicon
favicon_image = Image.open("C:\\Users\\gabri\\Desktop\\trabalho-vinijr\\images\\favicon2.png")
favicon_photo = PhotoImage(file="C:\\Users\\gabri\\Desktop\\trabalho-vinijr\images\\favicon2.png")

#Aqui estou definindo o favicon para a janela principal
root.iconphoto(True, favicon_photo)

def margem(altura): #aqui estou criando uma função margem, pois preciso dar varias margens ao longo do desenvolvimento do projeto, então quando se cria uma função, tudo fica mias facil (pois asism, é só executar a função)
    tela = Canvas(root, 
                  width=500, 
                  height=altura, 
                  bg= '#1d1d1d', 
                  bd=0, 
                  highlightthickness=0, 
                  relief='ridge')
    tela.pack()
margem(20)
titulo = Label (root, #aqui estou dando as especificações do texto que aparecerá no front
                bg='#1d1d1d', 
                fg='#800080', 
                font=('Montserrat',18,'bold'),
                text='Sistema Cadastral')
titulo.pack()  #uso essa função de execução, para aparecer a minha variavel no front
margem(30)
texto = Label (root,
               bg='#1d1d1d', 
               fg='#FFFFFF',
               font=('Montserrat',12),
               text= "1 - Cadastrar Dados.\n\n"
                     "2 - Listar Dados.\n\n"
                     "3 - Alterar Dados.\n\n"
                     "4 - Excluir Dados.\n\n"
                     "5 - Realizar backup do arquivo.\n\n")
texto.pack()
margem(10)

def botao(texto, comando, padx): #aquii estao dando a formatação do botão
    botao= Button(root,
                  text= texto,
                  padx=padx,
                  pady= 15,
                  command=comando,
                  fg= '#FFFFFF',
                  activebackground='#FFFFFF',
                  bg='#800080',
                  relief=FLAT,
                  font=('Montserrat', 12, 'bold'))
    botao.pack() #uso essa função de execução, para aparecer a minha variavel no front

#quando clicar no botao iniciar, ele vai para a opção que eu digitei no meu input
def inicia():
    opcao = int(e_txt.get())
    if opcao == 1:
        cadastrarDados()
    elif opcao == 2:
        listar_dados()
    elif opcao == 3:
        alterar_dados()
    elif opcao == 4:
        excluirDados()
    elif opcao == 5:
        realizarBackup()
    else:
        print("Opção inválida.")
    
margem(30)

def resetar():
    e_txt.delete(0, END) #aqui estou falando para ele deletar do inicio ao fim
    os.remove('Dados.txt')#aqui estou falando para ele entrar no sistema operacional e remover o arquivo
    print('Dados e arquivo excluidos com sucesso!')

insere_texto = Label (root, #aqui estou dando as especificações do texto que aparecerá no front
                bg='#1d1d1d', 
                fg='#FFFFFF', 
                font=('Montserrat',15),
                text= ("Insira a Opção Desejada:"))
insere_texto.pack()  #uso essa função de execução, para aparecer a minha variavel no front

margem(30)
e_txt = Entry(root,  #aqui estou dando as especificações da minha entrada de texto, ou seja, do meu input (onde o usuário vai digitar o texto que ele desejar)#FFFFFF#000000'
              width=20, 
              borderwidth=4, 
              relief=FLAT, 
              foreground= '#000000', 
              bg='#FFFFFF', 
              font=('Montserrat', 21, 'bold'),
              justify=CENTER)
e_txt.pack()  #uso essa função de execução, para aparecer a minha variavel no front
margem(30)
botao_iniciar = botao('INICIAR', inicia, 37) #aqui estou criando a variavel do botao, e aqui já coloco as suas especificações
margem(10)
botao_reset = botao('RESETAR', resetar, 28)
margem(10)

root.mainloop()
