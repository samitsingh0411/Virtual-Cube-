# Cube Manager

A Python library for creating and manipulating virtual 3x3 Rubik's cubes. Useful for **group theory**, **graph theory**, and cube algorithm experiments.

## Quick Start

```python
from CubeManager import RubixCube as Rc

cube = Rc.ThreeByThree(name="MyCube")
print(cube)
```

## Moves

Use the `do()` method with standard notation. See [cube notation](https://solvethecube.com/notation) for details.

```python
cube.do("R")       # Single move
cube.do("U'")      # Prime move
cube.do("R2")      # Double move
cube.do(move_list=["R", "U", "R'"])  # Sequence
cube.do('sexy')    # Named algorithm: ["R", "U", "R'", "U'"]
cube.do('x')       # Whole cube rotation
```

**Supported moves:** R, R', L, L', U, U', D, D', F, F', B, B', M, M', E, E', S, S', r,
r', l, l', u, u', d, d', f, f', b, b', x, x', y, y', z, z' (+ `2` variants like `R2`)

Check `CubeManager/alg_name.py` for all named algorithms.

## Utilities

```python
sequence = cube.shuffle()  # Returns shuffle as move list
cube.solve()
```

## Save & Load

```python
cube.do('sexy')
cube.save()  # Saves to <name>.json in current directory

cube.solve()
cube.load('MyCube.json', cube_name='LoadedCube')  # Restores saved state
print(cube)  # Shows the saved (scrambled) state
```

## Use Cases

- Timing apps needing cube visuals/shuffle sequences
- Group/graph theory experiments with cube operations
- Fun experiments like proving `sexy` x6 = solved state:

```python
for i in range(6):
    cube.do('sexy')
# cube is back to original state
```

