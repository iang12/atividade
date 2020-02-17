import networkx as nx
import matplotlib.pyplot as plt

#le arquivo
a = open("READ.md.txt","r")
b = a.readlines()
a.close()

G = nx.Graph()
vertices  = []
count = 0
arestas = []
numero_de_vertices = 0
dicionario_de_vertices = {}
dicionario_de_componentes_conexas = {}
for line in b:
	count += 1
	if count == 1:
		numero_de_vertices = line
		continue
	if count == 2:
		vertices = line.split()
		continue
	elif count >= 4:
		arestas.append(line.strip())
for i in arestas:
	G.add_edges_from([tuple(i.split())])
print('ARESTAS')
print(G.edges())
print('VERTICES')
print(G.nodes())

print('ADJACENCIA de A')
print(list(G.adj['a']))
print('\n')

def componentes_conexas():
	for i in  G.nodes():
		for x in vertices:
			dicionario_de_vertices[i] = 0
			dicionario_de_componentes_conexas[i] = 0
	print('DICIONARIO DE VERTICES')
	print(dicionario_de_vertices)
	print('DICIONARIO DE COMPONENTES')
	print(dicionario_de_vertices)

	
	for i in dicionario_de_vertices:
		if dicionario_de_vertices[i] == 0:
			dicionario_de_componentes_conexas[i] = 1 
			prof(i, dicionario_de_componentes_conexas)
			break

def prof(v,marca):
	comp = 1
	print(v,marca)
	if marca[v] > 0:
		marca[v] = comp
	else:
		marca[v] = comp
	

componentes_conexas()

#plotar o grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
nx.draw_networkx_edges(G, pos,arrows=False)
plt.show()
