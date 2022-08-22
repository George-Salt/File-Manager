import argparse
import os
from urllib.parse import urlparse


EXTENSIONS = {
    "video": [
        ".mp4", ".mov", ".avi",
        ".mkv", ".wmv", ".3gp",
        ".3g2", ".mpg", ".mpeg",
        ".m4v", ".h264", ".flv",
        ".rm", ".swf", ".vob"
    ],
    "image": [
        ".jpg", ".png", ".bmp",
        ".ai", ".psd", ".ico",
        ".jpeg", ".ps", ".svg",
        ".tif", ".tiff", ".gif"
    ],
    "text": [
        ".pdf", ".txt", ".doc", ".docx",
        ".rtf", ".tex", ".wpd", ".odt"
    ]
}


def get_extension(file):
    parsed_url = urlparse(file)
    extension = os.path.splitext(parsed_url.path)[1]
    return extension


def get_dir_by_file_type(file, image_exts, video_exts, text_docs_exts):
    extension = get_extension(file)

    for image_extension in image_exts:
        if extension == image_extension:
            return "Фото"
    for video_extension in video_exts:
        if extension == video_extension:
            return "Видео"
    for text_docs_extension in text_docs_exts:
        if extension == text_docs_extension:
            return "ТекстДок"


def replace_file_by_type(file, image_exts, video_exts, text_docs_exts, original_dir):
    dir_by_type = get_dir_by_file_type(
        file,
        image_exts,
        video_exts,
        text_docs_exts
    )
    os.replace(f"{original_dir}/{file}", f"{dir_by_type}/{file}")


def make_dirs():
    if not os.path.isdir("Фото"):
        os.mkdir("Фото")
    if not os.path.isdir("Видео"):
        os.mkdir("Видео")
    if not os.path.isdir("ТекстДок"):
        os.mkdir("ТекстДок")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Программа распределяет файлы по их типу."
    )
    parser.add_argument("--original_dir", type=str, help="Папка, из которой брать файлы.", default="Хлам")
    args = parser.parse_args()

    make_dirs()

    files = os.listdir(args.original_dir)

    for file in files:
        replace_file_by_type(
            file,
            EXTENSIONS["image"],
            EXTENSIONS["video"],
            EXTENSIONS["text"],
            args.original_dir
        )

    print("Выполнено!")
