##cadasttrar clientes imoveis 2

##cliente
Cadastro= {
    'Cliente': input("Digite o nome do cliente"),
    'Telefone': input("Digite o telefone do cliente"),
    'Email': input("Digite o email do cliente"),
    'Endereço': input("Digite o endereço do cliente")
}
    ##tipo de atendimento
##compra ou venda???'

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

cadastros = []
cadastros.append(Cadastro)

print(cadastros)
