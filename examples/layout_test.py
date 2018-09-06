from guizero import App, PushButton

a = App()

left = PushButton(a, align="left", text="left")
top_left = PushButton(a, align="top left", text="top left")
top_left = PushButton(a, align="top left", text="top left")
top_right = PushButton(a, align="top right", text="top right")
right = PushButton(a, align="right", text="right")
top = PushButton(a, align="top", text="top")
bottom = PushButton(a, align="bottom", text="bottom")
none = PushButton(a, text="none")
a.display()

