from tkinter import *
from tkinter import messagebox
from midiutil import MIDIFile
import random

# Generate Music Function
def generate_music():

    # Create MIDI object
    midi = MIDIFile(1)

    track = 0
    time = 0

    midi.addTrackName(track, time, "AI Music")
    midi.addTempo(track, time, 120)

    # Musical Notes
    notes = [60, 62, 64, 65, 67, 69, 71, 72]

    # Generate Random Melody
    for i in range(20):

        pitch = random.choice(notes)
        duration = random.choice([0.5, 1, 1.5])
        volume = random.randint(70, 100)

        midi.addNote(
            track,
            0,
            pitch,
            time,
            duration,
            volume
        )

        time += duration

    # Save MIDI File
    with open("ai_generated_music.mid", "wb") as output_file:
        midi.writeFile(output_file)

    messagebox.showinfo(
        "Success",
        "AI Music Generated Successfully!\nSaved as ai_generated_music.mid"
    )

# Main Window
root = Tk()
root.title("AI Music Generator")
root.geometry("650x500")
root.config(bg="#121212")

# Header
title = Label(
    root,
    text="🎵 AI Music Generator",
    font=("Helvetica", 24, "bold"),
    bg="#121212",
    fg="#00FFCC"
)
title.pack(pady=30)

# Description
desc = Label(
    root,
    text="Generate Random AI-Based MIDI Music",
    font=("Arial", 14),
    bg="#121212",
    fg="white"
)
desc.pack(pady=10)

# Generate Button
generate_btn = Button(
    root,
    text="Generate Music",
    font=("Arial", 16, "bold"),
    bg="#00ADB5",
    fg="white",
    padx=20,
    pady=10,
    command=generate_music
)
generate_btn.pack(pady=40)

# Info Box
info = Label(
    root,
    text="""
Features:
✔ AI-inspired melody generation
✔ MIDI music export
✔ Random musical notes
✔ Beginner-friendly AI project
""",
    font=("Arial", 12),
    bg="#121212",
    fg="#EEEEEE",
    justify=LEFT
)
info.pack(pady=20)

# Footer
footer = Label(
    root,
    text="VertexMind AI Internship Project",
    font=("Arial", 10),
    bg="#121212",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=20)

# Run App
root.mainloop()