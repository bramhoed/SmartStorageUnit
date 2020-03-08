# Smart Storage unit

Storage unit too smart for its own good..
Connects to SmartCuttingBoard over the OOCSI network and keeps track of the progress in a recipe.

# Software architecture

Multiple threads:

1. Main thread
  * Keeps track of the general state of the system, sensors and recipe
  * Handles the OOCSI networking and communication
1. The pressure sensor thread
  * Constantly polls the pressure sensor for a change in weight
  * If a weight change is detected it calls the `pressureHasChanged()` function in the main thread
1. The camera / barcode reader thread
  * Keeps track of the camera and calls its `yoBarcodeWasScanned()` function in main

# Recipes

Recipes are saved in json format and loaded in `Recipe` class, see `example_recipe.json` and `recipe.py`.Sensor data from SmartCuttingBoard (and possibly other things) is interpreted to keep track of the current step in the recipe.

