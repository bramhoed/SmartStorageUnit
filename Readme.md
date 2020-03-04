# Smart Storage unit

Storage unit too smart for its own good..

# Software architecture

Multiple threads:

1. Main thread
  * Keeps track of the general state of the system and sensors
  * Handles the OOCSI networking and communication
1. The pressure sensor thread
  * Constantly polls the pressure sensor for a change in weight
  * If a weight change is detected it calls the `pressureHasChanged()` function in the main thread
1. The camera / barcode reader thread
  * Keeps track of the camera and calls its `yoBarcodeWasScanned()` function in main
