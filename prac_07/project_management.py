import datetime
from project import Project


def main():
    default_file = 'projects.txt'
    projects = load_projects(default_file)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {default_file}")

    menu_options = {
        'l': "Load projects",
        's': "Save projects",
        'd': "Display projects",
        'f': "Filter projects by date",
        'a': "Add new project",
        'u': "Update project",
        'q': "Quit"
    }

    def display_menu():
        for key, value in menu_options.items():
            print(f"- ({key.upper()}) {value}")

    choice = ''
    while choice != 'q':
        display_menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'l':
            projects = load_projects(default_file)
            print(f"Loaded {len(projects)} projects from {default_file}")

        elif choice == 's':
            save_projects(default_file, projects)
            print("Projects saved successfully.")

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date)

        elif choice == 'a':
            add_new_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice.startswith('y'):
                save_projects(default_file, projects)
            print("Thank you for using custom-built project management software.")

        else:
            print("Invalid choice. Please enter again.")



def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()
            for line_number, line in enumerate(file, start=2):
                line = line.strip()
                if line:
                    try:
                        name, start_date, priority, cost_estimate, completion_pct = line.split('\t')
                        projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_pct)))
                    except ValueError:
                        print(f"Error in line {line_number}: Invalid format or values.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion (%)\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_pct}\n")







