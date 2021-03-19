
pieces = [[[0x0000AA, 0x0000AA],  # O
           [0x0000AA, 0x0000AA]],
          [[0xC0C0C0, 0x000000, 0x000000],  # J
           [0xC0C0C0, 0xC0C0C0, 0xC0C0C0],
           [0x000000, 0x000000, 0x000000]],
          [[0x000000, 0x000000, 0xAA00AA],  # L
           [0xAA00AA, 0xAA00AA, 0xAA00AA],
           [0x000000, 0x000000, 0x000000]],
          [[0x00AAAA, 0x00AAAA, 0x000000],  # Z
           [0x000000, 0x00AAAA, 0x00AAAA],
           [0x000000, 0x000000, 0x000000]],
          [[0x000000, 0x00AA00, 0x00AA00],  # S
           [0x00AA00, 0x00AA00, 0x000000],
           [0x000000, 0x000000, 0x000000]],
          [[0x000000, 0xAA5500, 0x000000],  # T
           [0xAA5500, 0xAA5500, 0xAA5500],
           [0x000000, 0x000000, 0x000000]],
          [[0x000000, 0x000000, 0x000000, 0x000000],  # I
           [0xAA0000, 0xAA0000, 0xAA0000, 0xAA0000],
           [0x000000, 0x000000, 0x000000, 0x000000],
           [0x000000, 0x000000, 0x000000, 0x000000]]]

hex = "0x000000"
h = hex.split('x')[1]

rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

print(rgb)
