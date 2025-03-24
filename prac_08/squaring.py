"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""
from kivy.app import App
from kivy.lang import Builder

class SquaringApp(App):
    def build(self):
        return Builder.load_file("squaring.kv")

    def handle_square(self):
        # Get the text from the input field
        input_text = self.root.ids.input_number.text
        try:
            # Attempt to convert the input to a float and square it
            number = float(input_text)
            squared = number ** 2
            self.root.ids.output_label.text = str(squared)
        except ValueError:
            # In case the conversion fails, show an error message
            self.root.ids.output_label.text = "Invalid input!"

if __name__ == '__main__':
    SquaringApp().run()