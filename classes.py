from operator import index


class car:

    def __init__(self,model,color,price,):
        self.model = model
        self.color = color
        self.price = price
class bus:
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price
class students:

    def __init__(sneh,attandance,name,major):
        sneh.attandance = attandance
        sneh.name = name
        sneh.major = major
    def should_call_parents(sneh):
        if sneh.attandance >= 75:
            return False
        else:
            return True
def implement():
    c1 = car("civic","blue",456636)
    print(c1.model)
    print(c1.color)
    print(c1.price)
    b1  = bus("tata","yellow",3463767)
    print(b1.model)
    print(b1.color)
    print(b1.price)
nums = [1,2,3,4]
nums = [5]+nums
print(nums)
index()
