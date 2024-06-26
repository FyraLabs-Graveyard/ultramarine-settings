# main.py
#
# Copyright 2021-2022 Cappy Ishihara
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KI\D,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name(s) of the above copyright
# holders shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written
# authorization.

import sys
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '4')
from gi.repository import Gtk, Gio, GLib, Gdk, GObject, GtkSource

from .window import UltramarineSettingsWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.ultramarine.settings',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        GLib.set_application_name(("Ultramarine Settings"))
        GLib.set_prgname("org.ultramarine.settings")

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = UltramarineSettingsWindow(application=self).window
        win.present()
    


def main(version):
    app = Application()
    return app.run(sys.argv)
