from python.serial.SerialManager import SerialManager
from guizero import App, Text, TextBox

if __name__ == "__main__":
    import sys
    sys.path.append("/home/pi/Documents/TempDataLogger-")
    sys.path.append("/home/pi/Documents/TempDataLogger-/python/serial")

    # serial = SerialManager()
    # serial.start()

    app = App(title="Hello world")

    welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")
    my_name = TextBox(app)

    app.display()