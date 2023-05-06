from guitar_chords.note import Note
def build_progression(root, chord_progression):
    chord_semitones = {
        "i": 0,
        "ii": 2,
        "iii": 4,
        "iv": 5,
        "v": 7,
        "vi": 9,
        "vii": 11
    }

    # Lowercase all the keys that are strings
    for chord in chord_progression:
        if isinstance(chord[0], str):
            chord[0] = chord[0].lower()

    # Replace string keys with their values in the chord_semitones dictionary
    for chord in chord_progression:
        if isinstance(chord[0], str):
            chord[0] = chord_semitones[chord[0]]

    # Create an instance of the Note class with the given note
    note1 = Note(root)

    # Transpose each key
    for chord in chord_progression:
        chord[0] = note1.transpose(chord[0])

    # Concatenate each key with each value
    result = []
    for chord in chord_progression:
        result.append(chord[0] + chord[1])

    return result



if __name__ == "__main__":
    # Example usage:
    chord_progression = [["I", "6"], [5, "add4"], ["Vi", "7"], [-1, "add4"]]
    note = "C"
    result = chord_progression_transpose(chord_progression, note)
    print(result)
