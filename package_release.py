"""Bundle the game, audio previews, development workflow and validation evidence."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
names = ['main.py', 'README.md', 'DESIGN.md', 'AGENT_ARCHITECTURE.md', 'AUDIO.md',
         'VALIDATION.md', 'TEST_REVIEW.md', 'Find-My-Drum-Audio-project.png',
         'assets.py', 'worlds.py', 'gameplay.py', 'soundtrack.py', 'sound_effects.py',
         'build_game.py', 'validate_game.py', 'render_audio_previews.py',
         'requirements-workflow.txt', 'run_workflow.bat', 'package_release.py',
         'compiler/package.json', 'compiler/pnpm-lock.yaml',
         'compiler/check_game.js', 'compiler/package_game.js']
files = [ROOT / name for name in names]
files += [p for p in (ROOT / 'workflow').rglob('*')
          if p.is_file() and '__pycache__' not in p.parts and p.suffix in {'.py','.json','.md','.mmd'}]
files += list((ROOT / 'audio-previews').glob('*.wav'))
files += [p for p in (ROOT / 'compiler' / 'results').glob('*')
          if p.is_file() and p.suffix in {'.json','.ts','.js'}]
destination = ROOT / 'Find-My-Drum.zip'
with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
    for file in sorted(set(files)):
        if not file.exists():
            raise FileNotFoundError(file)
        archive.write(file, file.relative_to(ROOT).as_posix())
print('Packaged', len(set(files)), 'files:', destination.name, destination.stat().st_size, 'bytes')
