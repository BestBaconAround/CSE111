"""def main():
    odometer = int(input("Enter the odometer: "))
    second_odometer = int(input("Enter the odometer after fill up: "))
    fuel_amount = float(input("How many gallons of fuel: "))

    mpg = miles_per_gallon(odometer, second_odometer, fuel_amount)
    lp100k = lp100k_from_mpg(mpg)

    print(f"MPG: {mpg:.2f}")
    print(f"LP100k: {lp100k:.2f}")
def miles_per_gallon(start, end, gallons):
    miles_driven = end - start
    mpg = miles_driven / gallons
    return mpg
def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

main()"""
"""
def main():
    #Gets the mileage before, after, and how much gas is used. Then prints MPG
    current_odometer = int(input("Current milage before fillup: "))
    after_fill_odometer = int(input("After fillup milage: "))
    fuel_gallons = float(input("How many gallons?: "))
    mpg = miles_per_gallon(current_odometer, after_fill_odometer, fuel_gallons)
    print(f"Your MPG {mpg}")
def miles_per_gallon(current_odometer, after_fill_odometer, fuel_gallons):
    #calculates the MPG
    mileage_driven = after_fill_odometer - current_odometer
    mpg = mileage_driven / fuel_gallons
    return mpg
main()"""
def fullname(w1,w2):
    return w1 + ' ' + w2
f=fullname(w2='faith', w1='charity')
print(f)