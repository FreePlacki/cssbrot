rows, cols = 20, 20

for y in range(1, rows + 1):
    for x in range(1, cols + 1):
        print(f"<div style=\"--x:{x}; --y:{y};\"></div>")
    print()

