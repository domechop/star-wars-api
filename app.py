import requests
import pandas as pd
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#Write a function that accepts an id to make a GET request to the /people endpoint. This function should return the person response.
#Write a function that makes a GET request to get that person's homeworld. The endpoint for the person's homeworld can be found in the GET /people response.
#Return the name of the person's homeworld to be printed
def retrieve_person(id: int):
    """
    Function to GET a person from the Star Wars API by their ID.

    Args:
    -----
    id (int): The ID of the person to retrieve.

    Returns:
    -----
    person (dict): The response containing information about the person.
    homeworld_name (str): The name of the person's homeworld.
    """
    url = f"https://swapi.dev/api/people/{id}/"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    person = response.json()
    
    # Get the person's homeworld
    homeworld_url = person['homeworld']
    homeworld_response = requests.get(homeworld_url, verify=False)
    homeworld_response.raise_for_status()
    homeworld_name = homeworld_response.json()['name']
    
    return person, homeworld_name


#Create a dataframe with the column names "Name", "Height", "Mass", "BMI", and "Birth Year".
def dataframe():
    """
    Create a DataFrame with the column names "Name", "Height", "Mass", "BMI", and "Birth Year".
    """

    data = {
        "Name": [],
        "Height": [],
        "Mass": [],
        "Birth Year": [],
    }

    # Retrieve person data
    person_id = 1  # Change the ID to whatever you want
    person, _ = retrieve_person(person_id)
    if person:
        data["Name"].append(person['name'])
        data["Height"].append(int(person['height']))
        data["Mass"].append(int(person['mass']))
        data["Birth Year"].append(str(person['birth_year']))

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Calculate BMI
    df["BMI"] = ((df["Height"]/100) / (df["Mass"])).round(2)

    return df

#Write a function that uses the homeworld response to do the following:
#Loop through the residents, calling each endpoint, and getting the person's name, height, mass, and birth year.
#Store those fields as values in a dataframe.
#Note that BMI is still missing, so it must be calculated. BMI is found as ((height/100)/mass). Add the value to each person's record.
#In the end, print the planet name, followed by the resident dataframe.
def retrieve_residents(planet_url):
    """
    Function to retrieve information about residents of a planet.

    Args:
    -----
    planet_url (str): The URL of the planet's API endpoint.

    Returns:
    -----
    DataFrame: A DataFrame containing information about the residents of the planet.
    """
    residents = []
    planet_response = requests.get(planet_url, verify=False)
    planet_data = planet_response.json()

    if "residents" in planet_data:
        for resident_url in planet_data["residents"]:
            resident_response = requests.get(resident_url, verify=False)
            resident_data = resident_response.json()

            if resident_response.status_code == 200:
                # Extract fields
                name = resident_data["name"]
                height_str = resident_data["height"]
                mass_str = resident_data["mass"]
                birth_year = resident_data["birth_year"]

                # Convert height from string to int
                if height_str.lower() != "unknown":
                    height = int(height_str)
                else:
                    height = None

                # Convert mass from string to float
                if mass_str.lower() != "unknown":
                    mass = float(mass_str)  # Convert mass string to float
                else:
                    mass = None

                # Calculate BMI if both height and mass are available
                if height is not None and mass is not None:
                    bmi = round(((height / 100) / mass), 2)  # BMI calculation results in a float
                else:
                    bmi = None

                residents.append({"Name": name, "Height": height, "Mass": mass, "BMI": bmi, "Birth Year": birth_year})

    df = pd.DataFrame(residents)

    return df

def retrieve_planets():
    """
    Function to retrieve a list of planets and their URLs from the Star Wars API.

    Returns:
    -----
    List: A list of dictionaries containing planet names and URLs.
    """
    planets_url = "https://swapi.dev/api/planets/"
    response = requests.get(planets_url, verify=False)
    response.raise_for_status()
    planets_data = response.json()["results"]

    # Extract planet names and URLs
    planets = [{"name": planet["name"], "url": planet["url"]} for planet in planets_data]

    return planets

def main():
    planets = retrieve_planets()

    for planet in planets:
        print(f"Planet: {planet['name']}")
        planet_url = planet['url']
        resident_df = retrieve_residents(planet_url)
        print("Residents:")
        print(resident_df)
        print("=" * 50)

if __name__ == "__main__":
    main()


def handler():
    """
    This is your "handler" or "controller" function. It is responsible for calling all other functions.
    """

    df = dataframe()

    df = df[["Name", "Height", "Mass", "BMI", "Birth Year"]]

    print(df)


    person_id = 1  
    person, homeworld_name = retrieve_person(person_id)
    if person:
        print(f"Person: {person['name']}")
        if homeworld_name:
            print(f"Homeworld: {homeworld_name}")
        else:
            print("Homeworld not found")
    else:
        print("Person not found")


if __name__ == "__main__":
    """
    This is the entrypoint to your code. 

    How to run
    ------
    In the current directory, run `python app.py`. 
    This will call the below handler() function
    """
    handler()
