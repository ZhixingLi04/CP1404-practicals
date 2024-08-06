from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        """This function initializes the application and sets up the main window."""
        self.title = "Dynamic Labels"
        self.names = ["Li", "Gao", "Zhang", "Wu"]
        self.root = Builder.load_file('dynamic_labels.kv')
        self.add_labels()
        return self.root

    def add_labels(self):
        """This function creates and adds labels to the main window."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)




DynamicLabelsApp().run()
