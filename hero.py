import time

Name = ""
print("Bem vind, aventureiro. Essa é a sua jornada, a sua história.")
while True:
    try:
        Name = input("Qual é o seu nome? ")
        if Name.strip() != "":
            break
    except ValueError:
        print("Nome inválido.")

while True:
    try:
        XP = int(input("Qual o seu XP? "))
        break
    except ValueError:
        print("Xp inválido")

if XP < 1000:
    lvl = "ferro"
if 1001 <= XP <= 2000:
    lvl = "bronze"
if 2001 <= XP <= 5000:
    lvl = "prata"
if 6001 <= XP <= 7000:
    lvl = "ouro"
if 7001 <= XP <= 8000:
    lvl = "platina"
if 8001 <= XP <= 9000:
    lvl = "ascendente"
if 9001 <= XP <= 10000:
    lvl = "imortal"
if 10001 <= XP:
    lvl = "radiante"

print(f"O Herói de nome {Name} está no nível de {lvl}")

