//  FIND MY DRUM - paste this entire file into MakeCode Arcade's Python editor.
//  All sprite art and maps are included. No extensions or separate uploads.
//  Original 16 x 16 pixel art for Find My Drum.
//  MakeCode Arcade supplies img(); these assets need no extensions or imports.
let HERO_IDLE = img`
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
`
let HERO_WALK = img`
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
`
let ENEMY_IMAGE = img`
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
`
let DRUM_IMAGE = img`
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
`
let EXIT_IMAGE = img`
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
`
let PULSE_IMAGE = img`
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
`
//  Find My Drum: 32-column x 12-row scrolling world layouts.
//  # = solid wall; . = walkable floor. All floor cells are connected.
//  Shared positions (column, row): start (2,6), exit (29,6),
//  drums (8,3), (16,8), (25,3), enemies (10,7), (19,3), (26,8).
let WORLD_1 = ["################################", "#..............................#", "#.....#......#.......#.........#", "#.....#......#.......#.........#", "#.....#......#.......#.........#", "#.....#..............#.........#", "#..............................#", "#............#.................#", "#.....#......#.......#.........#", "#.....#......#.......#.........#", "#..............................#", "################################"]
let WORLD_2 = ["################################", "#..............................#", "#...###........###.........###.#", "#...###....###.###.........###.#", "#..........###.................#", "#.......................####...#", "#..............................#", "#...................####.......#", "#...###.............####.......#", "#...###........................#", "#..............................#", "################################"]
let WORLD_3 = ["################################", "#.....#.......#.......#........#", "#.....#.......#.......#..####..#", "#.....#.......#.......#........#", "#.....#.......#.......#........#", "#.............#................#", "#.............#................#", "#.....#...............#........#", "#.....#...............#........#", "#.....#.####..#.......#........#", "#.....#.......#.......#........#", "################################"]
function load_world_map(level: number, floor_tile: Image, wall_tile: Image) {
    if (level == 0) {
        tiles.setCurrentTilemap(tiles.createTilemap(hex`20000c00020202020202020202020202020202020202020202020202020202020202020202010101010101010101010101010101010101010101010101010101010101020201010101010201010101010102010101010101010201010101010101010102020101010101020101010101010201010101010101020101010101010101010202010101010102010101010101020101010101010102010101010101010101020201010101010201010101010101010101010101010201010101010101010102020101010101010101010101010101010101010101010101010101010101010202010101010101010101010101020101010101010101010101010101010101020201010101010201010101010102010101010101010201010101010101010102020101010101020101010101010201010101010101020101010101010101010202010101010101010101010101010101010101010101010101010101010101020202020202020202020202020202020202020202020202020202020202020202`, image.create(32, 12), [image.create(16, 16), floor_tile, wall_tile], TileScale.Sixteen))
    } else if (level == 1) {
        tiles.setCurrentTilemap(tiles.createTilemap(hex`20000c00020202020202020202020202020202020202020202020202020202020202020202010101010101010101010101010101010101010101010101010101010101020201010102020201010101010101010202020101010101010101010202020102020101010202020101010102020201020202010101010101010101020202010202010101010101010101010202020101010101010101010101010101010101020201010101010101010101010101010101010101010101010202020201010102020101010101010101010101010101010101010101010101010101010101010202010101010101010101010101010101010101010202020201010101010101020201010102020201010101010101010101010101020202020101010101010102020101010202020101010101010101010101010101010101010101010101010202010101010101010101010101010101010101010101010101010101010101020202020202020202020202020202020202020202020202020202020202020202`, image.create(32, 12), [image.create(16, 16), floor_tile, wall_tile], TileScale.Sixteen))
    } else if (level == 2) {
        tiles.setCurrentTilemap(tiles.createTilemap(hex`20000c00020202020202020202020202020202020202020202020202020202020202020202010101010102010101010101010201010101010101020101010101010101020201010101010201010101010101020101010101010102010102020202010102020101010101020101010101010102010101010101010201010101010101010202010101010102010101010101010201010101010101020101010101010101020201010101010101010101010101020101010101010101010101010101010102020101010101010101010101010102010101010101010101010101010101010202010101010102010101010101010101010101010101020101010101010101020201010101010201010101010101010101010101010102010101010101010102020101010101020102020202010102010101010101010201010101010101010202010101010102010101010101010201010101010101020101010101010101020202020202020202020202020202020202020202020202020202020202020202`, image.create(32, 12), [image.create(16, 16), floor_tile, wall_tile], TileScale.Sixteen))
    }
    
}

