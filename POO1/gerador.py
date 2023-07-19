from tentativa import vezes
from limite import pontos, infer, super
import random

print("\033[0;32m    O número foi gerado agora precisa adivinhar o número escolhido de",infer,"até",super,".")
print("    E tem",vezes,"tentativas.\033[m")
numCPU = random.randint(infer,super)
for vez in range(1, vezes + 1):
    print("\033[0;36m   A",vez,"tentativa.\033[m")
    palpt = int(input("   Digite o seu palpite: "))           
    if palpt < numCPU:
        print("        Tente um número\033[0;36m MAIOR!\033[m")
        pontof = pontos - 10
    elif palpt > numCPU:
        print("        Tente um número\033[0;36m MENOR!\033[m")
        pontof = pontos - 10
    else:
        break        
