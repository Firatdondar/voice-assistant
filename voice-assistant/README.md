# 🎤 Voice Assistant

A Python-based voice-controlled assistant with a Tkinter GUI. Users can select color and object buttons using spoken commands, take voice notes, and interact with the assistant hands-free.

---

## 📸 Preview

The assistant opens a GUI window with:
- **Color buttons**: Red, Blue, Green, Yellow, Purple
- **Object buttons**: Apple 🍎, Pear 🍐, Car 🚗, Bicycle 🚲

---

## ✨ Features

- 🎙️ Real-time speech recognition (Google Speech API)
- 🔊 Text-to-speech responses (gTTS + Pygame)
- 🖱️ Voice-controlled button selection
- 📝 Voice note taking (saved as `.txt` files)
- 🖼️ Image buttons with fallback to text
- 🧵 Background threading to keep GUI responsive

---

## 🛠️ Requirements

- Python 3.8+
- See [requirements.txt](requirements.txt) for all dependencies

### System dependency (Windows)

PyAudio requires a compiled wheel on Windows. Install it using the provided `.whl` file:

```bash
pip install PyAudio-0.2.14-cp312-cp312-win_amd64.whl
```

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Firatdondar/voice-assistant.git
cd voice-assistant

# 2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# 3. Install PyAudio wheel (Windows only)
pip install PyAudio-0.2.14-cp312-cp312-win_amd64.whl

# 4. Install remaining dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py
```

---

## 🗂️ Project Structure

```
voice-assistant/
├── app.py                                  # Main application
├── araba.jpg                               # Car image
├── armut.jpeg                              # Pear image
├── bisiklet.jpeg                           # Bicycle image
├── elma.jpeg                               # Apple image
├── PyAudio-0.2.14-cp312-cp312-win_amd64.whl  # PyAudio wheel for Windows
├── requirements.txt                        # Python dependencies
├── CMakeLists.txt                          # CMake build config (optional C extensions)
├── .gitignore                              # Git ignore rules
└── README.md                               # Project documentation
```

---

## 🎤 Voice Commands

| Command             | Action                        |
|---------------------|-------------------------------|
| `red`               | Select Red button             |
| `blue`              | Select Blue button            |
| `green`             | Select Green button           |
| `yellow`            | Select Yellow button          |
| `purple`            | Select Purple button          |
| `apple`             | Select Apple button           |
| `pear`              | Select Pear button            |
| `car`               | Select Car button             |
| `bicycle` / `bike`  | Select Bicycle button         |
| `take note`         | Record and save a voice note  |
| `what time is it`   | Hear the current time         |
| `how are you`       | Greeting response             |
| `exit` / `stop`     | Close the assistant           |

---

## ⚠️ Notes

- An **internet connection** is required for Google Speech Recognition and gTTS.
- Make sure your **microphone** is connected and enabled.
- Voice notes are saved in the project directory as `note_YYYY-MM-DD_HH-MM-SS.txt`.

---

## 📄 License

MIT License — feel free to use and modify.
