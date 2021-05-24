import PySimpleGUI as sg

import tsp

from gui import addresses
import config

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
    while(i < len(tsp_result)-1):
        text += '{} -> {} Distance {} \n'.format(addresses[tsp_result[i]], addresses[tsp_result[i+1]], str(distance_matrix[tsp_result[i]][tsp_result[i+1]]))
        i+=1
        
    layout.append([sg.Text(text, size=elements_col_size)])

    #layout.append([sg.Graph((500,500),(0,0),(300,300))])

    window = sg.Window(config.title, layout)

    printResult(tsp_result, addresses)
    
    layout.append([sg.Exit()])
    while (True):
        # event é uma ação e values é uma lista de dados
        event, values = window.read()

        if event == '_calc':
            quant_addresses = window['_slider'].TKScale.get()
            print(quant_addresses)
            window.close()
            addresses.telaInicial(quant_addresses)

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
