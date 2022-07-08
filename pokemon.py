class Pokemon:
    def __init__(self, name, level, pokemon_type,
                max_health, health, is_knocked_out):
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        self.max_health = max_health
        self.health = health
        self.is_knocked_out = is_knocked_out
    
    
    def gain_health(self, health):
        if self.health == self.max_health:
            print(self.name + " is at full health!")
            self.health = 1
        else:
            gain = input("How much health would you like your Pokemon to gain? ")
            if self.health + gain == self.max_health:
                print(self.name + " is now at full health!")
                self.health = self.max_health
            else:
                print(self.name + " now has " + str(self.health + gain) + "health")
                self.health+=gain
        
                
    def lose_health(self, damage):
            self.health-=damage
            print(self.name + " now has " + str(self.health) + " health")
            
    def knock_out(self, health, is_knocked_out):
        if self.health == 0 or is_knocked_out:
            is_knocked_out = True
            print(self.name + " has been knocked out")
            
    def revive_knock_out(self, health, is_knocked_out):
        if is_knocked_out:
            self.gain_health
            if self.health > 0:
                print("Your pokemon has been revived!")
            
            
    def attack(self, type, other_pokemon):
        #fire, water, grass, normal
        if self.type == "Fire":
            if other_pokemon.type == "Fire":
                damage = other_pokemon.level/other_pokemon.max_health
                self.lose_health(damage)
            