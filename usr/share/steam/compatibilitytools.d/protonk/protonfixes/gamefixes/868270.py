""" The Cycle: Frontier
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """
    """

    # Install Proton BattleEye Runtime
    util.install_battleye_runtime()

    # Disable DX12
    util.append_argument('-dx12')

    # Reduce stuttering
    util.enable_dxvk_async()
