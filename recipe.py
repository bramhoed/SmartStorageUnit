

class Recipe: 
    """
    Class to represent a recipe  loaded from file 
    To keep track of cooking progress

    Attributes:
    ingredients (dict): {name (str) : amount (number) }
    num_persons (int): Number of persons that it feeds
    cooking_time (int): Time to prepare in minutes 
    recipe_text (str): total recipe in text form

    steps (list of dicts): [{ operation (str) : (bool)}]
        operation are used to keep progress and can be one of: 
            - Recipe text
            - cutting
            - splatting
            - cooking
            - frying
            - baking
    cur_step (int): Current step (also index into steps)
    """
    
    def __init__(self, filename):
        """
        Recipe Constructor

        Arguments:
        filename (str): filename of the recipe to be loaded
        """
        self.ingredients = {}
        self.num_persons = 0
        self.cooking_time = 0
        self.recipe_text = 'Cook ALL the things!'
        self.steps = [{}]
        self.cur_step = 0

