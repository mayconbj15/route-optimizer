import networkx as nx

def getGraph(tsp_result, addresses, distance_matrix):
    
    G = nx.DiGraph()
    
    i=0
    while(i < len(tsp_result)-1):
        G.add_weighted_edges_from([(addresses[tsp_result[i]],addresses[tsp_result[i+1]],str(distance_matrix[tsp_result[i]][tsp_result[i+1]]))])
        i+=1
    
    return G 


def main(tsp_result, addresses, distance_matrix):
    #tsp_result = [0, 2, 3, 1, 0]
    #distance_matrix = [[0, 120767, 19496, 228133], [119085, 0, 105592, 112085], [20209, 104912, 0, 212329], [224256, 109717, 210763, 0]]
    #addresses = ['Contagem', 'Itabira', 'Belo Horizonte', 'Ipatinga']
    
    return getGraph(tsp_result, addresses, distance_matrix)


if __name__ == '__main__':
  main(None)