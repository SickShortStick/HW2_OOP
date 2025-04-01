import random


results = list()


class Soldier:
    
    price: int
    damage: float
    proc_chance: float
    health: int

    def __init__(self):
        pass

    def attack(self, opponent_soldier):
        if random.random() < self.proc_chance:
            opponent_soldier.health -= self.damage
            if opponent_soldier.health <= 0:
                return True
            else:
                return False
        return False
    
    def __mul__(self, number: int):
        return self.price * number


class Infantry(Soldier):

    def __init__(self):
        super().__init__()
        self.price = 10
        self.damage = 1
        self.proc_chance = 0.8
        self.health = 3

    def attack(self, opponent_soldier):
        return super().attack(opponent_soldier)

    def __mul__(self, number):
        return super().__mul__(number)


class Cavalry(Soldier):

    def __init__(self):
        super().__init__()
        self.price = 25
        self.damage = 2
        self.proc_chance = 0.6
        self.health = 5

    def attack(self, opponent_soldier):
        return super().attack(opponent_soldier)

    def __mul__(self, number):
        return super().__mul__(number)


class Archer(Soldier):

    def __init__(self):
        super().__init__()
        self.price = 20
        self.damage = 1.5
        self.proc_chance = 0.75
        self.health = 2

    def attack(self, opponent_soldier):
        return super().attack(opponent_soldier)

    def __mul__(self, number):
        return super().__mul__(number)


class HeavyCavalry(Soldier):

    def __init__(self):
        super().__init__()
        self.price = 50
        self.damage = 4
        self.proc_chance = 0.4
        self.health = 10

    def attack(self, opponent_soldier):
        return super().attack(opponent_soldier)

    def __mul__(self, number):
        return super().__mul__(number)



class Player:

    all_players = dict()

    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.soldiers = dict()
        self.attack_token = False
        Player.all_players[self.name] = self

    def add_balance(self):
        self.balance += 50

    def lost_battle(self):
        self.balance -= 50
        if self.balance <= 0:
            state_machine.game_ended = True
        

    def won_battle(self):
        self.balance += 50

    def reset_all_attack_tokens():
        for player in Player.all_players.values():
            player.attack_token = False

    def buy_soldier(self, soldier_type, quantity: int):
        soldier: Soldier
        match soldier_type:
            case 'Cavalry':
                soldier = Cavalry()
            case 'Infantry':
                soldier = Infantry()
            case 'Archer':
                soldier = Archer()
            case 'Heavy':
                soldier = HeavyCavalry()
        if self.balance - quantity * soldier.price >= 0:
            self.balance -= quantity * soldier.price
            self.soldiers[soldier] = quantity
            return f'{self.name} bought {quantity} {soldier_type}'
        else:
            return f'Not eough balance'


class StateMachine:

    game_ended = False
    eliminated_player: Player
    loser: Player
    winner: Player

    def create_player(self, name: str):
        new_player = Player(name)
        return f'Registered {name} with initial money of 100'

    def end_day(self):
        for player in Player.all_players.values():
            player.add_balance()

    def attack_state(self, player1: str, player2: str):
        player1 : Player = Player.all_players[player1]
        player2 : Player = Player.all_players[player2]
        player1.attack_token = True
        while player1.soldiers and player2.soldiers:
            player1_soldier = random.choice(list(player1.soldiers.keys()))
            player2_soldier = random.choice(list(player2.soldiers.keys()))
            if player1.attack_token:
                turn_result = player1_soldier.attack(player2_soldier)
                if turn_result:
                    player2.soldiers[player2_soldier] -= 1
                    if player2.soldiers[player2_soldier] <= 0:
                        player2.soldiers.pop(player2_soldier)
                player1.attack_token = False
                player2.attack_token = True
            else:
                turn_result = player2_soldier.attack(player1_soldier)
                if turn_result:
                    player1.soldiers[player1_soldier] -= 1
                    if player1.soldiers[player1_soldier] <= 0:
                        player1.soldiers.pop(player1_soldier)
                player2.attack_token = False
                player1.attack_token = True
        if player1.soldiers:
            player1.won_battle()
            player2.lost_battle()
            self.loser = player2
            self.winner = player1
        else:
            player2.won_battle()
            player1.lost_battle()
            self.loser = player1
            self.winner = player2
        Player.reset_all_attack_tokens()
        return f'{self.loser.name} Lost the battle\n{self.loser.name} has taken 50 coins from {self.winner.name}'

    def get_eliminated_player(self):
        for player in Player.all_players.values():
            if player.balance <= 0:
                 self.game_ended = True
                 self.eliminated_player = player
                 return player



state_machine = StateMachine()

while not state_machine.game_ended:
    splitted_line = list(input().split())
    match splitted_line[0]:
        case 'CREATE_USER':
            print(state_machine.create_player(splitted_line[1]))
        case 'BUY':
            print(Player.all_players[splitted_line[1]].buy_soldier(splitted_line[2], int(splitted_line[-1])))
        case 'ATTACK':
            print(f'{splitted_line[1]} and {splitted_line[2]} started a battle')
            print(state_machine.attack_state(splitted_line[1], splitted_line[2]))
        case 'DAY':
            print(state_machine.end_day())
eliminated_player : Player = state_machine.get_eliminated_player()
print(f'End of the day, players budgets: {state_machine.winner.name} = {state_machine.winner.balance}، {eliminated_player.name} = {eliminated_player.balance}')
            