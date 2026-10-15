# Gameplay for Microsoft MakeCode Arcade Python.
# build_game.py combines this with the art and maps into main.py.
@namespace
class SpriteKind:
    Fragment = SpriteKind.create()
    Portal = SpriteKind.create()

pip: Sprite = None
portal: Sprite = None
level_index = 0
pieces = 0
facing_x = 1
facing_y = 0
last_shot = -1000
last_dash = -2000
dash_until = 0
hurt_until = 0
changing_level = False
world_names = ["Lantern Meadow", "Echo Quarry", "Moonlight Grove"]
worlds = [WORLD_1, WORLD_2, WORLD_3]
floor_colors = [7, 13, 8]
wall_colors = [6, 12, 15]

def spawn_enemy(column: number, row: number):
    enemy = sprites.create(ENEMY_IMAGE, SpriteKind.enemy)
    tiles.place_on_tile(enemy, tiles.get_tile_location(column, row))
    enemy.follow(pip, 22 + level_index * 6)

def load_level():
    global pieces, portal, changing_level, dash_until, hurt_until
    changing_level = True
    for kind in [SpriteKind.enemy, SpriteKind.Fragment, SpriteKind.Portal, SpriteKind.projectile]:
        for old_sprite in sprites.all_of_kind(kind):
            old_sprite.destroy()
    pieces = 0
    dash_until = 0
    controller.move_sprite(pip, 75, 75)
    floor_tile = image.create(16, 16)
    floor_tile.fill(floor_colors[level_index])
    floor_tile.set_pixel(3, 5, wall_colors[level_index])
    floor_tile.set_pixel(12, 11, wall_colors[level_index])
    wall_tile = image.create(16, 16)
    wall_tile.fill(wall_colors[level_index])
    wall_tile.draw_rect(1, 1, 14, 14, floor_colors[level_index])
    wall_tile.draw_line(0, 8, 15, 8, floor_colors[level_index])
    load_world_map(level_index, floor_tile, wall_tile)
    for row in range(12):
        for column in range(32):
            tiles.set_wall_at(tiles.get_tile_location(column, row), worlds[level_index][row].char_at(column) == "#")
    tiles.place_on_tile(pip, tiles.get_tile_location(2, 6))
    scene.camera_follow_sprite(pip)
    for index in range(3):
        fragment = sprites.create(DRUM_IMAGE, SpriteKind.Fragment)
        if index == 0:
            tiles.place_on_tile(fragment, tiles.get_tile_location(8, 3))
        elif index == 1:
            tiles.place_on_tile(fragment, tiles.get_tile_location(16, 8))
        else:
            tiles.place_on_tile(fragment, tiles.get_tile_location(25, 3))
    portal = sprites.create(EXIT_IMAGE, SpriteKind.Portal)
    tiles.place_on_tile(portal, tiles.get_tile_location(29, 6))
    portal.say_text("Find 3 pieces")
    pip.say_text(world_names[level_index], 1800)
    spawn_enemy(10, 7)
    spawn_enemy(19, 3)
    spawn_enemy(26, 8)
    hurt_until = game.runtime() + 1200
    start_map_music(level_index)
    if level_index > 0:
        play_transition_sound()
    changing_level = False

def shoot():
    global last_shot
    if changing_level or game.runtime() - last_shot < 250:
        return
    last_shot = game.runtime()
    pulse = sprites.create_projectile_from_sprite(PULSE_IMAGE, pip, facing_x * 150, facing_y * 150)
    pulse.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
    pulse.lifespan = 900
    play_shot_sound()
controller.A.on_event(ControllerButtonEvent.PRESSED, shoot)

def dash():
    global last_dash, dash_until
    if changing_level or game.runtime() - last_dash < 1500:
        return
    last_dash = game.runtime()
    dash_until = last_dash + 250
    controller.move_sprite(pip, 0, 0)
    pip.vx = facing_x * 190
    pip.vy = facing_y * 190
    play_dash_sound()
controller.B.on_event(ControllerButtonEvent.PRESSED, dash)

def collect_fragment(hero: Sprite, fragment: Sprite):
    global pieces
    if changing_level:
        return
    fragment.destroy()
    pieces += 1
    play_pickup_sound()
    info.change_score_by(10)
    hero.say_text("Pieces " + str(pieces) + "/3", 1000)
    if pieces == 3:
        portal.say_text("OPEN!")
        play_unlock_sound()
sprites.on_overlap(SpriteKind.player, SpriteKind.Fragment, collect_fragment)

def hit_enemy(pulse: Sprite, enemy: Sprite):
    if changing_level:
        return
    pulse.destroy()
    enemy.destroy(effects.disintegrate, 100)
    play_enemy_hit_sound()
    info.change_score_by(2)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, hit_enemy)

def touch_enemy(hero: Sprite, enemy: Sprite):
    global hurt_until
    now = game.runtime()
    if changing_level or now < hurt_until or now < dash_until:
        return
    hurt_until = now + 1200
    info.change_life_by(-1)
    if info.life() <= 0:
        return
    play_damage_sound()
    hero.start_effect(effects.fountain, 150)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, touch_enemy)

def enter_portal(hero: Sprite, beacon: Sprite):
    global level_index, changing_level
    if changing_level:
        return
    if pieces < 3:
        return
    changing_level = True
    if level_index == 2:
        play_victory_sound()
        game.over(True, effects.confetti)
    else:
        level_index += 1
        if info.life() < 5:
            info.change_life_by(1)
        load_level()
sprites.on_overlap(SpriteKind.player, SpriteKind.Portal, enter_portal)

def update_player():
    global facing_x, facing_y, dash_until
    if changing_level:
        return
    now = game.runtime()
    if dash_until > 0 and now >= dash_until:
        dash_until = 0
        controller.move_sprite(pip, 75, 75)
        pip.vx = 0
        pip.vy = 0
    if dash_until == 0:
        if controller.left.is_pressed():
            facing_x = -1
            facing_y = 0
        elif controller.right.is_pressed():
            facing_x = 1
            facing_y = 0
        elif controller.up.is_pressed():
            facing_x = 0
            facing_y = -1
        elif controller.down.is_pressed():
            facing_x = 0
            facing_y = 1
    if pip.vx != 0 or pip.vy != 0:
        if now % 320 < 160:
            pip.set_image(HERO_IDLE)
        else:
            pip.set_image(HERO_WALK)
    else:
        pip.set_image(HERO_IDLE)
game.on_update(update_player)

def add_enemy():
    if changing_level or len(sprites.all_of_kind(SpriteKind.enemy)) >= 6:
        return
    # Spawn on known floor cells, away from Pip; enemies respect map walls.
    if abs(pip.x - 168) + abs(pip.y - 120) > 100:
        spawn_enemy(10, 7)
    elif abs(pip.x - 424) + abs(pip.y - 136) > 100:
        spawn_enemy(26, 8)
game.on_update_interval(6000, add_enemy)

def lose_game():
    global changing_level
    changing_level = True
    play_defeat_sound()
    game.over(False)
info.on_life_zero(lose_game)

scene.set_background_color(15)
pip = sprites.create(HERO_IDLE, SpriteKind.player)
info.set_life(5)
info.set_score(0)
load_level()

