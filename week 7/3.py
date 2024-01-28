def get_capital(country, country_capitals):
    country = country.lower()
    if country in country_capitals:
        return country_capitals[country]
    else:
        return None


def main():
    country_capitals = {
        "nepal": "Kathmandu",
        "france": "Paris",
        "germany": "Berlin",
        "india": "New Delhi",
        "russia": "Moscow"
    }
    while True:
        country = input("Enter the name of a country (or type 'quit' to terminate): ").strip().lower()

        if country == 'quit':
            print(" The program is terminated.")
            break

        capital_city = get_capital(country, country_capitals)

        if capital_city:
            print(f"The capital city of {country.capitalize()} is {capital_city}.")
        else:
            new_capital = input(f"We don't have information about the capital city of {country.capitalize()}. "
                                f"Please enter it: ").strip()
            country_capitals[country] = new_capital
            print(f"Thank you! The capital city of {country.capitalize()} is now set to {new_capital}.")


if __name__ == "__main__":
    main()
