import os
import pathlib
from pathlib import Path
import shutil

def file_type(filepath):
    return str(filepath).split('.')[-1]
    



def analyze_files_on_desktop():
    """Analyzes all files on the desktop."""

    desktop_path = pathlib.Path.home() / "Desktop"
    pdf_path = pathlib.Path.home() / "Desktop/pdf"
    lnk_path = pathlib.Path.home() / "Desktop/lnk"
    img_path = pathlib.Path.home() / "Desktop/img"
    etc_path = pathlib.Path.home() / "Desktop/etc"
    #link_path
    for file_path in desktop_path.iterdir():
        if file_path.is_file():
            try:
                print(file_path.suffix.lower())
                print("X")
                fileExtension = file_type(file_path)
                print(fileExtension)
                match fileExtension:
                    case "pdf":
                        shutil.move(src=file_path, dst=pdf_path)
                    case "lnk":
                        shutil.move(src=file_path, dst=lnk_path)
                    case "png":
                        shutil.move(src=file_path, dst=img_path)
                    case _:
                        shutil.move(src=file_path, dst=etc_path)

            except Exception as e:
                print(f"Error analyzing {file_path.name}: {e}")
        else:
            print(file_path.name)

if __name__ == "__main__":
    analyze_files_on_desktop()