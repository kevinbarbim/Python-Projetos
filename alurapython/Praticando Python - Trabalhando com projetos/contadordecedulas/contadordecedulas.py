def main():
  saque = int(input("Digite o valor do saque: "))
  (calcula(saque))
def calcula(saque):
  cedulas = [100,50,20,10,5,2]
  try:
    if saque % 2 != 0:
      return print("Digite um numero par")
    elif saque<0:
      return print("Digite um valor positivo")
    else:
      print("Cedulas: ")
    for cedula in cedulas:
      quantidade = saque // cedula
      if quantidade>0:
        print(f"{quantidade} de R$ {cedula}")
      saque = saque % cedula
    
    
  except ValueError:
    print("Erro")  
    
main()