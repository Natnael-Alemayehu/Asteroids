
# Asteroids

A compact, readable Python implementation of the classic "Asteroids" game built with Pygame. This repository contains a small, well-structured codebase intended for learning game loops, sprite management, simple physics, and collision handling in a 2D environment.

## Features

- Player-controlled ship with rotation, forward/backward movement, and shooting.
- Procedural asteroid spawning and splitting on impact.
- Simple collision detection between circular sprites.
- Lightweight event and state logging for debugging and replay analysis.

## Requirements

- Python 3.13 or newer (configured in `pyproject.toml`).
- Pygame 2.6.1 (or compatible release).

Install dependencies with pip or an editable install during development (examples below).

## Installation

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the project dependencies:

```bash
pip install -r requirements.txt  # if you create one
pip install pygame==2.6.1
```

Alternatively, use the project metadata in `pyproject.toml` for packaging and dependency management.

## Running the Game

Start the game from the repository root:

```bash
python main.py
```

The game opens a Pygame window and runs the main loop defined in `main.py`.

## Controls

- `A`: Rotate left
- `D`: Rotate right
- `W`: Move forward
- `S`: Move backward
- `Space`: Fire shot

## Project Structure

- `main.py` — Application entry point and game loop. Initializes Pygame, sprite groups, and orchestrates update/draw cycles.
- `constants.py` — Centralized constants for screen size, speeds, radii, and spawn rates.
- `player.py` — `Player` sprite: handles input, movement, rotation, and firing shots.
- `shot.py` — `Shot` sprite: short-lived projectile object.
- `asteroid.py` — `Asteroid` sprite: movement and splitting logic.
- `asteroidfield.py` — Asteroid spawner and field manager; controls spawn timing and placement.
- `circleshape.py` — Base class `CircleShape` providing positional, velocity, radius data, and collision helper.
- `logger.py` — Lightweight logging utility that writes `game_state.jsonl` and `game_events.jsonl` for debugging and analysis.

## Logging

The repository includes `logger.py`, which emits two newline-delimited JSON log files in the working directory when the game runs:

- `game_state.jsonl` — periodic snapshots of selected game state.
- `game_events.jsonl` — discrete events like asteroid splits and player hits.

These files are intended for debugging and simple offline inspection.

## Development

Suggested workflow for contributors or when developing locally:

1. Create and activate a virtual environment (see Installation).
2. Install Pygame and any tooling you prefer (formatters, linters).
3. Run the game with `python main.py` and iterate on modules.

Notes:
- The code uses Pygame's `Vector2` for positions and velocities and `pygame.sprite.Group` for simple scene management.
- Constants are defined in `constants.py` for easy tuning of gameplay behavior.

## Contributing

Contributions are welcome. For small changes (bug fixes, doc improvements, refactors), open a pull request with a clear description of the change and motivation. For larger features, open an issue first to discuss design and scope.

Guidelines:
- Keep changes focused and well-documented.
- Follow Python best practices and project style.

## License

No license is included in this repository. If you intend to publish this project on GitHub and permit reuse, add a `LICENSE` file (for example, the MIT license) and reference it here.

## Acknowledgements

This project is a focused educational implementation inspired by the classic arcade game "Asteroids" and intended for learning Pygame and simple game architecture patterns.

