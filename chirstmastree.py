#given a number, create a christmas tree using only for and if statements
tree_height = 4
for i in range(tree_number):
  print((tree_number - i - 1) * ' ' + (2*i + 1) * '*')
