import PySimpleGUI as sg

import tsp

from gui import addresses

import config

elements_col_size = (50, 0)
zoom_buttons_size = (24, 0)


def telaInicial():
    #sg.theme(configs.theme)  # please make your windows colorful

    layout = [
        [sg.Text('Quantas cidade irá viajar?',
                 size=elements_col_size)],
        [sg.Slider(range = (3, 10), orientation='horizontal', key="_slider")],
        [sg.Button('BORA', size=elements_col_size,
                   key="_calc")],
        [sg.Exit()]
    ]

    window = sg.Window(config.title, layout)

    folder = "vazio"
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

def main():
    telaInicial()

if __name__ == "__main__":
    main()
