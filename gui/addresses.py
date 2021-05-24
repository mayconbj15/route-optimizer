import PySimpleGUI as sg

import tsp
import distances

from gui import result
import config

elements_col_size = (50, 0)
zoom_buttons_size = (24, 0)


def telaInicial(n_addresses):
    #sg.theme(configs.theme)  # please make your windows colorful

    layout = [
        [sg.Text('Adicione as cidades que irá viajar',
                 size=elements_col_size)],
        
    ]
    for i in range(n_addresses):
        layout.append([sg.Input(default_text = "", key='city' + str(i))])
    
    layout.append([sg.Button('BORA', size=elements_col_size,
                   key="_calc")])

    layout.append([sg.Exit()])

    window = sg.Window(config.title, layout)

    folder = "vazio"
    while (True):
        # event é uma ação e values é uma lista de dados
        event, values = window.read()

        if event == '_calc':
            addresses = []
            for i in range(n_addresses):
                addresses.append(values['city' + str(i)])
            
            print(addresses)

            #distance_matrix = distances.main(addresses)

            distance_matrix = [
                [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
                [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
                [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
                [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
                [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
                [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
                [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
                [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
                [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600]
            ]
        
            calc = tsp.TSP()
            tsp_result = calc.run(distance_matrix)
            addresses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

            result.telaInicial(tsp_result, addresses, distance_matrix)

        elif event == sg.WIN_CLOSED or event == 'Exit':
            break
