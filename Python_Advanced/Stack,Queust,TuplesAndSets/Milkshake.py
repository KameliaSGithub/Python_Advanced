chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = [int(x) for x in input().split(', ')]
milkshakes = 0

while chocolates and cups_of_milk:
    c_chocolate = chocolates.pop()
    if c_chocolate <= 0:
        continue

    c_cup = cups_of_milk.pop(0)
    if c_cup <= 0:
        chocolates.append(c_chocolate)
        continue

    if c_cup == c_chocolate:
        milkshakes += 1
    else:
        c_chocolate -= 5
        if c_chocolate > 0:
            chocolates.append(c_chocolate)
        else:
            chocolates.append(0)
        cups_of_milk.append(c_cup)

    if milkshakes == 5:
        break

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

result = ', '.join([str(x) for x in chocolates]) if chocolates else 'empty'
print(f'Chocolate: {result}')

result = ', '.join([str(x) for x in cups_of_milk]) if cups_of_milk else 'empty'
print(f'Milk: {result}')