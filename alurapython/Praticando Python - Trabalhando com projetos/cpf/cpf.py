def main():
  cpf=input("Digite seu cpf: ")
  valida(cpf)
def valida(cpf):
    if not len(cpf)==11:
      return print("Erro: O CPF deve ter exatamente 11 dígitos. ")
    if not cpf.isdigit():
      return print("Erro: O CPF deve conter apenas números.  ")
    return print("CPF válido.")
main()