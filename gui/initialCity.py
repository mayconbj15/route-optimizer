import PySimpleGUI as sg

import tsp
import distances

from gui import result
import config

elements_col_size = (50, 0)
zoom_buttons_size = (24, 0)

def getInitial(addresses, values):
    initial = 0 
    for i in range(0, len(addresses)):
        print(values['_radio{}'.format(i)])
        if values['_radio{}'.format(i)]:
            initial = i 
            break
    
    return initial

def telaInicial(addresses):
    #sg.theme(configs.theme)  # please make your windows colorful

    layout = [
        [sg.Text('Qual cidade deseja iniciar a sua viagem',
                 size=elements_col_size)],
        
    ]

    layout.append([sg.Radio(addresses[0],'City',default = True, disabled = False, key='_radio0')])
    for i in range(1, len(addresses)):
        layout.append([sg.Radio(addresses[i],'City',default = False, disabled = False, key='_radio{}'.format(i))])
    
    layout.append([sg.Button('BORA', size=elements_col_size,
                   key="_calc")])

    layout.append([sg.Button('Debug', size=elements_col_size,
                   key="_debug")])
    layout.append([sg.Exit()])

    window = sg.Window(config.title, layout)

    while (True):
        # event é uma ação e values é uma lista de dados
        event, values = window.read()

        if event == '_calc':
            print(addresses)

            distance_matrix = distances.main(addresses)

            initial = getInitial(addresses, values)
            calc = tsp.TSP()
            tsp_result = calc.run(distance_matrix, initial)
            
            window.close()
            result.telaInicial(tsp_result, addresses, distance_matrix, initial)

        elif event == sg.WIN_CLOSED or event == 'Exit':
            break