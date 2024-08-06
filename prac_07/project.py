import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_pct):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_pct = completion_pct

    def update_completion(self, new_completion):
        self.completion_pct = new_completion

    def update_priority(self, new_priority):
        self.priority = new_priority

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_pct}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority

