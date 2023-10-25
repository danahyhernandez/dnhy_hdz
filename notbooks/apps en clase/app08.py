from guizero import App, Text, TextBox, PushButton

def message_cuadrado():
    resultado = str(int(name.value)**2)
    app.info(title="resultado", text = resultado)


app = App(title="ICI App")

message = Text(app, text="Dame un numero")
name = TextBox(app, width=20)
button = PushButton(app, text="Calcular el cuadrado", command=message_cuadrado)
app.display()