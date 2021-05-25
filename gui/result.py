import PySimpleGUI as sg
import networkx as nx
import matplotlib.pyplot as plt

import graph
import config

from gui import quant


elements_col_size = (50, 0)
zoom_buttons_size = (24, 0)


def telaInicial(tsp_result, addresses, distance_matrix, initial):
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
    print(initial)
    while(i < len(tsp_result)-1):
        text += '{} -> {} Distance {} \n'.format(addresses[tsp_result[i]], addresses[tsp_result[i+1]], str(distance_matrix[tsp_result[i]][tsp_result[i+1]]))
        i+=1
        
    layout.append([sg.Text(text, size=elements_col_size)])

    layout.append([sg.Button('Nova entrada de dados', size=elements_col_size,key="_calc")])
    layout.append([sg.Exit()])

    window = sg.Window(config.title, layout)

    G, colors = graph.main(tsp_result, addresses, distance_matrix, initial)
    
    nx.draw_networkx(G, with_labels = True, node_size=500, arrowsize=30, node_color = colors, cmap = plt.cm.BrBG)
    nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
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
