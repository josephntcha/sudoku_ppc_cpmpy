import cpmpy as cp

SOLVER = "ortools"
grid = cp.intvar(1, 9, shape = (9,9), name ='grid')

#constraintes
constraintes = []
for i in range(9):
    constraintes.append(cp.AllDifferent(grid[i,:]))
    constraintes.append(cp.AllDifferent(grid[:, i]))
    constraintes.append(cp.AllDifferent(grid[3*(i//3):3*((i//3)+1), 3*(i%3):3*((i%3)+1)]))
m = cp.Model(constraintes)

trouver = m.solve(solver=SOLVER)
print(grid.value())
 

    
