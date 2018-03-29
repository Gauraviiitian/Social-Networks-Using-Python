import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

#add n number of nodes in a graph and return it
def add_nodes(n):
	G = nx.Graph()
	G.add_nodes_from(range(n))
	return G

#add one random edge
def add_random_edge(G):
        v1 = random.choice(list(G.nodes()))
        v2 = random.choice(list(G.nodes()))
        if (v1!=v2):
                G.add_edge(v1, v2)
        return G

#keep adding random edges till it becomes connected
def add_till_connectivity(G):
        while(nx.is_connected(G)==False):
                G = add_random_edge(G)
        return G

#creates an instance of entire process. takes number of nodes as a input and return number of edges required to make the graph connected
def create_instance(n):
        g = add_nodes(n)
        g = add_till_connectivity(g)
        return nx.number_of_edges(g)

#average instance hundred times
def create_avg_instance(n):
        sum = 0
        for i in range(100):
                sum = sum + create_instance(n)
        return sum/100

#plot desired graph for different number of edges
def plot_connectivity():
        i = 10
        x = []
        y = []
        while i<= 200:
                x.append(i)
                y.append(create_avg_instance(i))
                i = i+10
        x = np.array(x)
        y = np.array(y)
        plt.plot(x, y, "r", x, x*numpy.log(x), "b")
        plt.title("Emergence of Connectivity")
        plt.xlabel("Number of Nodes")
        plt.ylabel("Number of edges required to make the graph connected")
        plt.show()
        
