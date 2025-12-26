

number = int(input("tedad dars ro vared konid: "))

list_dros = []

while number > 0:
    dros = int(input(f"dars {number} = "))
    list_dros.append(dros)
    number -= 1

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

avg = calculate_average(list_dros)
print("moadele shoma =", avg)
