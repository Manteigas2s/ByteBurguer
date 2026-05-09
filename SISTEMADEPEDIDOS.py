itens  = ["X-Burguer", "X-Salada", "Fritas", "Refrigerante", "Suco", "Sorvete"]
precos = [18.50,        21.00,      9.00,     6.50,           7.00,   8.00     ]


clientes = []
faturamento = 0
pedidos_itens = []
pedidos_precos = []

while True:
    print("===== CARDÁPIO =====")
    for i, item in enumerate(itens):
        print(f"{i+1}. {item} ........ R$ {precos[i]:.2f}")
        
    nome_cliente = input("Digite seu nome: ")
    if nome_cliente == "fim":
        break
    else:
        print("Obrigado!")

    while True:
        pedido_cliente = int(input("Digite o número do item desejado: "))
        if pedido_cliente == 0:
            break
        pedidos_itens.append(itens[pedido_cliente-1])
        pedidos_precos.append(precos[pedido_cliente-1])


        

            
    