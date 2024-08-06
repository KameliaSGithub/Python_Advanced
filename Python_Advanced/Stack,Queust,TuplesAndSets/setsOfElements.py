n, m = map(int, input().split())
list1 = []
list2 = []
for _ in range(n):
    list1.append(int(input()))
for _ in range(m):
    list2.append(int(input()))
common_elements = []
for element in list1:
    if element in list2 and element not in common_elements:
        common_elements.append(element)
for element in common_elements:
    print(element)