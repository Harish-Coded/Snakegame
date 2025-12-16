## 🚀 Features of the Game

The game implements the core mechanics of the classic Snake game:

### 1. Core Gameplay
* **Grid-Based Movement:** The snake moves in fixed increments (10 pixels), simulating movement on a grid.
* **Snake Growth:** When the snake consumes food, it grows by one segment, and the player's score increases.
* **Persistent Movement:** The snake continuously moves in the current direction.

### 2. Controls and Input
* **Arrow Key Control:** Uses the four directional arrow keys for movement.
* **Direction Validation:** Prevents the snake from making an immediate 180-degree turn (a standard Snake mechanic).
* **Escape Key Exit:** Allows quick termination of the game by pressing the `ESC` key.

### 3. Game State Management
* **Game Over Conditions:** The game ends upon **Wall Collision** (hitting the $700 \times 400$ boundary) or **Self-Collision** (hitting its own body).
* **Score System:** Tracks the current score and displays it during gameplay and upon the Game Over screen.
* **Game Over Screen:** Displays a clear "GAME OVER" message along with the final score.

### 4. Graphics and Display
* **Window Setup:** A dedicated $700 \times 400$ pixel window displays the gameplay.
* **Drawing:** Utilizes Pygame's drawing functions to render the snake (green blocks) and food (red block).
* **FPS Control:** The game speed is regulated at 20 frames per second (FPS) for consistent play.
* **Initial Greeting:** Displays a startup message before the game loop starts.

## 💻 Technology Stack

The game is built using a focused and accessible tech stack:

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Primary language for all logic and structure. |
| **Game Engine/Library** | Pygame | Core framework for graphics rendering, input processing, and game loop management. |
| **Time Management** | `pygame.time.Clock` | Used to manage and enforce the game's frame rate (20 FPS). |
| **Randomization** | Python's `random` module | Used to determine the random coordinates for food spawning. |
