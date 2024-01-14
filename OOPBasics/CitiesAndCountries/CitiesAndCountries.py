


# NOTE:
'''PAUSING - NEED TO UNDERSTAND HOW TO DO CLASSES AND SUBCLASSES'''


list_of_cities=[]

class City:

    def __init__(self, name, size, population, military, governor, is_capital):
        self.name = name
        self.size = size
        self.population = population
        self.military = military
        self.governor = governor
        self.is_capital = is_capital
        self.houses = []

    def __str__(self): # A print of objects of this class returns this
        return f"\nCity: {self.name}\nSize: {self.size}\nPopulation: {self.population}\n" \
               f"Military: {self.military}\nGovernor: {self.governor}\nHouses: {self.houses}"

    def city_appender(self):
        list_of_cities.append(self)

    def add_house(self, specific_city):
        while True:
            specific_house = input("Which house would you like to add:\n")
            specific_city.houses.append(specific_house)
            response = input("House added. Would you like to add any more houses?\n")
            if response == 'n' or response == 'no':
                break

city1 = City("Albatroz", 33, 2233, 2222, "Tom", False)

city1.houses = ["Venn", "Martenz", "Eldenkranz"]
city1.city_appender()

for i in list_of_cities:
    print(i)

def main():


# Place the city management system inside the country management system
    while True:
        print("\nWelcome to the City Management System!")
        print("1. Show current cities")
        print("2. Add City")
        print("3. Describe Country")
        print("4. Describe City")
        print("5. Save and Exit")
        print("6. Houses Submenu")


        choice = input("Enter your choice: ")


        if choice == "1":
            for item in list_of_cities:
                print(item)
        elif choice == "2":
            city_data = {}
            city_name = input("Enter city name: ")
            city_data['name'] = city_name
            city_data['size'] = int(input("Enter city size: "))
            city_data['population'] = int(input("Enter city population: "))
            city_data['military'] = int(input("Enter military strength: "))
            city_data['governor'] = input("Enter governor's name: ")
            city_data['is_capital'] = input("Is this the capital (True/False): ").lower() == "true"
            new_city = City(**city_data)  # Using dictionary unpacking to pass the data to the constructor
            list_of_cities.append(new_city)

        elif choice == "3":
            return ""

        elif choice == "4":
            return""
        elif choice == "5":
            return ""

        elif choice == "6":
            while True:
                print("\nHouses of the Realm!")
                print("0. Go Back") # TBD
                print("1. Show existing Houses") # TBD
                print("2. Add House to City")

                choice = input("Enter your choice: ")

                if choice == "2":
                    specific_city_name = input("To which City would you like to add one or more Houses?\n")
                    found_city = None
                    for city in list_of_cities:
                     if city.name == specific_city_name:
                          found_city = city

                     if found_city:
                          found_city.add_house(found_city)
                    else:
                          print("City not found.")

if __name__ == "__main__":
    main()