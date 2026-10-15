"""Host-side contract checks; does not emulate Arcade rendering or physics.

Run with: python validate_game.py
The actual MakeCode compiler and simulator remain the platform authority.
"""
import ast
from collections import deque
from pathlib import Path
from types import SimpleNamespace
import unittest


ROOT = Path(__file__).resolve().parent


class Art:
    def __init__(self, width=16, height=16, rows=None):
        self.width, self.height, self.rows = width, height, rows

    def fill(self, *args):
        pass

    def set_pixel(self, *args):
        pass

    def draw_rect(self, *args):
        pass

    def draw_line(self, *args):
        pass


def img(source):
    rows = [line.split() for line in source.strip().splitlines()]
    assert len(rows) == 16, "Sprite must have 16 rows"
    assert all(len(row) == 16 for row in rows), "Sprite must have 16 columns"
    assert all(pixel in ".0123456789abcdef" and len(pixel) == 1
               for row in rows for pixel in row), "Invalid Arcade palette entry"
    return Art(rows=rows)


class Sprite:
    def __init__(self, art, kind):
        self.image, self.kind = art, kind
        self.x = self.y = self.vx = self.vy = 0
        self.destroyed = False
        self.flags = {}
        self.lifespan = None
        self.speech = None

    def destroy(self, *args):
        self.destroyed = True

    def follow(self, target, speed):
        self.target, self.follow_speed = target, speed

    def say_text(self, text, *args):
        self.speech = text

    def set_flag(self, flag, enabled):
        self.flags[flag] = enabled

    def start_effect(self, *args):
        pass

    def set_image(self, art):
        self.image = art


class Button:
    def __init__(self):
        self.callback = None
        self.pressed = False

    def on_event(self, event, callback):
        self.callback = callback

    def is_pressed(self):
        return self.pressed

    def press(self):
        self.callback()


