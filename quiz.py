#PART 2
#no.1

class Spell: #Parent Class
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        # change this to answer 1.d
        return 'This charm summons an object to the caster, potentially over a significant distance'

    def execute(self): print(self.incantation)

class Accio(Spell): #Child Classes
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell): #Child Classes
    def __init__(self): Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def get_description(self): return 'Causes the victim to become confused and befuddled.'

def study_spell(spell): print(spell)


spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
print(Accio())
study_spell(Confundo())

#1.a). Parent  = Class Spell
#      Child  = Class Accio, Class Confundo

#1.b). will print "Summoning Charm"

#1.c). will called get describ

#1.d). we need to change get_description function so that it can return



#2




