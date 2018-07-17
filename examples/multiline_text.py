from guizero import App, Text

app = App()
#app.enabled = False
text = Text(app, multiline=True)
text.value = "hello\ngoodbye\nno way\nthis is a very long stream of text, very long indeed, the best long line of text, its super bigly and very long, I dont think it could possibly be any better particularly as it was created by someone who is super good at creating long lines of text."
print(text.tk.keys())
app.display()