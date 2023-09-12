#função de repetição em caso de erro
def receber_valor_numerico(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print('O valor fornecido não é numérico. Por favor, digite um valor válido.')

#Atribuindo valor a algumas variáveis importantes
numero_de_variaveis = 3
valores = []
mensagem = ['Digite a primeira nota do aluno: ',
                'Digite a segunda nota do aluno: ',
                'Digite a terceira e última nota do aluno: ']
#Código principal
while True:
    for i in range(numero_de_variaveis):
        valor = receber_valor_numerico(mensagem[i])
        valores.append(valor)
    #Atribuindo valor à  variáveis para calcular a média
    n1 = valores[0]
    n2 = valores[1]
    n3 = valores[2]
    #O cálculo da média e arredondamento
    m = (n1 + n2 + n3) / 3
    ar = round(m) 
    print('A média arredondada do aluno é: {} ' .format(ar))
    continuar = (input('Deseja calcular outra média? (s/n): '))
    if continuar.lower() != 's':
        break
