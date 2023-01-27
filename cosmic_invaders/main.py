import random

from game import settings, utils, resources
from game.bullet import Bullet
from game.invader_ufo import InvaderUFO
from game.settings import game_window
from game.ship import Ship

from pyglet import (
    app,
    clock,
    font,
)
from pyglet.math import Vec2
from pyglet.window import key

game_state: str = 'main_menu'
font.add_directory('../fonts')


@game_window.event
def on_draw():
    game_window.clear()
    settings.main_batch.draw()


@game_window.event
def on_key_press(symbol, _):
    # Prevent exit on ESC
    if symbol == key.ESCAPE:
        return True

    if game_state == 'in_game':
        return

    if game_state == 'main_menu':
        if symbol == key.P:
            start_game()

        if symbol == key.Q:
            app.exit()

    if game_state == 'game_over':
        if symbol == key.R:
            start_game()

        if symbol == key.M:
            init_main_menu()


game_window.push_handlers(on_key_press)


def init_main_menu():
    global game_state
    global highscore

    game_state = 'main_menu'

    highscore = settings.get_highscore()

    settings.title_label.text = 'Cosmic Invaders'

    settings.instruction_label1.text = 'P to play'
    settings.instruction_label2.text = 'Q to quit'

    settings.instruction_label3.bold = True
    settings.instruction_label3.text = 'by FoxCheeze (2022)'

    settings.score_label.anchor_x = 'center'
    settings.score_label.font_size = 14
    settings.score_label.text = f'Highscore: {highscore["score"]}'
    settings.score_label.x = game_window.width // 2
    settings.score_label.y = game_window.height // 2

    settings.wave_label.anchor_x = 'center'
    settings.wave_label.font_size = 14
    settings.wave_label.text = f'Max. Waves: {highscore["wave"]}'
    settings.wave_label.x = game_window.width // 2
    settings.wave_label.y = game_window.height // 2 - 25


def start_game():
    global game_state
    global highscore
    global ship

    highscore = settings.get_highscore()

    game_state = 'in_game'

    for object in settings.game_objects:
        object.die()
        object.delete()

    # Clear previous game info
    settings.game_objects = []
    settings.score = 0
    settings.wave = 1
    enemies = []

    settings.score_label.anchor_x = 'left'
    settings.score_label.font_size = 18
    settings.score_label.x = 30
    settings.score_label.y = game_window.height - 50

    settings.wave_label.anchor_x = 'left'
    settings.wave_label.font_size = 12
    settings.wave_label.x = 32
    settings.wave_label.y = game_window.height - 80

    settings.instruction_label1.text = 'WASD to move'
    settings.instruction_label2.text = 'SPACE to shoot'
    settings.instruction_label3.text = '<> to rotate UP to flip'

    settings.instruction_label3.bold = False

    ship = Ship(x=game_window.width // 2, y=game_window.height // 2)

    for _ in range(2):
        while True:
            ufo = InvaderUFO(
                x=random.randint(0, game_window.width),
                y=random.randint(0, game_window.height),
            )

            if not ship.is_colliding_with(ufo):
                enemies.append(ufo)
                break

    settings.game_objects.append(ship)

    for enemy in enemies:
        settings.game_objects.append(enemy)

    for object in settings.game_objects:
        object.batch = settings.main_batch

        for handler in object.event_handlers:
            game_window.push_handlers(handler)

    settings.wave_label.text = f'WAVE: {settings.wave}'


def update(dt):
    # Labels
    if not game_state == 'main_menu':
        settings.title_label.text = ''

    if not game_state == 'game_over':
        settings.game_over_label.text = ''

    # Run update for each object
    for object in settings.game_objects:
        object.update(dt)

    if game_state == 'in_game':
        # Activate game over state
        if not utils.player_alive_in(settings.game_objects):
            game_over()

        # Remove dead objects
        for object in settings.game_objects:
            if object.dead:
                settings.game_objects.remove(object)
                object.delete()

        # Collision cheking
        for i in range(len(settings.game_objects)):
            for j in range(i + 1, len(settings.game_objects)):
                if settings.game_objects[i].is_colliding_with(
                    settings.game_objects[j]
                ):
                    settings.game_objects[i].on_collision(
                        settings.game_objects[j]
                    )
                    settings.game_objects[j].on_collision(
                        settings.game_objects[i]
                    )

        # Update score label text
        settings.score_label.text = f'SCORE: {settings.score}'

        # Check if all the enemies are dead
        if utils.no_enemies_in(settings.game_objects):
            respawn_enemies()


def respawn_enemies():
    # Update settings.wave label text
    settings.wave += 1
    settings.wave_label.text = f'WAVE: {settings.wave}'

    ship.velocity = Vec2(0, 0)
    ship.x = game_window.width // 2
    ship.y = game_window.height // 2
    ship.rotation = 0

    for object in settings.game_objects:
        if issubclass(type(object), Bullet):
            object.die()

    for _ in range(2):
        while True:
            ufo: InvaderUFO = InvaderUFO(
                x=random.randint(0, game_window.width),
                y=random.randint(0, game_window.height),
                batch=settings.main_batch,
            )

            if not ship.is_colliding_with(ufo):
                settings.game_objects.append(ufo)
                break

    resources.new_wave.play()


def game_over():
    global game_state

    game_state = 'game_over'

    settings.score_label.text = f'Final Score: {settings.score}'
    settings.score_label.anchor_x = 'center'
    settings.score_label.font_size = 14
    settings.score_label.x = game_window.width // 2
    settings.score_label.y = game_window.height // 2

    settings.wave_label.text = f'Waves Survived: {settings.wave - 1}'
    settings.wave_label.anchor_x = 'center'
    settings.wave_label.font_size = 14
    settings.wave_label.x = game_window.width // 2
    settings.wave_label.y = game_window.height // 2 - 25

    settings.instruction_label1.text = 'R to replay'
    settings.instruction_label2.text = 'M to main menu'
    settings.instruction_label3.text = ''

    if settings.score > highscore['score']:
        settings.update_highscore(settings.score, settings.wave - 1)

    settings.game_over_label.text = 'Game Over'


if __name__ == '__main__':
    clock.schedule_interval(update, 1 / 120.0)
    init_main_menu()
    app.run()
