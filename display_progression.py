from PIL import Image
import IPython.display as display
import os

def display_progression(chord_list, columns=4):
    # Add the prefix and suffix to each item in the list
    chord_list = [f"/content/guitar_chords/chords/{chord}.png" for chord in chord_list]

    # Calculate the number of rows based on the number of columns
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
