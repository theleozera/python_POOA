# versao 1 ---------------------------------------------------------------
class Humano:
    # atributo da classe(estatico)
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome


    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'

jose = Humano('jose')
grokn = Humano('grokn')
grokn.das_cavernas

print(f'Humano.especia {Humano.especie}')
print(f'jose e {jose.especie}')
print(f'grokn e {grokn.especie}')

# versao 2 -----------------------------------------------
class Humano:
    # atributo da classe(estatico)
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome


    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens' ) 
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]
    

    
jose = Humano('jose')
grokn = Humano('grokn')
print(f'evolucao {"".join(HomoSapiens.especies())}')
grokn.das_cavernas

print(f'Humano.especia {Humano.especie}')
print(f'jose e {jose.especie}')
print(f'grokn e {grokn.especie}')