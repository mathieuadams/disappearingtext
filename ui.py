from tkinter import *
from start_prompt import starting_sentence

THEME_COLOR = "#dcd5cd"

class DisappearingTextUI():
    def __init__(self):
        self.timer =60
        self.window = Tk()
        self.window.title("Disappearing Text")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas_frame = Frame(self.window)
        self.canvas_frame.grid(row=1, column=0, columnspan=7, pady=10)
        self.canvas = Canvas(self.canvas_frame, width=800, height=300, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        # --- Canvas with scrollbar ---

        self.scrollbar = Scrollbar(self.canvas_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.sentence = starting_sentence()

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.starting_sentence_label = Label(text=self.sentence, bg=THEME_COLOR, font=('Arial', 18))
        self.starting_sentence_label.grid(row=0, column=1, columnspan=5)

        self.RESET_btn = Button(text="Generate", width=13, command=self.reset_button, font=('Arial', 18))
        self.RESET_btn.grid(row=0, column=6)

        self.DISPLAY_TIMER_label = Label(text=f" {self.timer}", font=('Arial', 30))
        self.DISPLAY_TIMER_label.grid(row=2, column=0, columnspan=7)

        self.input_text_entry = Text(font=('arial.ttf', 20))
        self.input_text_entry.grid(row=1, column=0, columnspan=7)
        self.input_text_entry.bind("<KeyPress>", self.start_typing)
        self.typed_word = None
        self.timer_callback = None
        self.timer_started = False
        self.ready_for_input = False
        self.window.mainloop()


    def start_timer(self):
        if self.timer == 0:
            self.reset_button()
            return

        self.timer -= 1
        self.DISPLAY_TIMER_label.config(text=f" {self.timer}")
        self.timer_callback=self.window.after(1000, self.start_timer)



    def reset_button(self):
        self.sentence = starting_sentence()
        if self.timer_callback is not None:
            self.window.after_cancel(self.timer_callback)
            self.timer_callback = None


        self.timer=60
        self.timer_started = False  # <--- reset here
        self.DISPLAY_TIMER_label.config(text=f" {self.timer}")
        self.starting_sentence_label.config(text=f"{self.sentence}")
        self.input_text_entry.delete("1.0", END)

    def start_typing(self, event):
        # Ignore non-character keypresses (e.g. shift, ctrl)
        if not event.char or not event.char.isprintable():
            return

        # Reset timer to 60 on keypress
        self.timer = 60
        self.DISPLAY_TIMER_label.config(text=f"{self.timer}")

        # Start the timer if not started
        if not self.timer_started:
            self.timer_started = True
            self.start_timer()



sol = DisappearingTextUI()
sol