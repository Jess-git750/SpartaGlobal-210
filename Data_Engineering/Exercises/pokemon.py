import requests, random


#data = response.json

class Pokemon:
    def __init__(self, name):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/").json()
        self.name =response["name"]
        self.hp = response["stats"][0]["base_stat"]
        self.attack = response["stats"][1]["base_stat"]
        #print(self.attack)
        #self.defense = requests.get(f"https://pokeapi.co/api/v2/stat/3/").json()
  
class Battle:
    def this_is_sparta(self, pokemon1, pokemon2):
        print(f"{pokemon1.name} vs {pokemon2.name}")
        
        while True:
            
            damage = random.randint(1, pokemon1.attack)
            pokemon2.hp -= damage
            print(f"{pokemon1.name} attacks {pokemon2.name} with {damage} of damage!")
            if pokemon2.hp <= 0:
                print(f"{pokemon2.name} fainted!")
                break
            
            damage = random.randint(1, pokemon2.attack)
            pokemon1.hp -= damage
            print(f"{pokemon2.name} attacks {pokemon1.name} with {damage} of damage!")
            if pokemon1.hp <= 0:
                print(f"{pokemon1.name} fainted!")
                break
        



pokemon1 = Pokemon("charizard")
pokemon2 = Pokemon("nidoking")
battle = Battle()
battle.this_is_sparta(pokemon1, pokemon2)