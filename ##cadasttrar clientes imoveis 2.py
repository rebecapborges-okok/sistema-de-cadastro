##cadasttrar clientes imoveis 2
def cadastrar_cliente():
##cliente
    Cadastro= {
        'Cliente': input("Digite o nome do cliente"),
        'Telefone': input("Digite o telefone do cliente"),
        'Email': input("Digite o email do cliente"),
        'Endereço': input("Digite o endereço do cliente")
    }
    
    ##tipo de atendimento
##compra ou venda???

    tipo_atendimento = input("Compra ou venda?").lower()
    
    if tipo_atendimento in ["compra", "comprar"]:
        print("Cliente deseja comprar")
    ##imovel para comprar
        compra = {
            "Tipo": input("Casa, Terreno ou fazenda?"),
            'Valor': input("Valor que o cliente quer comprar"),
            'Tamanho' : input("Que tamanho precisa ter? Insira o valor em m²"),
            'Peças': input("Quantas peças precisam ter a casa?"),
            'Localizacao': input("Qual a localização desejada do imóvel?")
        }
        Cadastro["Imovel"]= compra
        print(Cadastro)

    elif tipo_atendimento in ["vender","venda"]:
        print("Cliente deseja vender")
        venda= {
            "Tipo": input("Casa, Terreno ou fazenda?"),
            'Valor': input("Valor que o cliente quer vender"),
            'Negociavel': input("O cliente aceita fazer negócio?"),
            'Tamanho': input("Insira o valor em m²"),
            'Peças': input("Quantas peças há na casa?"),
            'Localizacao': input("Qual a localização do imóvel?")
    }
        Cadastro["Imovel"]= venda
        print(Cadastro)

    else:
        print("Digite uma resposta válida") 
    return Cadastro

cadastros = []
## Cadastrar novo cliente
cadastros.append(cadastrar_cliente())

novo_cadastro = input("Deseja cadastrar outro cliente?").lower()

while novo_cadastro in ["sim", "s"]:
    cadastros.append(cadastrar_cliente())
    novo_cadastro = input("Deseja cadastrar outro cliente?").lower()

if novo_cadastro in["nao", "n", "não", "ñ"]:
    print("Cadastro concluído")
##listar clientes
for cliente in cadastros:
        print(cliente)

##BUSCAR cliente 
nome_busca = input("Digite o nome do cliente: ").lower()
encontrado = False

for cliente in cadastros:
    if cliente["Cliente"].lower() == nome_busca:
        print(cliente)
        encontrado =True
        
if encontrado == False:
    print("Cliente não encontrado")
        
def editar():
    nome_busca = input("Qual cliente deseja editar?").lower()
    
    encontrado = False

    for cliente in cadastros:
        if cliente["Cliente"].lower() == nome_busca:
            encontrado = True
            print("1 - Nome")
            print("2 - Telefone")
            print("3 - Email")
            print("4 - Endereço")
        
            opcao = input("O que deseja editar?")
            
            if opcao == "1":
                cliente["Cliente"] = input("Digite o novo nome: ")
            elif opcao == "2":
                cliente["Telefone"] = input("Digite o novo número: ")
            elif opcao == "3":
                cliente["Email"] = input("Digite um novo email: ")
            elif opcao == "4":
                cliente["Endereço"]= input("Digite o novo endereço: ")
            else:
                print("Para editar escolha entre 1, 2, 3 ou 4")
    if encontrado == False:
        print("Cliente não encontrado")
                
editar()
for cliente in cadastros:
    print(cliente)
    
def Excluir():
    nome_busca = input("Qual cliente deseja excluir?").lower()
    
    encontrado = False
    
    
    for cliente in cadastros:
        if cliente["Cliente"].lower() == nome_busca:
            encontrado = True
            
            confirma = input("Tem certeza?").lower()
            
            if confirma in ["s", "sim"]:
                cadastros.remove(cliente)
                print("Cliente removido")
            else:
                print("Operação cancelada")
            
    if encontrado == False:
        print("Cliente não encontrado")
    
Excluir()
for cliente in cadastros:
    print(cliente)
