# 🎯 Professional Pomodoro Timer

A visually engaging, keyboard-interactive Pomodoro timer built using Python and `pygame`. Designed to enhance productivity with minimal distraction, clear visuals, and customizable audio cues.

---

## ✨ Features

- ⏳ Countdown timer with a clean display.
- 🎯 Phase indication: clearly shows “Work Phase” or “Break Phase”.
- 🔊 Customizable alert sounds for each phase.
- ⌨️ Interactive keyboard controls:
  - Press `S` to stop current music playback.
  - Press `Q` to quit the application at any time.
- 🪟 Always-on-top, bottom-right corner window placement (for 1920x1080 screens).

---

## 🛠 Setup Instructions

### 1. Create and Activate Environment (Using Conda)

```bash
conda create -n pomodoro python=3.8 -y
conda activate pomodoro
```

### 2. Install Dependencies

```bash
pip install pygame
```

---

## 📂 Project Structure

```
pomodoro/
├── main.py
├── music/
│   ├── Rest.mp3            # Played after work period
│   └── BackToWork.mp3      # Played after break period
└── assets/
    └── demo.gif            # (Optional) Demo animation
```

---

## ▶️ Run the Timer

```bash
python main.py --help
```

### Example:

```bash
python main.py -M 25 -S 0 -R 4 --break-minutes 5 --break-seconds 0 \
--work-music music/Rest.mp3 --break-music music/BackToWork.mp3
```

This launches:
- 4 cycles of 25-minute work sessions
- 5-minute breaks between cycles
- Custom audio for work and break transitions

---

## 🎵 Changing the Music

To change the music:
1. Place your `.mp3` files in the `music/` directory.
2. Pass their names using the CLI:

```bash
python main.py --work-music music/my_work_sound.mp3 --break-music music/my_break_sound.mp3
```

---

## ⌨️ Keyboard Shortcuts

- `S` → Stop current audio playback.
- `Q` → Quit the timer and close the window.

---

## 📌 Notes

- The app is optimized for 1920×1080 resolution; adjust `WINDOW_WIDTH`, `WINDOW_HEIGHT`, and `set_window_position()` if needed.
- Make sure `.mp3` files are valid and not protected.

---

## 🧠 Inspired By

The original Pomodoro technique and the desire for a no-distraction visual timer.

---

Happy Focused Working! 💼⏱️
