first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    command_data = input().split()
    command = command_data[0]
    target_set = command_data[1]
    numbers = set(map(int, command_data[2:]))
    
    if command == "Add":
        if target_set == "First":
            first_sequence.update(numbers)
        elif target_set == "Second":
            second_sequence.update(numbers)
    elif command == "Remove":
        if target_set == "First":
            first_sequence.difference_update(numbers)
        elif target_set == "Second":
            second_sequence.difference_update(numbers)
    elif command == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")
print(", ".join(map(str, sorted(first_sequence))))
print(", ".join(map(str, sorted(second_sequence))))