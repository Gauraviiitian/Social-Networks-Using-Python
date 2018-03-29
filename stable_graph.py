import random 
import matplotlib.pyplot as plt
import networkx as nx
import itertools

def get_signs_of_tris(tris_list, G):
        all_signs = []
        for i in range(len(tris_list)):
                temp = []
                temp.append(G[tris_list[i][0]][tris_list[i][1]]['sign'])
                temp.append(G[tris_list[i][1]][tris_list[i][2]]['sign'])
                temp.append(G[tris_list[i][2]][tris_list[i][0]]['sign'])
                all_signs.append(temp)
        return all_signs

def count_unstable(all_signs):
        stable = 0
        unstable = 0
        for i in range(len(all_signs)):
                if all_signs[i].count('+') ==3 or all_signs[i].count('+') == 1:
                        stable += 1
                else:
                        unstable += 1
        print('stabel = ', stable)
        print('unstable = ', unstable)
        return unstable

def move_a_tri_to_stable(G, tris_list, all_signs):
        found_unstable = False
        while(found_unstable == False):
                index = random.randint(0, len(tris_list)-1)
                if all_signs[index].count('+') == 2 or all_signs[index].count('+') == 0:
                        found_unstable = True

        #move unstable triangle to stable state
        r = random.randint(1, 3) #choose an edge to invert
        if all_signs[index].count('+') ==2:
                if r==1:
                        if G[tris_list[index][0]][tris_list[index][1]]['sign'] == '+':
                                G[tris_list[index][0]][tris_list[index][1]]['sign'] = '-'
                        else:
                                G[tris_list[index][0]][tris_list[index][1]]['sign'] = '+'
                elif r==2:
                        if G[tris_list[index][1]][tris_list[index][2]]['sign'] == '+':
                                G[tris_list[index][1]][tris_list[index][2]]['sign'] = '-'
                        else:
                                G[tris_list[index][1]][tris_list[index][2]]['sign'] = '+'
                else:
                        if G[tris_list[index][0]][tris_list[index][2]]['sign'] == '+':
                                G[tris_list[index][0]][tris_list[index][2]]['sign'] = '-'
                        else:
                                G[tris_list[index][0]][tris_list[index][2]]['sign'] = '+'
        elif all_signs[index].count('+') == 0:
                if r==1:
                        G[tris_list[index][0]][tris_list[index][1]]['sign'] = '+'
                elif r==2:
                        G[tris_list[index][1]][tris_list[index][2]]['sign'] = '+'
                else:
                        G[tris_list[index][0]][tris_list[index][2]]['sign'] = '+'
        return G

def see_coalitions(G):
        first_coalition = []
        second_coalition = []

        nodes = list(G.nodes())
        r = random.choice(nodes)

        first_coalition.append(r)

        processed_nodes = []
        to_be_processed = [r]

        for each in to_be_processed:
                if each not in processed_nodes:
                        neigh = list(G.neighbors(each))

                        for i in range(len(neigh)):
                                if G[each][neigh[i]]['sign'] == '+':
                                        if neigh[i] not in first_coalition:
                                                first_coalition.append(neigh[i])
                                        if neigh[i] not in to_be_processed:
                                                to_be_processed.append(neigh[i])
                                elif G[each][neigh[i]]['sign'] == '-':
                                        if neigh[i] not in second_coalition:
                                                second_coalition.append(neigh[i])
                                                processed_nodes.append(neigh[i])
                        processed_nodes.append(each)

        return first_coalition, second_coalition
                                                

#create a graph of n nodes
G = nx.Graph()
n = 8
G.add_nodes_from([i for i in range(1, n+1)])
mapping = {1:'Alexandra', 2:'Anterim', 3:'Bercy', 4: 'Bearland', 5: 'Eplix', 6:'Gripa', 7:'Ikly', 8:'Jemla', 9:'Lema', 10:'Umesi', 11:'Mexim', 12:'Socialcity', 13:'Tersi', 14:'Xopia', 15:'Tamara'}
G = nx.relabel_nodes(G, mapping)

#complete the graph by adding edges and assign '+' or '-' to each edges
signs = ['+', '-']
for i in G.nodes():
    for j in G.nodes():
        if i!=j:
            G.add_edge(i, j, sign = random.choice(signs))
			
#display the network
edge_labels = nx.get_edge_attributes(G, 'sign')
pos = nx.circular_layout(G)
nx.draw(G, pos, node_size = 500, with_labels = 1)
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 20, font_color = 'red')
plt.show()

#Get a list of all the triangles in the network
nodes = G.nodes()
tris_list = [list(x) for x in itertools.combinations(nodes, 3)]

#Store the sign details of all the triangles
all_signs = get_signs_of_tris(tris_list, G)

#Count the number of unstable triangles in the network
unstable = count_unstable(all_signs)
unstable_track = []

#while the number of unstable triangles is not zero,
##select an unstable triangle
##Make that triangle stable
##Count the number of unstable triangles
while(unstable!=0):
        move_a_tri_to_stable(G, tris_list, all_signs)
        all_signs = get_signs_of_tris(tris_list, G)
        unstable = count_unstable(all_signs)
        unstable_track.append(unstable)

#plt.bar([i for i in range(len(unstable_track))], unstable_track)
#plt.show()

#now that graph is balanced
##divide it into two coaltitions
first, second = see_coalitions(G)
print(first)
print(second)
input()

#edge_labels = nx.get_edge_attributes(G, 'sign')
#pos = nx.circular_layout(G)
#nx.draw(G, pos, node_size = 500, with_labels = 1)
#nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 20, font_color = 'red')
#plt.show()

edge_labels = nx.get_edge_attributes(G, 'sign')
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist = first, node_color = 'red', node_size = 500, alpha = 0.8)
nx.draw_networkx_nodes(G, pos, nodelist = second, node_color = 'blue', node_size = 500, alpha = 0.8)
nx.draw_networkx_labels(G, pos, font_size = 10, font_family = 'sans-serif')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 20, font_color = 'green')
plt.show()
