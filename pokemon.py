type_advantages = {
    "Fire": "Grass",
    "Water": "Fire",
    "Grass": "Water"
}

class Pokemon:
    def __init__(self, name, level, pokemon_type,
                max_health, health, is_knocked_out):
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        self.max_health = max_health
        self.health = health
        self.is_knocked_out = is_knocked_out
        
    def __repr__(self):
        return(f"{self.name} is a level {self.level}, {self.type} type pokemon. {self.name} currently has {self.health} health, and its max health is {self.max_health}")
    
    
    def gain_health(self, heal):
        self.health+=heal
        if self.health == self.max_health:
            print(self.name + " is at full health!")
        else:
            print(f"{self.name} now has {self.health} health")
                
        
    def lose_health(self, damage):
            self.health-=damage
            if self.health > 0:
                print(f"{self.name} now has {self.health} health.")
            else:
                self.is_knocked_out = True
                self.knock_out() # calling the knockout method 
            
    def knock_out(self):
        if self.health == 0:
            is_knocked_out = True
            print(f"{self.name} has been knocked out")
            
    def revive_knock_out(self, heal, is_knocked_out):
        if is_knocked_out:
            self.gain_health(self.max_health/2) #restoring half of the revived pokemon's health
            
            
    def attack(self, foe):
        #fire, water, grass, normal
        damage = 0
        if self.is_knocked_out:
            print(f"{self.name} is knocked out. Please choose another Pokemon.")
        if foe.pokemon_type in type_advantages[self.pokemon_type]:
            damage = self.level * 2
            foe.lose_health(damage)
        elif self.pokemon_type in type_advantages[foe.pokemon_type]:
            damage = self.level / 2
            foe.lose_health(damage)
        else:
            damage = self.level
            
        print(f"{self.name} attacked {foe.name} and dealt {damage} damage!")
        foe.lose_health(damage)
        


class Trainer:
    def __init__(self, name, pokemon, potions):
        self.potions = potions
        self.pokemon = pokemon
        self.name = name
    
    def potion_heal(self):
        if self.potions == 0:
            print(f"{self.name} doesn't have any potions left!")
        else:
            print(f"{self.name} used a potion!")
            self.pokemon.gain_health(20)
        
    def trainer_battle(self, trainer_foe):
        print(f"{self.name} has declared a battle with {trainer_foe.name}!")
        self.pokemon.attack(trainer_foe.pokemon)
        

piplup = Pokemon("kiki", 3, "Water", 30, 20, False)
trainer1 = Trainer("emaan", piplup, 3)
charmander = Pokemon("flame god", 4, "Fire", 40, 25, False)
trainer2 = Trainer("austin", charmander, 2)

trainer1.trainer_battle(trainer2)
trainer2.trainer_battle(trainer1)
trainer1.trainer_battle(trainer2)
trainer2.trainer_battle(trainer1)


