import networkx as nx
import matplotlib.pyplot as plt


def set_all_B(G):
    for each in list(G.nodes()):
        G.node[each]['action'] = 'B'

def set_A(G, list1):
    for each in list1:
        G.node[each]['action'] = 'A'

def get_colors(G):
    list1 = []
    for each in list(G.nodes()):
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
    a = 4
    b = 3
    for each in G.nodes():
        num_A = find_neigh(each, 'A', G)
        num_B = find_neigh(each, 'B', G)
        payoff_A = num_A*a
        payoff_B = num_B*b
        if payoff_A>payoff_B:
            dict1[each] = 'A'
        else:
            dict1[each] = 'B'
    return dict1

def reset_node_attributes(G, action_dict):
    for each in action_dict:
        G.node[each]['action'] = action_dict[each]

G = nx.read_gml('random_graph.gml')
pass_dict = dict()
for i in range(10):
    pass_dict[str(i)] = i
nx.relabel_nodes(G, pass_dict, copy = False)
set_all_B(G)
list1 = [3, 7]
set_A(G, list1)
colors = get_colors(G)
nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
plt.show()
action_dict = recalculate_options(G)
reset_node_attributes(G, action_dict)
colors = get_colors(G)
nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
plt.show()


flag = 0
count = 0
while(1):
    flag = terminate(G, count)
    if flag == 1:
        break
    count += 1
    action_dict = recalculate_options(G)
    reset_node_attributes(G, action_dict)
    colors = get_colors(G)
    nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
