from datetime import datetime
from time import sleep


print("-=" * 19)
print("            Hora de comer")
print("-=" * 19)


def tratamento_hora():
    global atual, hora_atual, min # Tirando as vars do escopo local, mandando pro global
    atual = str(datetime.now().time()) # Transformando o datetime em string
    hora_atual = atual[0] + atual[1] # Pegando os valores de hora
    min = atual[3] + atual[4] # Pegando os valores de min
    hora_atual = int(hora_atual) # Transformando str em int
    min = int(min) # Transformando str em int



def contador(hora, minuto):
    tratamento_hora()
    horaComer = hora_atual + hora # Definindo a hora de comer
    minComer = min + minuto # Definindo o min de comer
    if minComer > 59: # O minuto nao passar de 60
        minComer -= 60
        horaComer += 1
    if horaComer >= 24: # A hora nao passar de 24
        horaComer -= 24
    print(f"O alarme esta setado para {horaComer}:{minComer}")
    while True:
        tratamento_hora()
        if horaComer == hora_atual and minComer == min: # Alarme
            print("Está na hora")
            break
        sleep(1)
    confirmacao()



def confirmacao():
        confComeu = str(input("Comeu? [S/N] ")).upper()[0]
        if confComeu in 'SN':
            confRepeat = str(input("Quer reiniciar o ciclo? [S/N] ")).upper()[0]
            if confRepeat == 'S':
                print("Reiniciando ciclo")
                contador(h, m) # Reiniciando a funcao com as mesmas vars passadas pelo usuario no começo
            else:
                print("Obrigado! ")  


 
h = int(input("Horas: "))
m = int(input("Minutos: "))
contador(h, m)
