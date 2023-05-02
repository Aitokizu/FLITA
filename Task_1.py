print("Enter the first set:")
set1 = {input()}
print("Enter the second set:")
set2 = {input()}
while True:
    print("Menu")
    print("Press 1 to add elements")
    print("Press 2 to remove elements")
    print("Press 3 to print sets")
    print("Press 0 to reset sets")
    print("Press 4 to exit")
    command = input()
    match command:
        case "1":
            print("To which set:")
            set = input()
            print("What element:")
            elem = input()
            if set=="1":
                set1.add(elem)
            elif set=="2":
                set2.add(elem)
            else:
                print("Such set doesn't exist")
                break
        case "2":
            print("To which set:")
            set = input()
            print("What element:")
            elem = input()
            if set == "1" and elem in set1:
                set1.remove(elem)
            elif set == "2" and elem in set2:
                set2.remove(elem)
            else:
                if set!="1" or set!="2":
                    print("Such set doesn't exist")
                elif elem not in set1 or elem not in set2:
                    print("No such element in set")
                break
        case "3":
            print(set1, set2)
        case "0":
            print("Warning! You will lose all elements. Which set:")
            set = input()
            if set == "1":
                set1.clear()
            elif set == "2":
                set2.clear()
            else:
                print("Such set doesn't exist")
                break
        case "4":
            print("You exited the menu")
            quit()
        case _:
            print('Command not recognized')
