class car (object):
    def __init__ (self, make, model, year, condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    def display(self, showAll):
        if showAll:
            print(f"This car is a {self.make} {self.model} from {self.year}, it is {self.condition} and has {self.kms} kms")
        else:
            print(f"this car is a {self.make} {self.model} from {self.year}")

whip = car("Ford", "Fusion", 2012, "new", 0)
whip.display(True) 