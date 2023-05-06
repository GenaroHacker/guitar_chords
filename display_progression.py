from PIL import Image
import IPython.display as display
import os

def display_progression(chord_list):
    # Add the prefix and suffix to each item in the list
    chord_list = [f"/content/guitar_chords/chords/{chord}.png" for chord in chord_list]

    # Define the number of columns
    columns = 4
    rows = (len(chord_list) + columns - 1) // columns

    # Initialize the new image
    images = [Image.open(chord) for chord in chord_list]
    width, height = images[0].size
    result_image = Image.new("RGBA", (width * columns, height * rows))

    # Paste the images into the new image
    for index, image in enumerate(images):
        x = (index % columns) * width
        y = (index // columns) * height
        result_image.paste(image, (x, y))

    # Display the resulting image
    display.display(result_image)
