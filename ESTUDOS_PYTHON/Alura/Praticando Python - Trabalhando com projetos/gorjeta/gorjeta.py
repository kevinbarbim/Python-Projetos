def main():
  conta = float(input("Digite sua conta: "))
  gorjeta = float(input("Digite a % de gorjeta: "))
  resultado = calculo(conta,gorjeta)
  print(f"Resultado: {resultado}")  
def calculo(conta,gorjeta):
  num = conta + conta*(gorjeta/100)
  return num
main()