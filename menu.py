'''
class menu
'''
class menu:
    name = []
    price = []
    def add(self,name,price=[]):
        '''
        ARGS:
        name = item_name
        price = item_price
        '''
        if name not in self.name:
            self.name.append(name)
            self.price.append(price)
    def show(self):
        for i in range(len(self.name)):
            print(self.name[i],self.price[i])
#instance of class menu
c = menu()

'''
adds items and price to list
c.add('item_name','item_price')

'''
c.add('idli',20)
c.add('sambhar',10)
c.show()                 
