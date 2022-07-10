class Donkey:
    def __init__(self,age,weight):
        self.age=age
        self.weight=weight
    def sound(self):
        print('Donkey makes eeyore sound')
    def show_info(self):
        print(f"Age : {self.age} y")
        print(f"Weight : {self.weight} kg")
my_donkey=Donkey(2,100)
my_donkey.show_info()
my_donkey.sound()