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

            distance_matrix = distances.main(addresses)
    
            calc = tsp.TSP()
            tsp_result = calc.run(distance_matrix)
            
            result.telaInicial(tsp_result, addresses, distance_matrix)

        elif event == sg.WIN_CLOSED or event == 'Exit':
            break
