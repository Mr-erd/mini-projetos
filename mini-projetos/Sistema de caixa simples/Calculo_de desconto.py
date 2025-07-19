import time

def exibir_menu_cupons():
    """Função que exibe os cupons disponíveis."""
    print("""
    \n============ Cupons Aplicáveis ===================
    - DESCONTO10 (para compras de R$ 51 a R$ 100)
    - DESCONTO20 (para compras acima de R$ 100)
    - SEM_DESCONTO (para qualquer compra)
==================================================\n
    """)

def simular_pagamento():
    """Simula uma barra de carregamento e exibe mensagem de sucesso."""
    print("\nProcessando pagamento...")
    for _ in range(30):
        print('█', end='', flush=True)
        time.sleep(0.05)
    print("\nPagamento realizado com sucesso!")

print(20*"=", " Bem-vindo ao Sistema de Caixa ", "="*20)

while True:
    exibir_menu_cupons()
    
    try:
        valor_original = float(input("Digite o valor original da peça: R$ "))
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido.")
        continue

    cupom_digitado = input("Digite seu cupom: ").upper().strip()

    percentual_desconto = 0.0

    if 51 <= valor_original <= 100 and cupom_digitado == "DESCONTO10":
        percentual_desconto = 0.10 
        print("✔️ Cupom 'DESCONTO10' aplicado!")
    elif valor_original > 100 and cupom_digitado == "DESCONTO20":
        percentual_desconto = 0.20 
        print("✔️ Cupom 'DESCONTO20' aplicado!")
    elif cupom_digitado == "SEM_DESCONTO":
        percentual_desconto = 0.0
        print("✔️ Nenhuma promoção aplicada.")
    else:
        print("❌ Cupom inválido para esta faixa de preço. Nenhum desconto aplicado.")

    
    valor_do_desconto = valor_original * percentual_desconto
    preco_final = valor_original - valor_do_desconto

    print(f"\nResumo da Compra:")
    print(f"Preço Original....: R$ {valor_original:.2f}")
    print(f"Desconto..........: R$ {valor_do_desconto:.2f}")
    print(f"Preço Final a Pagar: R$ {preco_final:.2f}")

    simular_pagamento()


    escolha = input("\nDeseja realizar outra operação? (S/N): ").upper().strip()
    if escolha != 'S':
        print("\nObrigado, volte sempre!")
        time.sleep(1)
        break
    else:
        print("\n" + 60*"=")