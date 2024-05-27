#1 10/04 imoport lib os (operational system)
import os


#restaurantes=['Bife Sujo', 'Saco de Feijão']
#inserir dicionario-em outras linguagens chave valor
restaurantes=[{'nome':'Bife-sujo','categoria':'prato-feito','ativo': True},
              {'nome':'Saco do feijão','categoria':'feijoada','ativo': False},
               {'nome':'Doces da Bernadete','categoria':'doceria','ativo': True},] 

def mostrar_subtitulo(texto):
    '''
    Essa função é responável por exibir o nome da ação que o usuário solicitou 
    '''
    os.system('clear')
    linha='*'*(len(texto))
    print(linha)
    print (texto)
    print(linha)
    print()

#2 declarando a função finalizar_app
def finalizar_app():
    '''
    Essa função é responsável por finalizar o programa 

    outputs:
    - adciona um título quando finaliza o programa 
    '''
    
    mostrar_subtitulo('Finalizando app')

def chamar_nome_do_app():
    '''
    Essa função é responsável por exibir o nome do programa
    '''
    print ('''
    
    𝑹𝒆𝒔𝒕𝒂𝒖𝒓𝒂𝒏𝒕𝒆 𝑬𝒙𝒑𝒓𝒆𝒔𝒔𝒐 𝑴𝒂𝒋𝒖
    
    ''')

def voltar_ao_menu_principal():
     input('\nDigite uma tecla para voltar ao menu principal')
     main()

# 12 criando opção_invalida
def opcao_invalida():
    '''
    Essa função é reponsável por exibir que a opção que o usuário digitou é inválida

    outputs:
    -pede para que o usuário digite uma tecla para voltar ao menu principal
    '''
    print ('opção invalida\n')
    #input('Digite uma tecla para voltar ao menu principal:')
    #main()
    voltar_ao_menu_principal()
    
def exibir_opcoes():
    '''
    Essa função é responsável por exibir as opções disponíveis para o seu restaurante
    '''
    print ("1 Cadastrar Restaurante")
    print ("2 Listar Restaurante")
    print ("3 Ativar Restaurente")
    print ("4 Sair\n")


def cadatrar_novo_restaurante():
    #docstring
    '''
    Essa função é responsável por cadastrar um novo restaurante

    inputs:
    -nome do restaurante
    -categoria do restaurante

    outputs:
    -adciona um novo restaurante ao dicionário 
    '''
    os.system('clear')
    nome_do_restaurante= input('digite o nome do novo restaurante:')
    categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante={'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Essa função é responsável por listar os restaurantes disponíveis

    outputs:
    -lista os restaurantes incluindo o restaurante que o usuário cadastrou
    '''
    mostrar_subtitulo('Listando os restaurantes')
    print(f'-Nome do Restaurante'.ljust(24),'-Categoria'.ljust(20),'-Ativo')
    for restaurante in restaurantes:
       nome_restaurante=restaurante['nome']
       categoria=restaurante['categoria']
       ativo='Ativo'if restaurante ['ativo'] else 'Desativado'
       print(f'-{nome_restaurante.ljust(20)} | -{categoria.ljust(20)} | -{ativo}')
    #chamar a duas funções e saída
    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    '''
    Essa função é responsável por alterar o status do restaurante (True ou False)

    input:
    -nome do restaurante 

    output:
    -altera o estado do restaurante 
    '''
    mostrar_subtitulo('Alternando o estado do restaurante')
    nome_restaurante=input('Digite o nome do restaurante que desejas alternar o estado: ')
    restaurante_encontrado=False

    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'Restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')        
    voltar_ao_menu_principal()


#8 declarando a função opcao_digitada1
def escolher_opcao():
    '''
    Essa função é responsável por exibir e requisitar ao usuário que escolha uma das opções

    input:
    - opção escolhida 

    output:
    - redireciona para a função que foi escolhida
    '''
    
    try:
        opcao_digitada = (int(input("Escolha uma opção")))
        print ("Você selecionou:",opcao_digitada, "\n")
        if(opcao_digitada==1):
            print("Você escolheu Cadastrar Restaurante\n")
            cadatrar_novo_restaurante()
            finalizar_app()
        elif(opcao_digitada==2):
           # print("Você escolheu Listar Restaurante\n") 
           listar_restaurantes()
           finalizar_app()
        elif(opcao_digitada==3):
            #mostrar_subtitulo("Voce escolheu Ativar Restaurante")
            alterar_estado_restaurante()
            finalizar_app()
        elif(opcao_digitada==4):
            # print('Voce escolheu sair do programa') 
             finalizar_app()
        #3 chamando a função finalizar_app 
        else:
            opcao_invalida()
    except:
        opcao_invalida()         
  
  #5 escrever a funçaõ main
def main():
    '''
    Essa função é responsável por servir como  ponto de partida para a execução do programa

    outputs:
    -exibe o nome do app
    -exibe as opções disponíveis 
    -pede ao usuária que escolha uma opção 
    '''
    #10 clear
    os.system('clear')
    #6 chamar o nome do app
    chamar_nome_do_app()
    #7 chamar a escolha de opções
    exibir_opcoes()
    #9 chamar a opção digitada
    escolher_opcao()

#4 criando a entrada através da variável main
if(__name__=='__main__'):
    main()
