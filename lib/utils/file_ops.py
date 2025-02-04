import os
import shutil

def create_folder(path):
    """Erstellt einen Ordner, falls er nicht existiert."""
    os.makedirs(path, exist_ok=True)

def delete_folder(path):
    """Löscht einen Ordner und dessen Inhalt."""
    if os.path.exists(path):
        shutil.rmtree(path)

def read_file(file_path):
    """Liest den Inhalt einer Datei."""
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

def write_file(file_path, content):
    """Schreibt Inhalt in eine Datei."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(content)

def delete_file(file_path):
    """Löscht eine Datei."""
    if os.path.exists(file_path):
        os.remove(file_path)
