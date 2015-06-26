from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line, Ellipse

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')

class MyApp(App):
    title = 'Simple Graphics'

    def build(self):
        w = Widget()

        with w.canvas:
            Color(1, 0, 0)
            Rectangle(pos=(50, 80), size=(120, 120))

            Color(1, 1, 0, .5)
            Line(points=[100, 50, 350, 250, 350, 50], width=10, close='True')

            Color(0, .5, 1)
            Ellipse(pos=(150, 150), size=(120, 120))

        return w

if __name__ == '__main__':
    MyApp().run()