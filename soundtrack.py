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
