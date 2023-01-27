from game import settings, resources
from game.enemy import Enemy
from game.player_bullet import PlayerBullet


class Invader(Enemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.score_value: int = 0

    def update(self, dt):
        super().update(dt)

    def on_collision(self, colliding_object):
        if type(colliding_object) is PlayerBullet:
            resources.enemy_hit.play()
            self.die()

    def on_death(self):
        settings.score += self.score_value
