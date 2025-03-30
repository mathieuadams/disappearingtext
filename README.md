
# 📝 Disappearing Text

A writing app that challenges users to keep typing! If you stop for more than 60 seconds, your work disappears and a new story prompt appears.

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/8cbecd71-0667-49b9-92d5-5c6c5df02319)


## 💡 Features

Random story starter from a set of 50 creative prompts

Countdown timer resets with every keystroke

If you stop typing for 60 seconds, your text vanishes

Clean, distraction-free UI with prompt regeneration

## 📁 Project Structure

DisappearingText/
│
├── main.py            # Entry point for the app
├── ui.py              # UI logic using Tkinter
├── start_prompt.py    # Contains 50 random story prompts
└── README.md          # This file

## 🚀 How to Run

Make sure you have Python installed (>=3.7)

Install Tkinter if it's not already installed:

```bash
sudo apt-get install python3-tk   # for Linux
# or just run on Windows/macOS – Tkinter is included by default
```

Run the app:

```bash
python main.py
```

## 🛠 How It Works

On startup, the app displays a random sentence.

You can begin typing in the input box.

A 60-second timer begins once you type your first letter.

The timer resets every time you press a key.

If the timer runs out: the input is erased and a new prompt appears.

## 🔄 Regenerate Prompt Manually

Click the "Generate" button at the top to:

Clear current text

Show a new prompt

Reset the timer

## 📦 Dependencies

tkinter (GUI library – included with Python)



Enjoy writing — just don't stop, or your story will disappear! 😄
```

