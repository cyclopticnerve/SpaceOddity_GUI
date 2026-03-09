
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# venv imports
import gi

gi.require_version("Pango", "1.0")

# pylint: disable=wrong-import-position
# pylint: disable=no-name-in-module

from gi.repository import Pango  # type: ignore

# pylint: enable=wrong-import-position
# pylint: enable=no-name-in-module

# ------------------------------------------------------------------------------

string_in = "Noto Sans Bold Italic 16"
path_out = ""

font = Pango.font_description_from_string(string_in)

print("family:", font.get_family())
# print("gravity:", font.get_gravity())
print("style:", font.get_style())
print("weight:", font.get_weight())
print("size:", font.get_size()) # has too many digits
