from builder_config import BuilderConfig

from typing import List
import os
import sys

class BuildCommand:
    def __init__(self):
        self.builder_config = BuilderConfig()

    # Команда создания .spec файла.
    def create_cmd_command(self) -> List[str]:
        cmd: List[str] = []

        # Добавляем стандартные параметры PyInstaller.
        for cmd_param in self.builder_config.get_command_params():
            cmd.append(cmd_param)

        cmd.append(f'--name={self.builder_config.start_file_name}')

        # Добавляем бинарные файлы в сборку.
        for binary_file_key, binary_file_value in self.builder_config.binary_files.items():
            cmd.append(f'--add-data={binary_file_key}{";" if sys.platform == "win32" else ":"}{binary_file_value}')

        # Добавляем явные пакеты библиотек.
        for package_append_command in self.builder_config.get_add_packages_command():
            cmd.append(package_append_command)

        cmd.append(f'--paths={self.builder_config.get_root_directory()}')
        cmd.append(os.path.join(self.builder_config.get_root_directory(), self.builder_config.root_file_name))

        return cmd