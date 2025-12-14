import random
def main():
  
  respostarobo = random.randint(1,100)
  while True:
    try:
      resposta = int(input("Tente adivinhar o número (1-100): "))
      if not 1<=resposta<=100:
        print("Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.")
      if respostarobo>resposta: 
        print(f"Muito baixo! Tente novamente: {resposta}   ")
      elif respostarobo<resposta: 
        print(f"Muito alto! Tente novamente: {resposta}   ")
      else:
        print(f"Parabéns! Você acertou o número {resposta}.   ")
        break
    except ValueError as e:
      print(f"Entrada inválida: {e}")
  

main()