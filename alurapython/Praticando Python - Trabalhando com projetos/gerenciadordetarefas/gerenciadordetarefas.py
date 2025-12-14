def main():
  tarefas = []
  while True:
    try:
      selecao = int(input("\n1. Adicionar tarefa \n2. Visualizar tarefas \n3. Remover tarefa \n4. Sair \nEscolha uma opção: \n"))
      
      if selecao == 1:
        
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
      elif selecao == 2:
        if not tarefas:
          print("Nenhuma tarefa cadastrada")
        else:
           for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
      elif selecao == 3:
        if not tarefas:
          print("Erro: Nenhuma tarefa para remover.")
        else:
          rmtarefa = int(input("Digite o número da tarefa a ser removida: "))
          removida = tarefas.pop(rmtarefa - 1)
          print(f"Tarefa '{removida}' removida!")
      elif selecao == 4: 
          print("Saindo do gerenciador de tarefas. Até mais!")
          break
    except ValueError: 
      print("Erro: Entrada inválida! Digite um número.")
      
main()