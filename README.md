# guitar_chords

To run the program run the main.ipynb file.

**Example input:**

("A", [["I", "7"],["I", "7"],["I", "7"],["I", "7"],
      ["IV", "7"],["IV", "7"],["I", "7"],["I", "7"],
      ["V", "7"],["IV", "7"],["I", "7"],["V", "7"],])
      
**Example output:**

![image](https://user-images.githubusercontent.com/95663273/236652133-6b69a298-04db-4162-bb18-bb9d28101493.png)



This program is a library of guitar chords and related functions written in Python. It contains the following files:

-`build_progression.py`

-`chord_library.py`

-`display_progression.py`

-`main.ipynb`





## build_progression.py

This file contains a function called `build_progression` that takes a root note and a chord progression as parameters and returns a list of chords in the specified progression. 


The `build_progression` function relies on the `Note` class from the `note.py` module, which is used to transpose notes. 

`build_progression` takes a root note and a chord progression as input, and returns a list of chords in the given progression, with each chord transposed.

## chord_library.py

This file contains two lists: `roots` and `chords`. `roots` is a list of root notes for chords and `chords` is a list of chord types (e.g. 7, 7sus4, etc.). 

## display_progression.py

This file contains a function called `display_progression` that takes a list of chords and the number of columns for display as parameters and returns an image of the chord progression. 

## main.ipynb

This file contains code for running the program. It imports all the necessary modules, prints out the lists of notes and chords, creates a chord progression, and displays the progression as an image. 
