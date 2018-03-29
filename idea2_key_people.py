import networkx as nx
import matplotlib.pyplot as plt

##G = nx.erdos_renyi_graph(10, 0.5)
##nx.write_gml(G, 'random_graph.gml')


def set_all_B(G):
    for each in G.nodes():
        G.node[each]['action'] = 'B'
    return G #we need to return graph in python 3 in order to change the value of graph

def set_A(G, list1):
    for each in list1:
        G.node[each]['action'] = 'A'
    return G

def get_colors(G):
    list1 = []
    for each in G.nodes():
        if G.node[each]['action'] == 'A':
            list1.append('green')
        else:
            list1.append('red')
    return list1

def find_neigh(each, c, G):
    num = 0
    for each1 in G.neighbors(each):
        if G.node[each1]['action'] == c:
            num = num + 1
    return num

def recalculate_options(G):
    dict1 = {}
    a = 9
    b = 5
    for each in G.nodes():
        num_A = find_neigh(each, 'A', G)
        num_B = find_neigh(each, 'B', G)
        payoff_A = num_A*a
        payoff_B = num_B*b
        if payoff_A>=payoff_B:
            dict1[each] = 'A'
        else:
            dict1[each] = 'B'
    return dict1

def reset_node_attributes(G, action_dict):
    for each in action_dict:
        G.node[each]['action'] = action_dict[each]
    return G

def terminate_1(c, G):
    f = 1
    for each in G.nodes():
        if G.node[each]['action']!=c:
            f = 0
            break
    return f

def terminate(G, count):
    flag1 = terminate_1('A', G)
    flag2 = terminate_1('B', G)
    if flag1==1 or flag2==1 or count>=100:
        return 1
    else:
        return 0

G = nx.read_gml('random_graph.gml')
pass_dict = dict()
for i in range(10):
    pass_dict[str(i)] = i
nx.relabel_nodes(G, pass_dict, copy = False)

for u in G.nodes():
    for v in G.nodes():
        if u<v:
            list1 = [u, v]
            print(list1, end = "  ---- ")
            #check for every pair whether it is bunch of key people or not
            G = set_all_B(G)
            G = set_A(G, list1)
            colors = get_colors(G)
            #nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
            #plt.show()

            #keep re assigning actions to nodes
            flag = 0
            count = 0
            while(1):
                flag = terminate(G, count)
                if flag == 1:
                    break
                count += 1
                action_dict = recalculate_options(G)
                G = reset_node_attributes(G, action_dict)
                colors = get_colors(G)

            c = terminate_1('A', G)
            if c==1:
                print('cascade complete')
            else:
                print('cascade incomplete')
            #nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
            #plt.show()
