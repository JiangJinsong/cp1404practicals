from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define a list of names (the data/model)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

    def build(self):
        # Load the kv file
        root = Builder.load_file("dynamic_labels.kv")
        # Retrieve the BoxLayout with id 'main'
        main_box = root.ids.main
        # Loop over the list and create a Label for each name, then add it to the layout
        for name in self.names:
            label = Label(text=name)
            main_box.add_widget(label)
        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()