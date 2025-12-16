import random
def main():
  input("Gerar senha? ")
  print(f"Senha gerada: {randomiza()}")
  
def randomiza():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"
    senhafinal = [
      random.choice(maiusculas),
      random.choice(minusculas),
      random.choice(numeros),
      random.choice(especiais)
    ]
    senha = maiusculas + minusculas + numeros + especiais
    senhafinal.extend(random.choices(senha, k=8))
    random.shuffle(senhafinal)
    return ''.join(senhafinal)

main()