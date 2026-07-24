import tkinter as tk
import random

FLASHCARDS = [
    ("le", "the (masculine)"),
    ("la", "the (feminine)"),
    ("les", "the (plural)"),
    ("un", "a / one (masculine)"),
    ("une", "a / one (feminine)"),
    ("et", "and"),
    ("à", "to / at"),
    ("de", "of / from"),
    ("en", "in / by"),
    ("dans", "in / inside"),
    ("je", "I"),
    ("tu", "you (informal)"),
    ("il", "he / it"),
    ("elle", "she / it"),
    ("on", "one / we (informal)"),
    ("nous", "we"),
    ("vous", "you (formal / plural)"),
    ("ils", "they (masculine)"),
    ("elles", "they (feminine)"),
    ("être", "to be"),
    ("avoir", "to have"),
    ("faire", "to do / to make"),
    ("aller", "to go"),
    ("pouvoir", "can / to be able to"),
    ("vouloir", "to want"),
    ("dire", "to say / to tell"),
    ("voir", "to see"),
    ("savoir", "to know (a fact)"),
    ("venir", "to come"),
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("French Flashcards")
        self.root.geometry("500x500")
        self.root.configure(bg="#008080")  # teal

        self.french_word = tk.StringVar()
        self.english_word = tk.StringVar()

        # --- Rounded Card ---
        self.card_canvas = tk.Canvas(root, width=350, height=200,
                                     bg="#008080", highlightthickness=0)
        self.card_canvas.pack(pady=40)

        self.rounded_rect(10, 10, 340, 190, radius=25, fill="#b2d8d8")

        # Text inside card
        self.card_canvas.create_text(175, 40, text="French",
                                     font=("Arial", 16, "bold"),
                                     fill="#004c4c")

        self.word_text = self.card_canvas.create_text(
            175, 110,
            text="",
            font=("Arial", 28, "bold"),
            fill="#004c4c"
        )

        # --- Buttons ---
        btn_frame = tk.Frame(root, bg="#008080")
        btn_frame.pack(pady=20)

        wrong_btn = tk.Button(btn_frame, text="✖", font=("Arial", 24),
                              bg="#cc4444", fg="white",
                              width=4, command=self.next_word)
        wrong_btn.grid(row=0, column=0, padx=20)

        right_btn = tk.Button(btn_frame, text="✔", font=("Arial", 24),
                              bg="#44aa44", fg="white",
                              width=4, command=self.show_translation)
        right_btn.grid(row=0, column=1, padx=20)

        # --- Translation Label ---
        self.translation_label = tk.Label(root, textvariable=self.english_word,
                                          font=("Arial", 20, "bold"),
                                          bg="#008080", fg="white")
        self.translation_label.pack(pady=10)

        self.next_word()

    def rounded_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        """Draws a rounded rectangle on the canvas."""
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1
        ]
        return self.card_canvas.create_polygon(points, smooth=True, **kwargs)

    def next_word(self):
        french, english = random.choice(FLASHCARDS)
        self.current_english = english
        self.french_word.set(french)
        self.english_word.set("")
        self.card_canvas.itemconfig(self.word_text, text=french)

    def show_translation(self):
        self.english_word.set(self.current_english)

root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
