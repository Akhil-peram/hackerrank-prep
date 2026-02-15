n = int(input(""))
phoneBook = {}
for i in range(n):
    name, number = input().strip().split()
    phoneBook[name] = number

while True:
    try:
        query = input()
        if query in phoneBook:
            print(query + "=" + phoneBook[query])
        else:
            print("Not found")
    except EOFError:
        break
