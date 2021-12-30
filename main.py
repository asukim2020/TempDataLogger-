from python.serial.SerialManager import SerialManager
from guizero import App, Text, TextBox, PushButton, Slider

def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value

if __name__ == "__main__":
    import sys
    sys.path.append("/home/pi/Documents/TempDataLogger-")
    sys.path.append("/home/pi/Documents/TempDataLogger-/python/serial")

    # serial = SerialManager()
    # serial.start()

    app = App(title="Hello world")

    welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")
    my_name = TextBox(app, width=40)
    update_text = PushButton(app, command=say_my_name, text="Display my name")
    text_size = Slider(app, command=change_text_size, start=10, end=80)

    app.display()