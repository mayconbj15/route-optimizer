import networkx as nx
import matplotlib.pyplot as plt

def getGraph(tsp_result, addresses, distance_matrix, initial):
    
    G = nx.DiGraph()
    
    i=0
    while(i < len(tsp_result)-1):
        G.add_weighted_edges_from([(addresses[tsp_result[i]],addresses[tsp_result[i+1]], str(distance_matrix[tsp_result[i]][tsp_result[i+1]]))])
        i+=1
    
    colors = ['b' for i in range(0,len(addresses))]
   
    for i in range(0, len(tsp_result)):
        if tsp_result[i] == initial:
            print(i)
            colors[i] = 'r' 
            break

    #nx.draw_networkx(G, with_labels = True, node_size=500, arrowsize=30, node_color = colors, cmap = plt.cm.BrBG)
    #nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))

    #plt.show()
    return G, colors


def main(tsp_result, addresses, distance_matrix, initial):
    #tsp_result = [0, 2, 3, 1, 0]
    #distance_matrix = [[0, 120767, 19496, 228133], [119085, 0, 105592, 112085], [20209, 104912, 0, 212329], [224256, 109717, 210763, 0]]
    #addresses = ['Contagem', 'Itabira', 'Belo Horizonte', 'Ipatinga']
    #initial = 2

    return getGraph(tsp_result, addresses, distance_matrix, initial)


if __name__ == '__main__':
  main([],[],[], 1)