# Importing required libraries
import speech_recognition as sr
import datetime
import os
from gtts import gTTS
import pygame.mixer  # Using pygame's mixer module to play audio
import time  # Short delay before deleting audio files

# Tkinter for GUI, Threading to run voice assistant in background
import tkinter as tk
import threading
import tkinter.font as tkFont

# Pillow (PIL) for adding images to buttons
from PIL import Image, ImageTk


# --- Initial Setup ---
# Initialize Pygame mixer for playing speech and sound effects
try:
    pygame.mixer.init()
    print("Pygame mixer initialized.")
    pygame_mixer_initialized = True
except Exception as e:
    print(f"Error: Pygame mixer could not be initialized: {e}")
    print("Audio playback may not work.")
    pygame_mixer_initialized = False

# Speech recognizer and microphone objects
r = None
mic = None

# Try to initialize speech recognition and microphone
try:
    r = sr.Recognizer()
    mic = sr.Microphone()
    print("Speech recognizer and microphone initialized.")
except Exception as e:
    print(f"Error: Speech recognizer or microphone could not be initialized: {e}")


# --- GUI Helper Functions ---

def on_button_select_by_voice(button_name):
    """Called when a button is selected via voice command."""
    print(f"Console: '{button_name}' button selected by voice command!")
    # Note: To update button appearance from this function safely,
    # use root.after() to run GUI updates on the main thread.
    # Example: root.after(0, update_button_appearance, button_name)


# --- Core Voice Assistant Functions (Speak, Listen, Take Note) ---

def speak(text):
    """Converts the given text to speech using gTTS and plays it with Pygame."""
    print(f"Assistant: {text}")
    if not text:
        return

    if not pygame_mixer_initialized:
        print("Error: Cannot speak because Pygame mixer is not initialized.")
        return

    try:
        tts = gTTS(text=text, lang='en', slow=False)
        temp_audio_file = "temp_speech.mp3"
        tts.save(temp_audio_file)

        if os.path.exists(temp_audio_file):
            try:
                sound = pygame.mixer.Sound(temp_audio_file)
                sound.play()
                time.sleep(sound.get_length() + 0.1)
                os.remove(temp_audio_file)
            except pygame.error as e:
                print(f"Audio file could not be played with Pygame: {e}")
                print("There may be an issue with the file format (MP3) or Pygame.")
            except Exception as e:
                print(f"Unexpected error while playing audio: {e}")
        else:
            print("Error: gTTS could not create audio file ('temp_speech.mp3').")

    except Exception as e:
        print(f"Error: Problem occurred during gTTS speech ({e})")
        print("Make sure you have an internet connection, or the gTTS service may be temporarily busy.")


def listen():
    """Listens to the microphone and converts speech to text."""
    if not r or not mic:
        print("Error: Cannot listen because speech recognizer or microphone is not initialized.")
        return None

    with mic as source:
        print("Listening...")
        try:
            r.adjust_for_ambient_noise(source, duration=0.5)
        except Exception as e:
            print(f"Ambient noise adjustment error: {e}")

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing...")
            command = r.recognize_google(audio, language='en-US')
            print(f"You: {command}")
            return command.lower()

        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Could not reach Google Speech Recognition service; {e}")
            print("Assistant: Sorry, the speech recognition service is currently unavailable.")
            return None
        except Exception as e:
            print(f"Unexpected error during listening: {e}")
            return None


def take_note():
    """Records a voice note from the user and saves it to a text file."""
    speak("I'm listening")

    note = listen()

    if note:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"note_{timestamp}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(note)
            speak(f"Your note has been saved as '{filename}'.")
        except Exception as e:
            speak("Sorry, an error occurred while saving the note.")
            print(f"File write error: {e}")
    else:
        speak("I didn't hear anything to note.")


# --- Main Voice Assistant Loop ---

