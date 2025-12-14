def main():
  texto = input("Digite um texto: ")
  resultado = vogal(texto)
  print(f"O texto contém {resultado} vogais.")
def limpartexto(texto):
  letras = "qwrtypsdfghjklzxcvbnm "
  for char in letras:
    texto = texto.replace(char ,"")
  return texto
def vogal(frase):
  frase = limpartexto(frase.lower())
  return len(frase)
main()