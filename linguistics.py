def createPhonology(phonology):
    phonology['p'] = Consonant('p', 'bilabial', 'plosive', 'voiceless')
    phonology['t'] = Consonant('t', 'alveolar', 'plosive', 'voiceless')
    phonology['k'] = Consonant('k', 'velar', 'plosive', 'voiceless')
    phonology['b'] = Consonant('b', 'bilabial', 'plosive', 'voiced')
    phonology['d'] = Consonant('d', 'alveolar', 'plosive', 'voiced')
    phonology['g'] = Consonant('g', 'velar', 'plosive', 'voiced')
    phonology['a'] = Vowel('a', 'low', 'central', 'unrounded')
    phonology['i'] = Vowel('i', 'high', 'front', 'unrounded')
    phonology['u'] = Vowel('u', 'high', 'back', 'rounded')


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

    def __init__(self, symbol, height, backness, roundness):
        self.symbol = symbol
        self.height = height
        self.backness = backness
        self.roundness = roundness

        def __repr__(self):
            return self.symbol + ': ' + self.place + ', ' + self.manner + ', ' + self.voicing

        def __str__(self):
            return self.symbol



phonology = {}
createPhonology(phonology)
