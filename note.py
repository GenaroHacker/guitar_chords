class Note:
    def __init__(self, note):
        self.note = note
        self.note_order = [
            "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
        ]

    def transpose(self, semitones):
        current_index = self.note_order.index(self.note)
        new_index = (current_index + semitones) % len(self.note_order)
        return self.note_order[new_index]



if __name__ == "__main__":
    # Example usage:
    note1 = Note("C")
    print(note1.transpose(1))  # Output: C#
    print(note1.transpose(-1))  # Output: B

    note2 = Note("G")
    print(note2.transpose(12))  # Output: G
    print(note2.transpose(13))  # Output: G#

    note3 = Note("D#")
    print(note3.transpose(-13))  # Output: D

