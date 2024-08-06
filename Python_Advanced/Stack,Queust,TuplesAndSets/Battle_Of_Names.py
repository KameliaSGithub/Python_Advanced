n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(char) for char in name)
    result = ascii_sum 
    
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    result_set = odd_set.union(even_set)
elif sum_odd > sum_even:
    result_set = odd_set.difference(even_set)
else:
    result_set = odd_set.symmetric_difference(even_set)

print(", ".join(map(str, result_set)))