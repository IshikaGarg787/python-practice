rows = 8

# Upper inverted pyramid
for i in range(rows):
    print(' ' * i + '*' * (2 * (rows - i) - 1))

# Lower upright pyramid
for i in range(1, rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

