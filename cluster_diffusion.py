# Proving the first claim
import networkx as nx
import matplotlib.pyplot as plt
import random

def set_all_B(G):
    for each in G.nodes():
        G.node[each]['action'] = 'B'
    return G

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
    a = 3
    b = 2
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


##nx.draw_circular(G, with_labels = True)
##plt.show()

list2 = [[0,1],[0,1,2,3,4,5,6,12]]
#Now we will see that for any list in list2 idea will not diffuse inside cluster given cluster density >(1-q)

for list1 in list2:
    G = nx.Graph()
    G.add_nodes_from([i for i in range(13)])
    G.add_edges_from([(0, 1), (0, 6), (1, 6), (1, 8), (1, 12), (1, 2), (2, 9), (2, 12), (3, 12), (3, 9), (3, 4), (4, 12), (4, 5), (5, 10),(5,6),(6,8),(7,8),(7,9),(7,11),(8,9),(8,10),(8,11),(9,10),(9,11),(10,11)])

    G = set_all_B(G)
    print(list1)
    G = set_A(G, list1)
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
        G = reset_node_attributes(G, action_dict)
        colors = get_colors(G)

    c = terminate_1('A', G)
    if c==1:
        print('cascade complete')
    else:
        print('cascade incomplete')
    nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
    plt.show()
