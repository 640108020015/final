class House:

    def __init__(self,name:str,color:str,max_height:int):
        self.name=name
        self.color=color
        self.max_height=max_height 

    def run(self):
        print('Khan Khan is running')
    def show_name(self):
        print('Name : Khan Khan')
    def show_info(self):
            print(f"Name : {self.name}")
            print(f"Colour : {self.color}")
            print(f"Name : {self.name}")
            print(f"Max Height :{self.max_height} kg")


    def __del__(self):
        print(f"Object was destroyed")
my_house=House("Khan Khan",'Gray',200)
my_house.run()
my_house.show_name()
my_house.show_info()









