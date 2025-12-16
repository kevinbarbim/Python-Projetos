import random
def main():
  escolha = input("Escolha: pedra, papel ou tesoura? ").lower()
  batalha(escolha)
  
def batalha(escolha):
  possibilidades = ["pedra", "papel", "tesoura"]
  opcoes = random.choice(possibilidades)
  if escolha not in possibilidades:
    return print("Escolha errada!")
  if escolha == opcoes:
    return print("Empate!")
  elif ((escolha == 'pedra' and opcoes == 'tesoura') or (escolha == 'papel' and opcoes == 'pedra') or (escolha == 'tesoura' and opcoes == 'papel')):
    return print("Voce venceu!")
  else:
    return print("Voce perdeu!")
  
main()