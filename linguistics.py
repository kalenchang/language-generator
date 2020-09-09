class Linguistics:

    def __init__(self):
        self.phonology = {}
        self.createPhonology()

    def createPhonology(self):
        self.phonology["p"] = Consonant("p", "bilabial", "plosive", "voiceless")
        self.phonology["t"] = Consonant("t", "alveolar", "plosive", "voiceless")
        self.phonology["k"] = Consonant("k", "velar", "plosive", "voiceless")
        self.phonology["b"] = Consonant("b", "bilabial", "plosive", "voiced")
        self.phonology["d"] = Consonant("d", "alveolar", "plosive", "voiced")
        self.phonology["g"] = Consonant("g", "velar", "plosive", "voiced")


class Consonant:

    def __init__(self, symbol, place, manner, voicing):
        self.symbol = symbol
        self.place = place
        self.manner = manner
        self.voicing = voicing

    def __repr__(self):
        return self.symbol + ': ' + self.place + ', ' + self.manner + ', ' + self.voicing

    def __str__(self):
        return self.symbol


class Vowel:

    def __init__(self, symbol, height, backness, tenseness):
        self.symbol = symbol
        self.height = height
        self.backness = backness
        self.tenseness = tenseness
