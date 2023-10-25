from guizero import App, Text, PushButton

def change_message():
    message.value = "Arriba el america!!! prros!!!"
app = App(title="ICI App")

message = Text(app,text="welcome to ICI world!")

button = PushButton(app,text="click here", command=change_message)
app.display()
