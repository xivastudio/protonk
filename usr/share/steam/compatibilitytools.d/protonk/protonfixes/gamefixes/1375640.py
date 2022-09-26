""" Game fix for Lost Keys
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Fix low FPS
    """

    #
    util.disable_dxvk()
    util.disable_esync()
    util.disable_fsync()
