"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder


__author__ = 'Zhixing Li'

MILES_TO_KM = 1.60934


class MilesToKmConverterApp(App):
    """ MilesToKmConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


    def calculate_conversion(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def change_input_value(self, change):
        """
        This function updates the input value and calls the calculation function.
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.calculate_conversion()

    #
    def get_validated_miles(self):
        """
        This function validates the input, converting it to a float or returning 0 if there's an error
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0



MilesToKmConverterApp().run()