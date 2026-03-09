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
from cnlib import cnfunctions as F  # pylint: disable=import-error
import gi

gi.require_version("Gtk", "3.0")

# pylint: disable=wrong-import-position
# pylint: disable=no-name-in-module

from gi.repository import Gtk, Gdk  # type: ignore

# pylint: enable=wrong-import-position
# pylint: enable=no-name-in-module

# local imports
import keys as K
from sanitize import do_sanitize

# ------------------------------------------------------------------------------
# Public methods
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# A convenience method to load data from a file into the GUI
# ------------------------------------------------------------------------------
def do_load(builder: Gtk.Builder, dict_cfg: dict) -> None:
    """
    A convenience method to load data from a file into the GUI

    Args:
        builder: The GtkBuilder object that owns our GUI file
        dict_cfg: The JSON file with our data
    """

    # --------------------------------------------------------------------------

    # sanitize dict first
    do_sanitize(dict_cfg)

    # --------------------------------------------------------------------------

    dict_cron = dict_cfg[K.S_KEY_CRON]

    ctl = builder.get_object("sw_cron")
    val = dict_cron[K.S_KEY_CRON_ENABLED]
    ctl.set_active(val)

    ctl = builder.get_object("spin_cron")
    val = dict_cron[K.S_KEY_CRON_INTERVAL]
    ctl.set_value(val)

    # --------------------------------------------------------------------------

    dict_cap = dict_cfg[K.S_KEY_CAPTION]

    ctl = builder.get_object("sw_caption")
    val = dict_cap[K.S_KEY_CAPTION_SHOW]
    ctl.set_active(val)

    ctl = builder.get_object("cmb_position")
    val = dict_cap[K.S_KEY_CAPTION_POS]
    ctl.set_active(val)

    ctl = builder.get_object("spin_wrap")
    val = dict_cap[K.S_KEY_CAPTION_WRAP]
    ctl.set_value(val)

    # --------------------------------------------------------------------------

    dict_info = dict_cap[K.S_KEY_CAPTION_INFO]

    ctl = builder.get_object("chk_info_title")
    val = dict_info[K.S_KEY_CAPTION_INFO_TITLE]
    ctl.set_active(val)

    ctl = builder.get_object("chk_info_date")
    val = dict_info[K.S_KEY_CAPTION_INFO_DATE]
    ctl.set_active(val)

    ctl = builder.get_object("chk_info_copyright")
    val = dict_info[K.S_KEY_CAPTION_INFO_COPY]
    ctl.set_active(val)

    ctl = builder.get_object("chk_info_explanation")
    val = dict_info[K.S_KEY_CAPTION_INFO_EXP]
    ctl.set_active(val)

    # --------------------------------------------------------------------------

    dict_font = dict_cap[K.S_KEY_CAPTION_FONT]

    # TODO: need to set font using path (fc-list) PIL DOES THIS!!!
    # NB: initial name null, "None", "", "Normal" work on my machine
    ctl = builder.get_object("btn_font")
    val = dict_font[K.S_KEY_CAPTION_FONT_NAME]
    ctl.set_font_name(val)

    ctl = builder.get_object("spin_font_size")
    val = dict_font[K.S_KEY_CAPTION_FONT_SIZE]
    ctl.set_value(val)

    ctl = builder.get_object("btn_font_color")
    val = dict_font[K.S_KEY_CAPTION_FONT_COLOR]
    val = _make_color(val)
    ctl.set_rgba(val)

    ctl = builder.get_object("spin_font_trans")
    val = dict_font[K.S_KEY_CAPTION_FONT_TRANS]
    # NB: interpolate from 8-bit(PIL/json) to percent(display)
    # no apparent loss of precision
    val = F.interpolate(val, 0, 255, 0, 100)
    ctl.set_value(val)

    # --------------------------------------------------------------------------

    dict_box = dict_cap[K.S_KEY_CAPTION_BOX]

    ctl = builder.get_object("btn_box_color")
    val = dict_box[K.S_KEY_CAPTION_BOX_COLOR]
    val = _make_color(val)
    ctl.set_rgba(val)

    ctl = builder.get_object("spin_box_trans")
    val = dict_box[K.S_KEY_CAPTION_BOX_TRANS]
    # NB: interpolate from 8-bit(PIL/json) to percent(display)
    # no apparent loss of precision
    val = F.interpolate(val, 0, 255, 0, 100)
    ctl.set_value(val)

    ctl = builder.get_object("spin_box_rad")
    val = dict_box[K.S_KEY_CAPTION_BOX_RAD]
    ctl.set_value(val)

    ctl = builder.get_object("spin_box_pad")
    val = dict_box[K.S_KEY_CAPTION_BOX_PAD]
    ctl.set_value(val)

    # --------------------------------------------------------------------------

    dict_pad = dict_cap[K.S_KEY_CAPTION_PAD]

    ctl = builder.get_object("spin_pad_l")
    val = dict_pad[K.S_KEY_CAPTION_PAD_L]
    ctl.set_value(val)

    ctl = builder.get_object("spin_pad_t")
    val = dict_pad[K.S_KEY_CAPTION_PAD_T]
    ctl.set_value(val)

    ctl = builder.get_object("spin_pad_r")
    val = dict_pad[K.S_KEY_CAPTION_PAD_R]
    ctl.set_value(val)

    ctl = builder.get_object("spin_pad_b")
    val = dict_pad[K.S_KEY_CAPTION_PAD_B]
    ctl.set_value(val)


# ------------------------------------------------------------------------------
# A helper method for creating a Gdk.Color from a list of values
# ------------------------------------------------------------------------------
def _make_color(val: list) -> Gdk.RGBA:
    """
    A helper method for creating a Gdk.Color from a list of values

    Args:
        val: List of red, green, and blue values

    Returns:
        A Gdk.RGBA object
    """

    # convert values to gdk spec
    val = [F.interpolate(item, 0, 255, 0, 1) for item in val]

    # create an opaque color from values
    new_color = Gdk.RGBA(val[0], val[1], val[2], 1.0)

    # return opaque color
    return new_color


# -)
