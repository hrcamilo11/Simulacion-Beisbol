
import numpy as np
import matplotlib.pyplot as plt


def calcular_momento_inercia():

    masa = float(input("Ingrese la masa de la esfera (kg): "))
    radio = float(input("Ingrese el radio de la esfera (m): "))

    momento_inercia = (2/5) * masa * radio**2

    print("Momento de inercia:", momento_inercia, "kg m²")

    return momento_inercia


def calcular_energia_cinetica():
    print("Energia Cinetica")
    momento_inercia = float(input("Ingrese el momento de inercia de la esfera (kg m²): "))
    velocidad_angular = float(input("Ingrese la velocidad angular de la esfera (rad/s): "))

    energia_cinetica = (1/2) * momento_inercia * velocidad_angular**2

    print("Energía cinética:", energia_cinetica, "J")

    return energia_cinetica


def calcular_energia_potencial_gravitatoria():

    print("Energia Potencial Gracitacional")

    masa = float(input("Ingrese la masa del objeto (kg): "))
    altura = float(input("Ingrese la altura del objeto (m): "))
    gravedad = float(input("Ingrese la aceleración debida a la gravedad (m/s²): "))

    energia_potencial_gravitatoria = masa * gravedad * altura

    print("Energía potencial gravitatoria:", energia_potencial_gravitatoria, "J")

    return energia_potencial_gravitatoria


def calcular_energia_mecanica():

    energia_cinetica = calcular_energia_cinetica()
    energia_potencial = calcular_energia_potencial_gravitatoria()

    energia_mecanica = energia_cinetica + energia_potencial

    print("Energía mecánica total:", energia_mecanica, "J")

    return energia_mecanica


def calcular_velocidad_angular():

    momento_inercia = float(input("Ingrese el momento de inercia del objeto (kg m²): "))
    energia_cinetica = float(input("Ingrese la energía cinética del objeto (J): "))

    if momento_inercia == 0:
        print("Error: El momento de inercia no puede ser 0.")
        return None


    velocidad_angular = np.sqrt(2 * energia_cinetica / momento_inercia)

    print("Velocidad angular:", velocidad_angular, "rad/s")

    return velocidad_angular


def calcular_trayectoria_magnus():
    masa = float(input("Ingrese la masa de la pelota de béisbol (kg): "))
    radio = float(input("Ingrese el radio de la pelota de béisbol (m): "))
    velocidad_inicial = float(input("Ingrese la velocidad inicial de la pelota de béisbol (m/s): "))
    velocidad_angular_inicial = float(input("Ingrese la velocidad angular inicial de la pelota de béisbol (rad/s): "))
    densidad_aire = float(input("Ingrese la densidad del aire (kg/m³): "))
    coeficiente_sustentacion = float(input("Ingrese el coeficiente de sustentación de la pelota de béisbol: "))
    gravedad = 9.80
    tiempo_simulacion = float(input("Ingrese el tiempo total de simulación (s): "))
    pasos_tiempo = int(input("Ingrese el número de pasos de tiempo para la simulación: "))

    # Inicializar vectores de posición y velocidad
    posicion = np.array([0, 0])
    velocidad = np.array([velocidad_inicial, 0])

    # Inicializar listas para almacenar la trayectoria
    trayectoria_x = []
    trayectoria_y = []

    # Calcular el intervalo de tiempo para cada paso
    delta_t = tiempo_simulacion / pasos_tiempo

    for i in range(pasos_tiempo):
        # Calcular fuerza de arrastre
        fuerza_arrastre = (1/2) * densidad_aire * np.dot(velocidad, velocidad) * radio**2 * np.dot(velocidad, velocidad) / np.linalg.norm(velocidad)**2

        # Calcular fuerza de Magnus
        fuerza_magnus = (1/2) * densidad_aire * velocidad_inicial**2 * radio**2 * coeficiente_sustentacion * np.cross(velocidad, np.array([0, 0, 1]))

        # Calcular fuerza neta
        fuerza_neta = fuerza_arrastre - fuerza_magnus - masa * gravedad * np.array([0, 1, 0])


        # Actualizar aceleración
        aceleracion = fuerza_neta / masa

        # Actualizar velocidad
        velocidad += aceleracion * delta_t

        # Actualizar posición
        posicion += velocidad * delta_t

        # Almacenar la posición en la trayectoria
        trayectoria_x.append(posicion[0])
        trayectoria_y.append(posicion[1])

    # Graficar la trayectoria
    plt.plot(trayectoria_x, trayectoria_y, 'o')
    plt.xlabel('Posición X (m)')
    plt.ylabel('Posición Y (m)')
    plt.title('Trayectoria de la Pelota de Béisbol con Fuerza de Magnus')
    plt.show()

    return trayectoria_x, trayectoria_y


def verificar_conservacion_momento_angular():
    momento_inercia_inicial = float(input("Ingrese el momento de inercia inicial del sistema (kg m²): "))
    velocidad_angular_inicial = float(input("Ingrese la velocidad angular inicial del sistema (rad/s): "))
    momento_inercia_final = float(input("Ingrese el momento de inercia final del sistema (kg m²): "))
    velocidad_angular_final = float(input("Ingrese la velocidad angular final del sistema (rad/s): "))

    momento_angular_inicial = momento_inercia_inicial * velocidad_angular_inicial
    momento_angular_final = momento_inercia_final * velocidad_angular_final

    conservacion_momento_angular = momento_angular_inicial == momento_angular_final

    if conservacion_momento_angular:
        print("Se conserva el momento angular.")
    else:
        print("No se conserva el momento angular.")

    return conservacion_momento_angular



def main():
    """
    Menú principal del programa.
    """

    while True:
        print("\nMenú principal:")
        print("1. Calcular momento de inercia")
        print("2. Calcular energía cinética")
        print("3. Calcular energía potencial gravitatoria")
        print("4. Calcular energía mecánica")
        print("5. Calcular velocidad angular")
        print("6. Calcular trayectoria con fuerza de Magnus")
        print("7. Verificar conservación del momento angular")
        print("8. Salir")

        opcion = int(input("Ingrese la opción deseada (1-8): "))

        if opcion == 1:
            calcular_momento_inercia()
        elif opcion == 2:
            calcular_energia_cinetica()
        elif opcion == 3:
            calcular_energia_potencial_gravitatoria()
        elif opcion == 4:
            calcular_energia_mecanica()
        elif opcion == 5:
            calcular_velocidad_angular()
        elif opcion == 6:
            calcular_trayectoria_magnus()
        elif opcion == 7:
            verificar_conservacion_momento_angular()
        elif opcion == 8:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

