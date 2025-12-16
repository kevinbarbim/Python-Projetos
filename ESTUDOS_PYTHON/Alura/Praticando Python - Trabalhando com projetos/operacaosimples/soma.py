def soma(a,b):
  return a+b
def main():
  try:
    numero1 = float(input('Digite o numero 1: '))
    numero2 = float(input('Digite o numero 2: '))
    resultado = soma(numero1,numero2)
    return print(f"Resultado: {resultado}")
  except ValueError:
    print("Erro: Digite um número válido!")
main()