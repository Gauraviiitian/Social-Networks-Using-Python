import networkx as nx
import matplotlib.pyplot as plt
import random

def display_graph(G, i, ne):
	pos = nx.circular_layout(G)
	if i=='' and ne=='':
		new_node = []
		rest_nodes = G.nodes()
		new_edges = []
		rest_edges = G.edges()
	elif i=='':
		new_node = []
		rest_nodes = G.nodes()
		new_edges = ne
		rest_edges = list(set(G.edges()) - set(new_edges) - set([(b,a) for (a,b) in new_edges]))
	nx.draw_networkx_nodes(G, pos, nodelist = new_node, node_color = 'g')
	nx.draw_networkx_nodes(G, pos, nodelist = rest_nodes, node_color = 'r')
	nx.draw_networkx_edges(G, pos, edgelist = new_edges, node_color = 'g', style = 'dashdot')
	nx.draw_networkx_edges(G, pos, edgelist = rest_edges, node_color = 'r')
	plt.show()

def erdos_renyi(G, p):
	for i in G.nodes():
		for j in G.nodes():
			if i!=j:
				r = random.random()
				if r<=p:
					G.add_edge(i, j)
					ne = [(i, j)]
					#display_graph(G, '', ne)

def plot_deg_dist(G):
	all_degrees = []
	for i in nx.degree(G):
		all_degrees.append(i[1])
	unique_degrees = list(set(all_degrees))
	unique_degrees.sort()
	count_of_degrees = []

	for i in unique_degrees:
		c = all_degrees.count(i)
		count_of_degrees.append(c)

	print unique_degrees
	print count_of_degrees

	plt.plot(unique_degrees, count_of_degrees, 'ro-')
	plt.xlabel('Degrees')
	plt.ylabel('Number of Nodes')
	plt.title('Degree Distribution')
	plt.show()


def main():
	n = input('Enter the value of n: ')
	p = input('Enter the value of p: ')
	G = nx.Graph()
	G.add_nodes_from([i for i in range(n)])

	display_graph(G, '', '')
	erdos_renyi(G, p)
	plot_deg_dist(G)

main()