from random import randint

class Player:
    life: int = 100
    name: str
    damage: int =10
    defense: int
    @property
    def is_alive(self) -> bool:
        return self.life > 0
    def __init__(self, name = str):
        self.name = name
        self.defense = randint(0, 25)
    def take_damage(self, damage: int) -> None:
        damage -= (self.defense * damage) / 100
        damage = int(damage)
        self.life -= damage
        return taken_damage
    def __str__(self) -> str:
        return f"Giocatore: {self.name} (life: {self.life}%)"