"""
Created on Sat Apr 15 13:14:15 2023

@author: olive
"""
import networkx as nx
import matplotlib.pyplot as plt
import random

# Generar pesos aleatorios para las aristas
weights = [random.randint(1, 100) for i in range(26)]

# Crear el grafo original
grafo = nx.Graph()
grafo.add_edge("A", "B", weight=weights[0])
grafo.add_edge("A", "C", weight=weights[1])
grafo.add_edge("B", "C", weight=weights[2])
grafo.add_edge("B", "D", weight=weights[3])
grafo.add_edge("B", "E", weight=weights[4])
grafo.add_edge("C", "E", weight=weights[5])
grafo.add_edge("C", "F", weight=weights[6])
grafo.add_edge("D", "E", weight=weights[7])
grafo.add_edge("E", "F", weight=weights[8])
grafo.add_edge("E", "G", weight=weights[9])
grafo.add_edge("F", "G", weight=weights[10])
grafo.add_edge("F", "H", weight=weights[11])
grafo.add_edge("G", "H", weight=weights[12])
grafo.add_edge("G", "I", weight=weights[13])
grafo.add_edge("H", "I", weight=weights[14])
grafo.add_edge("H", "J", weight=weights[15])
grafo.add_edge("I", "J", weight=weights[16])
grafo.add_edge("F", "I", weight=weights[17])
grafo.add_edge("G", "H", weight=weights[18])
grafo.add_edge("G", "I", weight=weights[19])
grafo.add_edge("G", "J", weight=weights[20])
grafo.add_edge("H", "I", weight=weights[21])
grafo.add_edge("H", "J", weight=weights[22])
grafo.add_edge("H", "A", weight=weights[23])
grafo.add_edge("I", "J", weight=weights[24])
grafo.add_edge("I", "A", weight=weights[25])

# Obtener el árbol de expansión mínima mediante Kruskal
arbol_expansion = nx.minimum_spanning_tree(grafo)

# Obtener las posiciones de los nodos para graficar
pos = nx.spring_layout(grafo)

# Obtener las etiquetas de las aristas con sus pesos
labels = nx.get_edge_attributes(grafo, 'weight')
labels_arbol = nx.get_edge_attributes(arbol_expansion, 'weight')

# Graficar el grafo original con las aristas etiquetadas con sus pesos
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
nx.draw(grafo, pos, with_labels=True, node_color='skyblue')
plt.show()

# Graficar el árbol de expansión mínima con las aristas etiquetadas con sus pesos
nx.draw_networkx_edge_labels(arbol_expansion, pos, edge_labels=labels_arbol)
nx.draw(arbol_expansion, pos, with_labels=True, node_color='violet')
plt.show()
