from guizero import App, Text, TextBox, PushButton
import pyttsx3

engine = pyttsx3.init()

def mensaje_cuadrado():
    resultado = str(int(name.value)**2)
    cadena = f"El cuadrado de {name.value}"
    engine.say(cadena)
    engine.runAndWait()


app = App(title="ICI App")

message = Text(app, text="Dame un numero")
name = TextBox(app, width=20)
button = PushButton(app, text="calcular el cuadrado", command=mensaje_cuadrado)
app.display()
