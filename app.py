import requests


def example_function_1(noun: str):
    """
    Function for demo purposes that accepts a noun and adds it to a greeting.

    Args
    -----
    noun (str): the thing that we'll say hello to

    Returns
    -----
    sentence (str): The full greeting or None

    NOTE: This function can be deleted.
    """
    if type(noun) == str:
        sentence = "Hello {}".format(noun)
    else:
        sentence = None

    return sentence

# def retrieve_person(id:int):
# This is the function that will GET a person from the Star Wars API.
# Create other functions after this pattern.


def handler():
    """
    This is your "handler" or "controller" function. It is responsible for calling all other functions.
    """
    sentence = example_function_1("world")
    print(sentence)

    # retrieve_person(1)
    # continue calling other functions here


if __name__ == "__main__":
    """
    This is the entrypoint to your code. 

    How to run
    ------
    In the current directory, run `python app.py`. 
    This will call the below handler() function
    """
    handler()
