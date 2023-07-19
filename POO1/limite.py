from tentativa import ponto, vezes    
        
print("\n  Escolha os limites do Jogo de 1 a 100, o ideal é a diferença até 50 números. ")    
while True:    
    infer = int(input("  Digite o limite inferior: "))
    super = int(input("  Digite o limite superior: "))                          
    quant = super - infer   
    # quando maior quantidade do limites é mais dificil    
    if 2 <= quant <= 9: 
        pontos = ponto + 5   
        break            
    elif 10 <= quant <= 19:
        pontos = ponto + 10                    
        break               
    elif 20 <= quant <= 29:
        pontos = ponto + 20
        break               
    elif 30 <= quant <= 39:
        pontos = ponto + 30            
        break              
    elif 40 <= quant <= 50:
        pontos = ponto + 50            
        break   
    elif 51 <= quant <=100:             
        pontos = ponto + 80            
        break   
    else:       
        print("\033[0;31m  Valor invalido.\033[m") 
        print("\033[0;31m  O limite superior não pode ser menor ou igual que limite inferior....\033[m")                           
        continue
#print(" linha 30 limite - quanto pontos ", pontos)


