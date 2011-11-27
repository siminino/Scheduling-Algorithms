from round_robin.round_robin import RoundRobin
from sjf.sjf import Sjf
from process.process import Process

schedule_algo = int(raw_input('Escolha o algoritmo de escaloamento a ser usado:\n[1] Round Robin\n[2] SJF\n'))

if schedule_algo == 1:
    schedule = RoundRobin(raw_input("Defina o quantum: "))

    opcao = 0
    while opcao != 4:
        print "[1] Adicionar novo processo\n[2] Redefinir quantum\n[3] Rodar processos\n[4] Sair\n"

        opcao = int(raw_input())

        if opcao == 1:
            schedule.add_process(Process(raw_input('Tamanho do processo: ')))
        elif opcao == 2:
            schedule.quantum = int(raw_input("Quantum: "))
        elif opcao == 3:
            schedule.run()

elif schedule_algo == 2:
    opcao = 0
    schedule = Sjf()
    while opcao != 4:
        print "[1] Adicionar novo processo\n[2] Rodar processos\n[4] Sair\n"

        opcao = int(raw_input())

        if opcao == 1:
            process = Process(raw_input('Tamanho do processo: '))
            schedule.add_process(process)
        elif opcao == 2:
            schedule.run()

