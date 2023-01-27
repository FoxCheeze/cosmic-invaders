import random

from pyglet.math import Vec2
from game import settings
from game.invader import Invader
from game.invader_ship import InvaderShip
from . import resources


class InvaderUFO(Invader):
    def __init__(self, *args, **kwargs):
        super().__init__(resources.ufo_image, *args, **kwargs)

        self.max_speed: int = 100
        self.speed: Vec2 = Vec2(
            random.randint(-self.max_speed, self.max_speed),
            random.randint(-self.max_speed, self.max_speed),
        )

        self.score_value = 100
        self.scale = 7

    def update(self, dt):
        super().update(dt)

        self.velocity.x = self.speed.x
        self.velocity.y = self.speed.y

        self.wrap_in_window()

    def on_death(self):
        super().on_death()

        new_invader1: InvaderShip = InvaderShip(
            x=self.x - 10, y=self.y, batch=self.batch
        )
        new_invader2: InvaderShip = InvaderShip(
            x=self.x + 10, y=self.y, batch=self.batch
        )

        settings.game_objects.append(new_invader1)
        settings.game_objects.append(new_invader2)
