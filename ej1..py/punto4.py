from itertools import permutations

# fuerza bruta como solucionador
def solver(graph, s, dict_of_names):
    # incluir todos los vertices menos el vertice inicio
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
            
    # inicializar el minimo costo como un valor grande
    final_path = []
    min_path = 10000000

    # obtener todas las permitaciones posibles de los nodos
    next_permutation = permutations(vertex)
    
    # recorrer cada permutación posible (camino)
    for i in next_permutation:
        # inicializar el costo del camino actual
        current_pathweight = 0
        
        # calcular el costo total del camino actual
        k = s
        current_path = []
        for j in i:
            # sumar el costo de visitar al vecino 
            current_pathweight += graph[k][j]
            current_path.append('{}-->{}'.format(dict_of_names[k],dict_of_names[j]))
            # actualizar el nodo para visitar el siguiente super heroe
            k = j

        # finalmente añadir el costo de regresar desde el ultimo super heroe al 
        # principio
        current_pathweight += graph[k][s]
        current_path.append('{}-->{}'.format(dict_of_names[k],dict_of_names[s]))

        #print(current_path, current_pathweight)
        # actualizar el valor minismo si se encuentra un camino con menor costo
        # actualizar el correspondiente camino
        if current_pathweight < min_path:
            final_path = current_path
            min_path = current_pathweight

    return min_path, final_path


# crear el diccionario de nombres y vertices
dict_of_names = {
    0:'Iron Man',
    1:'Hulk',
    2:'Khan',
    3:'Thor',
    4:'Captain America',
    5:'Ant-Man',
    6:'Nick Fury - S.H.I.E.L.D.',
    7:'The Winter Soldier'
}

# representación matricial del grafo
graph= [
[0, 675, 400, 166, 809, 720, 399, 233],
[675, 0, 540, 687, 179, 348, 199, 401],
[400, 540, 0, 107, 752, 521, 385, 280],
[166, 687, 107, 0, 111, 540, 990, 361],
[809, 179, 752, 111, 0, 206, 412, 576],
[720, 348, 521, 540, 206, 0, 155, 621],
[399, 199, 385, 990, 412, 155, 0, 100],
[233, 401, 280, 361, 576, 621, 100, 0]]

# numero de vertices en el grafo
V = 8

# vertice de inicio: Nick Fury
s = 6

final_cost, path = solver(graph, s, dict_of_names)
print('El minimo costo posible es: {} para el camino {}'.format(final_cost, path))
