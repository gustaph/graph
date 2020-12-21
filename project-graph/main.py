import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
   def __init__(self, tipo, tamanhoV):
      self.tipo = tipo
      self.tamanhoV = tamanhoV
      self.matriz = np.zeros([tamanhoV, tamanhoV], dtype = int)

   def addAresta(self, vX,  vY):
      self.matriz[vX][vY] = 1
      if self.tipo == "ND":
         self.matriz[vY][vX] = 1

   def aux_getKey(self, valorV):
      vertice = [vertice for (vertice, valor) in codigoVertices.items() if valor == valorV]
      return vertice
   
   def matrizAdj(self):
      for elemento in self.matriz:
         print(elemento)
         
   def saoAdj(self, vX, vY):
      if self.tipo == 'ND':
         if ((self.matriz[vX][vY] == 1) and (self.matriz[vY][vX] == 1)):
            print('Adjacentes!')
         else:
            print('Não adjacentes!')
      else:
         if (self.matriz[vX][vY] == 1):
            print('Adjacentes!')
         else:
            print('Não adjacentes!')

   def getGrau(self, vertice):
      grauEntrada, grauSaida = 0,0
      for i in self.matriz[:, vertice]: #coluna (vertices que apontam para ele)
         grauEntrada += i
      for i in self.matriz[vertice, :]: #linha (vertices para os quais ele aponta)
         grauSaida += i

      if self.tipo == "ND":
         print(f'Grau: {grauEntrada}')
      else:
         print(f'Grau de entrada: {grauEntrada}\nGrau de saída: {grauSaida}')
               
   def getVizinhos(self, vertice):
      vizinhos = []
      for vert in range(self.tamanhoV):
         if self.matriz[vertice][vert] == 1:
            vizinhos.append(self.aux_getKey(vert))
      return vizinhos

   def visitarArestas(self):
      print('Arestas visitadas: ')
      for i in range(self.tamanhoV):
         for j in range(self.tamanhoV):
            if self.matriz[i][j] == 1:
               print(self.aux_getKey(i), self.aux_getKey(j), sep='-')

   def visualizarGrafo(self):
      if self.tipo == "ND":
         graph = nx.Graph()
      else:
         graph = nx.DiGraph()

      graph.add_nodes_from(tuple([vertice for vertice in vertices if vertice != '']))
      graph.add_edges_from(tuple([aresta for aresta in arestas if aresta[0] != '' and aresta[1] != '']))

      options = {
         "with_labels": True,
         "node_color": "#ffb912",
         "font_size": 8,
         "font_weight": "bold",
         "linewidths": 0.5,
         "width": 0.4,
      }

      nx.draw(graph, **options)
      plt.show()

if __name__ == '__main__':

   nomeArq = input('Insira o nome do arquivo(sem a extensão): ')

   # ler dados do arquivo
   arq = open("data/" + nomeArq + ".txt", "r")
   tipo = arq.readline().strip()

   vertices = []
   arestas = []
   for linha in arq:
      pos = linha.find(",")
      v1 = str(linha[:pos].strip())
      v2 = str(linha[pos+1:].strip())
      if v1 not in vertices:
         vertices.append(v1)
      if v2 not in vertices:
         vertices.append(v2)
      arestas.append([v1,v2])
   
   arq.close()
 
   g = Grafo(tipo, len(vertices))
   codigoVertices = {vertice: valor for valor, vertice in enumerate(vertices)}
   for vX, vY in arestas:
      g.addAresta(codigoVertices[vX], codigoVertices[vY])
   
while True:
      opc = int(input('''
                     [Menu]\n
         (1) - Matriz de Adjacência;
         (2) - Verificar se são adjacentes;
         (3) - Calcular grau;
         (4) - Buscar vizinhos;
         (5) - Visitar todas as arestas;
         (6) - Visualizar grafo;
         (7) - [Extra] Mostrar vértices;
         (8) - [Extra] Mostrar arestas;
         (9) - Sair.\n
         Escolha: '''))
      print()

      if opc == 1:
         g.matrizAdj()
         
      elif opc == 2:
         v1, v2 = input('Vertices[vertice1, vertice2]: ').split(',')
         if v1 in vertices and v2 in vertices:
            g.saoAdj(codigoVertices[v1.strip()], codigoVertices[v2.strip()])
         else:
            print('Insira vértices válidos')
         
      elif opc == 3:
         vertice = input('Indique o vértice: ')
         if vertice in vertices:
            g.getGrau(codigoVertices[vertice])
         else:
            print('Insira vértices válidos')
            
      elif opc == 4:
         vertice = input('Indique o vértice: ')
         if vertice in vertices:
            print('Vizinhos:')
            print(g.getVizinhos(codigoVertices[vertice]))
         else:
            print('Insira vértices válidos')
      
      elif opc == 5:
         g.visitarArestas()

      elif opc == 6:
         g.visualizarGrafo()
         
      elif opc == 7:
         print(vertices)

      elif opc == 8:
         print(arestas)

      elif opc == 9:
         print("Xau!")
         exit()
      else:
         print("Opção inválida")
