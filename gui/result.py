import PySimpleGUI as sg
import networkx as nx
import matplotlib.pyplot as plt

import graph
import config

from gui import quant


elements_col_size = (50, 0)
zoom_buttons_size = (24, 0)


def telaInicial(tsp_result, addresses, distance_matrix):
    #sg.theme(configs.theme)  # please make your windows colorful

    layout = [
        [sg.Text('Resultado', size=elements_col_size)],
    ]

    layout.append([sg.Text('Sua melhor rota', size=elements_col_size)])

    text = ""
    i=0
    print(tsp_result)
    print(addresses)
    print(distance_matrix)
    while(i < len(tsp_result)-1):
        text += '{} -> {} Distance {} \n'.format(addresses[tsp_result[i]], addresses[tsp_result[i+1]], str(distance_matrix[tsp_result[i]][tsp_result[i+1]]))
        i+=1
        
    layout.append([sg.Text(text, size=elements_col_size)])

    layout.append([sg.Button('Nova entrada de dados', size=elements_col_size,key="_calc")])
    layout.append([sg.Exit()])

    window = sg.Window(config.title, layout)

    G = graph.main(tsp_result, addresses, distance_matrix)
    
    val_map = {addresses[tsp_result[0]]: 0.0}

    values = [val_map.get(node, 0.5) for node in G.nodes()]
    nx.draw_networkx(G, with_labels = True, node_size=500, node_color = values)
    plt.show()

    printResult(tsp_result, addresses)
    
    while (True):
        # event é uma ação e values é uma lista de dados
        event, values = window.read()

        if event == '_calc':
            window.close()
            plt.close()
            quant.telaInicial()

        elif event == sg.WIN_CLOSED or event == 'Exit':
            break

def printResult(tsp_result, addresses):
    print('Sua melhor rota')

    for i in tsp_result:
        print(str(addresses[int(i)]) + ' -> ')

def main():
    telaInicial()

if __name__ == "__main__":
    main()
