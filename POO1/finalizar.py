from gerador import pontof, palpt, numCPU, vez

import os
import time

if palpt == numCPU:
    print("\n\033[0;36m  Uuuuhhhhh.... Você acertou o número ",numCPU," e foram ",vez,"vezes.")        
    print("  E a tua Pontuação do Jogo foi: ",pontof,"pontos.")
    if pontof >= 50:
        print("  A tua Pontuação do Jogo foi Muito Excelente!!!!! Parabéns...\033[m\n")
    else:    
        print("  A tua Pontuação do Jogo foi Bom!!!!! Parabéns...\033[m\n")            
else:
    print("\n  Não foi desta vez.... O Número Secreto era",numCPU,".\n")
    print("  E a tua Pontuação do Jogo foi:",pontof,"pontos.\033[m\n")
    if pontof >= 5:
        print("  A tua Pontuação do Jogo foi Razoável...\033[m\n")
    else:    
        print("  A tua Pontuação do Jogo foi muito Baixo...\033[m\n")  
resp = input("\033[0;33m  Deseja Jogar novamente[S/N]?\033[m]").upper()
if resp == 'S':               
    #return comeco()    inicial.py   ## Não consegui voltar no começo... 
    exit()
else:    
    print("\n\033[1;36m         Feito por Sérgio Renato Steglich - SRSistemas\033[m\n") 
    print("\n\033[1;31m   Encerrado, até próxima!!!\033[m\n") 
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')       
    exit()            
    
    
    
