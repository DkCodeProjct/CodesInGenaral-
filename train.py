while True:
    
    try:
        mass = int(input("enter_mass KG/: "))
    except ValueError:
        pass
    else:

        C_speedOfLight = 300000000

        E_energy = mass * C_speedOfLight ** 2

        formated_energy = (f"{E_energy:_}")
        print(f"calculation[e = mc^2] = {formated_energy}")
    
    calcualtAnother = input("yes/no (y/n)").lower()
    if calcualtAnother == "n":
        break
print("thanks..!")

    
