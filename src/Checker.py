from src.Environment import Environment


class Checker:
    def __init__(self):
        self.env = Environment()
    
    def reminder(self, file):
        time = self.env.getTime()
        if time > 17 and self.env.wavWasPlayed(file) is False:
            self.env.playWavFile(file)
        else:
            self.env.resetWav(file)