//  Original map loops for Microsoft MakeCode Arcade Python.
//  One melody channel leaves room for short gameplay sound effects.
//  Octaves, rests, beat lengths, waveform and envelope use Arcade melody syntax.
let MEADOW_TRACK = "~1 @8,80,100,70 C4:2 E4:1 G4:1 B4:2 R:1 G4:1 A4:2 G4:1 E4:1 D4:2 R:1 E4:1 F4:2 A4:1 C5:1 E5:2 R:1 C5:1 G4:2 E4:1 D4:1 C4:3 R:1"
let QUARRY_TRACK = "~15 @2,45,75,35 A3:2 R:1 A3:1 C4:1 R:1 E4:2 G4:1 E4:1 R:1 C4:1 A3:3 R:1 D4:2 R:1 D4:1 F4:1 R:1 A4:2 G4:1 E4:1 R:1 C4:1 A3:3 R:1"
let GROVE_TRACK = "~3 @12,90,110,90 C4:2 E4:1 G4:1 A4:3 G4:1 E4:2 D4:1 C4:1 G3:3 R:1 F4:2 A4:1 C5:1 D5:2 C5:1 A4:1 G4:2 E4:1 D4:1 C4:3 R:1"
let map_music_level = -1
function stop_map_music() {
    
    music.stopAllSounds()
    map_music_level = -1
}

function start_map_music(level: number) {
    
    //  Repeated requests for the active map must not restart its loop.
    if (map_music_level == level) {
        return
    }
    
    stop_map_music()
    music.setVolume(140)
    if (level == 0) {
        music.play(music.stringPlayable(MEADOW_TRACK, 176), music.PlaybackMode.LoopingInBackground)
    } else if (level == 1) {
        music.play(music.stringPlayable(QUARRY_TRACK, 192), music.PlaybackMode.LoopingInBackground)
    } else if (level == 2) {
        music.play(music.stringPlayable(GROVE_TRACK, 168), music.PlaybackMode.LoopingInBackground)
    } else {
        return
    }
    
    map_music_level = level
}

