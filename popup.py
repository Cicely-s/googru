import PySimpleGUI as sg

class OptionPopup:
    def __init__(self, imp_name_list):
        self.layout = [[sg.Text('Check a Search Option')]] + \
            [[sg.Radio(name, 'option')] for name in imp_name_list if name is not None] + \
            [[sg.OK(), sg.Cancel()]]

        self.window = sg.Window(title='Search Option', layout=self.layout)
        self.exclude = set()
        self.imp_name_list = imp_name_list


    def get_excluded(self):
        while True:
            event, values = self.window.read()

            if event in ('Exit', 'Quit', 'Cancel', None):
                break

            elif event == 'OK':
                for name, check in zip(self.imp_name_list, values.values()):
                    if check:
                        self.exclude.add(name)
                break

        self.window.close()
        return self.exclude