class Runtime:
    def __init__(self):
        self.now = 0
        self.score = self.life_count = 0
        self.result = None
        self.active = []
        self.overlaps = {}
        self.updates = []
        self.intervals = []
        self.walls = {}
        self.map = None
        self.kind_counter = 3
        self.audio_events = []
        self.game_over_sounds = {}
        self.life_zero_callback = None
        self.controller = SimpleNamespace(**{key: Button() for key in
                                                ["A", "B", "left", "right", "up", "down"]})
        self.controller.move_sprite = self.move_sprite
        original_kinds = SimpleNamespace(player=0, enemy=1, projectile=2, create=self.next_kind)
        self.ns = {
            "Sprite": Sprite, "Image": Art, "number": float, "namespace": lambda cls: cls,
            "SpriteKind": original_kinds, "img": img, "hex": bytes.fromhex, "Buffer": bytes,
            "SpriteFlag": SimpleNamespace(DESTROY_ON_WALL="destroy_on_wall"),
            "ControllerButtonEvent": SimpleNamespace(PRESSED="pressed"),
            "TileScale": SimpleNamespace(SIXTEEN=4),
            "WaveShape": SimpleNamespace(TRIANGLE="triangle", NOISE="noise", SINE="sine", SAWTOOTH="sawtooth", SQUARE="square"),
            "SoundExpressionEffect": SimpleNamespace(NONE="none", VIBRATO="vibrato"),
            "InterpolationCurve": SimpleNamespace(CURVE="curve", LINEAR="linear"),
            "music": SimpleNamespace(
                PlaybackMode=SimpleNamespace(LOOPING_IN_BACKGROUND="loop", IN_BACKGROUND="background"),
                string_playable=lambda text, tempo: ("melody", text, tempo),
                create_sound_effect=lambda *args: ("effect",) + args,
                play=lambda playable, mode: self.audio_events.append(("play", playable, mode)),
                set_volume=lambda volume: self.audio_events.append(("volume", volume)),
                stop_all_sounds=lambda: self.audio_events.append(("stop",))),
            "effects": SimpleNamespace(disintegrate="disintegrate", fountain="fountain", confetti="confetti"),
            "image": SimpleNamespace(create=Art), "controller": self.controller,
            "sprites": SimpleNamespace(create=self.create_sprite,
                                       create_projectile_from_sprite=self.projectile,
                                       all_of_kind=self.all_of_kind,
                                       on_overlap=lambda a, b, callback: self.overlaps.update({(a, b): callback})),
            "tiles": SimpleNamespace(get_tile_location=lambda x, y: (x, y),
                                     place_on_tile=self.place,
                                     create_tilemap=self.create_tilemap,
                                     set_current_tilemap=self.set_map,
                                     set_wall_at=lambda tile, wall: self.walls.update({tile: wall})),
            "scene": SimpleNamespace(camera_follow_sprite=lambda sprite: None,
                                     set_background_color=lambda color: None),
            "game": SimpleNamespace(runtime=lambda: self.now,
                                    splash=lambda *args: None,
                                    set_game_over_playable=self.set_game_over_playable,
                                    over=self.game_over,
                                    on_update=self.updates.append,
                                    on_update_interval=lambda period, callback: self.intervals.append((period, callback))),
            "info": SimpleNamespace(set_life=self.set_life, set_score=self.set_score,
                                    change_score_by=self.change_score,
                                    change_life_by=self.change_life, life=lambda: self.life_count,
                                    on_life_zero=self.on_life_zero),
        }
        tree = ast.parse((ROOT / "main.py").read_text(encoding="utf-8"))
        # Arcade adds char_at to strings; CPython uses equivalent indexing.
        class ArcadeStrings(ast.NodeTransformer):
            def visit_Call(self, node):
                node = self.generic_visit(node)
                if isinstance(node.func, ast.Attribute) and node.func.attr == "char_at":
                    return ast.copy_location(ast.Subscript(node.func.value, node.args[0], ast.Load()), node)
                return node
        tree = ast.fix_missing_locations(ArcadeStrings().visit(tree))
        # MakeCode namespace classes extend the built-in namespace. CPython's
        # normal classes do not, so preserve the three built-in kind constants.
        class ArcadeNamespaces(ast.NodeTransformer):
            def visit_ClassDef(self, node):
                if node.name == "SpriteKind":
                    for name in ["player", "enemy", "projectile"]:
                        node.body.append(ast.Assign([ast.Name(name, ast.Store())], ast.Constant(getattr(original_kinds, name))))
                return node
        tree = ast.fix_missing_locations(ArcadeNamespaces().visit(tree))
        exec(compile(tree, str(ROOT / "main.py"), "exec"), self.ns)

    def next_kind(self):
        kind = self.kind_counter
        self.kind_counter += 1
        return kind

    def create_sprite(self, art, kind):
        sprite = Sprite(art, kind)
        self.active.append(sprite)
        return sprite

    def projectile(self, art, source, vx, vy):
        sprite = self.create_sprite(art, self.ns["SpriteKind"].projectile)
        sprite.x, sprite.y, sprite.vx, sprite.vy = source.x, source.y, vx, vy
        return sprite

    def all_of_kind(self, kind):
        return [sprite for sprite in self.active if sprite.kind == kind and not sprite.destroyed]

    def move_sprite(self, sprite, vx, vy):
        sprite.move_speed = (vx, vy)

    def place(self, sprite, tile):
        sprite.x, sprite.y = tile[0] * 16 + 8, tile[1] * 16 + 8

    def set_map(self, data):
        self.map = data
        self.walls = {}

    def create_tilemap(self, data, layer, images, scale):
        # Model the public argument contract, not MakeCode's type inference.
        assert isinstance(data, bytes), "Tilemap data must be a hex Buffer"
        assert isinstance(layer, Art), "Tilemap layer must be an Image"
        width = int.from_bytes(data[:2], "little")
        height = int.from_bytes(data[2:4], "little")
        assert (layer.width, layer.height) == (width, height)
        assert len(data) == 4 + width * height
        assert all(index < len(images) for index in data[4:])
        assert scale == 4  # Arcade stores the log2 tile-size enum.
        return data

    def game_over(self, won, effect=None):
        if self.result is not None:
            return
        self.result = won
        if won in self.game_over_sounds:
            playable, looping = self.game_over_sounds[won]
            self.audio_events.append(("play", playable, "loop" if looping else "background"))

    def set_game_over_playable(self, won, playable, looping):
        self.game_over_sounds[won] = (playable, looping)

    def set_life(self, value):
        self.life_count = value

    def set_score(self, value):
        self.score = value

    def change_life(self, delta):
        self.life_count += delta
        if self.life_count <= 0:
            if self.life_zero_callback:
                self.life_zero_callback()
            else:
                self.game_over(False)

    def on_life_zero(self, callback):
        self.life_zero_callback = callback

    def change_score(self, delta):
        self.score += delta

    def overlap(self, a, b):
        if not a.destroyed and not b.destroyed:
            self.overlaps[(a.kind, b.kind)](a, b)

    def advance(self, milliseconds):
        self.now += milliseconds
        for callback in self.updates:
            callback()

    @property
    def hero(self):
        return self.ns["pip"]

    @property
    def kinds(self):
        return self.ns["SpriteKind"]

    def collect_all(self):
        for drum in self.all_of_kind(self.kinds.Fragment):
            self.overlap(self.hero, drum)


