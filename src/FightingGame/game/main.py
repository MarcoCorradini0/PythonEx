#!/usr/bin/env python3

from game import Game
#
# - Attaccare solo gli altri
# - Attaccare solo i giocatori vivi
#
def get_players():
    player_count = int(input("Inserisci il numero dei giocatori: "))
    index = 0
    player_names = []
    while index < player_count:
        player_name = input(f"Inserisci il nome del {index + 1}° giocatore: ")
        if player_name not in player_names:
            player_names.append(player_name)
            index += 1
        else:
            print(f"Il giocatore \"{player_name}\" è già esistente. Scegli un altro nome.")
    return player_names

def handle_player_turn(game: Game) -> None:
    print(f"\n{game.current_player}: quale giocatore vuoi attaccare? ")
    for index, player in enumerate(game.players):
        print(f"{index + 1}) {player}")
    target_index = int(input("\nSelezione: ")) - 1
    if not 0 <= target_index < len(game.players):
        print("La tua selezione non è valida. Riprova.")
        return
    taken_damage = game.attack_player(target_index)
    print(f"{game.current_player} ha inflitto {taken_damage} danni.")
    game.next_turn()

def main() -> None:
    player_names = get_players()
    game = Game(player_names)
    while game.is_running:
        handle_player_turn(game)
    print(game.current_index)
    print(f"{game.current_player} ha vinto.")

if __name__ == "__main__":
    main()