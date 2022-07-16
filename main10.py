from concurrent.futures import BrokenExecutor
from webbrowser import BackgroundBrowser


print("BEM VINDO A ILHA DO TESOURO!!")
nome= input("Qual seu nome marujo? ").upper()
aventura= input(f"Olá,{nome}!\nTem um tesouro escondido nessa ilha e precisamos de pessoas corajosas para encontra-lo. \nVocê gostaria de embarcar nessa aventura?\nSim ou Não? \n").lower()
if aventura == "sim":
    partida= input("Que legal! Então boa sorte!\nVocê acabou de desembarcar na praia.\nVocê pode ir beirando a praia ou entrar na floresta?\nPraia ou floresta? \n").lower()
    if partida == "floresta":
        rio= input("Você adentrou na mata.\njá caminhou mais de uma hora e encontrou um rio. O que fazer?\nContornar ou nadar? \n").lower()
        if rio == "contornar":
            cachoeira= input(f"{nome}, você agora chegou ao pé de uma cachoeira. O que você decide fazer?\nEscalar ou contornar?  \n").lower()
            if cachoeira == "escalar":
                baú= input("Você chegou ao topo da cachoeira e encontrou um baú. Será o tesouro?\nEle está trancado com um cadeado numérico.\nTem espaço para colocar apenas um número de 0 a 9.\nQual número você escolhe? \n").lower()
                if baú == "7":
                    print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
                    print(f"Uhuuu {nome}, Você encontrou o tesouro perdido!\nParabéns!!")
                else: print("Oh não o número estava incorreto e o báu esplodiu :( \nGAME OVER")
            else: print("Você demorou muito para dar a volta e acabou anoitecendo e as feras selvagens acabaram te devorando.\nGAME OVER!")
        else: print(f"{nome} o rio estava cheio de piranhas e você foi devorado.\nGAME OVER!")    
    else: x= input("Uma tribo nativa te encontrou na praia e você foi capturado.\nGAME OVER!")
else: print("Tudo bem! Não será dessa vez que esse tesouro será encontrado.\nDexemos então para uma proxima!")




