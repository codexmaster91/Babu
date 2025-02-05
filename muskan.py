import time
import os
import random
import subprocess  # For calling Termux commands

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound():
    # Playing a short melody sound after countdown or heart animation using termux-media-player
    try:
        # Replace with the path to your audio file (e.g., "path/to/sound.mp3")
        subprocess.run(["termux-media-player", "play", "/data/data/com.termux/files/home/sound.mp3"])
    except Exception as e:
        print(f"Error playing sound: {e}")

def print_animated_heart():
    colors = ['\033[91m', '\033[95m', '\033[93m', '\033[96m', '\033[94m']
    heart_frames = [
        """
         ♥♥♥  
       ♥♥♥♥♥♥♥ 
      ♥♥♥♥♥♥♥♥♥
       ♥♥♥♥♥♥♥ 
         ♥♥♥  
        """,
        """
        ♥♥♥♥♥   
      ♥♥♥♥♥♥♥♥♥ 
     ♥♥♥♥♥♥♥♥♥♥♥
      ♥♥♥♥♥♥♥♥♥ 
        ♥♥♥♥♥   
        """,
        """
         ♥♥♥  
       ♥♥♥♥♥♥♥ 
      ♥♥♥♥♥♥♥♥♥
       ♥♥♥♥♥♥♥ 
         ♥♥♥  
        """
    ]
    
    for _ in range(5):
        for color in colors:
            clear_screen()
            print(color)
            for frame in heart_frames:
                print(frame.center(os.get_terminal_size().columns))
                time.sleep(0.1)
                clear_screen()
            print("\033[0m")

def print_fancy_name(name):
    colors = ['\033[92m', '\033[96m', '\033[94m', '\033[93m', '\033[95m']
    clear_screen()
    for i, letter in enumerate(name):
        print(colors[i % 5] + " "*(i*2) + "╔═" + letter.upper() + "═╗" + " "*(i*2))
        print(" "*(i*2) + "╚═" + "═"*len(letter) + "═╝" + " "*(i*2))
        time.sleep(0.2)
    print("\033[0m")

def countdown():
    for i in range(5, 0, -1):
        clear_screen()
        print(f"\033[1;31m{i}...\033[0m")
        time.sleep(1)
    clear_screen()

def random_quote():
    quotes = [
        "You are the sunshine of my life. ☀️",
        "Every moment with you is a treasure. 💎",
        "Your smile is my favorite part of the day! 😊",
        "In a sea of people, my eyes will always search for you. 🌊",
        "Love is the bridge between two hearts. ❤️"
    ]
    return random.choice(quotes)

def main():
    crush_name = "Muskaan"
    
    # Countdown
    countdown()
    
    # Play sound (using Termux media player)
    play_sound()
    
    # Animated heart
    print_animated_heart()
    
    # Fancy name printing
    print_fancy_name(crush_name)
    
    # Final message with random quote
    print("\n\033[1;35m✿◕ ‿ ◕✿\033[0m", end=" ")
    print("\033[3;36mYou make my world brighter! \033[0m\033[5m✨\033[0m")
    print("\033[1;31m~" * (len(crush_name) * 3 + 10))
    print("\033[1;33mAlways keep smiling! 😊\033[0m")
    
    # Random quote at the end
    print("\n\033[1;32m" + random_quote() + "\033[0m")

if __name__ == "__main__":
    main()
