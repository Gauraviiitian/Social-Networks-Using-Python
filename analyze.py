import networkx as nx
import matplotlib.pyplot as plt
import random

def plot_density():
    x = []
    y = []
    for i in range(0, 10):
        G = nx.read_gml('evolution_' + str(i) + '.gml')
        x.append(i)
        y.append(nx.density(G))
    plt.xlabel('Time')
    plt.ylabel('Density')
    plt.title('Change in Density')
    plt.plot(x, y)
    plt.show()

def obesity(G):
    count = 0
    for each in G.nodes():
        if G.node[each]['name'] == 40:
            count = count +1
    return count

def plot_obesity():
    x = []
    y = []
    for i in range(0, 10):
        G = nx.read_gml('evolution_' + str(i) + '.gml')
        x.append(i)
        y.append(obesity(G))
    plt.xlabel('Time')
    plt.ylabel('Obesity')
    plt.title('Change in Obesity')
    plt.plot(x, y)
    plt.show()

plot_density()
plot_obesity()
