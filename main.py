# Hunter Tysdal


from PokeClass import Pokemon

pokeList = Pokemon.readIn()
# newList = pokeList.split("/n")
# print(pokeList)
print()
# print(pokeList[1])


finList = []

counter = True

for i in range(len(pokeList)):
    newList = pokeList[i].split(" ")
    # print(newList)
    finList.append(newList)

print("Welcome to the Generation 8 Pokedex! \n")
# print(finList)
choice = ''
while choice != 'n':
    desiredMon = []

    print("-" * 45)
    print()
    choice = input("Would you like to search by Pokemon Name or Number? Or press Q to quit -> ")

    if choice.lower() == 'name':
        print("Finding by name... \n")
        pokeName = input("Which Pokemon name? \n")

        for i in range(len(finList)):
            # print(finList[i][1]
            if pokeName.title() == finList[i][1]:
                print("Found Pokemon! \n")
                print("Finding Stats... \n")
                desiredMon.append(finList[i])

                # print(desiredMon)
                break







            elif i == (len(finList) - 1) and finList[i][1] != pokeName.lower():
                print("Pokemon not found, maybe double check the spelling. \nTry again")
                counter = False

        if counter == False:
            continue
        else:
            num = desiredMon[0][0]
            PokeName = desiredMon[0][1]
            health = desiredMon[0][2]
            attack = desiredMon[0][3]
            defense = desiredMon[0][4]
            specAtt = desiredMon[0][5]
            specDef = desiredMon[0][6]
            Speed = desiredMon[0][7]
            primary = desiredMon[0][8]
            secondary = desiredMon[0][9]
            prevolution = desiredMon[0][10]

            desiredPoke = Pokemon(num, PokeName, health, attack, defense, specAtt, specDef, Speed, primary, secondary,
                                  prevolution)
            desiredPoke.show()

            # (self, number, name, hp, att, defense, spAtt, spDef, speed, type1, type2, pre)

        Pokemon.PrimWR(primary, secondary)






    elif choice.lower() == 'number':
        print("Finding by number... \n")
        pokeNum = input("Which Pokemon number would you like to search for (national Pokedex)? \n")

        for i in range(len(finList)):
            # print(finList[i][1]
            if pokeNum == finList[i][0]:
                print("Found Pokemon! \n")
                print("Finding Stats... \n")
                desiredMon.append(finList[i])

                # print(desiredMon)
                break




            elif i == (len(finList) - 1) and finList[i][0] != pokeNum:
                print("Pokemon not found, try again")
                counter = False

        if counter == False:
            continue
        else:
            num = desiredMon[0][0]
            PokeName = desiredMon[0][1]
            health = desiredMon[0][2]
            attack = desiredMon[0][3]
            defense = desiredMon[0][4]
            specAtt = desiredMon[0][5]
            specDef = desiredMon[0][6]
            Speed = desiredMon[0][7]
            primary = desiredMon[0][8]
            secondary = desiredMon[0][9]
            prevolution = desiredMon[0][10]

            desiredPoke = Pokemon(num, PokeName, health, attack, defense, specAtt, specDef, Speed, primary, secondary,
                                  prevolution)
            desiredPoke.show()

            Pokemon.PrimWR(primary, secondary)


    elif choice.lower() == 'q':
        print("Thank you!")
        break

    else:
        print("That is not an option, try again")
        continue