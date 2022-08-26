def func(number):
    """
    if and loop statements dont have (), instead you use tabs. You can concattenate as many tabs as you want
    """

    if number < 5:
        print("smaller than five")


    elif number >= 6:
        print("bigger equal six") 

        for x in range(5):
            print(x)



class Duck:
    """
    Define classes with the 'class' keyword. Each class needs a constructor function, it is always called '__init__(self)' and needs 'self' as parameter. Each class attribut starts with self.attribut_name.
    """
    def __init__(self, legs):
        self.legs = legs
        self.eyes = 2

    def show_what_you_have(self):
        print("I have " + str(self.legs) + " legs and " + str(self.eyes) + " eyes")
        # better:
        print(f'I have {self.legs} legs and {self.eyes} eyes')




duck = Duck(8)
duck.show_what_you_have()

func(7)