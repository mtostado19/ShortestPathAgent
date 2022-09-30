
def StartAgent(map, origen, dest):
    inf = 999999
    # Declarar valores utilizados para la memoria
    data = {
      'A': { 'costo': inf , 'camino': [], 'nombre': 'Oradea'},
      'B': { 'costo': inf , 'camino': [], 'nombre': 'Zerind'},
      'C': { 'costo': inf , 'camino': [], 'nombre': 'Arad'},
      'D': { 'costo': inf , 'camino': [], 'nombre': 'Timisoara'},
      'E': { 'costo': inf , 'camino': [], 'nombre': 'Lugoj'},
      'F':  { 'costo': inf , 'camino': [], 'nombre': 'Mehadia'},
      'G': { 'costo': inf , 'camino': [], 'nombre': 'Drobeta'},
      'H': { 'costo': inf , 'camino': [], 'nombre': 'Sibiu'},
      'I': { 'costo': inf , 'camino': [], 'nombre': 'Fagaras'},
      'J': { 'costo': inf , 'camino': [], 'nombre': 'Rimnicu Vilcea'},
      'K': { 'costo': inf , 'camino': [], 'nombre': 'Pitesti'},
      'L': { 'costo': inf , 'camino': [], 'nombre': 'Craiova'},
      'M': { 'costo': inf , 'camino': [], 'nombre': 'Bucharest'},
      'N': { 'costo': inf, 'camino': [], 'nombre': 'Urziceni'},
      'O': { 'costo': inf, 'camino': [], 'nombre': 'Giurgiu'},
      'P': { 'costo': inf, 'camino': [], 'nombre': 'Hirsova'},
      'Q': { 'costo': inf, 'camino': [], 'nombre': 'Eforie'},
      'R': { 'costo': inf, 'camino': [], 'nombre': 'Vaslui'},
      'S': { 'costo': inf, 'camino': [], 'nombre': 'Iasi'},
      'T': { 'costo': inf, 'camino': [], 'nombre': 'Neamt'},
    }
    data[origen]['costo'] = 0
    visited = []
    ayuda = origen
    filas = []
    finish=0

    #Inicio del ciclo hasta encontrar analizar todos los caminos posibles.
    while finish==0:
      if ayuda not in visited:
        visited.append(ayuda)
        filas = AnalyseCurrentState(ayuda, data, filas, visited, map)

      #Al terminar de evaluar la casilla por completo, sacarlo de la fila.
      for x in visited:
          cont2=0
          for m in filas:
            if m[1]==x:
              filas.pop(cont2)
            cont2=cont2+1

      #Evaluar si se agotaron todas las opciones, terminar o seguir el programa
      if len(filas) == 0:
        finish=1
      else:
        filas = ChooseHappiestPath(filas)
        #Moverse al siguiente espacio
        ayuda = filas[0][1]
        
    #Imprimir decision final
    print("camino:", data[dest]['camino'] + list(dest))
    caminoName = []
    for c in data[dest]['camino']:
      for d in data.keys():
        if c == d:
          caminoName.append(data[d]['nombre'])
    caminoName.append(data[dest]['nombre'])
    print("camino", caminoName)
    print("costo fue de:", data[dest]['costo'])


#Funcion para leer el estado actual en donde se encuentra el agente
def AnalyseCurrentState(posActual, data, filas, visited, map):
  #Analisis de la casilla actual
  for j in map[posActual]:
    if j not in visited:
      cost = data[posActual]['costo'] + map[posActual][j]
      #El agente decide la mejor opcion y actualiza su memoria.
      if cost < data[j]['costo']:
        data[j]['costo'] = cost
        data[j]['camino'] = data[posActual]['camino'] + list(posActual)
        if len(filas)==0:
          filas.append(tuple((data[j]['costo'], j)))
        else:
          cont=0
          for f in filas:
            if f[1]==j:
              filas.pop(cont)
            cont = cont+1
          filas.append(tuple((data[j]['costo'], j)))

  return filas

#El agente organiza los valores obtenidos en base a lo considero el mejor
def ChooseHappiestPath(filas):
  filasLength= len(filas)
  for k in range(filasLength-1):
    for i in range(filasLength-k-1):
      if filas[i][0] > filas[i+1][0]:
        filas[i], filas[i+1] = filas[i+1], filas[i]
  return filas

map = {
  'A' : { 'B': 71, 'H': 151 }, #Oradea
  'B' : { 'A': 71, 'C': 75 }, # Zerind
  'C' : { 'B': 75, 'H': 140, 'D': 118 }, #Arad
  'D' : { 'C': 118, 'E': 111 }, #Timisoara
  'E': {'D': 111, 'F': 70}, #Lugoj
  'F': {'E': 70, 'G': 75}, #Mehadia
  'G': {'F': 75, 'L': 120}, #Drobeta
  'H': { 'I': 99, 'J': 80, 'A': 151, 'C': 140}, #Sibiu
  'I': { 'H': 99, 'M': 211}, #Fagaras
  'J': {'H': 80, 'K': 97, 'L': 146}, #Rimnicu Vilcea
  'K': {'J': 97, 'L': 138, 'M': 101}, #Pitesti
  'L': {'J': 146, 'K': 138, 'G': 120}, #Craiova
  'M': {'I': 211, 'K': 101, 'N': 85, 'O':90}, #Bucharest
  'N': {'M': 85, 'P':98, 'R':142}, #Urziceni
  'O': {'M': 90}, #Giurgiu
  'P': {'N':98, 'Q':86}, #Hirsova
  'Q': {'P':86}, #Eforie
  'R': {'N':142, 'S':92}, #Vaslui
  'S': {'R':92, 'T':87}, #Iasi
  'T': {'S':87}, #Neamt
}

inicio = 'H'
goal = 'E'
StartAgent(map, inicio, goal)