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
