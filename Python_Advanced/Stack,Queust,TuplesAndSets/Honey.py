bees = [int(b) for b in input().split(' ')]
nectar = [int(b) for b in input().split(' ')]
symbols = input().split(' ')
total_honey = 0

while bees and nectar and symbols:
    c_bee = bees.pop(0)
    c_nectar = nectar.pop()

    if c_bee <= c_nectar:
        honey_made = 0
        c_symbol = symbols.pop(0)
        if c_symbol == '+':
            honey_made = c_bee + c_nectar
        elif c_symbol == '-':
            honey_made = abs(c_bee - c_nectar)
        elif c_symbol == '*':
            honey_made = c_bee * c_nectar
        elif c_symbol == '/':
            if c_nectar != 0:
                honey_made = c_bee / c_nectar
        total_honey += honey_made
    else:
        bees.insert(0, c_bee)

print(f'Total honey made: {total_honey}')

if bees:
    print('Bees left: ' + ', '.join([str(b) for b in bees]))
if nectar:
    print('Nectar left: ' + ', '.join([str(b) for b in nectar]))