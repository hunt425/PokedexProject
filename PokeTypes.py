class PokeTypes:
    def Normal():
        normalWeak = ['Fighting']
        normalRes = ['None']
        normalImm = ['Ghost']
        return normalWeak, normalRes, normalImm

    def Fire():
        FireWeak = ['Water', 'Ground', 'Rock']
        FireRes = ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy']
        FireImm = ['None']
        return FireWeak, FireRes, FireImm

    def Water():
        WaterWeak = ['Grass', 'Electric']
        WaterRes = ['Fire', 'Water', 'Ice', 'Steel']
        WaterImm = ['None']
        return WaterWeak, WaterRes, WaterImm

    def Grass():
        GrassWeak = ['Fire', 'Ice', 'Poison', 'Flying', 'Bug']
        GrassRes = ['Water', 'Grass', 'Electric', 'Ground']
        GrassImm = ['None']
        return GrassWeak, GrassRes, GrassImm

    def Electric():
        ElectricWeak = ['Ground']
        ElectricRes = ['Electric', 'Flying', 'Steel']
        ElectricImm = ['None']
        return ElectricWeak, ElectricRes, ElectricImm

    def Ice():
        IceWeak = ['Fire', 'Fighting', 'Rock', 'Steel']
        IceRes = ['Ice']
        IceImm = ['None']
        return IceWeak, IceRes, IceImm

    def Fighting():
        FightingWeak = ['Flying', 'Psychic', 'Fairy']
        FightingRes = ['Bug', 'Rock', 'Dark']
        FightingImm = ['None']
        return FightingWeak, FightingRes, FightingImm

    def Poison():
        PoisonWeak = ['Ground', 'Psychic']
        PoisonRes = ['Grass', 'Fighting', 'Poison', 'Bug', 'Fairy']
        PoisonImm = ['None']
        return PoisonWeak, PoisonRes, PoisonImm

    def Ground():
        GroundWeak = ['Grass', 'Water', 'Ice']
        GroundRes = ['Poison', 'Rock']
        GroundImm = ['Electric']
        return GroundWeak, GroundRes, GroundImm

    def Flying():
        FlyingWeak = ['Electric', 'Ice', 'Rock']
        FlyingRes = ['Grass', 'Fighting', 'Bug']
        FlyingImm = ['Ground']
        return FlyingWeak, FlyingRes, FlyingImm

    def Psychic():
        PsychicWeak = ['Bug', 'Ghost', 'Dark']
        PsychicRes = ['Fighting', 'Psychic']
        PsychicImm = ['None']
        return PsychicWeak, PsychicRes, PsychicImm

    def Bug():
        BugWeak = ['Fire', 'Flying', 'Rock']
        BugRes = ['Grass', 'Fighting', 'Ground']
        BugImm = ['None']
        return BugWeak, BugRes, BugImm

    def Rock():
        RockWeak = ['Water', 'Grass', 'Fighting', 'Ground', 'Steel']
        RockRes = ['Normal', 'Fire', 'Poison', 'FLying']
        RockImm = ['None']
        return RockWeak, RockRes, RockImm

    def Ghost():
        GhostWeak = ['Ghost', 'Dark']
        GhostRes = ['Poison', 'Bug']
        GhostImm = ['Normal', 'Fighting']
        return GhostWeak, GhostRes, GhostImm

    def Dragon():
        DragonWeak = ['Ice', 'Dragon', 'Fairy']
        DragonRes = ['Fire', 'Water', 'Grass', 'Electric']
        DragonImm = ['None']
        return DragonWeak, DragonRes, DragonImm

    def Dark():
        DarkWeak = ['Fighting', 'Bug', 'Fairy']
        DarkRest = ['Ghost', 'Dark']
        DarkImm = ['Psychic']
        return DarkWeak, DarkRes, DarkImm

    def Steel():
        SteelWeak = ['Fire', 'Fighting', 'Ground']
        SteelRes = ['Normal', 'Grass', 'Ice', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy']
        SteelImm = ['Poison']
        return SteelWeak, SteelRes, SteelImm

    def Fairy():
        FairyWeak = ['Poison', 'Steel']
        FairyRes = ['Fighting', 'Bug', 'Dark']
        FairyImm = ['Dragon']
        return FairyWeak, FairyRes, FairyImm