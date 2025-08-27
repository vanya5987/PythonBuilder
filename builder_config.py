from builder_packages import BuilderPackages
from root_directory_path import RootDirectoryPath

from typing import List, Dict
import subprocess
import os
import sys

class BuilderConfig:
    def __init__(self):
        # Путь к корню проекта.
        self.root_directory_path: str = RootDirectoryPath().get_project_path()

        # Пути к бинарным файлам и директориям. (Аналогично path_config но с собственной конфигурацией). (Измените на свой набор файлов и директорий).
        data_base_path: str = os.path.join(self.root_directory_path, "backend", "src", "db", "clients.sqlite")
        excel_directory_path: str = os.path.join(self.root_directory_path, "backend", "excel_files")

        # Имя исполняемого файла в зависимости от системы.
        self.start_file_name: str = "ShootingGallery.exe" if sys.platform == "win32" else "ShootingGallery"

        # Путь куда будет сохранена директория со сборкой.
        self.build_directory = os.path.join(self.root_directory_path, "builder", "dist")

        # Имя исполняемого скрипта (Обязательно должен лежать в корне согласно src).
        self.root_file_name: str = "Main.py"

        # Словарь бинарных файлов для скрытого импорта в сборку. (Измените на свой набор файлов и директорий).
        self.binary_files: Dict[str, str] = {
            data_base_path: os.path.join("backend", "src", "db"),
        }

        # Словарь файлов для копирования в partable папку с исполняемым файлом. (Измените на свой набор файлов и директорий).
        self.files_for_copy: Dict[str, str] = {
            data_base_path: os.path.join("backend", "src", "db"),
            excel_directory_path: os.path.join("backend", "excel_files")
        }

        # Список стандартных флагов для сборки.
        self.command_params: List[str] = ['pyinstaller', '--onefile', '--windowed']

        # Список модулей для ручного импорта (Актуально для Linux).
        self.add_packages_commands: List[str] = []

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

    # Возвращает команду сборки скрытых импортов.
    @staticmethod
    def get_hidden_import_command() -> List[str]:
        packages = [line.split('==')[0] for line in subprocess.run([sys.executable, '-m', 'pip', 'freeze'],
                                                                   capture_output=True, text=True,
                                                                   check=True).stdout.split('\n') if
                                                                   line and '==' in line]

        return BuilderPackages().get_hidden_import_commands(packages)