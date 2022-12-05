while (True):
    horai = int(input("Digite a hora de início do jogo:"))
    minutoi = int(input("Digite o minuto de início do jogo:"))
    horaf = int(input("Digite a hora de encerramento do jogo"))
    minutof = int (input("Digite o minuto de encerramento do jogo"))
    
  
    if((horai >= 0) and (minutoi >= 1) and (horaf <= 24) and (minutof <= 60) and (horai <= horaf) and (minutoi <= minutof)) :
        break
    print("Horário inválido")

print(f"O jogo durou {horaf - horai} hora(s) e {minutof - minutoi} minuto(s)")
    



