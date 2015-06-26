from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App

Builder.load_string("""
<CellarDoor>:
    ToggleButton:
        text: 'Reverse'
        on_state: root.beer_sort((True if self.state=='down' else False))
#    ListView:
#        adapter: root.beer_la
""")

class CellarDoor(BoxLayout):
    def __init__(self, **kwargs):
        self.beer_archive = ["Item #{0}".format(i) for i in range(10)]
        self.beer_la = ListAdapter(data=self.beer_archive,
                          cls=ListItemButton,
                          selection_mode='single',
                          allow_empty_selection=True)

        super(CellarDoor, self).__init__(**kwargs)
        self.add_widget(ListView(adapter=self.beer_la))


    def beer_sort(self, reverse):
        self.beer_la.data = sorted(self.beer_archive,
                                   reverse=reverse)
        print self.beer_la.data

class TestApp(App):
    def build(self):
        return CellarDoor()

if __name__ == '__main__':
    TestApp().run()