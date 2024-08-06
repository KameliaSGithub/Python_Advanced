N = int(input())
unique_usernames = set()
for _ in range(N):
    username = input().strip()  
    unique_usernames.add(username)
for username in unique_usernames:
    print(username)