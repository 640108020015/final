class JuiceOrder :
    menu_type = "Juice"
    
    def __init__(self,menu:str,size:str,price:int)->None:
        self.menu=menu.upper()
        self.size=size
        self.price=price

    def check_menu(self): 
        menu_dictionary ={
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30 
            }
        if self.menu in menu_dictionary:
           self.price = menu_dictionary.get({self.menu})

    def compute_price(self):
        print(self.size)
        if self.size == 'R':
            self.price = self.price + 0
            self.price +=0
        elif     self.size == 'L':
            self.price = self.price + 5
            self.price +=5
        else: 
            self.price
        JuiceOrder.total = self.price*self.menu


    def display_order(self): 
        return (f'รายการที่ 1 :{self.menu} ({self.size} 0=> {self.price} baht')
    
    def __del__(self):
        print('Object was dwstroyed') 
order1=JuiceOrder('WJ','L')
order2=JuiceOrder('OJ','R')
order3=JuiceOrder('PJ','L')


order1.check_menu()
order1.compute_price()
print(order1.display_order())


order2.check_menu()
order2.compute_price()
print(order2.display_order())

order3.check_menu()
order3.compute_price()
print(order3.display_order())






