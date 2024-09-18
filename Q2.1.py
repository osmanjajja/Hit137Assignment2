import time
from PIL import Image

# Step 1: Generate the number (n) using the provided algorithm
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated number (n): {generated_number}")

# Step 2: Open the image
image_path = "D:\CDU-MsCyberSecurity\Semester2\HIT137-SoftwareNow\Hit137Assignment2\chapter1.jpg"
image = Image.open(image_path)
pixels = image.load()

# Step 3: Modify the image pixels
width, height = image.size
new_image = Image.new('RGB', (width, height))

# Initialize sum of red pixel values
red_pixel_sum = 0

for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        new_r = min(r + generated_number, 255)
        new_g = min(g + generated_number, 255)
        new_b = min(b + generated_number, 255)
        new_image.putpixel((x, y), (new_r, new_g, new_b))

        # Sum the red pixel values in the new image
        red_pixel_sum += new_r

# Step 4: Save the new image
output_image_path = "chapter1out.png"
new_image.save(output_image_path)
print(f"New image saved as {output_image_path}")

# Step 5: Print the sum of red pixel values
print(f"Sum of red pixel values: {red_pixel_sum}")
