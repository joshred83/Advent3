
from math import prod
def boxed_cell(s, idx):
  s2 = ''
  tree = False
  for i, ch in zip(range(len(s)), s):
    if idx == i:
      s2 += f"[{ch}]"
      if ch == '#':
        tree = True

    else:
       s2 += f" {ch} "
  return s2, tree

def count_trees( ski_slope, coords, slope):
  tree_count = 0
  while coords[1] < len(ski_slope):
    parsed_row, tree = boxed_cell(ski_slope[coords[1]], coords[0])
    print(parsed_row, tree)
    tree_count += tree
    #print(''.join(arr[coords[0]]), arr[coords[0], coords[1] ], coords)
    coords[0] += slope[0]
    coords[1] += slope[1]
    if coords[0] >= len(ski_slope[0]):
      coords[0] -=  len(ski_slope[0])
  return(tree_count)

slopes =[(1,1),
         (3,1),
         (5,1),
         (7,1),
         (1,2)]

with open("toboggan_map_d3") as f:
  ski_slope = [line.strip() for line in f.readlines()]  
  n_trees = []
  for slope in slopes:
    coords = [0,0]
    n_trees.append(count_trees(ski_slope,coords, slope))

print(n_trees)
print(prod(n_trees)    )

  



  
