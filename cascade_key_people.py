#cascade key people
import networkx as nx
import matplotlib.pyplot as plt
"""
G=nx.erdos_renyi_graph(10,0.5)
nx.write_gml(G,"erdos_graph.gml")"""

def set_all_B(G):
    for i in G.nodes():
        G.node[i]['action']='B'
    return G


def set_A(G,list1):    
    for i in list1:        
        G.node[i]['action']='A'
    return G


def get_colors(G):
    color=[]
    for i in G.nodes():
        if(G.node[i]['action']=='B'):
            color.append('red')
        else:
            color.append('green')
    return color


def recalcute_options(G):
    dict1={}
    #payoff(A)=a=4
    #payoff(B)=b=3
    a=10
    b=5
    for i in G.nodes():
        neigh=G.neighbors(i)
        count_A=0
        count_B=0
        
        for j in neigh:
            if(G.node[j]['action']=='A'):
                count_A+=1
            else:
                count_B+=1
                
        payoff_A=a*count_A
        payoff_B=b*count_B    
        
        if(payoff_A>=payoff_B):
            dict1[i]='A'
        else:
            dict1[i]='B'
            
    return dict1
    
def reset_node_attributes(G,action_dict):
    for i in action_dict:
        #print(i,action_dict[i])
        G.node[i]['action']=action_dict[i]
    return G

def terminate(G ):
    continuee=True
    count=0
    c=0
    
    while(continuee and count<100):
        count+=1
        action_dict=recalcute_options(G)#action_dict will hold a dictionary
        #print(action_dict)
        G=reset_node_attributes(G,action_dict)
        colors=get_colors(G)        
        if(colors.count('red')==len(colors) or colors.count('green')==len(colors)):
            continuee=False
            if(colors.count('green')==len(colors)):
                c=1
            
    if(c==1):
        print('cascade complete')
    else:
        print('cascade incomplete')
#    nx.draw(G, with_labels=1,node_color=colors, node_size=800)
#    plt.show()
    
G=nx.read_gml('random_graph.gml')

for i in G.nodes():
    for j in G.nodes():
        if(i<j):
            list1=[]
            list1.append(i)
            list1.append(j)
            print(list1,':',end="")
            
            G=set_all_B(G)            
            G=set_A(G,list1)
            colors=get_colors(G)
            #nx.draw(G, with_labels=1,node_color=colors, node_size=800)
            #plt.show()            
            terminate(G)
