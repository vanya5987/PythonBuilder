from builder_packages import BuilderPackages
from root_directory_path import RootDirectoryPath

from typing import List, Dict
from pathlib import Path

import os
import sys

class BuilderConfig:
    def __init__(self):
        # Путь к корню проекта.
        self.root_directory_path: str = RootDirectoryPath().get_project_path()

        # Имя исполняемого файла в зависимости от системы.
        self.start_file_name: str = "ShootingGallery.exe" if sys.platform == "win32" else "ShootingGallery"

        self.uploading_dist_name: str = "ShootingGallery"

        # Путь куда будет сохранена директория со сборкой.
        self.build_directory = os.path.join(str(Path(self.root_directory_path).parent), self.uploading_dist_name)

        # Имя исполняемого скрипта (Обязательно должен лежать в корне согласно src).
        self.root_file_name: str = "Main.py"

        # Словарь файлов для скрытого добавления в сборку. (Измените на свой набор файлов).
        self.binary_files: Dict[str, str] = {
            os.path.join(self.root_directory_path, "Documentation", "Manual"): "Core/Documentation/Manual",
            os.path.join(self.root_directory_path, "Resources", "Backgrounds"): "Core/Resources/Backgrounds",
            os.path.join(self.root_directory_path, "Resources", "Cursor"): "Core/Resources/Cursor",
            os.path.join(self.root_directory_path, "Resources", "Fonts"): "Core/Resources/Fonts",
            os.path.join(self.root_directory_path, "Resources", "Icons"): "Core/Resources/Icons",
            os.path.join(self.root_directory_path, "Resources", "Targets"): "Core/Resources/Targets",
        }

        # Список файлов для копирования в partable папку с исполняемым файлом. (Относительно корня проекта).
        # Формат ввода: Ключ - куда копируем, значение: что именно будем копировать.
        self.files_for_copy: Dict[str, str] = {
            os.path.join(str(Path(self.root_directory_path).parent), "Core/DatasHandler/JsonFiles"): os.path.join(self.build_directory, "JsonFiles"),
            os.path.join(str(Path(self.root_directory_path).parent), "Core/DatasHandler/DataBaseFile"): os.path.join(self.build_directory, "DataBaseFile"),
            os.path.join(str(Path(self.root_directory_path).parent), "Core/Tools/ShootingReportGenerator/Reports"): os.path.join(self.build_directory, "Reports"),
            os.path.join(str(Path(self.root_directory_path).parent), "Core/SoundsController/Sounds"): os.path.join(self.build_directory, "SoundsController/Sounds"),
            os.path.join(str(Path(self.root_directory_path).parent), "Core/Documentation/Logs"): os.path.join(self.build_directory, "Logs"),
            os.path.join(str(Path(self.root_directory_path).parent), "wh20python.lib"): "wh20python.lib",
            os.path.join(str(Path(self.root_directory_path).parent), "icon.ico"): "icon.ico",
            os.path.join(str(Path(self.root_directory_path).parent), "CHANGELOG.md"): "CHANGELOG.md",
            os.path.join(str(Path(self.root_directory_path).parent), "7z"): "7z"
        }

        # Список стандартных флагов для сборки.
        self.command_params: List[str] = ['pyinstaller', '--onefile', '--icon=icon.ico', '--windowed',
                                          f'--distpath={self.uploading_dist_name}']

        # Список библиотек для ручного импорта.
        self.add_packages_commands: List[str] = ["PIL", "PyQt5", "numpy", "cv2", "dotenv", "httpx", "idna", "pygrabber",
                                                 "httpcore", "certifi", "h11", "h2", "patoolib"]

    # Возвращает путь к директории куда будет сохранена сборка.
    def get_build_directory(self) -> str:
        return self.build_directory

    # Возвращает путь к корневой директории собираемого проекта.
    def get_root_directory(self) -> str:
        return self.root_directory_path

    # Возвращает команду сборки стандартных флагов PyInstaller.
    def get_command_params(self) -> List[str]:
        return self.command_params

    # Возвращает команду сборки бинарных файлов.
    def get_add_packages_command(self) -> List[str]:
        return BuilderPackages().get_add_packages_command(self.add_packages_commands)