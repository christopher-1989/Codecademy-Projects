class Trainer:
  def __init__(self, trainer_name, held_pokemon, potions=0, revives=0, currently_active_number=0):
    self.held_pokemon = held_pokemon
    self.trainer_name = trainer_name
    self.potions = potions
    self.revives = revives
    self.active_number = currently_active_number
    

  def get_next_pokemon(self):
    current_pokemon_number = self.active_number
    number_pokemon_held = len(self.held_pokemon)
    if number_pokemon_held - 1 == current_pokemon_number:
      print((self.trainer_name + " has no more pokemon."))
      return False
    else:
      self.active_number += 1
      return True

class Pokemon:
  def __init__(self, pokemon_name, level, typ, max_hp, ko=False):
    self.pokemon_name = pokemon_name
    self.level = level
    self.typ = typ
    self.max_hp = max_hp
    self.current_hp = max_hp
    self.ko = ko

  def state_health(self):
    print(self.pokemon_name + " now has " + str(self.current_hp) + " health")
    return
     
  def heal_hp(self, increase):
    new_current_hp = self.current_hp + increase
    if new_current_hp >=self.max_hp:
      self.current_hp = self.max_hp
      return(Pokemon.state_health(self))
    else:
      self.current_hp = new_current_hp
      return (Pokemon.state_health(self))

  def lose_hp(self, decrease):
    new_current_hp = self.current_hp - decrease
    if new_current_hp <=0:
      self.current_hp = 0
      return self.faint()
    else:
      self.current_hp = new_current_hp
      return Pokemon.state_health(self)


  def faint(self):
    print("XXXX " + defender.trainer_name + "'s " + self.pokemon_name.upper() + " HAS FAINTED. XXXX") 
    self.ko = True
    if defender.get_next_pokemon() == True:
      print(defender.held_pokemon[defender.active_number].pokemon_name + " is now the active Pokemon with " + str(defender.held_pokemon[defender.active_number].current_hp) + " HP")
      return defender.held_pokemon[defender.active_number], self.ko
    else:
      print("The game has ended")
      return False
    
def potion():
  if attacker.potions > 0:
    print(attacker.trainer_name + " has used a potion.")
    attacker.potions-=1
    print (attacker.held_pokemon[attacker.active_number].heal_hp(20))
    return
  else:
    print("You do not have any potions!")
    return 
  
def revive(self):
  if self.ko == True:
    print(self.name + " has been revived to full health")
    self.current_hp = self.max_hp
    self.ko = False
    return self.current_hp, self.ko 
  else:
    print("It failed because the pokemon isn't knocked out")
    return

def attack():
  attacking_pokemon = attacker.held_pokemon[attacker.active_number]
  defending_pokemon = defender.held_pokemon[defender.active_number]
  damage = 1  #set damage multiplier
  print(attacker.trainer_name + "'s " + attacking_pokemon.pokemon_name + " attacked " + defender.trainer_name + "'s " + defending_pokemon.pokemon_name)
  if types_strong_against[attacking_pokemon.typ] == defending_pokemon.typ:
    print("It's super effective!")
    damage = 2*damage
  weakness_list = types_weaknesses[attacking_pokemon.typ]
  for pokemon_type in weakness_list:
      if pokemon_type == defending_pokemon.typ:
        print("It's not very effective!")
        damage = damage/2
  return defending_pokemon.lose_hp(attacking_pokemon.level*damage)

def end_game():
  game_over = True
  return game_over
types_weaknesses = {"Fire": ["Water", "Fire"],
	              "Water": ["Grass", "Water"],
                "Grass": ["Fire", "Grass"]}
types_strong_against = {"Fire": "Grass",
                "Water": "Fire",
                "Grass": "Water"}


charmander_1 = Pokemon("Charmander", 5, "Fire", 22)
charmander_2 = Pokemon("Charmander", 5, "Fire", 20)
squirtle = Pokemon("Squirtle", 5, "Water",30)
bulbasaur = Pokemon("Bulbasaur", 5, "Grass", 23)

player_1 = Trainer("Mekka", [bulbasaur, charmander_1], 1)
opponent = Trainer("HANNA", [squirtle, charmander_2], 1)
players = [player_1, opponent]

for player in players: #list the players and their pokemon
  starting_list = []
  for pokemon in player.held_pokemon:
    starting_list.append(pokemon.pokemon_name)
  print(player.trainer_name + " has " + ", ".join(starting_list))
turn=1
game_over = False
while game_over == False:
    print("\nRound number: ", turn)	  
    #player 1 is attacker and computer is defender
    attacker = players[0]
    defender = players[1]
    if attack() == False:
      break
    #Computer is attacker and player 1 is defender
    attacker = players[1]
    defender = players[0]
    if attack() == False:
      break
    turn+=1