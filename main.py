from round_robin.round_robin import RoundRobin
from process.process import Process

schedule = RoundRobin(raw_input("Defina o quantum: "))

opcao = 0
while opcao != 4:
    print "[1] Adicionar novo processo\n[2] Redefinir quantum\n[3] Rodar processos\n[4] Sair\n"

    opcao = int(raw_input())

    if opcao == 1:
        schedule.add_process(Process(raw_input('Quantidade de processos: ')))
    elif opcao == 2:
        schedule.quantum = int(raw_input("Quantum: "))
    elif opcao == 3:
        schedule.run()
