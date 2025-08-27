from typing import List, Union, Tuple
from pathlib import Path
import os
import importlib.util
import sys

class BuilderPackages:
    # Возвращает команды добавления пакетов в сбоку.
    @staticmethod
    def get_add_packages_command(package_names: List[str]) -> Union[List[str], None]:
        try:
            commands: List[str] = []

            for package_name in package_names:
                spec = importlib.util.find_spec(package_name)

                if spec and spec.origin:
                    commands.append(f'--add-data={os.path.join(str(Path(spec.origin).parent), ";" if sys.platform == "win32" else ":", package_name)}')

            return commands
        except ImportError as ex:
            print("Package is not found!", ex)

    # Возвращает команды добавления скрытых импортов в сборку.
    @staticmethod
    def get_hidden_import_commands(package_names: List[str]) -> Union[List[str], None]:
        try:
            commands: List[str] = []

            for package_name in package_names:
                commands.append(f'--hidden-import={package_name}')

            return commands
        except ImportError as ex:
            print("Hidden import is not found!", ex)

    # Возвращает список файлов или директорий для копирования.
    @staticmethod
    def get_files_for_copy() -> List[Tuple[str, str]]:
        from builder_config import BuilderConfig

        file_for_copy: List[Tuple[str, str]] = []

        for _, binary_file_value in BuilderConfig().files_for_copy.items():
            file_for_copy.append((binary_file_value, binary_file_value))

        return file_for_copy