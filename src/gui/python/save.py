# ------------------------------------------------------------------------------
# Project : SpaceOddity_GUI                                        /          \
# Filename: save.py                                               |     ()     |
# Date    : 02/26/2026                                            |            |
# Author  : cyclopticnerve                                        |   \____/   |
# License : WTFPLv2                                                \          /
# ------------------------------------------------------------------------------

"""
A class to save data from a specific Window (or type of window).

This class manages the more advanced functions of a window, such as specific
control handlers.
Remember to connect all the appropriate window events in your ui file to the
private functions declared here.
"""

def do_save(builder, ui_file, window, dict_cfg):
    """
    Save a dict from a GUI into a file
    """

    # -)
