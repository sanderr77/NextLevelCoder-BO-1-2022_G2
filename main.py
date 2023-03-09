from dino_runner.components.game import Game


if __name__ == "__main__":
    game = Game()
    game.run()
    death_count = 0
    while game.game_running:
        if not game.playing:
            game.show_menu(death_count=death_count)
            death_count += 1

