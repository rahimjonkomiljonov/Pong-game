# Pong Game

A classic Pong game implementation using Python's Turtle graphics with two paddles, a ball, and a scoreboard.

## Features
- Two-player paddle control (W/S for left, Up/Down for right)
- Ball bouncing off paddles and top/bottom walls
- Score tracking for both players
- Automatic ball speed increase on paddle hit
- Game reset on miss

## Prerequisites
- Python 3.x
- Required Python packages:
  - `turtle` (included with Python)
- Custom classes:
  - `paddle.py` (Paddle class)
  - `ball.py` (Ball class)
  - `scoreboard.py` (Scoreboard class)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/pong-game.git
cd pong-game
```

2. Ensure all required class files are present:
- `paddle.py`
- `ball.py`
- `scoreboard.py`

## Usage
1. Run the game:
```bash
python pong.py
```

2. Controls:
- Left Paddle: W (up), S (down)
- Right Paddle: Up Arrow (up), Down Arrow (down)
- Exit: Click the window

## How It Works
- **Setup**: 800x600 black window with two paddles and a ball
- **Movement**: Continuous paddle movement while keys are pressed
- **Collision**: Ball bounces off paddles and walls
- **Scoring**: Point awarded when ball passes paddle
- **Reset**: Ball returns to center after scoring

## File Structure
- `pong.py`: Main game script
- `paddle.py`: Paddle class definition
- `ball.py`: Ball class definition
- `scoreboard.py`: Scoreboard class definition

## Game Mechanics
- Window: 800x600 pixels
- Paddle positions: ±350 x-coordinate
- Ball bounce: Top/bottom (±280 y), paddles (±320 x)
- Score trigger: Ball beyond ±380 x
- Speed: Increases on paddle hit

## Controls
- Right Paddle:
  - Up Arrow: Move up
  - Down Arrow: Move down
- Left Paddle:
  - W: Move up
  - S: Move down

## Customization
- Window size: `screen.setup(width=800, height=600)`
- Background: `screen.bgcolor('black')`
- Paddle positions: `Paddle(350)` and `Paddle(-350)`
- Ball speed: Controlled in `ball.move_speed`
- Collision distances: Adjustable in if conditions

## Notes
- Uses `screen.tracer(0)` for manual updates
- Continuous loop with `time.sleep()` for frame rate
- Requires click to exit
- Scoreboard updates on each point
- Ball resets to center after scoring

## Limitations
- No pause functionality
- No win condition
- Basic collision detection
- Requires separate class files

## License
[MIT License](LICENSE)

## Disclaimer
- Ensure all class files are implemented
- Game runs indefinitely until window closed
- No sound effects
- Simple graphics via Turtle
```
