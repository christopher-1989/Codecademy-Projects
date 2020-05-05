

class Trainer:
  def __init__(self, name, held_poke, potions, currently_active_number):
    self.held_poke = held_poke
    self.trainer_name = t_name
    self.potions = potions
    self.active = currently_active_number
    self.pokemon = self.held_poke[self.active].name
  def potion(self):
    statement = self.held_poke[self.active].heal_hp(20)
    return statement
  def fainted(self):
    print("XXXX " + self.name.upper() + " HAS FAINTED. XXXX") 
    trainers_name = player1
    opponent_name = player2
    opponent_name.held_poke[opponent_name.active].ko = True
    #print(trainers_name.held_poke[trainers_name.active].ko)
    opponent_name.active += 1
    try:
      statement = opponent_name.held_poke[opponent_name.active].name + " is now the active Pokemon with " + str(opponent_name.held_poke[opponent_name.active].current_hp) + " HP"
    except:
      statement = str(opponent_name.name) + " has no more pokemon.\n" + str(opponent_name.name) + " blacked out!"
      return statement
    #print(opponent_name.active)
    #if opponent_name.held_poke[opponent_name.active].ko == False:
    #statement = opponent_name.held_poke[opponent_name.active].name + " is now the active Pokemon"
    #print(statement)
    return statement
    #else:
      #statement = str(opponent_name.name) + " has no more pokemon.\n" + str(opponent_name.name) + " blacked out!"
      #game_end = True
   # return statement

class Pokemon:
  def __init__(self, name, level, typ, max_hp_factor, current_hp, ko=False):
    self.name = name
    self.level = level
    self.typ = typ
    self.max_hp = current_hp
    self.current_hp = current_hp
    self.ko = ko
  def state_health(self):
    statement = self.name + " now has " + str(self.current_hp) + " health"
    return statement
  
  def revive(self):
    if self.ko == True:
      statement = self.name + " has been revived to full health"
      self.current_hp = self.max_hp
      self.ko = False
      return statement 
    else:
      print("It failed because the pokemon isn't knocked out")
      return
 
  def heal_hp(self, increase):
    new_current_hp = self.current_hp + increase
    if new_current_hp >=self.max_hp:
      self.current_hp = self.max_hp
      return Pokemon.state_health(self)
    else:
      self.current_hp = new_current_hp
      return Pokemon.state_health(self)
  def attack(self, attacker_pokemon):
    damage = 1
    print(player1.name + "'s " + self.name + " attacked " + player2.name + "'s " + attacker_pokemon.name)
    if types_strong_against[self.typ] == attacker_pokemon.typ:
      damage = 2*damage
    elif types_weaknesses[self.typ] == attacker_pokemon.typ:
      damage = damage/2
    return attacker_pokemon.lose_hp(self.level*damage)
  def lose_hp(self, decrease):
    new_current_hp = self.current_hp - decrease
    if new_current_hp <=0:
      self.current_hp = 0
      return Trainer.fainted(self)
    else:
      self.current_hp = new_current_hp
      return Pokemon.state_health(self)
  
def endgame(players):
  for player in players:
    for i in player.held_poke:
      if i.ko == False:
        return False
  return True
types_weaknesses = {"Fire": "Water",
                "Water": "Grass",
                "Grass": "Fire"}
types_strong_against = {"Fire": "Grass",
                "Water": "Fire",
                "Grass": "Water"}
charmander = Pokemon("Charmander", 5, "Fire", 4, 20)
squirtle = Pokemon("Squirtle", 5, "Water", 4, 30)
bulbasaur = Pokemon("Bulbasaur", 5, "Grass", 4, 19)
char1 = charmander
char2 = charmander
bulb1 = bulbasaur
bulb2 = bulbasaur
squirt1 = squirtle
squirt2 = squirtle
mekka = Trainer("Mekka", [squirt1, squirt2], 4, 0)
hanna = Trainer("HANNA", [bulb1, bulb2], 4, 0)


players = [mekka, hanna]

num = 0
turn = 1
for player in players: #list the players and their pokemon
  starting_list = []
  for pokemon in player.held_poke:
    starting_list.append(pokemon.name)
  print(player.name + " has " + ", ".join(starting_list))
print("Round number: ", turn)
while num < 20:
  if num > 1 and num % 2 == 0: #count number of turns
    turn += 1
    print("Round number: ", turn)
  test = num%2 
  if test == 0: #change who is attacking. 0 is attacker, 1 is being attacked
    player1 = players[0]
    player2 = players[1]
  else:
    player1 = players[1]
    player2 = players[0]
    #print(player1.active, player2.active)
  print(Pokemon.attack(player1.held_poke[player1.active], player2.held_poke[player2.active]))
  num+=1


  
 # print(Pokemon.attack(depps.held_poke[mekka.active], 

#print(mekka.held_poke[mekka.active].name)
#{print(Pokemon.attack(squirtle, charmander))
#print(Trainer.potion(mekka))
#print(Pokemon.attack(charmander, squirtle))
#print(Pokemon.attack(squirtle, charmander))
#print(Pokemon.attack(charmander, squirtle))
#print(Pokemon.attack(squirtle, charmander))
#print(mekka.active)
#print(mekka.held_poke[mekka.active].name + " is now the active Pokemon")
#print(Trainer.potion(mekka))
