from pyglet import graphics, image, resource


def centered_image(img: image.AbstractImage) -> image.AbstractImage:
    centered_img = img

    centered_img.anchor_x = img.width // 2
    centered_img.anchor_y = img.height // 2

    return centered_img


image.Texture.default_mag_filter = graphics.GL_NEAREST
image.Texture.default_min_filter = graphics.GL_NEAREST

resource.path = ['../image']
resource.reindex()

player_image: image.AbstractImage = resource.image('ship.png')
player_image = centered_image(player_image)

player_bullet: image.AbstractImage = resource.image('ship_bullet.png')
player_bullet = centered_image(player_bullet)

enemy_bullet: image.AbstractImage = resource.image('enemy_bullet.png')
enemy_bullet = centered_image(enemy_bullet)

ufo_image: image.AbstractImage = resource.image('invaderUFO.png')
ufo_image = centered_image(ufo_image)

invader_ship_image: image.AbstractImage = resource.image('invader_ship.png')
invader_ship_image = centered_image(invader_ship_image)

invader_alien: image.AbstractImage = resource.image('invader_alien.png')
invader_alien = centered_image(invader_alien)

# Audios
resource.path = ['../audio']
resource.reindex()

enemy_hit = resource.media('enemy-hit.mp3', streaming=False)
enemy_shoot = resource.media('enemy-shoot.mp3', streaming=False)

new_wave = resource.media('new-wave.mp3', streaming=False)

player_hit = resource.media('player-hit.mp3', streaming=False)
player_shoot = resource.media('player-shoot.mp3', streaming=False)
