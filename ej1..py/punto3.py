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

print('Puntos a y b:')
# puntos a y b:
graph_twitter = [
    [0, 75, 40, 16, 80, 20, 99, 23],
    [75, 0, 50, 67, 79, 38, 99, 41],
    [40, 50, 0, 17, 75, 52, 85, 28],
    [16, 67, 17, 0, 11, 50, 90, 36],
    [80, 79, 75, 11, 0, 26, 12, 56],
    [20, 38, 52, 50, 26, 0, 55, 61],
    [99, 99, 85, 90, 12, 55, 0, 10],
    [23, 41, 28, 36, 56, 61, 10, 0]];

print('Grafo twitter:', graph_twitter)

graph_instagram = [
    [0, 61, 44, 66, 56, 74, 11, 65],
    [12, 0, 47, 41, 12, 38, 99, 41],
    [41, 23, 0, 45, 12, 89, 42, 14],
    [12, 69, 11, 0, 12, 50, 78, 63],
    [89, 19, 72, 11, 0, 26, 12, 56],
    [72, 34, 21, 65, 12, 0, 78, 41],
    [12, 87, 35, 99, 42, 15, 0, 10],
    [33, 41, 24, 61, 45, 41, 11, 0]];

print('\nGrafo Instagram:', graph_instagram)

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

# Punto c: Algoritmo prim para el arbol de expansión máximo
print('\nPunto c:')
print('Twitter')
# ejecutar algoritmo
print(maximumSpanningTree(graph_twitter));

print('\nInstagram')
# ejecutar algoritmo
print(maximumSpanningTree(graph_instagram));	

# Punto d: 
print('\nPunto d:')
print('Capitana Marvel no se encuentra representada en el grafo')

# Punto e:
print('\nPunto e')
# The winter soldier es el último heroe
# Iron man el primero
if graph_twitter[-1][0]!= 0 and graph_twitter[0][-1]!=0:
	print('Si es posible conectar a Iron man con The winter soldier por twitter, son amigos!!')
 
if graph_instagram[-1][0]!= 0 and graph_instagram[0][-1]!=0:
	print('Si es posible conectar a Iron man con The winter soldier por Instagram, son amigos!!')

# Punto f:
print('\nPunto f')
# Thor es el vertice 3
for ind, vecino in enumerate(graph_instagram[3]):
	if vecino != 0:
		print('Thor sigue a {}'.format(dict_of_names[ind]))
