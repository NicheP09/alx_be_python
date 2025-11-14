pattern_size = int(input("Enter the size of the pattern: "))
i = 1
j = 1
while i <= pattern_size:
    for j in range(1, pattern_size + 1):
        print("*", end="")
        j = j - 1

    print()
    i += 1
