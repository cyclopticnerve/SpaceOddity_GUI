# ------------------------------------------------------------------------------
# Project : SpaceOddity_GUI                                        /          \
# Filename: load.py                                               |     ()     |
# Date    : 02/26/2026                                            |            |
# Author  : cyclopticnerve                                        |   \____/   |
# License : WTFPLv2                                                \          /
# ------------------------------------------------------------------------------

"""
A class to load data into a specific Window (or type of window).

This class manages the more advanced functions of a window, such as specific
control handlers.
Remember to connect all the appropriate window events in your ui file to the
private functions declared here.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# venv imports
from cnlib import cnfunctions as F
import gi
gi.require_version("Gtk", "3.0")

# pylint: disable=wrong-import-position
# pylint: disable=no-name-in-module

from gi.repository import Gtk  # type: ignore

# pylint: enable=wrong-import-position
# pylint: enable=no-name-in-module

# ------------------------------------------------------------------------------
# Public methods
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# A convenience method for subclasses to show a dialog
# ------------------------------------------------------------------------------
def do_load(builder: Gtk.Builder, dict_cfg: dict) -> None:
    """
    Load a dict from a file into a GUI
    """

    dict_curr = dict_cfg["cron"]

    ctl = builder.get_object("sw_cron")
    val = dict_curr["cron_enabled"]
    ctl.set_active(val)

    ctl = builder.get_object("spin_cron")
    val = dict_curr["cron_interval"]
    ctl.set_value(val)

# ------------------------------------------------------------------------------

    dict_curr = dict_cfg["caption"]

    ctl = builder.get_object("sw_caption")
    val = dict_curr["caption_show"]
    ctl.set_active(val)

    ctl = builder.get_object("cmb_position")
    val = dict_curr["caption_pos"]
    ctl.set_active(val)

    ctl = builder.get_object("spin_wrap")
    val = dict_curr["caption_wrap"]
    ctl.set_value(val)

# ------------------------------------------------------------------------------

    dict_curr = dict_curr["caption_font"]

    ctl = builder.get_object("btn_font")
    val = dict_curr["caption_font_name"]
    # ctl.set_font_name()

    ctl = builder.get_object("spin_font_size")
    val = dict_curr["caption_font_size"]
    ctl.set_value(val)

    ctl = builder.get_object("btn_font_color")
    val = dict_curr["caption_font_color"]
    # ctl.set_rgba(val)

    ctl = builder.get_object("spin_font_trans")
    val = dict_curr["caption_font_trans"]
    ctl.set_value(val)

# # ------------------------------------------------------------------------------

#     ctl = builder.get_object("caption_box")

#     //
#     val = dict_curr["caption_box_color"]
#     # ctl.set_rgba(val)

#     ctl = builder.get_object("spin_box_trans")
#     val = dict_curr["caption_box_trans"]
#     ctl.set_value(val)

#     ctl = builder.get_object("spin_box_rad")
#     val = dict_curr["caption_box_rad"]
#     ctl.set_value(val)

#     ctl = builder.get_object("spin_box_pad")
#     val = dict_curr["caption_box_pad"]
#     ctl.set_value(val)

#     dict_curr = dict_curr["caption_pad"]

#     ctl = builder.get_object("spin_pad_l")
#     val = dict_curr["caption_pad_l"]
#     ctl.set_value(val)

#     ctl = builder.get_object("spin_pad_t")
#     val = dict_curr["caption_pad_t"]
#     ctl.set_value(val)

#     ctl = builder.get_object("spin_pad_r")
#     val = dict_curr["caption_pad_r"]
#     ctl.set_value(val)

#     ctl = builder.get_object("spin_pad_b")
#     val = dict_curr["caption_pad_b"]
#     ctl.set_value(val)

    # -)
