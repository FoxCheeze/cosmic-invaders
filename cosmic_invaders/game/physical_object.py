from pyglet import sprite
from pyglet.window import key
from pyglet.math import Vec2
from game.settings import game_window


class PhysicalObject(sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dead: bool = False

        self.key_handler: key.KeyStateHandler = key.KeyStateHandler()
        self.event_handlers: list = [self, self.key_handler]

        self.velocity: Vec2 = Vec2(0, 0)

    def update(self, dt):
        # Clear new objects for not getting added every frame
        self.new_objects = []

        # Move Object
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt

    # Wraps object in the window if it is out of the bounds
    def wrap_in_window(self):
        if self.x - self.width > game_window.width:
            self.x = 0
        if self.x + self.width < 0:
            self.x = game_window.width

        if self.y - self.height > game_window.height:
            self.y = 0
        if self.y + self.height < 0:
            self.y = game_window.height

    def is_on_window(self) -> bool:
        if self.x - self.width > game_window.width:
            return False
        if self.x + self.width < 0:
            return False
        if self.y - self.height > game_window.height:
            return False
        if self.y + self.height < 0:
            return False

        return True

    def is_colliding_with(self, other) -> bool:
        position: Vec2 = Vec2(self.x, self.y)
        other_position: Vec2 = Vec2(other.x, other.y)

        distance: float = position.distance(other_position)
        collision_area: float = (self.width + other.width) * 0.5

        return distance <= collision_area

    def die(self):
        self.on_death()
        self.dead = True

    def on_collision(self, colliding_object):
        pass

    def on_death(self):
        pass
