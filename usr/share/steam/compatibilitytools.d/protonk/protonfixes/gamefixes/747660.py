""" Five Nights at Freddy's: Security Breach
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """
    """

    # Disable DX12
    util.append_argument('-d3d11')

    # Reduce stuttering
    util.enable_dxvk_async()
