import sys

# Función que encuentra el indice del vertice
# de mayor peso a partir del conjunto de vertices no visitados
def findMaxVertex(visited, weights):

	# Stores the index of max-weight vertex
	# from set of unvisited vertices
	index = -1;

	# Almacena el indice del vertice de mayor peso
	# a partir del conjunto de vertices no visitados
	maxW = -sys.maxsize;

	# Itera sobre todos los posibles nodos del grafo
	for i in range(V):

		# Si el nodo actual no ha sido visitado
		# y el peso del vertice actual es mayor que el maximo 
		if (visited[i] == False and weights[i] > maxW):
		
			# Actualiza el máximo
			maxW = weights[i];

			# Actualiza el indice
			index = i;
	return index;

def printMaximumSpanningTree(graph, parent):

	# Alamacena el peso total
	# del árbol de expansión máximo 
	# del grafo
	MST = 0;

	# Itera sobre todos los posibles nodos
	# del grafo
	for i in range(1, V):
	
		# Actualiza el MST
		MST += graph[i][parent[i]];

	print("Peso del árbol máximo de expansión: ", MST);
	print();
	print("Arista \tPeso");

	# Muestra las aristas y el peso
	# del árbol de expansión máximo
	for i in range(1, V):
		print(parent[i] , " - " , i , " \t" , graph[i][parent[i]]);

# Función que encuentra el arbol de expansión máximo usando el algoritmo de prim
def maximumSpanningTree(graph):

	# visited[i]:Revisa si el vertice i
	# es visitado o no
	visited = [True]*V;

	# weights[i]: Almacena el máximo peso del
	# grafo que conecta una arista con i
	weights = [0]*V;

	# parent[i]: Almacena el nodo padre del vertice i
	parent = [0]*V;

	# Inicializa los pesos como -infinito,
	# coloca todos los nodos como no visitados
	for i in range(V):
		visited[i] = False;
		weights[i] = -sys.maxsize; # se busca entonces el valor máximo

	# Incluir el primer vertice en el árbol de expansión máxima
	weights[0] = sys.maxsize;
	parent[0] = -1;

	# Buscar para el resto de vertices (V-1) vertices
	# y construir el árbol
	for i in range(V - 1):

		# Almacena el indice del vertice con mayor peso
		# a partir de un conjunto de vertices no visitados
		maxVertexIndex = findMaxVertex(visited, weights);

		# Marca el vertice como visitado
		visited[maxVertexIndex] = True;

		# Actualiza los vertices adjacentes del
		# vertice visitado actual
		for j in range(V):
			# Si hay una arista entre j y 
			# y el vertice actual visitado y 
			# también j es un vertice no visitado
			if (graph[j][maxVertexIndex] != 0 and visited[j] == False):

				# si graph[v][x] es
				# mayor que weight[v]
				if (graph[j][maxVertexIndex] > weights[j]):
				
					# Actualiza weights[j]
					weights[j] = graph[j][maxVertexIndex];

					# Actualiza parent[j]
					parent[j] = maxVertexIndex;

	# Muestra el árbol de expansión máximo
	printMaximumSpanningTree(graph, parent);


# número de vertices
V = 8;

# Punto a:
print('Punto a:')

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

graph = [
    [0, 6, 0, 1, 8, 7, 3, 2],
    [6, 0, 0, 6, 1, 8, 9, 1],
    [0, 0, 0, 1, 2, 1, 5, 0],
    [1, 6, 1, 0, 1, 5, 9, 3],
    [8, 1, 2, 1, 0, 2, 4, 5],
    [7, 8, 1, 5, 2, 0, 1, 6],
    [3, 9, 5, 9, 4, 1, 0, 1],
    [2, 1, 0, 3, 5, 6, 1, 0]];

print('Diccionario de nombres y vertices:', dict_of_names)
print('Grafo', graph)

print('\nPunto b:')
print('Árbol de expansión máximo:')
print(maximumSpanningTree(graph));

print('\nPunto c:')
# determinar el máximo de episodios entre personajes
maxEpisodios = max([max(vertices) for vertices in graph])
print('Número máximo de episodios entre dos personajes: {}'.format(maxEpisodios))

# para determinar cuales personajes tiene 9 episodios juntos
for ind, vertices in enumerate(graph):
    # como es una matriz simetrica solo recorremos la mitad hasta el indice de
    # la diagonal
    for ind2, peso in enumerate(vertices[:ind]):
        if peso == maxEpisodios:
            print('{} y {} comparten {} episodios juntos.'.format(dict_of_names[ind], dict_of_names[ind2], maxEpisodios))
        
print('\nPuntos d y e:')
# para determinar el número de episodios de cada persona en la saga
# sumar los episodios de todos los personas 

for ind, vertices in enumerate(graph):
    if sum(vertices) == 9:
        print('{} aparece en exactamente {} episodios de la saga'.format(dict_of_names[ind], 9))
