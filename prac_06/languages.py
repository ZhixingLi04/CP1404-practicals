# Define the ProgrammingLanguage class
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"


# Create instances of ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print the instances to test __str__
print(python)


# Create a list of ProgrammingLanguage instances
languages = [python, ruby, visual_basic]

# Loop through the list and print dynamically typed languages
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)

