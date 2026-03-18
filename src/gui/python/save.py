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

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# venv imports
from cnlib import cnfunctions as F  # type: ignore # pylint: disable=import-error
import gi

gi.require_version("Gtk", "3.0")

# pylint: disable=wrong-import-position
# pylint: disable=no-name-in-module

from gi.repository import Gtk, Gdk, Pango  # type: ignore

# pylint: enable=wrong-import-position
# pylint: enable=no-name-in-module

# local imports
import keys as K
import sanitize

# from sanitize import do_sanitize

# ------------------------------------------------------------------------------
# Public methods
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# A convenience method to save data to a file from the GUI
# ------------------------------------------------------------------------------
def do_save(builder: Gtk.Builder, dict_cfg: dict) -> None:
    """
    A convenience method to load data from a file into the GUI

    Args:
        builder: The GtkBuilder object that owns our GUI file
        dict_cfg: The JSON file with our data
    """

    # --------------------------------------------------------------------------

    # sanitize dict first
    sanitize.do_sanitize(dict_cfg)

    # --------------------------------------------------------------------------

    dict_cron = dict_cfg[K.S_KEY_CRON]

    ctl = builder.get_object("sw_cron")
    val = ctl.get_active()
    dict_cron[K.S_KEY_CRON_ENABLED] = val

    ctl = builder.get_object("spin_cron")
    val = ctl.get_value()
    dict_cron[K.S_KEY_CRON_INTERVAL] = int(val)

    # --------------------------------------------------------------------------

    dict_cap = dict_cfg[K.S_KEY_CAPTION]

    ctl = builder.get_object("sw_caption")
    val = ctl.get_active()
    dict_cap[K.S_KEY_CAPTION_SHOW] = val

    ctl = builder.get_object("cmb_position")
    val = ctl.get_active()
    dict_cap[K.S_KEY_CAPTION_POS] = val

    ctl = builder.get_object("spin_wrap")
    val = ctl.get_value()
    dict_cap[K.S_KEY_CAPTION_WRAP] = int(val)

    # --------------------------------------------------------------------------

    dict_info = dict_cap[K.S_KEY_CAPTION_INFO]

    ctl = builder.get_object("chk_info_title")
    val = ctl.get_active()
    dict_info[K.S_KEY_APOD_TITLE] = val

    ctl = builder.get_object("chk_info_date")
    val = ctl.get_active()
    dict_info[K.S_KEY_APOD_DATE] = val

    ctl = builder.get_object("chk_info_copyright")
    val = ctl.get_active()
    dict_info[K.S_KEY_APOD_COPY] = val

    ctl = builder.get_object("chk_info_explanation")
    val = ctl.get_active()
    dict_info[K.S_KEY_APOD_EXP] = val

    # --------------------------------------------------------------------------

    dict_font = dict_cap[K.S_KEY_CAPTION_FONT]

    # TODO: need to get font path (fc-list)
    ctl = builder.get_object("btn_font")
    val = ctl.get_font_name()
    dict_font[K.S_KEY_CAPTION_FONT_NAME] = val

    # --------------------------------------------------------------------------

    pfd = Pango.font_description_from_string(val)
    print(pfd.get_family())
    print(pfd.get_style())

    # --------------------------------------------------------------------------

    ctl = builder.get_object("spin_font_size")
    val = ctl.get_value()
    dict_font[K.S_KEY_CAPTION_FONT_SIZE] = int(val)

    ctl = builder.get_object("btn_font_color")
    val = ctl.get_rgba()
    val = _unmake_color(val)
    dict_font[K.S_KEY_CAPTION_FONT_COLOR] = val

    ctl = builder.get_object("spin_font_trans")
    val = ctl.get_value()
    # no appreciable loss of precision
    val = F.interpolate(val, 0, 100, 0, 255)
    dict_font[K.S_KEY_CAPTION_FONT_TRANS] = int(val)

    # --------------------------------------------------------------------------

    dict_box = dict_cap[K.S_KEY_CAPTION_BOX]

    ctl = builder.get_object("btn_box_color")
    val = ctl.get_rgba()
    val = _unmake_color(val)
    dict_box[K.S_KEY_CAPTION_BOX_COLOR] = val

    ctl = builder.get_object("spin_box_trans")
    val = ctl.get_value()
    # no appreciable loss of precision
    val = F.interpolate(val, 0, 100, 0, 255)
    dict_box[K.S_KEY_CAPTION_BOX_TRANS] = int(val)

    ctl = builder.get_object("spin_box_pad")
    val = ctl.get_value()
    dict_box[K.S_KEY_CAPTION_BOX_PAD] = int(val)

    ctl = builder.get_object("spin_box_rad")
    val = ctl.get_value()
    dict_box[K.S_KEY_CAPTION_BOX_RAD] = int(val)

    # --------------------------------------------------------------------------

    dict_pad = dict_cap[K.S_KEY_CAPTION_PAD]

    ctl = builder.get_object("spin_pad_l")
    val = ctl.get_value()
    dict_pad[K.S_KEY_CAPTION_PAD_L] = int(val)

    ctl = builder.get_object("spin_pad_t")
    val = ctl.get_value()
    dict_pad[K.S_KEY_CAPTION_PAD_T] = int(val)

    ctl = builder.get_object("spin_pad_r")
    val = ctl.get_value()
    dict_pad[K.S_KEY_CAPTION_PAD_R] = int(val)

    ctl = builder.get_object("spin_pad_b")
    val = ctl.get_value()
    dict_pad[K.S_KEY_CAPTION_PAD_B] = int(val)


# ------------------------------------------------------------------------------
# A helper method for creating a list of values from a Gdk.Color
# ------------------------------------------------------------------------------
def _unmake_color(val: Gdk.RGBA) -> list[int]:
    """
    A helper method for creating a list of values from a Gdk.Color

    Args:
        val: A Gdk.RGBA object

    Returns:
        A list of red, green, and blue values
    """

    # get values from color
    new_list = [val.red, val.green, val.blue]

    # convert from 0-1 to 0-255
    new_list = [F.interpolate(item, 0, 1, 0, 255) for item in new_list]

    # convert from float to int
    new_list = [int(item) for item in new_list]

    # return new list compatible with PIL
    return new_list


# -)
