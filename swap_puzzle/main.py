from grid import Grid
from solver import Solver
g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
Grid.find(g,3)
print(Grid.find(g,3))

grid = Grid.grid_from_file("../input/grid1.in")
Grid.swap_seq(grid,Solver.get_solution(grid))