from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

    def build(self):
        root = Builder.load_file("dynamic_labels.kv")
        main_box = root.ids.main
        for name in self.names:
            label = Label(text=name)
            main_box.add_widget(label)
        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()