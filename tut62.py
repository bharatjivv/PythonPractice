# Multi-level Inheritence
class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times "

class Grandson(Son):
    dance = 6
    # def isdance(self):
        # return f"Jackson Yeah!" \
        # f"Yeas I dance very awesomly {self.dance} no of times "

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.basketball)