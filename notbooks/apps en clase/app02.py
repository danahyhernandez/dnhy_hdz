import pyttsx3

engine = pyttsx3.int()
engine.say(f"Dame tu nombre")
engine.runAndWait()

name = input("Dame tu nombre")

engine.say(f"Hola (name)")
engine.runAndWait()
