from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemoApp(App):

    def build(self):
        """This function initializes the application and sets up the main window."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def greet_user(self):
        """This function handles the greeting by updating the output label with the input name."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def clear_input(self):
        """This function clears the input text and the output label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""




BoxLayoutDemoApp().run()
