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
