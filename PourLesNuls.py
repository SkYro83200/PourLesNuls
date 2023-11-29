from random import choice

class perle:
    def __init__(self,couleur, suivant=None):
        self.suiv = suivant
        self.couleur = couleur

    def __repr__(self):
        return str(self.couleur)

class file:
    def __init__(self):
        self.tete = None

    def enfiler(self, x):
        if self.tete is None:
            self.tete = perle(x)
        else:
            p = self.tete
            while p.suiv is not None:
                p = p.suiv
            p.suiv = perle(x)

    def defiler(self):
        assert self.tete is not None, "La file est vide"
        p = self.tete
        self.tete = self.tete.suiv
        return p.couleur

    def voirTete(self):
        assert self.tete is not None, "La file est vide"
        return self.tete.couleur

    def estVide(self):
        return self.tete is None

    def __repr__(self):
        if self.tete is None:
            return "La file est vide"
        else:
            p = self.tete
            s = ""
            while p.suiv is not None:
                s += str(p.couleur) + " -> "
                p = p.suiv
            s += str(p.couleur)
            return s

W = file()
for i in range(50):
    a = perle(couleur=choice(['rouge', 'Blanc', 'Noir']))
    W.enfiler(a)

fileRouge = file()
fileBlanc = file()
fileNoir = file()

while not W.estVide():
    a = W.defiler()
    if a.couleur == 'rouge':
        fileRouge.enfiler(a)
    elif a.couleur == 'Blanc':
        fileBlanc.enfiler(a)
    else:
        fileNoir.enfiler(a)

