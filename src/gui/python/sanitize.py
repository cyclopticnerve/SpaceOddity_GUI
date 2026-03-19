# ------------------------------------------------------------------------------
# Project : SpaceOddity_GUI                                        /          \
# Filename: sanitize.py                                           |     ()     |
# Date    : 12/29/2025                                            |            |
# Author  : cyclopticnerve                                        |   \____/   |
# License : WTFPLv2                                                \          /
# ------------------------------------------------------------------------------

"""
This module contains helper stuff to sanitize the config file in case it was
edited by hand. Basically we just ensure bools are True/False and numbers are
clamped to a sensible range.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# venv imports
from cnlib import cnfunctions as F

# local imports
import keys as K

# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Ranges

# ranges for number entries
R_INTERVAL = [1, 59]
R_POS = [0, 8]
R_WRAP = [0, 100]
R_FONT_SIZE = [1, 100]
R_COLOR = [0, 255]  # r, g, b, and transparency
R_BOX_RAD = [0, 100]
R_BOX_PAD = [0, 100]
R_EXT_PAD = [0, 100]

# ------------------------------------------------------------------------------
# Sanitize the dictionary in place
# ------------------------------------------------------------------------------
def do_sanitize(dict_cfg: dict):
    """
    Sanitize the dictionary in place

    :param dict_cfg: The dictionary to sanitize
    :type dict_cfg: dict

    This method takes a dictionary and clamps its values to sensible values.
    """

    # --------------------------------------------------------------------------

    # these are in the cron dict
    dict_cron = dict_cfg[K.S_KEY_CRON]

    dict_cron[K.S_KEY_CRON_ENABLED] = bool(
        dict_cron[K.S_KEY_CRON_ENABLED]
    )
    dict_cron[K.S_KEY_CRON_INTERVAL] = _do_clamp(
        dict_cron[K.S_KEY_CRON_INTERVAL], R_INTERVAL
    )

    # --------------------------------------------------------------------------

    dict_cap = dict_cfg[K.S_KEY_CAPTION]

    dict_cap[K.S_KEY_CAPTION_SHOW] = bool(
        dict_cap[K.S_KEY_CAPTION_SHOW]
    )
    dict_cap[K.S_KEY_CAPTION_POS] = _do_clamp(
        dict_cap[K.S_KEY_CAPTION_POS], R_POS
    )
    dict_cap[K.S_KEY_CAPTION_WRAP] = _do_clamp(
        dict_cap[K.S_KEY_CAPTION_WRAP], R_WRAP
    )

    # --------------------------------------------------------------------------

    dict_info = dict_cap[K.S_KEY_CAPTION_INFO]

    dict_info[K.S_KEY_CAPTION_INFO_TITLE] = bool(
        dict_info[K.S_KEY_CAPTION_INFO_TITLE]
    )
    dict_info[K.S_KEY_CAPTION_INFO_DATE] = bool(
        dict_info[K.S_KEY_CAPTION_INFO_DATE]
    )
    dict_info[K.S_KEY_CAPTION_INFO_COPY] = bool(
        dict_info[K.S_KEY_CAPTION_INFO_COPY]
    )
    dict_info[K.S_KEY_CAPTION_INFO_EXP] = bool(
        dict_info[K.S_KEY_CAPTION_INFO_EXP]
    )

    # --------------------------------------------------------------------------

    dict_font = dict_cap[K.S_KEY_CAPTION_FONT]

    dict_font[K.S_KEY_CAPTION_FONT_NAME] = str(
        dict_font[K.S_KEY_CAPTION_FONT_NAME]
    )
    dict_font[K.S_KEY_CAPTION_FONT_SIZE] = _do_clamp(
        dict_font[K.S_KEY_CAPTION_FONT_SIZE], R_FONT_SIZE
    )
    dict_font[K.S_KEY_CAPTION_FONT_COLOR] = _clamp_list(
        dict_font[K.S_KEY_CAPTION_FONT_COLOR], R_COLOR
    )
    dict_font[K.S_KEY_CAPTION_FONT_TRANS] = _do_clamp(
        dict_font[K.S_KEY_CAPTION_FONT_TRANS], R_COLOR
    )

    # --------------------------------------------------------------------------

    dict_box = dict_cap[K.S_KEY_CAPTION_BOX]

    dict_box[K.S_KEY_CAPTION_BOX_COLOR] = _clamp_list(
        dict_box[K.S_KEY_CAPTION_BOX_COLOR], R_COLOR
    )
    dict_box[K.S_KEY_CAPTION_BOX_TRANS] = _do_clamp(
        dict_box[K.S_KEY_CAPTION_BOX_TRANS], R_COLOR
    )
    dict_box[K.S_KEY_CAPTION_BOX_RAD] = _do_clamp(
        dict_box[K.S_KEY_CAPTION_BOX_RAD], R_BOX_RAD
    )
    dict_box[K.S_KEY_CAPTION_BOX_PAD] = _do_clamp(
        dict_box[K.S_KEY_CAPTION_BOX_PAD], R_BOX_PAD
    )

    # --------------------------------------------------------------------------

    dict_pad = dict_cap[K.S_KEY_CAPTION_PAD]

    dict_pad[K.S_KEY_CAPTION_PAD_L] = _do_clamp(
        dict_pad[K.S_KEY_CAPTION_PAD_L], R_EXT_PAD
    )
    dict_pad[K.S_KEY_CAPTION_PAD_T] = _do_clamp(
        dict_pad[K.S_KEY_CAPTION_PAD_T], R_EXT_PAD
    )
    dict_pad[K.S_KEY_CAPTION_PAD_R] = _do_clamp(
        dict_pad[K.S_KEY_CAPTION_PAD_R], R_EXT_PAD
    )
    dict_pad[K.S_KEY_CAPTION_PAD_B] = _do_clamp(
        dict_pad[K.S_KEY_CAPTION_PAD_B], R_EXT_PAD
    )


# ------------------------------------------------------------------------------
# Clamp a value to a range
# ------------------------------------------------------------------------------
def _do_clamp(val_in: float, vals: list[int]) -> float:
    """
    Clamp a value to a range

    Args:
        val_in: value to be clamped
        vals: list of min/max range
    """

    res = F.clamp(val_in, vals[0], vals[1])
    return res


# ------------------------------------------------------------------------------
# Clamp all values in a list (used for color vals)
# ------------------------------------------------------------------------------
def _clamp_list(list_in: list[int], vals: list[int]) -> list[float]:
    """
    Clamp all values in a list (used for color vals 0-255)

    :param list_in: The list of values to be clamped
    :type list_in: list[int]
    :param vals: The range to clamp, as a tuple
    :type vals: tuple(int, int)
    :return: A new list with clamped values
    :rtype: list[int]
    """

    new_list = [F.clamp(item, vals[0], vals[1]) for item in list_in]
    return new_list


# -)
