from root_directory_path import RootDirectoryPath

from typing import List, Union, Tuple
from pathlib import Path

import importlib.util
import sys

class BuilderPackages:
    def __init__(self):
        self.root_directory_path: str = str(Path(RootDirectoryPath().get_project_path()).parent)

    # Возвращает команды добавления пакетов в сбоку.
    @staticmethod
    def get_add_packages_command(package_names: List[str]) -> Union[List[str], None]:
        try:
            commands: List[str] = []

            for package_name in package_names:
                spec = importlib.util.find_spec(package_name)

                if spec and spec.origin:
                    commands.append(f'--add-data={str(Path(spec.origin).parent)}{";" if sys.platform == "win32" else ":"}{package_name}')

            return commands
        except ImportError as ex:
            print("Package is not found!", ex)

    # Возвращает список файлов или директорий для копирования.
    @staticmethod
    def get_files_for_copy() -> List[Tuple[str, str]]:
        from builder_config import BuilderConfig
        builderConfig = BuilderConfig()

        file_for_copy: List[Tuple[str, str]] = []

        for src, copy in builderConfig.files_for_copy.items():
            file_for_copy.append((src, copy))

        return file_for_copy