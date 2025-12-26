class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"berand {self.brand}, sal sakht {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"tadad dar  {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        if self.has_sidecar == 1:
            print("no")
        elif self.has_sidecar == 2:
            print("yes")
        else:
            print("esh tebah")


v = Vehicle("Toyota", 2020)
c = Car("BMW", 2022, 4)
m = Motorcycle("Honda", 2021, 1) 

print("darbare Vehicle:")
v.display_info()

print("\ndarbare Car:")
c.display_info()

print("\ndarbare Motorcycle:")
m.display_info()
#  ببخشید توی فایل های قبلی اسم متغییر هارو هرچ دوست داشتم میزاشم