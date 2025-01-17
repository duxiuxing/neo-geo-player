# -- coding: UTF-8 --

import fnmatch
import os

from console_impl import ConsoleImpl
from export_neo_emu_cn_roms import ExportNeoEmuCnRoms
from export_wii_apps import ExportWiiApps
from import_mvs_covers import ImportMvsCovers
from local_configs import LocalConfigs
from main_menu import MainMenu
from wiiflow import WiiFlow


class NeoGeoMVS(ConsoleImpl):
    def create_wiiflow(self):
        return WiiFlow(self, "NEOGEO")

    def root_folder_path(self):
        return os.path.join(LocalConfigs.repository_folder_path(), "mvs")

    def rom_extension(self):
        return ".zip"
    
    def rom_extension_match(self, file_name):
        if file_name == "neogeo.zip":
            return False
        else:
            return fnmatch.fnmatch(file_name, "*.zip")


wii_app_files_tuple = (
    "apps\\ra-neogeo\\boot.dol",
    "apps\\ra-neogeo\\icon.png",
    "apps\\ra-neogeo\\meta.xml",
    "private"
)


MainMenu.console = NeoGeoMVS()
MainMenu.init_default_cmd_handlers()
MainMenu.add_cmd_handler(ExportWiiApps(wii_app_files_tuple))
MainMenu.add_cmd_handler(ImportMvsCovers())
MainMenu.add_cmd_handler(ExportNeoEmuCnRoms())
MainMenu.show()
