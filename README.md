# Star Wars API

## Overall Goal
Interact with the [Star Wars API](https://swapi.dev/) by making requests and manipulating responses using Python

## Cloning the Repo

Clone this repository using `git clone`. This will create a folder in your current directory called `star-wars-api`. `cd` into that folder to edit the code.

## How to Run the Code

You can run the app by running the command

```bash
python app.py
```

## Steps
The code skeleton exists in app.py. Modify it to do the following:
1. Write a function that accepts an id to make a GET request to the /people endpoint. This function should return the person response.
2. Write a function that makes a GET request to get that person's homeworld. The endpoint for the person's homeworld can be found in the GET /people response.
3. Return the name of the person's homeworld to be printed
4. Create a dataframe with the column names "Name", "Height", "Mass", "BMI", and "Birth Year".
5. Write a function that uses the homeworld response to do the following:
- Loop through the `residents`, calling each endpoint, and getting the person's name, height, mass, and birth year.
- Store those fields as values in a dataframe.
- Note that BMI is still missing, so it must be calculated. BMI is found as ((height/100)/mass). Add the value to each person's record.
6. In the end, print the planet name, followed by the resident dataframe. The final result should look like this, using person "1" as an example: 

```
Tatooine

Residents:
```

| Name | Height | Mass | BMI | Birth Year |
|------|--------|------|-----|------------|
|   Luke Skywalker  |    172    |   77   |  0.02   |     19BBY       |
| ...  |   ...  |  ... | ... |     ...    |


