""" Game fix for OUTRIDERS
"""
#pylint: disable=C0103

import glob
import os
import subprocess
from protonfixes import util

def main():
    """ This is a workaround that allows the game to be played with EAC.
    """

    # Install Proton EAC Runtime
    util.install_eac_runtime()

    # EAC hack
    install_dir = glob.escape(util.get_game_install_path())
    eac_file = util.protondir() + '/protonfixes/components/easyanticheat_x64.so'

    if not os.path.isfile(install_dir + '/EasyAntiCheat/easyanticheat_x64.so'):
        subprocess.call(['cp', eac_file, install_dir + '/EasyAntiCheat'])
