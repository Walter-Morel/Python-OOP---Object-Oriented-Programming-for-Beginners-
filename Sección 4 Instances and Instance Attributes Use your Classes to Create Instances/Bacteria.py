class Bacterium:
    def __init__(self, bacilos, cocci, vidrio, baston, spirilli='Forma de espiral'):
        self.bacilos = bacilos
        self.cocci = cocci
        self.vidrio = vidrio
        self.baston = baston
        self.spirilli = spirilli


bacterias = Bacterium('Tienen forma de varilla', 'Tienen forma de esfera', 'ligeramente curvados y en forma de coma', 'forma de bastoncillo')
print('Los Bacilos:', bacterias.bacilos)
print('Los Cocci:', bacterias.cocci)
print('Los Vidrios', bacterias.vidrio)
print('Los Baston', bacterias.baston)
print('Los Spirilli', bacterias.spirilli)


        