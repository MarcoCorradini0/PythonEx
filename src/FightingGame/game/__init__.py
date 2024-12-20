from random import randint
from .player import Player

class Game:
    current_index: int = 0
    @property
    def current_player(self) -> Player:
        return self.players[self.current_index]
    players: list[Player]
    def __init__(self, player_names: list[str]):
        total_players = len(player_names)
        self.current_index = randint(0, total_players - 1)
        self.players = []
        for name in player_names:
            player = Player(name)
            self.players.append(player)

    #def _are_players_alive(self) -> bool:
    #   return(len(filter(lambda p: p.is_alive, self.players)) > 1)
    
    def are_players_alive(self) -> bool:
        players_alive = 0
        for player in self.players:
            if player.is_alive:
                players_alive += 1
        return (players_alive > 1)
    def attack_player(self, target_index: int) -> int:
        randomness = randint(0, 10) - 5
        damage = self.current_player.damage + randomness
        target_player = self.players[target_index]
        taken_damage = target_player.take_damage(damage)
        return taken_damage
    def next_turn(self) -> bool:
        self.current_index = (self.current_index + 1) % len(self.players)
        return self.are_players_alive()
    def __str__(self) -> str:
        value = "Stato partita:\n"
        for player in self.players:
            value += f"{player}\n"
        return value