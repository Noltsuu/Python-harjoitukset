kuhamitta = float(input("kuinka pitkä kuha on: "))
a = 37
while True:
    if kuhamitta > 37:
        print("kuha on tarpeeks pitkä")
        break
    else:
        tarvitavapituus = a -kuhamitta
        print(f"laske kuha takaisin järveen! \ntarvitavapituus {tarvitavapituus}!")
        break