import PySimpleGUI as sg

from gui import quant

#sg.theme(configs.theme)  # please make your creations colorful

layoutInicial = [
    [sg.Button('Iniciar', key='_start', size=(62, 1))],
    [sg.Button("Sobre o trabalho", size=(30, 1), key='_sobre'),
        sg.Button("Como funciona?", size=(30, 1), key='_tutorial')],
    [sg.Exit()]
]

# MAIN |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def main():
    window = sg.Window('Processamento de Imagens', layoutInicial)

    while True:
        event, values = window.read()
        # Se a janela for fechada ou o botao EXIT for apertado, ele para o programa.
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
            window.close()
        if event == '_start':
            window.close()
            quant.telaInicial()
    
if __name__ == "__main__":
    main()
