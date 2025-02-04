import functools
from tkinter import messagebox

def deactive(reason="Diese Funktion ist deaktiviert."):
    """Ein Decorator, der eine Funktion deaktiviert."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            messagebox.showerror(f"Funktion '{func.__name__}' ist deaktiviert: {reason}")
        return wrapper
    return decorator