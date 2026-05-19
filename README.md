# ChessVar – King Of The Hills Chess Variant

A Python implementation of the chess variant "King Of The Hills".

## Overview

This project implements an abstract board game based on the chess variant "King Of The Hills". The game follows standard chess movement rules with several modified win conditions and simplified gameplay mechanics.

The game is implemented using object-oriented programming in Python through a `ChessVar` class that manages:
- the game board,
- player turns,
- legal movement validation,
- capturing pieces,
- and determining the game winner.

---

## Features

- Standard chess board setup
- Full piece movement validation
- Turn-based gameplay
- Piece capturing
- Win by:
  - capturing the opponent's king
  - moving your king to one of the four center squares:
    - d4
    - e4
    - d5
    - e5
- Legal king movement into check
- No:
  - check/checkmate
  - castling
  - en passant
  - pawn promotion

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)

---

## Class Methods

### `__init__()`
Initializes the chess board, pieces, player turn, and game state.

### `get_game_state()`
Returns:
- `UNFINISHED`
- `WHITE_WON`
- `BLACK_WON`

### `get_board()`
Returns the current game board.

### `make_move(from_square, to_square)`
Attempts to move a piece from one square to another.

Returns:
- `True` if the move is successful
- `False` if the move is invalid

---

## Example Usage

```python
game = ChessVar()

game.make_move('e2', 'e4')
game.make_move('e7', 'e5')

print(game.get_game_state())
```

---

## Project Concepts

This project demonstrates:
- Object-oriented programming
- Board representation using nested lists
- Turn management
- Movement validation logic
- Game state management
- Coordinate conversion using algebraic notation
- Conditional logic and rule enforcement

---







