import networkx as nx

def edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G)
    list_of_tuples = list(dict1.items())
    list_of_tuples.sort(key = lambda x:x[1], reverse = True)
    return list_of_tuples[0][0] # in form (a, b)

def girvan(G):
    c = list(nx.connected_component_subgraphs(G))
    l = len(c)
    print("The number of connected components are ", l)

    while(l==1):
        G.remove_edge(*edge_to_remove(G)) #((a,b)) to (a,b)
        c = list(nx.connected_component_subgraphs(G))
        l = len(c)
        print("The number of connected components are ", l)
    
    return c

G = nx.karate_club_graph()
c = girvan(G)
for i in c:
    print(i.nodes())
    print("--------")
