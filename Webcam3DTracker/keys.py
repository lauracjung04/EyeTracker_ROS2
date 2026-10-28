from pynput import keyboard as _pk

_pressed = set()

def _name(key):
    if isinstance(key, _pk.KeyCode):
        return key.char.lower() if key.char else None
    return key.name  # e.g. 'f7', 'esc', 'shift'

def _on_press(key):
    n = _name(key)
    if n:
        _pressed.add(n)

def _on_release(key):
    _pressed.discard(_name(key))

_listener = _pk.Listener(on_press=_on_press, on_release=_on_release, daemon=True)
_listener.start()

def is_pressed(name: str) -> bool:
    return name.lower() in _pressed
