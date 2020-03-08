
class EventHandler:
    """
    Wrapper class for the event handlers. 

    Attributes:
    user_cutting (bool): Wether or not the user is cutting

    
    """

    def __init__(self, _global_state):
        self.global_state = _global_state
        self.user_cutting = False

    def onCuttingVolume(self, sender, event):

        if ((int(event['volume']) > 0) and (not self.user_cutting)):

            print('User is cutting something!')
            self.user_cutting = True

        elif((int(event['volume']) <= 0) and (self.user_cutting)):

            print('User stopped cutting something!')
            self.user_cutting = False

    def onSoundSpectrum(self, sender, event):
        print('Sound Spectrum event!')

    def onBoardWeight(self, sender, event):
        print('Board Weight event!')

    def onCuttingSpeed(self, sender, event):
        print('Cutting Speed event!')
