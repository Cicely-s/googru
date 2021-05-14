import PySimpleGUI as sg

import webbrowser
from popup import OptionPopup

sg.theme('SystemDefault')

red_x_base64 = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAC8AAAAvAHPHSQeAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAfFJREFUOI21krFLW1EUxn95970UWzEhMQgiQXl2aJ+6FQmdHBxEEDso0iE6ZC84+Cc4a90cCloIdGkWpf+CWhCDTUtrEumgTWr6ioQX0kTf6ZC8RBLaqf2We7nfOR/n+86F/4k0PPgE4b/V+DofzqCvCqu6UnF/MDiiaRq1SuW65jhvNVi3IPtHgY/wEKXeRSzLDJkmmq63uEqpRCGdrlZs+/k4pLoEzqCvrtSxublp+oeHYXcXRNrq09NINMrX5eW6Uyw+HYP3AJrHV2E1YlmN5tlZiMfbzTMzkEjgCwYZisUMZRhbHtWaUVcqHjJN2NmBeh3m5xvE5SWsrMDREWxsoBsGgWh0MpPLjVqQ1QEy0OsPBEZanpPJxumJNJu5vQXgfn8/P3K5CSDrWfDfDQyAq6v2vVQC120nrxQ+uNey8Bh+fnGcayDgBUYiAYeHUCzC3Fwj0GawtXIZOtbJKbxypqZEtrdFXFfk4EBkaUlkYUEklRIREdnbE1lclHwo9E2aC2htQYP1QjpdlcHBLs8kk7C/D5EIdj6PY9trPnCh4yOdwrPegYE3Q7GYoRsGnbDPz/l+cvLy0c3Ni1YenUUf4IkyjK1ANDrZEw6jdJ1f5TLli4uCY9tr4/D6bn2XgIcMjLowoUGPC5/H4Ngb+5/iN+YHueS9rMuEAAAAAElFTkSuQmCC'

search_param = {'通常': '',
                '画像': 'isch',
                '動画': 'vid',
                'ニュース': 'nws',
                'ショッピング': 'shop',
                '書籍': 'bks',
                'ブログ': 'blg',
                '特許': 'pts',}

layout = [[sg.Text('Option'),
        sg.Combo(values=(list(search_param)),
            key='-OPTION-', size=(15, 0),
            default_value='通常'),
        sg.Text('', size=(27, 0)),
        sg.Button('',
            image_data=red_x_base64,
            button_color=(sg.theme_background_color(),
                sg.theme_background_color()),
            border_width=0,
            key='-EXIT-'),],
        [sg.InputText(key='-IN-'),
        sg.Button('Search',
            key='-SEARCH-',
            bind_return_key=True),
        sg.Button('Clear',
            key='-CLEAR-'),]]

window = sg.Window('ググるやつ。', icon='images/logo.ico', grab_anywhere=True, keep_on_top=True, no_titlebar=True).Layout(layout)

while True:
    event, values = window.read()
    print(event, values)

    if event in (sg.WINDOW_CLOSED, '-EXIT-'):
        break
    elif event == '-SEARCH-':
        webbrowser.open('https://www.google.co.jp/search?q=' +
                        values['-IN-'] +'&ie=utf-8&oe=utf-8&tbm=' +
                        search_param[values['-OPTION-']])
    elif event == '-CLEAR-':
        window['-IN-'].update('')

window.close()