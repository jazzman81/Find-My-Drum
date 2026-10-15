# FIND MY DRUM - paste this entire file into MakeCode Arcade's Python editor.
# All sprite art and maps are included. No extensions or separate uploads.


# Original 16 x 16 pixel art for Find My Drum.
# MakeCode Arcade supplies img(); these assets need no extensions or imports.

HERO_IDLE = img("""
    . . . . . . 8 8 8 8 . . . . . .
    . . . . . 8 8 8 8 8 8 . . . . .
    . . . . . 8 8 8 8 8 8 8 . . . .
    . . . . . d d d d d . . . . . .
    . . . . . d f d f d . . . . . .
    . . . . . d d d d d . . . . . .
    . . . . . . d d d . . . . . . .
    . . . . 9 9 9 9 9 9 9 . . . . .
    . . . d 9 9 9 1 9 9 9 d . . . .
    . . . d 9 9 1 1 1 9 9 d . . . .
    . . . d . 9 9 1 9 9 . d . . . .
    . . . . . 9 9 9 9 9 . . . . . .
    . . . . . 8 8 8 8 8 . . . . . .
    . . . . . 8 8 . 8 8 . . . . . .
    . . . . . f f . f f . . . . . .
    . . . . f f f . f f f . . . . .
""")

HERO_WALK = img("""
    . . . . . . 8 8 8 8 . . . . . .
    . . . . . 8 8 8 8 8 8 . . . . .
    . . . . . 8 8 8 8 8 8 8 . . . .
    . . . . . d d d d d . . . . . .
    . . . . . d f d f d . . . . . .
    . . . . . d d d d d . . . . . .
    . . . . . . d d d . . . . . . .
    . . . . 9 9 9 9 9 9 9 d . . . .
    . . . . 9 9 9 1 9 9 9 d . . . .
    . . . d 9 9 1 1 1 9 9 . . . . .
    . . . d . 9 9 1 9 9 . . . . . .
    . . . . . 9 9 9 9 9 . . . . . .
    . . . . . 8 8 8 8 8 . . . . . .
    . . . . 8 8 . . 8 8 . . . . . .
    . . . . f f . . 8 8 . . . . . .
    . . . f f f . . . f f f . . . .
""")

ENEMY_IMAGE = img("""
    . . . . . . . . . . . . . . . .
    . . . . . . a a a a . . . . . .
    . . . . a a a a a a a a . . . .
    . . . a a c c c c c c a a . . .
    . . a a c c c c c c c c a a . .
    . . a c c 1 1 c c 1 1 c c a . .
    . a a c c 1 f c c f 1 c c a a .
    . a c c c c c c c c c c c c a .
    . a c c c c c c c c c c c c a .
    . a c c c c c f f c c c c c a .
    . a a c c c f f f f c c c a a .
    . . a c c c c c c c c c c a . .
    . . a a c c c c c c c c a a . .
    . . . a a a a a a a a a a . . .
    . . . . a a . . . . a a . . . .
    . . . . . . . . . . . . . . . .
""")

DRUM_IMAGE = img("""
    . . . . . . . . . . . . . . . .
    . . . . . . 5 5 5 5 . . . . . .
    . . . . 5 5 1 1 1 1 5 5 . . . .
    . . . 5 1 1 1 1 1 1 1 1 5 . . .
    . . . 5 1 1 1 1 1 1 1 1 5 . . .
    . . . 5 5 1 1 1 1 1 1 5 5 . . .
    . . . e 5 5 5 5 5 5 5 5 e . . .
    . . . e 2 5 2 2 2 2 5 2 e . . .
    . . . e 2 5 2 2 2 2 5 2 e . . .
    . . . e 5 2 5 2 2 5 2 5 e . . .
    . . . e 5 2 5 2 2 5 2 5 e . . .
    . . . e 2 5 2 5 5 2 5 2 e . . .
    . . . e 2 5 2 5 5 2 5 2 e . . .
    . . . e e 5 5 5 5 5 5 e e . . .
    . . . . e e e e e e e e . . . .
    . . . . . . . . . . . . . . . .
""")

EXIT_IMAGE = img("""
    . . . . . 5 5 5 5 5 5 . . . . .
    . . . . 5 5 9 9 9 9 5 5 . . . .
    . . . 5 5 9 8 8 8 8 9 5 5 . . .
    . . 5 5 9 8 8 8 8 8 8 9 5 5 . .
    . . 5 9 8 8 8 9 9 8 8 8 9 5 . .
    . . 5 9 8 8 9 1 1 9 8 8 9 5 . .
    . . 5 9 8 9 1 1 1 1 9 8 9 5 . .
    . . 5 9 8 8 8 1 1 8 8 8 9 5 . .
    . . 5 9 8 8 8 1 1 8 8 8 9 5 . .
    . . 5 9 8 8 8 1 1 8 8 8 9 5 . .
    . . 5 9 8 8 8 1 1 8 8 8 9 5 . .
    . . 5 9 8 8 8 8 8 8 8 8 9 5 . .
    . . 5 9 8 8 8 8 8 8 8 8 9 5 . .
    . . 5 5 9 9 9 9 9 9 9 9 5 5 . .
    . . 5 5 5 5 5 5 5 5 5 5 5 5 . .
    . . . . . . . . . . . . . . . .
""")