class GameContracts(unittest.TestCase):
    def setUp(self):
        self.r = Runtime()

    def test_tilemap_literals_avoid_buffer_inference_regression(self):
        tree = ast.parse((ROOT / "main.py").read_text(encoding="utf-8"))
        calls = [node for node in ast.walk(tree)
                 if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                 and isinstance(node.func.value, ast.Name)
                 and node.func.value.id == "tiles" and node.func.attr == "create_tilemap"]
        self.assertEqual(len(calls), 3)
        for call in calls:
            self.assertEqual(len(call.args), 4)
            data = call.args[0]
            self.assertIsInstance(data, ast.Call)
            self.assertIsInstance(data.func, ast.Name)
            self.assertEqual(data.func.id, "hex")
            self.assertEqual(len(data.args), 1)
            self.assertIsInstance(data.args[0], ast.Constant)
            self.assertIsInstance(data.args[0].value, str)
            self.assertEqual(len(bytes.fromhex(data.args[0].value)), 388)
        # Standalone pasted MakeCode Python cannot import local source modules.
        self.assertFalse(any(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree)))

    def test_assets_and_map_bytes(self):
        for name in ["HERO_IDLE", "HERO_WALK", "ENEMY_IMAGE", "DRUM_IMAGE", "EXIT_IMAGE", "PULSE_IMAGE"]:
            self.assertEqual((self.r.ns[name].width, self.r.ns[name].height), (16, 16))
        for level in range(1, 4):
            self.r.ns['load_world_map'](level - 1, Art(), Art())
            data = self.r.map
            rows = self.r.ns[f"WORLD_{level}"]
            self.assertEqual(data[:4], bytes([32, 0, 12, 0]))
            self.assertEqual(len(data), 388)
            self.assertEqual(len(rows), 12)
            self.assertTrue(all(len(row) == 32 for row in rows))
            self.assertEqual(data[4:], bytes(2 if tile == "#" else 1 for row in rows for tile in row))

    def test_all_floors_and_gameplay_points_reachable(self):
        points = [(2, 6), (29, 6), (8, 3), (16, 8), (25, 3), (10, 7), (19, 3), (26, 8)]
        for level in range(1, 4):
            rows = self.r.ns[f"WORLD_{level}"]
            floor = {(x, y) for y, row in enumerate(rows) for x, tile in enumerate(row) if tile == "."}
            seen, pending = {points[0]}, deque([points[0]])
            while pending:
                x, y = pending.popleft()
                for neighbor in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if neighbor in floor and neighbor not in seen:
                        seen.add(neighbor)
                        pending.append(neighbor)
            self.assertEqual(seen, floor, f"Disconnected floor in world {level}")
            self.assertTrue(all(point in seen for point in points))

    def test_startup_population_walls_and_follow(self):
        self.assertEqual(self.r.life_count, 5)
        self.assertEqual(self.r.score, 0)
        self.assertEqual((self.r.hero.x, self.r.hero.y), (40, 104))
        self.assertEqual(len(self.r.all_of_kind(self.r.kinds.Fragment)), 3)
        self.assertEqual(len(self.r.all_of_kind(self.r.kinds.Portal)), 1)
        enemies = self.r.all_of_kind(self.r.kinds.enemy)
        self.assertEqual(len(enemies), 3)
        self.assertTrue(all(enemy.target is self.r.hero and enemy.follow_speed == 22 for enemy in enemies))
        rows = self.r.ns["WORLD_1"]
        self.assertEqual(self.r.walls, {(x, y): tile == "#" for y, row in enumerate(rows) for x, tile in enumerate(row)})

    def test_projectile_direction_cooldown_and_hit_score(self):
        self.r.controller.up.pressed = True
        self.r.advance(1)
        self.r.controller.A.press()
        self.r.controller.A.press()
        pulses = self.r.all_of_kind(self.r.kinds.projectile)
        self.assertEqual(len(pulses), 1)
        pulse = pulses[0]
        self.assertEqual((pulse.vx, pulse.vy, pulse.lifespan), (0, -150, 900))
        self.assertTrue(pulse.flags["destroy_on_wall"])
        enemy = self.r.all_of_kind(self.r.kinds.enemy)[0]
        self.r.overlap(pulse, enemy)
        self.assertTrue(pulse.destroyed and enemy.destroyed)
        self.assertEqual(self.r.score, 2)
        self.r.overlap(pulse, enemy)
        self.assertEqual(self.r.score, 2)
        self.r.advance(250)
        self.r.controller.A.press()
        self.assertEqual(len(self.r.all_of_kind(self.r.kinds.projectile)), 1)

    def test_portal_gate_pickups_and_level_cleanup(self):
        old_portal = self.r.ns["portal"]
        self.r.overlap(self.r.hero, old_portal)
        self.assertEqual(self.r.ns["level_index"], 0)
        drum = self.r.all_of_kind(self.r.kinds.Fragment)[0]
        self.r.overlap(self.r.hero, drum)
        self.r.overlap(self.r.hero, drum)
        self.assertEqual((self.r.ns["pieces"], self.r.score), (1, 10))
        self.r.overlap(self.r.hero, old_portal)
        self.assertEqual(self.r.ns["level_index"], 0)
        self.r.collect_all()
        self.assertEqual(old_portal.speech, "OPEN!")
        self.r.controller.A.press()
        old_sprites = [sprite for sprite in self.r.active if sprite is not self.r.hero]
        self.r.set_life(3)
        self.r.overlap(self.r.hero, old_portal)
        self.assertEqual((self.r.ns["level_index"], self.r.ns["pieces"], self.r.life_count), (1, 0, 4))
        self.assertTrue(all(sprite.destroyed for sprite in old_sprites))
        expected = bytes([32, 0, 12, 0]) + bytes(2 if ch == '#' else 1 for row in self.r.ns['WORLD_2'] for ch in row)
        self.assertEqual(self.r.map, expected)
        self.assertEqual(len(self.r.all_of_kind(self.r.kinds.projectile)), 0)
        self.assertTrue(all(enemy.follow_speed == 28 for enemy in self.r.all_of_kind(self.r.kinds.enemy)))

    def test_three_worlds_victory_and_life_cap(self):
        for expected in range(3):
            self.assertEqual(self.r.ns["level_index"], expected)
            self.r.collect_all()
            self.r.overlap(self.r.hero, self.r.ns["portal"])
        self.assertTrue(self.r.result)
        self.assertEqual(self.r.score, 90)
        self.assertEqual(self.r.life_count, 5)
        self.assertTrue(self.r.ns["changing_level"])

    def test_dash_expiry_and_cooldown_boundary(self):
        self.r.controller.B.press()
        self.assertEqual((self.r.hero.vx, self.r.hero.vy), (190, 0))
        self.assertEqual(self.r.hero.move_speed, (0, 0))
        self.r.advance(249)
        self.assertEqual(self.r.hero.move_speed, (0, 0))
        self.r.advance(1)
        self.assertEqual(self.r.hero.move_speed, (75, 75))
        self.assertEqual((self.r.hero.vx, self.r.hero.vy), (0, 0))
        self.r.advance(1249)
        self.r.controller.B.press()
        self.assertEqual(self.r.ns["dash_until"], 0)
        self.r.advance(1)
        self.r.controller.B.press()
        self.assertEqual(self.r.ns["dash_until"], 1750)

    def test_damage_spawn_grace_repeat_grace_and_dash_immunity(self):
        enemy = self.r.all_of_kind(self.r.kinds.enemy)[0]
        self.r.overlap(self.r.hero, enemy)
        self.assertEqual(self.r.life_count, 5)
        self.r.advance(1200)
        self.r.overlap(self.r.hero, enemy)
        self.r.overlap(self.r.hero, enemy)
        self.assertEqual(self.r.life_count, 4)
        self.r.advance(1200)
        self.r.controller.B.press()
        self.r.overlap(self.r.hero, enemy)
        self.assertEqual(self.r.life_count, 4)
        self.r.advance(250)
        self.r.overlap(self.r.hero, enemy)
        self.assertEqual(self.r.life_count, 3)

    def test_spawning_is_bounded_and_away_from_hero(self):
        spawn = next(callback for period, callback in self.r.intervals if period == 6000)
        for _ in range(100):
            spawn()
        self.assertEqual(len(self.r.all_of_kind(self.r.kinds.enemy)), 6)
        enemies = self.r.all_of_kind(self.r.kinds.enemy)
        enemies[0].destroy()
        self.r.place(self.r.hero, (10, 7))
        spawn()
        latest = self.r.all_of_kind(self.r.kinds.enemy)[-1]
        self.assertGreater(abs(latest.x - self.r.hero.x) + abs(latest.y - self.r.hero.y), 100)
        self.assertFalse(self.r.walls[(int(latest.x // 16), int(latest.y // 16))])

    def test_transition_lock_blocks_actions_and_spawning(self):
        self.r.ns["changing_level"] = True
        initial_population = len(self.r.active)
        initial_audio = list(self.r.audio_events)
        self.r.controller.A.press()
        self.r.controller.B.press()
        next(callback for period, callback in self.r.intervals if period == 6000)()
        self.r.overlap(self.r.hero, self.r.all_of_kind(self.r.kinds.Fragment)[0])
        self.r.advance(2000)
        self.r.overlap(self.r.hero, self.r.all_of_kind(self.r.kinds.enemy)[0])
        self.assertEqual(len(self.r.active), initial_population)
        self.assertEqual((self.r.score, self.r.life_count, self.r.ns["pieces"]), (0, 5, 0))
        self.assertEqual(self.r.audio_events, initial_audio)

    def test_map_music_changes_per_level_and_stops_on_victory(self):
        def loops():
            return [event for event in self.r.audio_events if event[0] == "play" and event[2] == "loop"]
        self.assertEqual(len(loops()), 1)
        self.assertEqual(loops()[0][1][1], self.r.ns["MEADOW_TRACK"])
        self.r.ns["start_map_music"](0)
        self.assertEqual(len(loops()), 1, "Duplicate map requests must not restart music")
        for level, track in [(1, "QUARRY_TRACK"), (2, "GROVE_TRACK")]:
            self.r.collect_all()
            self.r.overlap(self.r.hero, self.r.ns["portal"])
            self.assertEqual(loops()[-1][1][1], self.r.ns[track])
            self.assertEqual(self.r.ns["map_music_level"], level)
        self.assertEqual(len({event[1][1] for event in loops()}), 3)
        self.r.collect_all()
        stop_count = self.r.audio_events.count(("stop",))
        self.r.overlap(self.r.hero, self.r.ns["portal"])
        self.assertTrue(self.r.result)
        self.assertEqual(self.r.ns["map_music_level"], -1)
        self.assertEqual(self.r.audio_events.count(("stop",)), stop_count + 1)
        self.assertEqual(self.r.audio_events[-1][2], "background")
        self.assertIn(True, self.r.game_over_sounds)
        self.assertFalse(self.r.game_over_sounds[True][1])
        self.assertIn("C6:3", self.r.game_over_sounds[True][0][1])

    def test_sound_effects_follow_mechanics_and_respect_cooldowns(self):
        calls = []
        names = ["shot", "dash", "pickup", "damage", "unlock", "transition", "victory", "defeat", "enemy_hit"]
        for name in names:
            key = "play_" + name + "_sound"
            self.assertIn(key, self.r.ns)
            original = self.r.ns[key]
            def tracked(original=original, name=name):
                calls.append(name)
                original()
            self.r.ns[key] = tracked
        self.r.controller.A.press()
        self.r.controller.A.press()
        self.assertEqual(calls.count("shot"), 1)
        pulse = self.r.all_of_kind(self.r.kinds.projectile)[0]
        enemy = self.r.all_of_kind(self.r.kinds.enemy)[0]
        self.r.overlap(pulse, enemy)
        self.assertEqual(calls.count("enemy_hit"), 1)
        self.r.controller.B.press()
        self.r.controller.B.press()
        self.assertEqual(calls.count("dash"), 1)
        enemy = self.r.all_of_kind(self.r.kinds.enemy)[0]
        self.r.overlap(self.r.hero, enemy)
        self.assertNotIn("damage", calls)
        self.r.advance(1200)
        self.r.overlap(self.r.hero, enemy)
        self.r.overlap(self.r.hero, enemy)
        self.assertEqual(calls.count("damage"), 1)
        stop_count = self.r.audio_events.count(("stop",))
        self.r.collect_all()
        self.assertEqual(calls.count("pickup"), 3)
        self.assertEqual(calls.count("unlock"), 1)
        self.assertEqual(self.r.audio_events.count(("stop",)), stop_count,
                         "Ordinary sound effects must not stop the map music")
        self.r.overlap(self.r.hero, self.r.ns["portal"])
        self.assertEqual(calls.count("transition"), 1)
        # On defeat, stop the loop and play the terminal cue once.
        self.r.set_life(1)
        self.r.advance(1200)
        self.r.overlap(self.r.hero, self.r.all_of_kind(self.r.kinds.enemy)[0])
        self.assertFalse(self.r.result)
        self.assertEqual(calls.count("defeat"), 1)
        self.assertEqual(self.r.ns["map_music_level"], -1)
        self.assertIn(False, self.r.game_over_sounds)
        self.assertFalse(self.r.game_over_sounds[False][1])
        self.assertIn("G3:3", self.r.game_over_sounds[False][0][1])
        self.assertEqual(self.r.audio_events[-1],
                         ("play", self.r.game_over_sounds[False][0], "background"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
