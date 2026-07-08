if __name__ == '__main__':

    n = int(input())       # Number of commands
    lst = []               # Initialize empty list

    for _ in range(n):
        command = input().split()

        if command[0] == "insert":
            index = int(command[1])
            value = int(command[2])
            lst.insert(index, value)

        elif command[0] == "print":
            print(lst)

        elif command[0] == "remove":
            value = int(command[1])
            lst.remove(value)

        elif command[0] == "append":
            value = int(command[1])
            lst.append(value)

        elif command[0] == "sort":
            lst.sort()

        elif command[0] == "pop":
            lst.pop()

        elif command[0] == "reverse":
            lst.reverse()
