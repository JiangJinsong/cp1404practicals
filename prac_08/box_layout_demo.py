from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemoApp(App):
    def build(self):
        return Builder.load_file("box_layout.kv")

    def handle_greet(self):
        # For debugging
        print("greet")
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    BoxLayoutDemoApp().run()