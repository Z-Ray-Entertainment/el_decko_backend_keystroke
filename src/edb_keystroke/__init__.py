import keyboard
import asyncio

VERSION = "2023.5.7"
loop = None


def edb_init():
    pass


def edb_stop():
    pass


def edb_fire_event(event_type: str, event_parameters: dict = None):
    global loop
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as ex:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    loop.run_until_complete(__wait_for_keyboard())


def edb_available_events() -> dict:
    pass


def __wait_for_keyboard():
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print("Buttons where pressed: " + event.name)


def __keypress(shortcut: str):
    keyboard.send(shortcut)
