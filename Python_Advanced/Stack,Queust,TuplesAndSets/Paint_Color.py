def add_color(first_part, second_part):
    word = first_part + second_part

    if word in all_colors:
        if word not in founded_colors:
            founded_colors.append(word)
        return True
    else:
        return False

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
all_colors = main_colors + secondary_colors
result = []
founded_colors = []

line = input().split()

while line:
    if len(line) == 1:
        line.append('')

    left_substring = line.pop(0)
    right_substring = line.pop()

    if add_color(left_substring, right_substring):
        continue
    elif add_color(right_substring, left_substring):
        continue
    else:
        left_substring = left_substring[:len(left_substring) - 1]
        right_substring = right_substring[:len(right_substring) - 1]
        if right_substring:
            line.insert(len(line)//2, right_substring)
        if left_substring:
            line.insert(len(line)//2, left_substring)

result = []
for color in founded_colors:
    if color not in result:
        if color in main_colors:
            result.append(color)
        else:
            if color == 'orange':
                if ('red' in founded_colors) and ('yellow' in founded_colors):
                    result.append(color)
            elif color == 'purple':
                if 'red' in founded_colors and 'blue' in founded_colors:
                    result.append(color)
            elif color == 'green':
                if 'blue' in founded_colors and 'yellow' in founded_colors:
                    result.append(color)
print(result)