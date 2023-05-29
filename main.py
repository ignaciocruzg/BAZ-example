from collections import defaultdict


def cuenta_ocurrencias(diccionario):
    # Mi solucion
    frecuencia = {}
    for i in diccionario.values():
        frecuencia[i] = frecuencia.get(i, 0) + 1

    return frecuencia


def contar_rocky_sparky(diccionario):
    # Mi solucion
    contador_rocky = 0
    contador_sparky = 0

    for elemento in diccionario.values():
        if elemento == 'Rocky':
            contador_rocky += 1
        elif elemento == 'Sparky':
            contador_sparky += 1

    return "Rocky: " + str(contador_rocky), "Sparky: " + str(contador_sparky)


def imprime_nombres_perros(diccionario):
    # Mi solucion
    lista = []
    for elemento in diccionario.values():
        lista.append(elemento)

    return lista


if __name__ == '__main__':
    dogs = {
        'perro1': 'Sparky',
        'perro2': 'Hunter',
        'perro3': 'Loki',
        'perro4': 'Astro',
        'perro5': 'Sparky',
        'perro6': 'Rocky',
        'perro7': 'Rocky',
        'perro8': 'Toby',
        'perro9': 'Chelsea',
        'perro10': 'Maple',
        'perro11': 'Maya',
        'perro12': 'Loki',
        'perro13': 'Sparky',
        'perro14': 'Toby',
        'perro15': 'Sparky',
        'perro16': 'Dexter',
        'perro17': 'Fido',
        'perro18': 'Sparky'
    }

    # print(cuenta_ocurrencias(dogs))
    # print(contar_rocky_sparky(dogs))
    # print(imprime_nombres_perros(dogs))

    # Solucion del instructor
    dogs1 = ['Sparky', 'Hunter', 'Loki', 'Astro', 'Sparky', 'Rocky', 'Rocky', 'Toby', 'Chelsea', 'Maple', 'Maya', 'Loki', 'Sparky', 'Toby', 'Sparky', 'Dexter', 'Fido', 'Sparky']
    dog_dic = defaultdict(int)
    for dog in dogs1:
        dog_dic[dog] += 1

    print('Rocky: ', dog_dic['Rocky'])
    print('Sparky: ', dog_dic['Sparky'])
    print(list(dog_dic.keys()))

# Comment
# Comment 2