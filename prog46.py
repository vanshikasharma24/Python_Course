
class Dad:
    basketball=1

class Son(Dad):
    dance=6
    def isdance(self):
        print(f"Yes I dance {self.dance} no of times")
class Grandson(Son):
    guitar=1
    # dance=5
    def isdance(self):
        print(f"Jackson yeah!Yes I dance very awesomely {self.guitar} no of times")
harry=Dad()
larry=Son()
marry=Grandson()
marry.isdance()
print(marry.dance)
