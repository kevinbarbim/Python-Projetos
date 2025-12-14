def main():
  try:
    n1 = float(input("Digite o primeiro número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    n2 = float(input("Digite o segundo número: "))
    
    if operacao=='+':
      resultado = n1+n2
    elif operacao=='-':
      resultado = n1-n2
    elif operacao=='*':
      resultado = n1*n2
    elif operacao=='/':
      resultado = n1/n2
    else:
      print("Opção inválida")
  except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
  except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
main()