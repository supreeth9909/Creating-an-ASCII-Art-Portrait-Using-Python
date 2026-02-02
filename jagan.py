ASCII_CHARS = "@%#*+=-:. "

def read_ppm_p3(filename):
    with open(filename, "r") as f:
        data = f.read().split()

    if data[0] != "P3":
        raise ValueError("Not a P3 ASCII PPM file")

    width = int(data[1])
    height = int(data[2])

    pixels = list(map(int, data[4:]))

    image = []
    i = 0
    for _ in range(height):
        row = []
        for _ in range(width):
            r, g, b = pixels[i], pixels[i+1], pixels[i+2]
            i += 3
            gray = (r + g + b) // 3
            row.append(gray)
        image.append(row)

    return image


def to_ascii(image):
    ascii_img = []
    scale = len(ASCII_CHARS) - 1

    for row in image:
        line = ""
        for px in row:
            line += ASCII_CHARS[px * scale // 255]
        ascii_img.append(line)

    return ascii_img


# -------- MAIN --------
image = read_ppm_p3("output_image_P3 (1).ppm")
ascii_image = to_ascii(image)

with open("ascii_output.txt", "w") as f:
    for line in ascii_image:
        f.write(line + "\n")

print("ASCII art created: ascii_output.txt")
