# -- coding: UTF-8 --

import fnmatch
import os

from console_impl import ConsoleImpl
from export_ngp_emu_cn_roms import ExportNgpEmuCnRoms
from export_wii_apps import ExportWiiApps
from import_pocket_covers import ImportPocketCovers
from local_configs import LocalConfigs
from main_menu import MainMenu
from wiiflow import WiiFlow


class NeoGeoPocket(ConsoleImpl):
    def create_wiiflow(self):
        return WiiFlow(self, "NEOPOCKET_BW")

    def root_folder_path(self):
        return os.path.join(LocalConfigs.repository_folder_path(), "ngp")

    def rom_extension(self):
        return ".ngp"

    def rom_extension_match(self, file_name):
        return fnmatch.fnmatch(file_name, "*.ngp")


wii_app_files_tuple = (
    # "apps\\ra-neogeo\\boot.dol",
    # "apps\\ra-neogeo\\icon.png",
    # "apps\\ra-neogeo\\meta.xml",
    # "private"
)


MainMenu.console = NeoGeoPocket()
MainMenu.init_default_cmd_handlers()
# MainMenu.add_cmd_handler(ExportWiiApps(wii_app_files_tuple))
MainMenu.add_cmd_handler(ImportPocketCovers())
MainMenu.add_cmd_handler(ExportNgpEmuCnRoms())
MainMenu.show()
