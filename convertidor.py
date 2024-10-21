# convertidor.py

from masa import *
from temperatura import *
from tiempo import *

def convertir_temperatura():
    celsius = float(input("Ingrese el valor en Celsius: "))
    print(f"{celsius}°C a Fahrenheit: {celsius_a_fahrenheit(celsius)}°F")
    print(f"{celsius}°C a Kelvin: {celsius_a_kelvin(celsius)}K")

def convertir_masa():
    kilogramos = float(input("Ingrese el valor en Kilogramos: "))
    print(f"{kilogramos} kg a Libras: {kilogramos_a_libras(kilogramos)} lbs")
    print(f"{kilogramos} kg a Onzas: {kilogramos_a_onzas(kilogramos)} oz")

def convertir_tiempo():
    segundos = float(input("Ingrese el valor en Segundos: "))
    print(f"{segundos} s a Minutos: {segundos_a_minutos(segundos)} min")
    print(f"{segundos} s a Horas: {segundos_a_horas(segundos)} h")

def main():
    while True:
        categoria = input("Seleccione una categoría (temperatura, masa, tiempo) o 'salir' para terminar: ").strip().lower()
        if categoria == 'temperatura':
            convertir_temperatura()
        elif categoria == 'masa':
            convertir_masa()
        elif categoria == 'tiempo':
            convertir_tiempo()
        elif categoria == 'salir':
            break
        else:
            print("Categoría no válida. Intente de nuevo.")

if _name_ == "_main_":
    main()