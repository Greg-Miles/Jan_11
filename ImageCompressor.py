
import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener

QUALITY: int = 50  # Можно настроить качество сжатия

class ImageCompressor(__quality, supported_formats):
    def __init__(self, quality: int = QUALITY):
        self.__quality = quality

    def compress_image(input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.

        Args:
            input_path (str): Путь к исходному изображению.
            output_path (str): Путь для сохранения сжатого изображения.

        Returns:
            None
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=QUALITY)
        print(f"Сжато: {input_path} -> {output_path}")

    def process_directory(directory: str) -> None:
        """
        Обрабатывает все изображения в указанной директории и её поддиректориях.

        Args:
            directory (str): Путь к директории для обработки.

        Returns:
            None
        """
        for root, _, files in os.walk(directory):
            for file in files:
                # Проверяем расширение файла
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    compress_image(input_path, output_path)

    @property
    def quality(self) -> int:
        """
        Геттер для текущего качества сжатия.
        Args:
            None
        Returns:
            int: Качество сжатия.
        """
        return self.__quality

    @quality.setter
    def quality(self, quality: int) -> None:
        """
        Сеттер для установки качества сжатия.
        Args:
            quality (int): Качество сжатия (от 0 до 100).
        """
        self.__quality = quality
