import csv

from pyglet import graphics, text, window
from os.path import exists

game_window: window.Window = window.Window()

main_batch: graphics.Batch = graphics.Batch()

game_objects: list = []
score: int = 0
wave: int = 1

game_over_label = text.Label(
    text='',
    anchor_x='center',
    align='center',
    batch=main_batch,
    bold=True,
    color=(0, 255, 155, 255),
    font_name='dogica',
    font_size=32,
    x=game_window.width // 2,
    y=game_window.height // 2 + 50,
)

instruction_label1 = text.Label(
    text='',
    batch=main_batch,
    color=(0, 255, 155, 255),
    font_name='dogica',
    font_size=12,
    x=30,
    y=30,
)

instruction_label2 = text.Label(
    anchor_x='right',
    text='',
    batch=main_batch,
    color=(0, 255, 155, 255),
    font_name='dogica',
    font_size=12,
    x=game_window.width - 30,
    y=30,
)

instruction_label3 = text.Label(
    anchor_x='center',
    text='',
    batch=main_batch,
    color=(0, 255, 155, 255),
    font_name='dogica',
    font_size=12,
    x=game_window.width // 2,
    y=30,
)

score_label = text.Label(
    text='',
    batch=main_batch,
    color=(0, 255, 155, 255),
    font_name='dogica',
    font_size=18,
    x=30,
    y=game_window.height - 50,
)

title_label = text.Label(
    anchor_x='center',
    batch=main_batch,
    bold=True,
    color=(0, 255, 155, 255),
    font_name='dogica',
    font_size=38,
    x=game_window.width // 2,
    y=game_window.height // 2 + 50,
)

wave_label = text.Label(
    text='',
    batch=main_batch,
    color=(0, 255, 155, 255),
    font_name='dogica',
    font_size=12,
    x=32,
    y=game_window.height - 80,
)


def get_highscore() -> dict:
    if not exists('cosmic-invaders-highscore.csv'):
        with open('cosmic-invaders-highscore.csv', 'w') as file:
            field_names = ['score', 'wave']
            writer = csv.writer(file)

            writer.writerow(field_names)
            writer.writerow([0, 0])

    with open('cosmic-invaders-highscore.csv', 'r') as file:
        reader = csv.DictReader(file)

        loaded_score = {'score': 0, 'wave': 0}

        for row in reader:
            loaded_score['score'] = int(row['score'])
            loaded_score['wave'] = int(row['wave'])

        return loaded_score


def update_highscore(new_score: int, new_wave: int):
    with open('cosmic-invaders-highscore.csv', 'w') as file:
        field_names = ['score', 'wave']
        writer = csv.writer(file)

        writer.writerow(field_names)
        writer.writerow([new_score, new_wave])
