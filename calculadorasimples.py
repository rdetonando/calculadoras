#função de recebimento de um valor e repetição em caso de erro
def receber_valor_numerico():
    while True:
        try:
            valor = int(input('digite um número: '))
            return valor
        except ValueError:
            print('Erro: Digite apenas números inteiros')
#funções das operações
def adição(n1, n2):
    return n1 + n2
def subtração(n1, n2):
    return n1 - n2
def multiplicação(n1, n2):
    return n1 * n2
def divisão(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return 'Erro: Divisão por zero'
    

#função que atribui uma função para cada operador e retorna um erro em caso de um valor que não seja int
def operações(operador, n1, n2):
    
    if operador == "+":
        return adição(n1, n2)
    elif operador == "-":
        return subtração(n1, n2)
    elif operador == "/":
        return divisão(n1, n2)
    elif operador == "*":
        return multiplicação(n1, n2)


#código principal com um laço de repetição caso o usuário decida fazer outra operação
while True:
     
        n1 = receber_valor_numerico()
        operador = ''
        while operador not in ('+', '-', '*', '/'):
            print('Erro: operador inválido')
            operador = input("Digite o operador (+, -, *, /): ")
        n2 = receber_valor_numerico()
        resultado = operações(operador, n1, n2)
        print('O resultado da operação é: {:.2f}'.format(resultado))
        continuar = (input('Deseja fazer outra operação? (s/n): '))
        if continuar.lower() != 's':
            break
