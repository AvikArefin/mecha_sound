# Logging
import logging
logger = logging.getLogger("MechaSound")

# Add this import at the top of your script
import time

# pip install pynput
from pynput.keyboard import Listener 
# pip install pygame
import pygame.mixer
import threading         

# File path
keyboard_name = "eg-oreo"

# Default Audio File path
audio_file_z_path = ".\\audio_split_output\\" + keyboard_name + "\\1.wav"

# Pygame Mixer Initialization
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

# Default audio file path
z = pygame.mixer.Sound(audio_file_z_path)

# play_audio
def play_audio(real_key):
    audio_file_path = ".\\audio_split_output\\" + keyboard_name + "\\"+ real_key + ".wav"
    try:
        x = pygame.mixer.Sound(audio_file_path)
        pygame.mixer.Sound.play(x)
    except:
        pygame.mixer.Sound.play(z)


# Keymap used to find find audio file
key_map = {
    'Key.esc': '1',
    'F1': '59',
    'F2': '60',
    'F3': '61',
    'F4': '62',
    'F5': '63',
    'F6': '64',
    'F7': '65',
    'F8': '66',
    'F9': '67',
    'F10': '68',
    'F11': '87',
    'F12': '88',
    'F13': '91',
    'F14': '92',
    'F15': '93',
    '`': '41',
    '1': '2',
    '2': '3',
    '3': '4',
    '4': '5',
    '5': '6',
    '6': '7',
    '7': '8',
    '8': '9',
    '9': '10',
    '0': '11',
    '-': '12',
    '!': '2',
    '@': '3',
    '#': '4',
    '$': '5',
    '%': '6',
    '^': '7',
    '&': '8',
    '(': '10',
    ')': '11',
    '_': '12',
    '=': '13',
    'Key.backspace': '14',
    'Key.tab': '15',
    'Key.capslock': '58',
    'a': '30',
    'b': '48',
    'c': '46',
    'd': '32',
    'e': '18',
    'f': '33',
    'g': '34',
    'h': '35',
    'i': '23',
    'j': '36',
    'k': '37',
    'l': '38',
    'm': '50',
    'n': '49',
    'o': '24',
    'p': '25',
    'q': '16',
    'r': '19',
    's': '31',
    't': '20',
    'u': '22',
    'v': '47',
    'w': '17',
    'x': '45',
    'y': '21',
    'z': '44',
    '[': '26',
    ']': '27',
    '\\': '43',
    ';': '39',
    "'": '40',
    'Key.enter': '28',
    ',': '51',
    '.': '52',
    '/': '53',
    'Key.space': '57',
    'PrtSc': '3639',
    'ScrLk': '70',
    'Pause': '3653',
    'Ins': '3666',
    'Key.del': '3667',
    'Home': '3655',
    'End': '3663',
    'PgUp': '3657',
    'PgDn': '3665',
    '↑': '57416',
    '←': '57419',
    '→': '57421',
    '↓': '57424',
    'Key.shift': '42',
    'Key.ctrl_l': '29',
    'Key.ctrl_r': '29',
    'Key.alt': '56',
    'Meta': '3675',
    'Menu': '3677',
    'Num\nLock': '69',
    '/': '3637',
    '*': '55',
    '-': '74',
    '=': '3597',
    '+': '78',
    'Numpad Enter': '3612',
    '.': '83',
    '1': '79',
    '2': '80',
    '3': '81',
    '4': '75',
    '5': '76',
    '6': '77',
    '7': '71',
    '8': '72',
    '9': '73',
    '0': '82'
}


# Add this global variable at the beginning of your script
key_pressed = set()  # Use a set to keep track of keys being held down

# Modify the on_key_press function as follows
def on_key_press(key):
    global key_pressed
    real_key = '1'
    try:
        # Check if the key is a special key (e.g., a function key)
        if hasattr(key, 'char'):
            real_key : str = key_map[key.char.lower()]
            logger.debug(real_key)
        else:
            # Key is not a printable character (e.g., Shift, Ctrl, etc.)
            logger.debug(f'Special key {key} pressed (keycode: {key.value.vk})')
            # real_key : int = key_map[key.value.vk]
            real_key : str = key_map[str(key)]    
            logger.debug(real_key)
    except:
        # Key does not have 'char' or 'value' attributes (e.g., multimedia keys)
        logger.debug(f'Not found in dict Special key {key} pressed (keycode: {key})')

    # Check if the key is not already in the set (i.e., it's not being held down)
    if real_key not in key_pressed:
        threading.Thread(target=play_audio, args=[real_key]).start()
        key_pressed.add(real_key)  # Add the key to the set

# Modify the on_key_release function as follows
def on_key_release(key):
    global key_pressed
    real_key = '1'
    try:
        if hasattr(key, 'char'):
            real_key : str = key_map[key.char.lower()]
        else:
            real_key : str = key_map[str(key)]
    except:
        pass  # Handle exceptions if necessary

    if real_key in key_pressed:
        key_pressed.remove(real_key)  # Remove the key from the set

# main
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG) 
    with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()
