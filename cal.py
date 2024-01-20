def main():
    menu = [
        {"food": "Baja Taco", "price": 4.00},
        {"food": "Burrito", "price": 7.50},
        {"food": "Bowl", "price": 8.50},
        {"food": "Nachos", "price": 11.00},
        {"food": "Quesadilla", "price": 8.50},
        {"food": "Super Burrito", "price": 8.50},
        {"food": "Super Quesadilla", "price": 9.50},
        {"food": "Taco", "price": 3.00},
        {"food": "Tortilla Salad", "price": 8.00}
    ]
    
    total = 0
    print('~~ PRESS; `Q` to Quit ~~')
    print('~~ PRESS `D` for Disocunt')
    while True:
        found = False
        user = validInput('Add To Cart: ').title()
        

        for food   in menu:
            if food['food'] or 'q' or 'd' == user:
                print(food['price'])
                total += food['price']
                found = True
                break
        if not found:
            print("invalidINout")
        if user == 'D':
            disCount = int(input('-Discount- '))
            dis = total - disCount
            print(f"Total:{total}\nDiscount: {total}-{disCount} = {dis}")
            break
        if user == 'Q':
            print(f'Total cost: ${total:.2f}')
            print("Thank You Come Again")
            break 

def validInput(propmt):
    while True:
        try:
            user = input(propmt)
            if user.isalpha():
                return user
            else:
                pass
        except ValueError:
            pass       

if __name__ == "__main__":
    main()