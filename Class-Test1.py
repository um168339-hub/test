class product:
    def _init_(self,name,price):
        self.name = name
        self.price = price

class cartitems:
    def _init_(self,product,quantity):
        self.product = product
        self.quantity = quantity
        

    def item_total(self):
        return self.pro.price *self.quantity
    
p1 = product('laptop', 15000)
p2 = product('mouse', 500)
p3 = product('keyboard', 1000)


q1 = cartitems(p1,3)
q2 = cartitems(p2,1)
q3 = cartitems(p3,2)

total_bill = q1.item_total() + q2.item_total() + q3.item_total()
print(total_bill)