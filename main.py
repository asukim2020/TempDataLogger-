from python.serial.SerialManager import SerialManager
from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

def do_booking():
    info("Booking", "Thank you for booking")

# from guizero import App, Text, TextBox, PushButton, Slider

# def say_my_name():
#     welcome_message.value = my_name.value
#
# def change_text_size(slider_value):
#     welcome_message.size = slider_value

if __name__ == "__main__":
    import sys
    sys.path.append("/home/pi/Documents/TempDataLogger-")
    sys.path.append("/home/pi/Documents/TempDataLogger-/python/serial")

    # serial = SerialManager()
    # serial.start()

    # app = App(title="My second GUI app", width=300, height=200, layout="grid")
    #
    # film_description = Text(app, text="Which film?", grid=[0, 0], align="left")
    # film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1, 0], align="left")
    #
    # film_description = Text(app, text="Seat type", grid=[0, 1], align="left")
    # vip_seat = CheckBox(app, text="VIP seat?", grid=[1, 1], align="left")
    #
    # film_description = Text(app, text="Seat location", grid=[0, 2], align="left")
    # row_choice = ButtonGroup(app, options=[["Front", "F"], ["Middle", "M"], ["Back", "B"]], selected="M", horizontal=True, grid=[1, 2], align="left")
    #
    # book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[1, 3], align="left")
    #
    # app.display()

    # app = App(title="Hello world")
    #
    # welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")
    # my_name = TextBox(app, width=40)
    # update_text = PushButton(app, command=say_my_name, text="Display my name")
    # text_size = Slider(app, command=change_text_size, start=10, end=80)
    #
    # app.display()





    # from guizero import App, Box, TextBox, PushButton
    #
    # app = App()
    # app.tk.attributes("-fullscreen", True)
    #
    # def exit_full_screen():
    #     app.destroy()
    #
    # for y in range(4):
    #     button_box = Box(app, align="top", width="fill")
    #     for z in range(4):
    #         PushButton(button_box, command=exit_full_screen, align="left", width="fill")
    #
    # textboxes_box = Box(app, align="top", width="fill")
    #
    # TextBox(textboxes_box, width="fill", height="fill", multiline=True)

    serial = SerialManager()
    # serial.setApp(app)
    serial.start()

    # app.display()

