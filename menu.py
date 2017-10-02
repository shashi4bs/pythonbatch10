class menu:
    name = []
    price = []
    def add(self,name,price=[]):
        self.name.append(name)
        self.price.append(price)
    def show(self):
        for i in range(len(self.name)):
            print(self.name[i],self.price[i])
c = menu()
c.add('idli',20)
c.add('sambhar',10)
c.show()                 