//  Native synthesized sound effects; all return immediately.
//  Ordinary cues never stop the map music. Terminal cues configure game-over audio.
function play_shot_sound() {
    music.play(music.createSoundEffect(WaveShape.Triangle, 1100, 260, 135, 0, 80, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
}

function play_dash_sound() {
    music.play(music.createSoundEffect(WaveShape.Noise, 400, 2200, 90, 0, 110, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
}

function play_pickup_sound() {
    music.play(music.createSoundEffect(WaveShape.Sine, 660, 1320, 180, 0, 180, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
}

function play_damage_sound() {
    music.play(music.createSoundEffect(WaveShape.Sawtooth, 240, 70, 180, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
}

function play_enemy_hit_sound() {
    music.play(music.createSoundEffect(WaveShape.Square, 740, 180, 150, 0, 95, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
}

function play_unlock_sound() {
    music.play(music.createSoundEffect(WaveShape.Triangle, 440, 1760, 190, 0, 240, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
}

function play_transition_sound() {
    music.play(music.createSoundEffect(WaveShape.Sine, 330, 990, 145, 0, 220, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
}

function play_victory_sound() {
    stop_map_music()
    game.setGameOverPlayable(true, music.stringPlayable("~1 @4,70,170,80 C5:1 E5:1 G5:1 C6:3", 240), false)
}

function play_defeat_sound() {
    stop_map_music()
    game.setGameOverPlayable(false, music.stringPlayable("~3 @5,70,130,80 E4:1 D4:1 C4:1 G3:3", 200), false)
}

//  Gameplay for Microsoft MakeCode Arcade Python.
//  build_game.py combines this with the art and maps into main.py.
namespace SpriteKind {
    export const Fragment = SpriteKind.create()
    export const Portal = SpriteKind.create()
}

let pip : Sprite = null
let portal : Sprite = null
let level_index = 0
let pieces = 0
let facing_x = 1
let facing_y = 0
let last_shot = -1000
let last_dash = -2000
let dash_until = 0
let hurt_until = 0
let changing_level = false
let world_names = ["Lantern Meadow", "Echo Quarry", "Moonlight Grove"]
let worlds = [WORLD_1, WORLD_2, WORLD_3]
let floor_colors = [7, 13, 8]
let wall_colors = [6, 12, 15]
function spawn_enemy(column: number, row: number) {
    let enemy = sprites.create(ENEMY_IMAGE, SpriteKind.Enemy)
    tiles.placeOnTile(enemy, tiles.getTileLocation(column, row))
    enemy.follow(pip, 22 + level_index * 6)
}

function load_level() {
    let fragment: Sprite;
    
    changing_level = true
    for (let kind of [SpriteKind.Enemy, SpriteKind.Fragment, SpriteKind.Portal, SpriteKind.Projectile]) {
        for (let old_sprite of sprites.allOfKind(kind)) {
            old_sprite.destroy()
        }
    }
    pieces = 0
    dash_until = 0
    controller.moveSprite(pip, 75, 75)
    let floor_tile = image.create(16, 16)
    floor_tile.fill(floor_colors[level_index])
    floor_tile.setPixel(3, 5, wall_colors[level_index])
    floor_tile.setPixel(12, 11, wall_colors[level_index])
    let wall_tile = image.create(16, 16)
    wall_tile.fill(wall_colors[level_index])
    wall_tile.drawRect(1, 1, 14, 14, floor_colors[level_index])
    wall_tile.drawLine(0, 8, 15, 8, floor_colors[level_index])
    load_world_map(level_index, floor_tile, wall_tile)
    for (let row = 0; row < 12; row++) {
        for (let column = 0; column < 32; column++) {
            tiles.setWallAt(tiles.getTileLocation(column, row), worlds[level_index][row].charAt(column) == "#")
        }
    }
    tiles.placeOnTile(pip, tiles.getTileLocation(2, 6))
    scene.cameraFollowSprite(pip)
    for (let index = 0; index < 3; index++) {
        fragment = sprites.create(DRUM_IMAGE, SpriteKind.Fragment)
        if (index == 0) {
            tiles.placeOnTile(fragment, tiles.getTileLocation(8, 3))
        } else if (index == 1) {
            tiles.placeOnTile(fragment, tiles.getTileLocation(16, 8))
        } else {
            tiles.placeOnTile(fragment, tiles.getTileLocation(25, 3))
        }
        
    }
    portal = sprites.create(EXIT_IMAGE, SpriteKind.Portal)
    tiles.placeOnTile(portal, tiles.getTileLocation(29, 6))
    portal.sayText("Find 3 pieces")
    pip.sayText(world_names[level_index], 1800)
    spawn_enemy(10, 7)
    spawn_enemy(19, 3)
    spawn_enemy(26, 8)
    hurt_until = game.runtime() + 1200
    start_map_music(level_index)
    if (level_index > 0) {
        play_transition_sound()
    }
    
    changing_level = false
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function shoot() {
    
    if (changing_level || game.runtime() - last_shot < 250) {
        return
    }
    
    last_shot = game.runtime()
    let pulse = sprites.createProjectileFromSprite(PULSE_IMAGE, pip, facing_x * 150, facing_y * 150)
    pulse.setFlag(SpriteFlag.DestroyOnWall, true)
    pulse.lifespan = 900
    play_shot_sound()
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function dash() {
    
    if (changing_level || game.runtime() - last_dash < 1500) {
        return
    }
    
    last_dash = game.runtime()
    dash_until = last_dash + 250
    controller.moveSprite(pip, 0, 0)
    pip.vx = facing_x * 190
    pip.vy = facing_y * 190
    play_dash_sound()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Fragment, function collect_fragment(hero: Sprite, fragment: Sprite) {
    
    if (changing_level) {
        return
    }
    
    fragment.destroy()
    pieces += 1
    play_pickup_sound()
    info.changeScoreBy(10)
    hero.sayText("Pieces " + ("" + pieces) + "/3", 1000)
    if (pieces == 3) {
        portal.sayText("OPEN!")
        play_unlock_sound()
    }
    
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function hit_enemy(pulse: Sprite, enemy: Sprite) {
    if (changing_level) {
        return
    }
    
    pulse.destroy()
    enemy.destroy(effects.disintegrate, 100)
    play_enemy_hit_sound()
    info.changeScoreBy(2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function touch_enemy(hero: Sprite, enemy: Sprite) {
    
    let now = game.runtime()
    if (changing_level || now < hurt_until || now < dash_until) {
        return
    }
    
    hurt_until = now + 1200
    info.changeLifeBy(-1)
    if (info.life() <= 0) {
        return
    }
    
    play_damage_sound()
    hero.startEffect(effects.fountain, 150)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Portal, function enter_portal(hero: Sprite, beacon: Sprite) {
    
    if (changing_level) {
        return
    }
    
    if (pieces < 3) {
        return
    }
    
    changing_level = true
    if (level_index == 2) {
        play_victory_sound()
        game.over(true, effects.confetti)
    } else {
        level_index += 1
        if (info.life() < 5) {
            info.changeLifeBy(1)
        }
        
        load_level()
    }
    
})
game.onUpdate(function update_player() {
    
    if (changing_level) {
        return
    }
    
    let now = game.runtime()
    if (dash_until > 0 && now >= dash_until) {
        dash_until = 0
        controller.moveSprite(pip, 75, 75)
        pip.vx = 0
        pip.vy = 0
    }
    
    if (dash_until == 0) {
        if (controller.left.isPressed()) {
            facing_x = -1
            facing_y = 0
        } else if (controller.right.isPressed()) {
            facing_x = 1
            facing_y = 0
        } else if (controller.up.isPressed()) {
            facing_x = 0
            facing_y = -1
        } else if (controller.down.isPressed()) {
            facing_x = 0
            facing_y = 1
        }
        
    }
    
    if (pip.vx != 0 || pip.vy != 0) {
        if (now % 320 < 160) {
            pip.setImage(HERO_IDLE)
        } else {
            pip.setImage(HERO_WALK)
        }
        
    } else {
        pip.setImage(HERO_IDLE)
    }
    
})
game.onUpdateInterval(6000, function add_enemy() {
    if (changing_level || sprites.allOfKind(SpriteKind.Enemy).length >= 6) {
        return
    }
    
    //  Spawn on known floor cells, away from Pip; enemies respect map walls.
    if (Math.abs(pip.x - 168) + Math.abs(pip.y - 120) > 100) {
        spawn_enemy(10, 7)
    } else if (Math.abs(pip.x - 424) + Math.abs(pip.y - 136) > 100) {
        spawn_enemy(26, 8)
    }
    
})
info.onLifeZero(function lose_game() {
    
    changing_level = true
    play_defeat_sound()
    game.over(false)
})
scene.setBackgroundColor(15)
pip = sprites.create(HERO_IDLE, SpriteKind.Player)
info.setLife(5)
info.setScore(0)
load_level()
