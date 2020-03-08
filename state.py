from recipe import Recipe

class StorageUnitState:
    """
    Class to represent the global state of the storage unit

    Attributes:

    oocsi (OOCSI): the oocsi network handle
    items (dict): Items currently stored in the unit with amounts
    curr_recipe (Recipe): The active recipe
    """
    
    def __init__(self, _oocsi):
        self.oocsi = _oocsi
        self.items = 0
        self.curr_recipe = Recipe('example_recipe.json')

        
