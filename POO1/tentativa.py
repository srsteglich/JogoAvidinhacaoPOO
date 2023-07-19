import os
import time

nivel = 0  
ponto = 0    
while nivel != 4:       
    print("  Qual o nível de dificuldade de tentativas? ")
    print("  1 - Fácil (20 Tentativas)")
    print("  2 - Médio (10 Tentativas)")
    print("  3 - Difícil (05 Tentativas)")
    print("  4 - Sair do Jogo")
    nivel = input("  Digite um número para nível de dificuldade: ")               
    if nivel.isdigit():
        nivel = int(nivel)        
        if nivel == 1:
            ponto = 5
            vezes = 20                                
            break
        elif nivel == 2:
            ponto = 10
            vezes = 10                                              
            break            
        elif nivel == 3:
            ponto = 30            
            vezes = 5                                
            break
        elif nivel == 4:   
            print("\n\033[0;32m  Saiu...\033[m\n")
            print("\033[1;36m        Feito por Sérgio Renato Steglich - SRSistemas\033[m\n") 
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')                         
            exit()
        else: 
            print("\n\033[1;31m  Opção inválida.... Escolha os números selecionados! \033[m 👀\n")  
            time.sleep(1.0)
            os.system('cls' if os.name == 'nt' else 'clear')                         
        continue
    else:
        print("\n\033[1;31m   Valor informado não é numérico. Favor execute e informe um número selecionado!\033[m 👀")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')  
 

    
