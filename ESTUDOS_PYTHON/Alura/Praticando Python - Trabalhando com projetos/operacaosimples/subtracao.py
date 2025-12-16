def sub(a,b):
  return a-b
def main():
  try:
    num1 = float(input("Digite o numero 1: "))
    num2 = float(input("Digite o numero 2: "))
    resultado = sub(num1,num2)
    return print(f'Resultado: {resultado}')
  except ValueError:
    print("Erro, digite um valor válido!")
main()