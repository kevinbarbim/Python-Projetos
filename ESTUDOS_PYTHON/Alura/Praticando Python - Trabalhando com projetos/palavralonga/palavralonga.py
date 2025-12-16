def main():
  texto = input("Digite um texto: ")
  longa(texto)

def longa(texto):
  palavras = texto.split()
  palavraslongas=[]
  for palavra in palavras:
    if len(palavra)>10:
      palavraslongas.append(palavra)
  if palavraslongas:
    print("Palavras longas encontradas: ")
    for palavra in palavraslongas:
      print(palavra)
  else:
    print("Nenhuma palavra longa foi encontrada no texto.")

main()