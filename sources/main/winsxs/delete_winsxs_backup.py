from sources.wim.wim import Wim
import os
import subprocess


class DeleteWinSxSBackup(Wim):
    def __init__(self):
        self.command = f"delete_winsxs_backup.bat \"{self.mount_path}\""

    def delete_winsxs_backup(self):
        os.chdir("batch")

        subprocess.run(self.command, shell=True)

        os.chdir("..")
