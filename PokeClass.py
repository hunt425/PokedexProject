from PokeTypes import PokeTypes


class Pokemon:

    def __init__(self, number, name, hp, att, defense, spAtt, spDef, speed, type1, type2, pre):
        self.number = number
        self.name = name
        self.hp = hp
        self.att = att
        self.defense = defense
        self.spAtt = spAtt
        self.spDef = spDef
        self.speed = speed
        self.type1 = type1
        self.type2 = type2
        self.pre = pre

    def show(self):  # displays stats and general messages
        print("Pokedex Entry: ")
        print("Pokemon #" + self.number + ": " + self.name)

        if self.type2 == 'None':  # not all pokemon have 2 types.
            print("Pokemon Type: " + self.type1)

        else:
            print("Pokemon Type: " + self.type1 + "/ " + self.type2)

        print()
        print("Stats:")
        print("HP: " + self.hp)

        print("Attack: " + self.att)
        print("Defense: " + self.defense)

        print("Special Attack: " + self.spAtt)
        print("Special Defense: " + self.spDef)

        print("Speed: " + self.speed)

        # adds all stats for total base stat
        total = int(self.hp) + int(self.att) + int(self.defense) + int(self.spAtt) + int(self.spDef) + int(self.speed)

        print("Stat Total = " + str(total) + "\n")

        if self.pre != 'None':
            print("Is the Evolution of: " + self.pre + "\n")

        if total >= 680:
            print("Legendary Pokemon")

        elif total >= 600 and total < 680:
            print("Pseudo Legendary or Mythical Pokemon")

        elif total >= 450 and total < 600:
            print("Good Pokemon to use")

        else:
            print("Either a pre-evolution or bad Pokemon to use")

    def readIn():  # creates list of all pokemon entered in the txt file
        with open("Pokemon.txt") as poke:
            pokemon = ''
            while True:
                insert = poke.read()
                pokemon = pokemon + insert

                if not insert:
                    break

            pokemon = pokemon.split("\n")  # splits at new line

        return pokemon  # returns list

    def PrimWR(primary, secondary):
        weak1 = []
        weak2 = []
        resist1 = []
        resist2 = []
        imm1 = []
        imm2 = []
        veryWeak = []
        VeryRes = []

        if secondary == 'None':
            weak1, resist1, imm1 = Pokemon.FirstWR(primary)
            print("Weaknesses: " + ", ".join(weak1))
            print("Resistances: " + ", ".join(resist1))
            print("Immunities: " + ", ".join(imm1))

        else:
            weak1, resist1, imm1 = Pokemon.FirstWR(primary)
            if resist1[0] == 'None':
                resist1.remove('None')
            if imm1[0] == 'None':
                imm1.remove('None')
            weak2, resist2, imm2 = Pokemon.FirstWR(secondary)

            for i in range(len(weak2)):
                if weak2[i] in weak1:
                    weak1.remove(weak2[i])
                    veryWeak.append(weak2[i])
                elif weak2[i] not in weak1 and weak2[i] not in resist1:
                    weak1.append(weak2[i])
                elif weak2[i] in resist1:
                    resist1.remove(weak2[i])

            for i in range(len(resist2)):
                if resist2[i] in weak1:
                    weak1.remove(resist2[i])
                if resist2[i] in resist1:
                    resist1.remove(resist2[i])
                    VeryRes.append(resist2[i])
                if resist2[i] not in resist1 and resist2[i] not in VeryRes:
                    resist1.append(resist2[i])

            for i in range(len(imm2)):
                if imm2[i] in weak1:
                    weak1.remove(imm2[i])
                if imm2[i] in resist1:
                    resist1.remove(imm2[i])
                if imm2[i] not in imm1:
                    imm1.append(imm2[i])

            print("Weaknesses: " + ", ".join(weak1))
            print("Resistances: " + ", ".join(resist1))
            print("Immunities: " + ", ".join(imm1))
            print("Very Weak to: " + ", ".join(veryWeak))
            print("4x resistant to: " + ", ".join(VeryRes))

    def FirstWR(type):
        weakTo = []
        Resists = []
        Immune = []
        if type == 'Normal':
            weakTo, Resists, Immune = PokeTypes.Normal()
            return weakTo, Resists, Immune

        if type == 'Fire':
            weakTo, Resists, Immune = PokeTypes.Fire()
            return weakTo, Resists, Immune

        if type == 'Water':
            weakTo, Resists, Immune = PokeTypes.Water()
            return weakTo, Resists, Immune

        if type == 'Grass':
            weakTo, Resists, Immune = PokeTypes.Grass()
            return weakTo, Resists, Immune

        if type == 'Electric':
            weakTo, Resists, Immune = PokeTypes.Electric()
            return weakTo, Resists, Immune

        if type == 'Ice':
            weakTo, Resists, Immune = PokeTypes.Ice()
            return weakTo, Resists, Immune

        if type == 'Fighting':
            weakTo, Resists, Immune = PokeTypes.Fighting()
            return weakTo, Resists, Immune

        if type == 'Poison':
            weakTo, Resists, Immune = PokeTypes.Poison()
            return weakTo, Resists, Immune

        if type == 'Ground':
            weakTo, Resists, Immune = PokeTypes.Ground()
            return weakTo, Resists, Immune

        if type == 'Flying':
            weakTo, Resists, Immune = PokeTypes.Flying()
            return weakTo, Resists, Immune

        if type == 'Psychic':
            weakTo, Resists, Immune = PokeTypes.Psychic()
            return weakTo, Resists, Immune

        if type == 'Bug':
            weakTo, Resists, Immune = PokeTypes.Bug()
            return weakTo, Resists, Immune

        if type == 'Rock':
            weakTo, Resists, Immune = PokeTypes.Rock()
            return weakTo, Resists, Immune

        if type == 'Ghost':
            weakTo, Resists, Immune = PokeTypes.Ghost()
            return weakTo, Resists, Immune

        if type == 'Dragon':
            weakTo, Resists, Immune = PokeTypes.Dragon()
            return weakTo, Resists, Immune

        if type == 'Dark':
            weakTo, Resists, Immune = PokeTypes.Dark()
            return weakTo, Resists, Immune

        if type == 'Fairy':
            weakTo, Resists, Immune = PokeTypes.Fairy()
            return weakTo, Resists, Immune

