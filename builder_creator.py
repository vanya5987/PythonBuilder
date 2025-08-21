from builder_config import BuilderConfig
from builder_packages import BuilderPackages
from build_command import BuildCommand

import subprocess
import os
import shutil

class BuildCreator:
    def __init__(self):
        self.builder_config = BuilderConfig()

    def create_build(self):
        try:
            subprocess.run(BuildCommand().create_cmd_command(), check=True)

            for src_rel, dest_rel in BuilderPackages().get_files_for_copy():
                src = os.path.join(self.builder_config.get_root_directory(), src_rel)
                dest = os.path.join(self.builder_config.get_build_directory(), dest_rel)

                if os.path.exists(src):
                    if os.path.isdir(src):
                        shutil.copytree(src, dest, dirs_exist_ok=True)
                    else:
                        shutil.copy2(src, dest)
                    print(f"📂 Скопировано: {src} -> {dest}")
                else:
                    print(f"⚠️ Файл/папка не найдена: {src}")

            print("\n✅ Сборка успешно завершена! Данные скопированы рядом с .exe")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Ошибка сборки (код {e.returncode}):")
            print(e.stderr.decode() if e.stderr else "См. вывод выше")
        except Exception as e:
            print(f"\n❌ Неожиданная ошибка: {str(e)}")
            raise

build_creator = BuildCreator()
build_creator.create_build()