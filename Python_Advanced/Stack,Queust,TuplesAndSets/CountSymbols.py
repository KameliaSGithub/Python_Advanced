text = input()
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
sorted_chars = sorted(char_count.keys())
for char in sorted_chars:
    print(f"{char}: {char_count[char]} time/s")