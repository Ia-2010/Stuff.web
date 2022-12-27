import eel
eel.init(r"C:\Users\drkpp\Webbo sito\website\templates")

@eel.expose
def demo(x):
    return x**2

# 1000 is width of window and 600 is the height
eel.start(r"C:\Users\drkpp\Webbo sito\website\templates\index.html", size=(1000, 600))
demo#
def oo():
 print("deez nuts")

 