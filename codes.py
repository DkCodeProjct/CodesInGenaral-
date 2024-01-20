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
while True:
    found = False
    user = input('Add To Cart: ').title()
    

    for food   in menu:
        if food['food'] or 'q' == user:
            print(food['price'])
            total += food['price']
            found = True
            break
    if not found:
        print("invalidINout")
    if user == 'Q':
        break
print(f'Total cost: ${total:.2f}')
print("Thank You Come Again")        