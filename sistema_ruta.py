# paso A : Definir las conexiones (nuestra base de conociento)
# Que estaciones estan juntas 
estaciones = {
    'Portal Norte': ['calle 100', 'Toberin'], 
    'Toberin': ['Portal Norte', 'Calle 161'],
    'Calle 161': ['Toberín', 'Calle 142'],
    'Calle 142': ['Calle 161', 'Prado'],
    'Prado': ['Calle 142', 'Calle 127'],
    'Calle 127': ['Prado', 'Pepe Sierra'],
    'Pepe Sierra': ['Calle 127', 'Calle 100'],
    'Calle 100': ['Portal Norte', 'Pepe Sierra', 'Calle 85'],
    'Calle 85': ['Calle 100', 'Virrey'],
    'Virrey': ['Calle 85', 'Calle 72'],
    'Calle 72': ['Virrey', 'Avenida Caracas']
}
def encontrar_ruta_inteligente(inicio, destino, grafo):
    # La cola guarda el camino 
    cola = [[inicio]]
    visitados = set() # No vamos a dar vueltas en círculo

    while cola:
        # Sacamos el primer camino de la lista
        camino = cola.pop(0)
        # Obtenemos la última estación de ese camino
        estacion_actual = camino[-1]

        # ¿Llegamos al destino?
        if estacion_actual == destino:
            return camino

        # Si no la hemos visitado, exploramos sus vecinos
        if estacion_actual not in visitados:
            for vecino in grafo.get(estacion_actual, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
            
            visitados.add(estacion_actual)

    return None