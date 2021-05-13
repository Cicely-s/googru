import PySimpleGUI as sg

import webbrowser

sg.theme('SystemDefault')

layout = [[sg.InputText(key='-IN-'),
        sg.Button('Search', key='-SEARCH-', bind_return_key=True),
        sg.Button('Clear', key='-CLEAR-')],]

window = sg.Window('ググるやつ。', icon='images/logo.ico', grab_anywhere=True, keep_on_top=True).Layout(layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == '-SEARCH-':
        webbrowser.open('https://www.google.co.jp/search?q=' +
                        values['-IN-'] +'&ie=utf-8&oe-utf-8&hl=ja')
    elif event == '-CLEAR-':
        window['-IN-'].update('')

window.close()