import csv

filename = 'wimbledon.csv'
year_to_data = {}
datas = []

def main():
    """Display the player names and their frequencies by country."""
    year_to_data = read_wimbledon_data()
    winner_detail, names = display_name(year_to_data)
    name_time = count_name_times(names)
    display_data(name_time)
    country = extract_winner_countries(winner_detail)
    number = count_country_number(country)
    display_winner_country(number, country)


def read_wimbledon_data():
    """Reads the Wimbledon data from the given CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for data in reader:
            datas.append(data)
            year_to_data[data[0]] = data[1:-1]
    return year_to_data


def display_name(year_to_data):
    """show the no.1 name and winner details"""
    winner_detail = list(year_to_data.values())
    names = []
    for i in winner_detail:
        names.append(i[1])
    return winner_detail, names


def count_name_times(names):
    """calculate the name times"""
    name_to_count = {}
    for name in names:
        if name in name_to_count:
            name_to_count[name] += 1
        else:
            name_to_count[name] = 1
    return name_to_count


def display_data(name_frequency):
    """Displays player names and their occurrence frequencies."""
    for name, count in name_frequency.items():
        print(f"{name}: {count}")


def extract_winner_countries(winner_detail):
    """Extracts player names and their countries from wimbledon data."""
    country = set()
    for i in winner_detail:
        country.add(i[0])
    country = sorted(country)
    return country


def count_country_number(country):
    """calculate the country number """
    number = len(country)
    return number


def display_winner_country(number, countries):
    """display the winner country"""
    print(f"These {number} countries have won Wimbledon:")
    countries_str = ".".join(countries)
    print(f"{countries_str}")


main()