PULSE_IMAGE = img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . 9 9 9 9 . . . . . .
    . . . . 9 9 1 1 1 1 9 9 . . . .
    . . . . 9 1 5 5 5 5 1 9 . . . .
    . . . 9 1 5 5 1 1 5 5 1 9 . . .
    . . . 9 1 5 1 1 1 1 5 1 9 . . .
    . . . 9 1 5 1 1 1 1 5 1 9 . . .
    . . . 9 1 5 5 1 1 5 5 1 9 . . .
    . . . . 9 1 5 5 5 5 1 9 . . . .
    . . . . 9 9 1 1 1 1 9 9 . . . .
    . . . . . . 9 9 9 9 . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
""")


# Find My Drum: 32-column x 12-row scrolling world layouts.
# # = solid wall; . = walkable floor. All floor cells are connected.
# Shared positions (column, row): start (2,6), exit (29,6),
# drums (8,3), (16,8), (25,3), enemies (10,7), (19,3), (26,8).

WORLD_1 = [
    "################################",
    "#..............................#",
    "#.....#......#.......#.........#",
    "#.....#......#.......#.........#",
    "#.....#......#.......#.........#",
    "#.....#..............#.........#",
    "#..............................#",
    "#............#.................#",
    "#.....#......#.......#.........#",
    "#.....#......#.......#.........#",
    "#..............................#",
    "################################",
]

WORLD_2 = [
    "################################",
    "#..............................#",
    "#...###........###.........###.#",
    "#...###....###.###.........###.#",
    "#..........###.................#",
    "#.......................####...#",
    "#..............................#",
    "#...................####.......#",
    "#...###.............####.......#",
    "#...###........................#",
    "#..............................#",
    "################################",
]

WORLD_3 = [
    "################################",
    "#.....#.......#.......#........#",
    "#.....#.......#.......#..####..#",
    "#.....#.......#.......#........#",
    "#.....#.......#.......#........#",
    "#.............#................#",
    "#.............#................#",
    "#.....#...............#........#",
    "#.....#...............#........#",
    "#.....#.####..#.......#........#",
    "#.....#.......#.......#........#",
    "################################",
]



def load_world_map(level: number, floor_tile: Image, wall_tile: Image):
    if level == 0:
        tiles.set_current_tilemap(tiles.create_tilemap(hex("""20000c00020202020202020202020202020202020202020202020202020202020202020202010101010101010101010101010101010101010101010101010101010101020201010101010201010101010102010101010101010201010101010101010102020101010101020101010101010201010101010101020101010101010101010202010101010102010101010101020101010101010102010101010101010101020201010101010201010101010101010101010101010201010101010101010102020101010101010101010101010101010101010101010101010101010101010202010101010101010101010101020101010101010101010101010101010101020201010101010201010101010102010101010101010201010101010101010102020101010101020101010101010201010101010101020101010101010101010202010101010101010101010101010101010101010101010101010101010101020202020202020202020202020202020202020202020202020202020202020202"""), image.create(32, 12), [image.create(16, 16), floor_tile, wall_tile], TileScale.SIXTEEN))
    elif level == 1:
        tiles.set_current_tilemap(tiles.create_tilemap(hex("""20000c00020202020202020202020202020202020202020202020202020202020202020202010101010101010101010101010101010101010101010101010101010101020201010102020201010101010101010202020101010101010101010202020102020101010202020101010102020201020202010101010101010101020202010202010101010101010101010202020101010101010101010101010101010101020201010101010101010101010101010101010101010101010202020201010102020101010101010101010101010101010101010101010101010101010101010202010101010101010101010101010101010101010202020201010101010101020201010102020201010101010101010101010101020202020101010101010102020101010202020101010101010101010101010101010101010101010101010202010101010101010101010101010101010101010101010101010101010101020202020202020202020202020202020202020202020202020202020202020202"""), image.create(32, 12), [image.create(16, 16), floor_tile, wall_tile], TileScale.SIXTEEN))
    elif level == 2:
        tiles.set_current_tilemap(tiles.create_tilemap(hex("""20000c00020202020202020202020202020202020202020202020202020202020202020202010101010102010101010101010201010101010101020101010101010101020201010101010201010101010101020101010101010102010102020202010102020101010101020101010101010102010101010101010201010101010101010202010101010102010101010101010201010101010101020101010101010101020201010101010101010101010101020101010101010101010101010101010102020101010101010101010101010102010101010101010101010101010101010202010101010102010101010101010101010101010101020101010101010101020201010101010201010101010101010101010101010102010101010101010102020101010101020102020202010102010101010101010201010101010101010202010101010102010101010101010201010101010101020101010101010101020202020202020202020202020202020202020202020202020202020202020202"""), image.create(32, 12), [image.create(16, 16), floor_tile, wall_tile], TileScale.SIXTEEN))

# Original map loops for Microsoft MakeCode Arcade Python.
# One melody channel leaves room for short gameplay sound effects.
# Octaves, rests, beat lengths, waveform and envelope use Arcade melody syntax.
MEADOW_TRACK = "~1 @8,80,100,70 C4:2 E4:1 G4:1 B4:2 R:1 G4:1 A4:2 G4:1 E4:1 D4:2 R:1 E4:1 F4:2 A4:1 C5:1 E5:2 R:1 C5:1 G4:2 E4:1 D4:1 C4:3 R:1"
QUARRY_TRACK = "~15 @2,45,75,35 A3:2 R:1 A3:1 C4:1 R:1 E4:2 G4:1 E4:1 R:1 C4:1 A3:3 R:1 D4:2 R:1 D4:1 F4:1 R:1 A4:2 G4:1 E4:1 R:1 C4:1 A3:3 R:1"
GROVE_TRACK = "~3 @12,90,110,90 C4:2 E4:1 G4:1 A4:3 G4:1 E4:2 D4:1 C4:1 G3:3 R:1 F4:2 A4:1 C5:1 D5:2 C5:1 A4:1 G4:2 E4:1 D4:1 C4:3 R:1"
map_music_level = -1

def stop_map_music():
    global map_music_level
    music.stop_all_sounds()
    map_music_level = -1

def start_map_music(level: number):
    global map_music_level
    # Repeated requests for the active map must not restart its loop.
    if map_music_level == level:
        return
    stop_map_music()
    music.set_volume(140)
    if level == 0:
        music.play(music.string_playable(MEADOW_TRACK, 176), music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif level == 1:
        music.play(music.string_playable(QUARRY_TRACK, 192), music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif level == 2:
        music.play(music.string_playable(GROVE_TRACK, 168), music.PlaybackMode.LOOPING_IN_BACKGROUND)
    else:
        return
    map_music_level = level


# Native synthesized sound effects; all return immediately.
# Ordinary cues never stop the map music. Terminal cues configure game-over audio.

def play_shot_sound():
    music.play(music.create_sound_effect(WaveShape.TRIANGLE, 1100, 260, 135, 0, 80, SoundExpressionEffect.NONE, InterpolationCurve.CURVE), music.PlaybackMode.IN_BACKGROUND)

def play_dash_sound():
    music.play(music.create_sound_effect(WaveShape.NOISE, 400, 2200, 90, 0, 110, SoundExpressionEffect.NONE, InterpolationCurve.LINEAR), music.PlaybackMode.IN_BACKGROUND)

def play_pickup_sound():
    music.play(music.create_sound_effect(WaveShape.SINE, 660, 1320, 180, 0, 180, SoundExpressionEffect.NONE, InterpolationCurve.LINEAR), music.PlaybackMode.IN_BACKGROUND)

def play_damage_sound():
    music.play(music.create_sound_effect(WaveShape.SAWTOOTH, 240, 70, 180, 0, 150, SoundExpressionEffect.NONE, InterpolationCurve.CURVE), music.PlaybackMode.IN_BACKGROUND)

def play_enemy_hit_sound():
    music.play(music.create_sound_effect(WaveShape.SQUARE, 740, 180, 150, 0, 95, SoundExpressionEffect.NONE, InterpolationCurve.LINEAR), music.PlaybackMode.IN_BACKGROUND)

def play_unlock_sound():
    music.play(music.create_sound_effect(WaveShape.TRIANGLE, 440, 1760, 190, 0, 240, SoundExpressionEffect.VIBRATO, InterpolationCurve.LINEAR), music.PlaybackMode.IN_BACKGROUND)

def play_transition_sound():
    music.play(music.create_sound_effect(WaveShape.SINE, 330, 990, 145, 0, 220, SoundExpressionEffect.NONE, InterpolationCurve.CURVE), music.PlaybackMode.IN_BACKGROUND)

def play_victory_sound():
    stop_map_music()
    game.set_game_over_playable(True, music.string_playable("~1 @4,70,170,80 C5:1 E5:1 G5:1 C6:3", 240), False)

def play_defeat_sound():
    stop_map_music()
    game.set_game_over_playable(False, music.string_playable("~3 @5,70,130,80 E4:1 D4:1 C4:1 G3:3", 200), False)


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