def run_voice_assistant():
    """Runs the voice command listening and processing loop."""
    if r and mic and pygame_mixer_initialized:
        speak("Hello! How can I help you?")

        while True:
            command = listen()

            if command:
                # --- Recognized Commands ---
                if "how are you" in command:
                    speak("I'm fine, I'm listening.")
                elif "what time is it" in command or "time" in command:
                    now = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The current time is {now}")
                elif "take note" in command or "note this" in command:
                    take_note()
                elif "thank you" in command or "thanks" in command:
                    speak("You're welcome!")
                elif "close" in command or "exit" in command or "stop" in command:
                    speak("Goodbye!")
                    break

                # --- Voice Button Selection Commands ---
                # Color buttons
                elif "red button" in command or "red" in command:
                    on_button_select_by_voice("Red")
                    speak("Red button selected.")
                elif "blue button" in command or "blue" in command:
                    on_button_select_by_voice("Blue")
                    speak("Blue button selected.")
                elif "green button" in command or "green" in command:
                    on_button_select_by_voice("Green")
                    speak("Green button selected.")
                elif "yellow button" in command or "yellow" in command:
                    on_button_select_by_voice("Yellow")
                    speak("Yellow button selected.")
                elif "purple button" in command or "purple" in command:
                    on_button_select_by_voice("Purple")
                    speak("Purple button selected.")

                # Number buttons (currently disabled)
                # elif "first button" in command or "one" in command:
                #    on_button_select_by_voice("First (1)")
                #    speak("First button selected.")
                # elif "second button" in command or "two" in command:
                #    on_button_select_by_voice("Second (2)")
                #    speak("Second button selected.")
                # elif "third button" in command or "three" in command:
                #    on_button_select_by_voice("Third (3)")
                #    speak("Third button selected.")

                # Object buttons
                elif "apple button" in command or "apple" in command:
                    on_button_select_by_voice("Apple")
                    speak("Apple button selected.")
                elif "pear button" in command or "pear" in command:
                    on_button_select_by_voice("Pear")
                    speak("Pear button selected.")
                elif "car button" in command or "car" in command:
                    on_button_select_by_voice("Car")
                    speak("Car button selected.")
                elif "bicycle button" in command or "bicycle" in command or "bike" in command:
                    on_button_select_by_voice("Bicycle")
                    speak("Bicycle button selected.")

                else:
                    # Unknown command - do nothing
                    pass

    else:
        print("Required engines (speech or recognizer) could not be started. Voice commands will not be available.")


# --- Main Program Entry Point ---

