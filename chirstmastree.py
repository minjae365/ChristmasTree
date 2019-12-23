#given a number, create a christmas tree using only for and if statements
tree_height = 4
tree_root = 2
for i in range(tree_number):
  print((tree_number - i - 1) * ' ' + (2*i + 1) * '*')
  #print((leaf - i - 1)*' ' + '*' + (i*2 + 1)*'='+'*')
  #if wanna do second row, change tree_number - i -1 to tree_number - i
  for j in range(tree_root):
    print((leaf - 1)* ' ' + '|')
