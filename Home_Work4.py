class Book:
    def __init__(self, namebook, nevisande, ghymat):
        self.namebook = namebook
        self.nevisande = nevisande
        self.ghymat = float(ghymat)

    def display_details(self):
        print("\n--- darbare ketab  ---")
        print(f"name : {self.namebook}")
        print(f"nevisande: {self.nevisande}")
        print(f"ghymat : {self.ghymat:.2f} ")

    def apply_discount(self, takhfif_):
        discount_amount = (takhfif_ / 100) * self.ghymat
        self.ghymat -= discount_amount
        print(f" {takhfif_}  ghymat jadid: {self.ghymat:.2f} ")


name1 = input("name ketab: ")
nevisande1 = input("name nevisande: ")
gheymat1 = input("gheymat : ")

book1 = Book(name1, nevisande1, gheymat1)


book2 = Book("data", "mohammadreza", 150)


book1.display_details()


discount = float(input("% = ? ? ?"))
book2.apply_discount(discount)


book1.display_details()
book2.display_details()