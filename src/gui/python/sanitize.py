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

# TODO: there may be more onus on this func to fix F.bool and F.clamp to
# separate vals (like F.interpolate) as i update cnlib

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

    dict_cron[K.S_KEY_CRON_ENABLED] = F.do_bool(
        dict_cron[K.S_KEY_CRON_ENABLED]
    )
    dict_cron[K.S_KEY_CRON_INTERVAL] = F.clamp(
        dict_cron[K.S_KEY_CRON_INTERVAL], R_INTERVAL
    )

    # --------------------------------------------------------------------------

    dict_cap = dict_cfg[K.S_KEY_CAPTION]

    dict_cap[K.S_KEY_CAPTION_SHOW] = F.do_bool(
        dict_cap[K.S_KEY_CAPTION_SHOW]
    )
    dict_cap[K.S_KEY_CAPTION_POS] = F.clamp(
        dict_cap[K.S_KEY_CAPTION_POS], R_POS
    )
    dict_cap[K.S_KEY_CAPTION_WRAP] = F.clamp(
        dict_cap[K.S_KEY_CAPTION_WRAP], R_WRAP
    )

    # --------------------------------------------------------------------------

    dict_info = dict_cap[K.S_KEY_CAPTION_INFO]

    dict_info[K.S_KEY_CAPTION_INFO_TITLE] = F.do_bool(
        dict_info[K.S_KEY_CAPTION_INFO_TITLE]
    )
    dict_info[K.S_KEY_CAPTION_INFO_DATE] = F.do_bool(
        dict_info[K.S_KEY_CAPTION_INFO_DATE]
    )
    dict_info[K.S_KEY_CAPTION_INFO_COPY] = F.do_bool(
        dict_info[K.S_KEY_CAPTION_INFO_COPY]
    )
    dict_info[K.S_KEY_CAPTION_INFO_EXP] = F.do_bool(
        dict_info[K.S_KEY_CAPTION_INFO_EXP]
    )

    # --------------------------------------------------------------------------

    dict_font = dict_cap[K.S_KEY_CAPTION_FONT]

    dict_font[K.S_KEY_CAPTION_FONT_NAME] = str(
        dict_font[K.S_KEY_CAPTION_FONT_NAME]
    )
    dict_font[K.S_KEY_CAPTION_FONT_SIZE] = F.clamp(
        dict_font[K.S_KEY_CAPTION_FONT_SIZE], R_FONT_SIZE
    )
    dict_font[K.S_KEY_CAPTION_FONT_COLOR] = _clamp_list(
        dict_font[K.S_KEY_CAPTION_FONT_COLOR], R_COLOR
    )
    dict_font[K.S_KEY_CAPTION_FONT_TRANS] = F.clamp(
        dict_font[K.S_KEY_CAPTION_FONT_TRANS], R_COLOR
    )

    # --------------------------------------------------------------------------

    dict_box = dict_cap[K.S_KEY_CAPTION_BOX]

    dict_box[K.S_KEY_CAPTION_BOX_COLOR] = _clamp_list(
        dict_box[K.S_KEY_CAPTION_BOX_COLOR], R_COLOR
    )
    dict_box[K.S_KEY_CAPTION_BOX_TRANS] = F.clamp(
        dict_box[K.S_KEY_CAPTION_BOX_TRANS], R_COLOR
    )
    dict_box[K.S_KEY_CAPTION_BOX_RAD] = F.clamp(
        dict_box[K.S_KEY_CAPTION_BOX_RAD], R_BOX_RAD
    )
    dict_box[K.S_KEY_CAPTION_BOX_PAD] = F.clamp(
        dict_box[K.S_KEY_CAPTION_BOX_PAD], R_BOX_PAD
    )

    # --------------------------------------------------------------------------

    dict_pad = dict_cap[K.S_KEY_CAPTION_PAD]

    dict_pad[K.S_KEY_CAPTION_PAD_L] = F.clamp(
        dict_pad[K.S_KEY_CAPTION_PAD_L], R_EXT_PAD
    )
    dict_pad[K.S_KEY_CAPTION_PAD_T] = F.clamp(
        dict_pad[K.S_KEY_CAPTION_PAD_T], R_EXT_PAD
    )
    dict_pad[K.S_KEY_CAPTION_PAD_R] = F.clamp(
        dict_pad[K.S_KEY_CAPTION_PAD_R], R_EXT_PAD
    )
    dict_pad[K.S_KEY_CAPTION_PAD_B] = F.clamp(
        dict_pad[K.S_KEY_CAPTION_PAD_B], R_EXT_PAD
    )


# ------------------------------------------------------------------------------
# Clamp all values in a list (used for color vals 0-255)
# ------------------------------------------------------------------------------
def _clamp_list(list_in: list[int], vals: list[int]) -> list[int]:
    """
    Clamp all values in a list (used for color vals 0-255)

    :param list_in: The list of values to be clamped
    :type list_in: list[int]
    :param vals: The range to clamp, as a tuple
    :type vals: tuple(int, int)
    :return: A new list with clamped values
    :rtype: list[int]
    """
    new_list = [F.clamp(item, vals) for item in list_in]
    return new_list


# -)
