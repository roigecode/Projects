
# Dieta automática usando Python:

print( """
________  .__        __           ___________             .__.__   
\______ \ |__| _____/  |______    \_   _____/____    ____ |__|  |  
 |    |  \|  |/ __ \   __\__  \    |    __) \__  \ _/ ___\|  |  |  
 |    `   \  \  ___/|  |  / __ \_  |     \   / __ \\\  \___|  |  |__
/_______  /__|\___  >__| (____  /  \___  /  (____  /\___  >__|____/
        \/        \/          \/       \/        \/     \/         
""")

print("··· Para poder empezar digita los siguientes datos: ···")
sexo = input("¿Eres hombre [H] o mujer [M]? ")
peso = int(input("¿Cuánto pesas [kg]? "))
altura = float(input ("¿Cuánto mides [cm]? "))
edad = int(input("¿Cuántos años tienes? "))

if sexo == "H":
    tmb = (10*peso)+(6.25*altura)-(5*edad)+5
    print("TMB [H] = ", tmb)
elif sexo == "M":
    tmb = (10*peso)+(6.25*altura)-(5*edad)-161
    print("· TMB [M] = ", tmb)
else:
    print("No has introducido la letra correspondiente a tu sexo [H/M]")
    
print("___________________________________\n")

print("¿Cuánto ejercicio haces a la semana?")
print("""
        0.- Poco o ninguno        (0 días por semana)
        1.- Ejercicio ligero      (1-3 días por semana)
        2.- Ejercicio Moderado    (3-5 días por semana)
        3.- Ejercicio Fuerte      (6 días por semana)
        4.- Ejercicio Profesional
""")

ejercicio = int(input("-> Num: "))

switcher = {
    0: 1.2 ,
    1: 1.375 ,
    2: 1.55 ,
    3: 1.725 ,
    4: 1.9 
}

kcal = round(tmb*switcher.get(ejercicio),2)

print("\n\t¡Deberás consumir ",kcal," kcal diarias!\n")

print("1.- Desayuno: ",round(kcal*0.2,1)," kcal")
print("2.- Almuerzo: ",round(kcal*0.1,1)," kcal")
print("3.- Comida:   ",round(kcal*0.3,1)," kcal")
print("4.- Merienda: ",round(kcal*0.1,1)," kcal")
print("5.- Cena:     ",round(kcal*0.3,1)," kcal")
