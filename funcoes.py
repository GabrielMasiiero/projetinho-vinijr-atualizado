#aqui estou importando o meu tkinter e suas especificações do código em que eu o criei
from main import *

#OPÇÃO QUE O USUARIO PODE SELECIONAR (aqui começa a lógica do projeto)
#EXIBIR MENU
exit = 0

def exibir_menu():
    while True:
        print("1 - Cadastrar Dados.")
        print("2 - Listar Dados.")
        print("3 - Alterar Dados.")
        print("4 - Excluir Dados.")
        print("5 - Realizar backup do arquivo.")
        print("0 - Para encerrar o atendimento.")
        escolha = int(input("Escolha a opção que deseja realizar: "))
        
        if (escolha == 1):
            cadastrarDados()
        elif (escolha == 2):
            listar_dados()
        elif (escolha == 3):
            alterar_dados()
        elif (escolha == 4):
            excluirDados()
        elif (escolha == 5):
            realizarBackup()
        elif (escolha == exit):
            break
        else:
            print("Opção inválida. Digite um número corresponde ao menu.")
            


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

        # Aqui vai solicitar ao usuário o código do aluno que deseja alterar
        codigo_atleta = int(input("Digite o código do aluno que deseja alterar: "))
        encontrado = False

        for i in range(len(linhas)):
            # Dividir a linha em partes separadas por vírgulas e remover os espaços em branco
            dados = linhas[i].strip().split(', ')

            # Verificar se o código do aluno na linha atual corresponde ao código fornecido pelo usuário
            if int(dados[0]) == codigo_atleta:
                novo_codigo_atleta = int(input("Digite o novo código do atleta: "))
                novo_nome = input("Digite o novo nome do atleta: ")
                nova_idade = int(input("Digite a nova idade do atleta: "))
                novo_telefone = int(input("Digite o novo telefone do atleta: "))
                novo_documento = int(input("Digite o novo número de documento: "))
                novo_sexo = input("Digite o novo sexo do atleta: ")

                print("Dados do atleta alterados com sucesso!")
                encontrado = True

                novo = f"Novo código do atleta: {novo_codigo_atleta} | Novo nome do atleta: {novo_nome} | Nova idade do atleta: {nova_idade} | Novo telefone do atleta: {novo_telefone} | Novo número de documento do atleta: {novo_documento} | Novo sexo do atleta:  {novo_sexo} "
                print(novo)

                # Substituir a linha no arquivo de dados velhos pelos dados novos
                linhas[i] = novo

            if not encontrado:
                print("Nenhum atleta encontrado com o código fornecido.")

            # Abrir o arquivo 'Dados.txt' novamente em modo de escrita 'w', para conseguir alterar e substituir os dados velhos pelos novos dados
            with open('Dados.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            #aqui vou começar os meus erros
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
        
        codigo_aluno = int(input("Digite o código do atleta que deseja excluir: "))
        encontrado = False

        with open('Dados.txt', 'w') as arquivo:
            for linha in linhas:
                dados = linha.strip().split(', ')
                if int(dados[0]) == codigo_aluno:
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

#lembrar de fazer a confirmação de exclusao. Se a resposta for sim, excluir, se for diferente disso, nao exclui