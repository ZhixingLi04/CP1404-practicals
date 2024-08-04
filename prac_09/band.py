class Band:
    def __str__(self):
        """Return a string representation of the band, including its name and members."""
        member_string = ', '.join([f'{member.name} ({member.instruments})' for member in self.members])
        return f'{self.name} ({member_string})'

    def __init__(self, name):
        """Initialize a Band object with a name and an empty list of members."""
        self.name = name
        self.members = []

    def play(self):
        """Make all band members play their instruments and return the result as a string."""
        return '\n'.join([member.play() for member in self.members])

    def add_member(self, member):
        """Add a new member to the band's list of members."""
        self.members.append(member)



