from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="viaje_chile_argentina")

while True:

    origen = input("\nCiudad de origen (Chile) o 's' para salir: ")

    if origen.lower() == "s":
        print("Programa finalizado.")
        break

    destino = input("Ciudad de destino (Argentina): ")

    if destino.lower() == "s":
        print("Programa finalizado.")
        break

    print("\nSeleccione el medio de transporte:")
    print("1. Automóvil")
    print("2. Autobús")
    print("3. Avión")

    opcion = input("Opción: ")

    velocidades = {
        "1": 80,
        "2": 70,
        "3": 800
    }

    medios = {
        "1": "Automóvil",
        "2": "Autobús",
        "3": "Avión"
    }

    if opcion not in velocidades:
        print("Opción inválida.")
        continue

    try:
        ciudad_origen = geolocator.geocode(origen + ", Chile")
        ciudad_destino = geolocator.geocode(destino + ", Argentina")

        if ciudad_origen is None or ciudad_destino is None:
            print("No se pudo encontrar alguna de las ciudades.")
            continue

        distancia = geodesic(
            (ciudad_origen.latitude, ciudad_origen.longitude),
            (ciudad_destino.latitude, ciudad_destino.longitude)
        )

        kilometros = distancia.kilometers
        millas = distancia.miles

        tiempo = kilometros / velocidades[opcion]

        horas = int(tiempo)
        minutos = int((tiempo - horas) * 60)

        print("\n========== RESULTADO ==========")
        print(f"Origen: {origen}")
        print(f"Destino: {destino}")
        print(f"Distancia: {kilometros:.2f} km")
        print(f"Distancia: {millas:.2f} millas")
        print(f"Duración estimada: {horas} horas {minutos} minutos")
        print(f"Medio de transporte: {medios[opcion]}")

        print("\nNarrativa:")
        print(f"El viaje desde {origen} hasta {destino} utilizando {medios[opcion]} tiene una distancia aproximada de {kilometros:.2f} kilómetros ({millas:.2f} millas), con una duración estimada de {horas} horas y {minutos} minutos.")

    except Exception as e:
        print("Error:", e)
