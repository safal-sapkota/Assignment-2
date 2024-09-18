import time
from PIL import Image

def generate_number():
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50
    if generated_number % 2 == 0:
        generated_number += 10
    return generated_number

def modify_image(input_path, output_path):
    # Open the image
    img = Image.open(input_path)
    pixels = img.load()

    # Get the generated number
    n = generate_number()
    print(f"Generated number: {n}")

    # Modify each pixel
    width, height = img.size
    total_red = 0
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            new_r = (r + n) % 256
            new_g = (g + n) % 256
            new_b = (b + n) % 256
            pixels[x, y] = (new_r, new_g, new_b)
            total_red += new_r

    # Save the new image
    img.save(output_path)

    return total_red

# Usage
input_image = "./chapter1.jpg"  # Replace with your input image path
output_image = "Chapter1out.png"
total_red_sum = modify_image(input_image, output_image)
print(f"Sum of all red pixel values: {total_red_sum}")