if __name__ == "__main__":

    def create_gui_window():
        root = tk.Tk()
        root.title("Assistant Control Panel")

        root.geometry("600x850")
        root.resizable(True, True)

        large_font = tkFont.Font(family="Arial", size=14, weight="bold")

        label = tk.Label(root, text="Please Select a Button by Voice Command:", font=large_font)
        label.pack(pady=20)

        # --- Color Buttons Frame ---
        color_frame = tk.Frame(root)
        color_frame.pack(pady=10, fill=tk.X, padx=10)

        for i in range(5):
            color_frame.grid_columnconfigure(i, weight=1)

        btn_red = tk.Button(color_frame, text="Red", bg="red", fg="white",
                            font=large_font, pady=15,
                            command=lambda: on_button_select_by_voice("Red"))
        btn_red.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        btn_blue = tk.Button(color_frame, text="Blue", bg="blue", fg="white",
                             font=large_font, pady=15,
                             command=lambda: on_button_select_by_voice("Blue"))
        btn_blue.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        btn_green = tk.Button(color_frame, text="Green", bg="green", fg="white",
                              font=large_font, pady=15,
                              command=lambda: on_button_select_by_voice("Green"))
        btn_green.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        btn_yellow = tk.Button(color_frame, text="Yellow", bg="yellow", fg="black",
                               font=large_font, pady=15,
                               command=lambda: on_button_select_by_voice("Yellow"))
        btn_yellow.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

        btn_purple = tk.Button(color_frame, text="Purple", bg="purple", fg="white",
                               font=large_font, pady=15,
                               command=lambda: on_button_select_by_voice("Purple"))
        btn_purple.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)

        # Number buttons frame (currently unused)
        number_frame = tk.Frame(root)
        # number_frame.pack(pady=10, fill=tk.X, padx=10)

        # for i in range(3):
        #    number_frame.grid_columnconfigure(i, weight=1)

        # btn_one = tk.Button(number_frame, text="1",
        #                     font=large_font, pady=15,
        #                     command=lambda: on_button_select_by_voice("First (1)"))
        # btn_one.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # btn_two = tk.Button(number_frame, text="2",
        #                     font=large_font, pady=15,
        #                     command=lambda: on_button_select_by_voice("Second (2)"))
        # btn_two.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # btn_three = tk.Button(number_frame, text="3",
        #                       font=large_font, pady=15,
        #                       command=lambda: on_button_select_by_voice("Third (3)"))
        # btn_three.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        # --- Object Buttons Frame ---
        object_frame = tk.Frame(root)
        object_frame.pack(pady=10, fill=tk.X, padx=10)

        object_frame.grid_columnconfigure(0, weight=1)
        object_frame.grid_columnconfigure(1, weight=1)
        object_frame.grid_rowconfigure(0, weight=1)
        object_frame.grid_rowconfigure(1, weight=1)

        def load_image_for_button(image_path, button_name, target_width=None, target_height=None):
            """Loads an image file and returns a Tkinter-compatible PhotoImage.
            Returns None if the file is not found or cannot be loaded."""
            try:
                img = Image.open(image_path)

                if target_width is not None and target_height is not None:
                    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

                photo = ImageTk.PhotoImage(img)
                print(f"Image '{image_path}' loaded successfully.")
                return photo
            except FileNotFoundError:
                print(f"Error: Image '{image_path}' not found. '{button_name}' button will use text.")
                return None
            except Exception as e:
                print(f"Error: Could not load image '{image_path}': {e}. '{button_name}' button will use text.")
                return None

        # Image size for all object buttons
        image_size = (100, 100)

        # Image file paths
        apple_image_path = "elma.jpeg"
        pear_image_path = "armut.jpeg"
        car_image_path = "araba.jpg"
        bicycle_image_path = "bisiklet.jpeg"

        apple_photo = load_image_for_button(apple_image_path, "Apple", *image_size)
        pear_photo = load_image_for_button(pear_image_path, "Pear", *image_size)
        car_photo = load_image_for_button(car_image_path, "Car", *image_size)
        bicycle_photo = load_image_for_button(bicycle_image_path, "Bicycle", *image_size)

        # Apple button
        btn_apple = tk.Button(object_frame,
                              text="Apple" if apple_photo is None else "",
                              image=apple_photo,
                              compound=tk.TOP if apple_photo else tk.CENTER,
                              font=large_font if apple_photo is None else None,
                              command=lambda: on_button_select_by_voice("Apple"))
        btn_apple.image = apple_photo  # Prevent garbage collection
        btn_apple.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Pear button
        btn_pear = tk.Button(object_frame,
                             text="Pear" if pear_photo is None else "",
                             image=pear_photo,
                             compound=tk.TOP if pear_photo else tk.CENTER,
                             font=large_font if pear_photo is None else None,
                             command=lambda: on_button_select_by_voice("Pear"))
        btn_pear.image = pear_photo
        btn_pear.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Car button
        btn_car = tk.Button(object_frame,
                            text="Car" if car_photo is None else "",
                            image=car_photo,
                            compound=tk.TOP if car_photo else tk.CENTER,
                            font=large_font if car_photo is None else None,
                            command=lambda: on_button_select_by_voice("Car"))
        btn_car.image = car_photo
        btn_car.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Bicycle button
        btn_bicycle = tk.Button(object_frame,
                                text="Bicycle" if bicycle_photo is None else "",
                                image=bicycle_photo,
                                compound=tk.TOP if bicycle_photo else tk.CENTER,
                                font=large_font if bicycle_photo is None else None,
                                command=lambda: on_button_select_by_voice("Bicycle"))
        btn_bicycle.image = bicycle_photo
        btn_bicycle.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        # Start the voice assistant loop in a background thread to keep GUI responsive
        voice_thread = threading.Thread(target=run_voice_assistant, daemon=True)
        voice_thread.start()

        # Start the Tkinter main loop
        root.mainloop()

        print("GUI window closed.")

    # Create and run the GUI window
    create_gui_window()
