import sys

from main import Weather


class Menu:

    def __init__(self):
        self.weather = Weather()
        self.choices = {
            '1': self.sync,
            '2': self.display,
            '3': self.quit,
        }

    def run(self):
        while True:
            print('''
1. sync weather data with server
2. display last synced weather data
3. quit 
''')
            choice = input('Your choice: ')
            action = self.choices.get(choice)
            if action:
                action()

    def sync(self):
        self.weather.sync()

    def display(self):
        self.weather.display()

    def quit(self):
        sys.exit(0)


if __name__== '__main__':
    Menu().run()