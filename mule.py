class Mule:
    def __init__(self,name,color,max_height,age):
        self.name=name
        self.color=color
        self.max_height=max_height
        self.age=age

    def run(self):
        print('Muls is running')

    def show_info(self):
        print(f'********info*******')
        print(f"Name : {self.name}")
        print(f"Color : {self.color}")
        print(f"Max Height :{self.max_height} kg")
        print(f"Age : {self.age} y")
    
    def __del__(self):
        print(f"Object was destroyed")

    

mule1=Mule("Mumu","Blue-eyed cream",3,200)
mule1.show_info()

mule2=Mule("Meme","Palomino",1,120.7)
mule2.show_info()

        


