from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def key_press_event(key):
    logging.info(str(key))

try:
    # Ask for user's permission
    user_confirmation = input("Do you want to start the logger? (yes/no): ").lower()

    if user_confirmation == "yes":
        with Listener(on_press=key_press_event) as listener:
            print("Logger started. Press Ctrl+C to exit.")
            listener.join()
    else:
        print("Logger not started. Exiting.")

except KeyboardInterrupt:
    print("Ctrl+C pressed. Exiting.")
except Exception as error:
    print(f"An error occurred: {error}")
