while (True):
    horai = int(input("Digite a hora de início do jogo:"))
    minutoi = int(input("Digite o minuto de início do jogo:"))
    horaf = int(input("Digite a hora de encerramento do jogo"))
    minutof = int (input("Digite o minuto de encerramento do jogo"))
    horat = 0
    
    if (horaf < horai):
        horat = ((24 - horai) + horaf)

  
    if( (((horai >= 0) and (horai <= 24)) and ((horaf >= 0) and (horaf <= 24))) and (((minutoi >= 0) and (minutoi < 60)) and ((minutof >= 0) and (minutof < 60))) and (horat <= 24)) :

        if (horaf < horai):
            horat
            minutot = (minutof - minutoi)
            break
        elif ((horaf == horai) and (minutof == minutoi)):
            horat = horai
            minutot = minutoi
            break
        elif(horai < horaf):
            horat = (horaf - horai)
            minutot = (minutof - minutoi)
            break
        
    
    print("Horário inválido")


print(f"O jogo durou {horat} hora(s) e {abs(minutot)} minuto(s)")
    
