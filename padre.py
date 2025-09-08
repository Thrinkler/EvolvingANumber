from random import randint
class Padre:
    probPasar = 0 
    def __init__(self,limiteMayor):
        self.val = randint(1, limiteMayor)
