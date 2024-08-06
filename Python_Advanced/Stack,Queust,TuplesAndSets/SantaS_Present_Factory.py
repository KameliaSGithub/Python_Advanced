materials = [int(m) for m in input().split(' ')]
magics = [int(m) for m in input().split(' ')]
gifts = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_presents = {}
while materials and magics:
    material = materials.pop()
    c_magic = magics.pop(0)
    if material == 0 or c_magic == 0:
        if material != 0:
            materials.append(material)
        if c_magic != 0:
            magics.insert(0, c_magic)
    else:
        magic_level = c_magic * material

        if magic_level < 0:
            materials.append(material + c_magic)
        elif magic_level > 0:
            if magic_level in gifts:
                c_present = gifts[magic_level]
                if c_present in crafted_presents:
                    crafted_presents[c_present] += 1
                else:
                    crafted_presents[c_present] = 1
            else:
                material += 15
                materials.append(material)

is_pair_one = 'Doll' in crafted_presents and 'Wooden train' in crafted_presents
is_pair_two = 'Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents

if  is_pair_one or is_pair_two :
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if magics:
    magic_left = [str(m) for m in magics[::-1]]
    print(f'Magic left: {", ".join(magic_left)}')
if materials:
    material_left = [str(m) for m in materials[::-1]]

    print(f'Materials left: {", ".join(material_left)}')

crafted_presents = dict(sorted(crafted_presents.items(), key=lambda kvp: kvp[0]))
for toy_name, toy_count in crafted_presents.items():
    
    print(f'{toy_name}: {toy_count}')