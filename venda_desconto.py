print("="*37 + "\nBem vindo a loja do Gabriel Schinoff!\n" + "="*37) #meu identificador
while True: #um teste para caso o input seja algo além de um numero
    try:
        valor = float(input("Entre o valor do produto: "))
        quant = int(input("Entre a quantidade do produto: "))
        break
    except ValueError:
        print("Por favor, digite um número válido.") #oq irá aparecer caso de um erro

resul = valor * quant #a formula para saber o valor

if quant >= 10 and quant < 100: #caso esteja dentro deste padrão terá 5% de desconto
    desc5 = resul * 0.05
    resulN = resul - desc5
    print(f"O valor sem o desconto é: R$ {resul:.2f}")
    print(f"O valor com o desconto é: R$ {resulN:.2f} (desconto 5%)")
elif quant >= 100 and quant < 1000: #caso esteja dentro deste padrão terá 10% de desconto
    desc10 = resul * 0.1
    resulN = resul - desc10
    print(f"O valor sem o desconto é: R$ {resul:.2f}")
    print(f"O valor com o desconto é: R$ {resulN:.2f} (desconto 10%)")
elif quant >= 1000: #caso esteja dentro deste padrão terá 15% de desconto
    desc15 = resul * 0.15
    resulN = resul - desc15
    print(f"O valor sem o desconto é: R$ {resul:.2f}")
    print(f"O valor com o desconto é: R$ {resulN:.2f} (desconto 15%)")
else:  #e por ultimo caso não esteja em nennhum dos padrões não terá desconto
    print(f"O valor da sua compra é: R${resul:.2f}")
    print("Infelizmente não temos desconto para está quantidade de produtos!")
