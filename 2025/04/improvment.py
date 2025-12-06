""" IA generated solution"""

from pathlib import Path
import numpy as np
from scipy.signal import convolve2d

from utils.time_decorator import timer

PATH = Path(__file__).parent / "data.txt"


def parse_file(path: Path) -> np.ndarray:
    """Parse input file into numpy array grid.
    
    Maps '@' to 1, other characters to 0 for efficient computation.
    
    Args:
        path: Path to input file
        
    Returns:
        2D numpy array representing the grid
    """
    with path.open() as file:
        lines = [line.strip() for line in file]
    
    rows = len(lines)
    cols = len(lines[0])
    grid = np.zeros((rows, cols), dtype=np.int8)
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "@":
                grid[i, j] = 1
    
    return grid


def count_adjacent_papers(grid: np.ndarray) -> np.ndarray:
    """Count adjacent '@' cells for each cell using convolution.
    
    Uses a 3x3 kernel to efficiently count neighbors in a single operation.
    
    Args:
        grid: Binary grid where 1 = '@', 0 = other
        
    Returns:
        Array with count of adjacent '@' cells for each position
    """
    kernel = np.ones((3, 3), dtype=np.int8)
    kernel[1, 1] = 0  # Don't count center cell
    
    return convolve2d(grid, kernel, mode='same', boundary='fill')


@timer
def solve(should_loop: bool = False) -> int:
    """Solve the problem using vectorized numpy operations.
    
    Args:
        should_loop: If False, only removes accessible cells once.
                    If True, iteratively removes until no more accessible cells.
    
    Returns:
        Total number of removed cells
    """
    grid = parse_file(PATH)
    total_removed = 0
    first_pass = True
    
    while first_pass or should_loop:
        first_pass = False
        
        # Count neighbors for all cells at once
        adjacent_counts = count_adjacent_papers(grid)
        
        # Find accessible cells: has '@' AND <4 neighbors
        accessible_mask = (grid == 1) & (adjacent_counts < 4)
        
        num_accessible = np.sum(accessible_mask)
        if num_accessible == 0:
            break
        
        # Remove all accessible cells
        grid[accessible_mask] = 0
        total_removed += num_accessible
        
        if not should_loop:
            break
    
    return total_removed


def main() -> None:
    print("Result 1:")
    print(solve(should_loop=False))
    print("Result 2:")
    print(solve(should_loop=True))


if __name__ == "__main__":
    main()
