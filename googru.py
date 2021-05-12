import PySimpleGUI as sg

import webbrowser

sg.theme('SystemDefault')

layout = [[sg.InputText(key='-IN-'),
           sg.Button('Search', key='-SEARCH-'),
           sg.Button('Clear', key='-CLEAR-')],]

window = sg.Window('ググるやつ。', layout, grab_anywhere=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-SEARCH-':
        webbrowser.open('https://www.google.co.jp/search?q=' +
                        values['-IN-'] +'&ie=utf-8&oe-utf-8&hl=ja')
    if event == '-CLEAR-':
        window['-IN-'].update('')

window.close()