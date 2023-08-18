# Second attempt at OOP
import json # To save stuff into a text file
class Country:

    def __init__(self, name, size, population, military_size, cities=None):
        self.name = name
        self.size = size
        self.population = population
        self.military_size = military_size
        self.cities = cities if cities is not None else [] # list to store cities

    def add_city(self, city):
        if city not in self.cities:
            if city.country is None:
                City.independent_cities.append(city)
            else:
                self.cities.append(city)  # Only add to the country's cities list if it has a specific country
                city.country.cities.append(city)
        else:
            print(f"The city of {city} is already part of the great nation of {self.name}!")


    def removeCity(self, city):
        if city in self.cities:
            self.cities.remove(city)
            city.country = None  # Remove the city's association with the country
        else:
            print(f"The great nation of {name} has no such city as {city}!")

    def describe(self):
        print(f"The Nation of {self.name} occupies {self.size} square meters, has a population of {self.population}"
              f" and a standing army of {self.militarySize}.")


class City:

    independent_cities = [] # A list of cities without a Country

    def __init__(self, name, country, is_capital, size, population, governor, military_size):
        if not isinstance(name, str):
            raise ValueError("name must be a string, please.")
        self.name = name
        self.country = country
        self.is_capital = is_capital
        self.size = size
        if not isinstance(population, int):
            raise ValueError("Give us an int.")
        self.population = population
        self.governor = governor
        self.military_size = military_size
        self.houses = [] # list to store Houses

    def toggle_capital(self):
        if self.is_capital == True:
            self.is_capital = not self.is_capital

    def add_house(self, noble_house):
        self.houses.append(noble_house)

    def remove_house(self, noble_house):
        self.houses.remove(noble_house)

    def describe(self):
        capital_text = " is a Capital city." if self.is_capital else ""
        country_text = f" in the independent city of {self.name}" if self.country is None else f" "
        f"in the country of {self.country.name}"
        description = (
            f"The City of {self.name} occupies {self.size} square meters,"
            f" has a population of {self.population} and a standing army of {self.military_size}."
            f"The current governor is {self.governor}."
            f"{capital_text}"
        )
        print(description)

def save_data(countries):
    with open('data.json', 'w') as f:
        json.dump(countries, f, default=lambda obj: obj.__dict__, indent=4)

def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            print("Loaded data:", data)  # Add this line
            countries = [Country(**country) for country in data]
            for country in countries:
                for city in country.cities:
                    city.country = country
            return countries
    except FileNotFoundError:
        return []

# note: we need exceptions and controls for user nonsense
def main():
    countries = load_data()

    while True:
        print("\nWelcome to the City and Country Management System!")
        print("1. Add Country")
        print("2. Add City")
        print("3. Describe Country")
        print("4. Describe City")
        print("5. Save and Exit")

        choice = input("Enter you choice: ")

        if choice == '1':
            name = input("Enter the country name: ")
            size = int(input("Enter the country size: "))
            population = int(input("Enter country population: "))
            military_size = int(input("Enter country military size: "))
            country = Country(name, size, population, military_size)
            countries.append(country)
            print(f"Country {name} added!\n")

        elif choice == '2':
            name = input("Enter city name: ")
            country_name = input("Enter country name (leave empty for independent city): ")
            is_capital = input("Is it a capital city? (yes/no): ").lower() == 'yes'
            size = int(input("Enter city size: "))
            population = int(input("Enter city population: "))
            governor = input("Enter city governor: ")
            military_size = int(input("Enter city military size: "))

            if country_name:
                for c in countries:
                    if c.name == country_name:
                        country = c
                        break
                else:
                    print("Country not found!")
                    continue
            else:
                country = None

            city = City(name, country, is_capital, size, population, governor, military_size)
            if country is None:
                City.independent_cities.append(city)
            else:
                country.addCity(city)
            print(f"City {city} added!\n")
        elif choice == '3':
            country_name = input("Enter country name: ")
            for country in countries:
                if country.name == country_name:
                    country.describe()
                    break
            else:
                print("Country not found!")

        elif choice == '4':
            city_name = input("Enter city name: ")
            city_found = False # keep track if city is found
            for country in countries:
                for city in country.cities:
                    if city.name == city_name:
                        city.describe()
                        city_found = True
                        break
                if city_found:
                    break #exit outer loop if city is found
            if not city_found:
                print("City not found!")

if __name__ == "__main__":
    main()



# Idea: have a pop-up program (terminal) ask the user to add cities or nations
# then write those additions into one of two folders, one with cities and the other with nations
# Or: how do we make these changes permanent? Using SQL and a DB? mh........... damn.


