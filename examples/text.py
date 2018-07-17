from guizero import App, Text
app = App()
text = Text(app, text="display some text")
text.when_clicked = lambda: print("hi")
#text.when_clicked = lambda: text.disable()
text.disable()
app.display()