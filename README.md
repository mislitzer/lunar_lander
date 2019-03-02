# Lunar Lander

Lunar Lander Game by Tobi Heiss & Martin Islitzer. (Python Implementation)

## Prerequisites

Lunar Lander is based on the python module "pymunk", which is a Physics Emulation Module.
Also you have to install the "arcade" module which is responsible for the Drawing.

```
pip install pymunk
pip install arcade
```

## Starting
Run from root.

```
python ./main.py
```

## How to use
The Game is easy to use and has a hand full of "must-knows" to consider.

### Goal
To complete a level successfully you have to touch down on one of the green colored platforms.

### Rules
On landing, if you hit the platform with a "Vertical Speed" higher than 10, you will lose.
Also you have a limited amount of fuel. If your fuel is empty you are not able to navigate your Lander anymore.

### Controls
To move your Lunar Lander UP, RIGHT or LEFT: Simply use the arrow keys. By default the Lander is moving down by a certain velocity.

### Levels & Weight of platforms
Every time if you successfully touch a platform you climb up a level higher. Every platform has a certain weight which increases your actual score. In every level there is a platform where you receive a fuel bonus too. The platform weight and the additional fuel amount is visualized below or above the corresponding platform.