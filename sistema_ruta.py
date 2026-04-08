# ============================================================
# Sistema de Rutas Inteligente - TransMilenio (BFS)
# ============================================================

# Base de conocimiento: conexiones entre estaciones
# Nombres normalizados: Title Case, tildes consistentes

estaciones = {
    'Portal Norte': ['Calle 100', 'Toberin'],
    'Toberin':      ['Portal Norte', 'Calle 161'],
    'Calle 161':    ['Toberin', 'Calle 142'],
    'Calle 142':    ['Calle 161', 'Prado'],
    'Prado':        ['Calle 142', 'Calle 127'],
    'Calle 127':    ['Prado', 'Pepe Sierra'],
    'Pepe Sierra':  ['Calle 127', 'Calle 100'],
    'Calle 100':    ['Portal Norte', 'Pepe Sierra', 'Calle 85'],
    'Calle 85':     ['Calle 100', 'Virrey'],
    'Virrey':       ['Calle 85', 'Calle 72'],
    'Calle 72':     ['Virrey', 'Avenida Caracas'],
}


def construir_grafo_bidireccional(estaciones: dict) -> dict:
    """
    Construye un grafo bidireccional sin duplicados
    a partir del diccionario de estaciones.
    """
    grafo = {}

    for estacion, vecinos in estaciones.items():
        if estacion not in grafo:
            grafo[estacion] = []
        for vecino in vecinos:
            # Evitar duplicados al agregar el vecino
            if vecino not in grafo[estacion]:
                grafo[estacion].append(vecino)
            # Agregar la conexión inversa
            if vecino not in grafo:
                grafo[vecino] = []
            if estacion not in grafo[vecino]:
                grafo[vecino].append(estacion)

    return grafo


def encontrar_ruta_inteligente(inicio: str, destino: str, grafo: dict) -> list | None:
    """
    Encuentra la ruta más corta entre dos estaciones usando BFS.
    Retorna la lista de estaciones del camino, o None si no existe ruta.
    """
    if inicio == destino:
        return [inicio]

    cola = [[inicio]]
    visitados = set()

    while cola:
        camino = cola.pop(0)
        estacion_actual = camino[-1]

        if estacion_actual == destino:
            return camino

        if estacion_actual not in visitados:
            visitados.add(estacion_actual)
            for vecino in grafo.get(estacion_actual, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)

    return None


def mostrar_estaciones_disponibles(grafo: dict) -> None:
    """Imprime todas las estaciones disponibles en orden alfabético."""
    print("\nEstaciones disponibles:")
    for nombre in sorted(grafo.keys()):
        print(f"  • {nombre}")


def main():
    print("\n" + "=" * 45)
    print("   Sistema de Rutas Inteligente - BFS")
    print("=" * 45)

    grafo = construir_grafo_bidireccional(estaciones)

    origen  = input("\nIngrese la estación de salida:  ").strip().title()
    destino = input("Ingrese la estación de destino: ").strip().title()

    # Validar que ambas estaciones existen antes de buscar
    errores = []
    if origen not in grafo:
        errores.append(f"  • '{origen}' no está en la base de conocimiento.")
    if destino not in grafo:
        errores.append(f"  • '{destino}' no está en la base de conocimiento.")

    if errores:
        print("\n⚠️  Error:")
        for e in errores:
            print(e)
        mostrar_estaciones_disponibles(grafo)
        print("=" * 45 + "\n")
        return

    # Ejecutar el motor de inferencia (BFS)
    ruta = encontrar_ruta_inteligente(origen, destino, grafo)

    print("\n" + "-" * 45)
    if ruta:
        paradas = len(ruta) - 1
        print(f"✅ ¡Ruta encontrada!")
        print(f"   Paradas:    {paradas}")
        print(f"   Estaciones: {len(ruta)}")
        print("\n   " + " → ".join(ruta))
    else:
        print("❌ No se encontró ruta entre las estaciones indicadas.")

    print("-" * 45 + "\n")


if __name__ == "__main__":
    main()