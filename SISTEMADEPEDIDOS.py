itens  = ["X-Burguer", "X-Salada", "Fritas", "Refrigerante", "Suco", "Sorvete"]
precos = [18.50,        21.00,      9.00,     6.50,           7.00,   8.00     ]


clientes = []
faturamento = 0
pedidos_itens = []
pedidos_precos = []

while True:
    print()
    print("===== CARDÁPIO =====\n")
    for i, item in enumerate(itens):
        print(f"{i+1}. {item} ........ R$ {precos[i]:.2f}")
        
    nome_cliente = input("\nDigite seu nome: ")
    
    if nome_cliente == "fim":
        break
    else:
        print("Obrigado!")
    
    clientes.append(nome_cliente)
    pedidos_itens = []
    pedidos_precos = []


    while True:
        
        pedido_cliente = int(input("Digite o número do item desejado: "))
        if pedido_cliente == 0:
            break
        pedidos_itens.append(itens[pedido_cliente-1])
        pedidos_precos.append(precos[pedido_cliente-1])
        soma = sum(pedidos_precos)

    for i, item in enumerate(pedidos_itens):
        print(f" - {item} ........ R$ {pedidos_precos[i]:.2f}")

    print(f"TOTAL: R$ {soma:.2f}")
    faturamento += soma

    remover = input("Deseja remover algum item? (Sim/Não)")
    if remover == "sim":
        num = print(input("Digite o número do item: "))
        num - 1

print(f"""
------ RELATÓRIO FINAL ------
      
    Total de clientes: {len(clientes)}
    Nome de todos os clientes: {clientes}
    Item mais caro: {max(pedidos_precos):.2f}
    Item mais barato: {min(pedidos_precos):.2f}
    Faturamento total: {faturamento:.2f}
""")



