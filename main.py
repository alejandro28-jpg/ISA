import os
import sys
import time
 
# ====== PERSONALIZA AQUÍ ======
PARA = "Mi amor"
DE = "Tu nombre"
FECHA = "03 de noviembre de 2026"
MOMENTO = "el día que nos conocimos"  # un recuerdo especial
CARTA = [
    f"Hoy se cumple nuestro primer mes juntos y no puedo dejar de sonreír.",
    f"Desde {MOMENTO}, mis días tienen otro color.",
    "Gracias por tu paciencia, tus risas y por hacerme sentir tan yo.",
    "Un mes se siente corto, pero ya me enseñaste que lo bonito está en los detalles.",
    "Quiero seguir creando recuerdos contigo, un mes tras otro.",
]
# ==============================
 
os.system("")  # habilita colores ANSI en Windows
ROSA, ROJO, DORADO, RESET, NEGRITA = "\033[95m", "\033[91m", "\033[93m", "\033[0m", "\033[1m"
 
 
def escribir(texto, color="", velocidad=0.04, fin="\n"):
    """Efecto máquina de escribir."""
    sys.stdout.write(color)
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    sys.stdout.write(RESET + fin)
 
 
def corazon():
    forma = [
        "  ***   ***  ",
        " ***** ***** ",
        "*************",
        " *********** ",
        "   *******   ",
        "     ***     ",
        "      *      ",
    ]
    for linea in forma:
        print(ROJO + linea.center(50) + RESET)
        time.sleep(0.15)
 
 
def main():
    os.system("cls" if os.name == "nt" else "clear")
    corazon()
    print()
    escribir("♥ 1 MES JUNTOS ♥".center(50), NEGRITA + DORADO, 0.06)
    print(DORADO + FECHA.center(50) + RESET + "\n")
    time.sleep(0.8)
 
    escribir(f"Querido(a) {PARA},", NEGRITA + ROSA, 0.05)
    print()
    for parrafo in CARTA:
        escribir("  " + parrafo, ROSA, 0.035)
        time.sleep(0.6)
 
    print()
    escribir("Con todo mi cariño,", ROSA, 0.05)
    escribir(f"{DE} ♥", NEGRITA + ROJO, 0.07)
    print()
    escribir("Te quiero muchísimo. Feliz primer mes. ♥".center(50), DORADO, 0.04)
 
 
if __name__ == "__main__":
    main()
