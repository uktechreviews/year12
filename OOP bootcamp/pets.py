class Pet(object):
    def __init__(self,name,species,description):
        self.name = name
        self.species = species
        self.description = description
    def get_name(self):
        return self.name
    def get_species(self):
        return self.species
    def get_description(self):
        return self.descriprion
    def get_describe(self):
        return self.name,self.species,self.description
    
    def set_name(self,name):
        self.name = name