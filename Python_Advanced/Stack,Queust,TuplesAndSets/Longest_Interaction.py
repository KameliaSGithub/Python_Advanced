def get_range_set(range_str):
    start, end = map(int, range_str.split(','))
    return set(range(start, end + 1))
n = int(input())
longest_intersection = set()
for _ in range(n):
    first_range, second_range = input().split('-')
    first_set = get_range_set(first_range)
    second_set = get_range_set(second_range)

    intersection = first_set & second_set
    
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f"Longest intersection is [{', '.join(map(str, sorted(longest_intersection)))}] with length {len(longest_intersection)}")