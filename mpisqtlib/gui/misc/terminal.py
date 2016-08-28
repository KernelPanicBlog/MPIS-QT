#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of MPIS (https://github.com/KernelPanicBlog/MPIS-QT).
#
# MPIS-QT(Manjaro Post Installation Script GUI QT) is free software; you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 3 of
# the License,or any later version.
#
# MPIS-QT (Manjaro Post Installation Script) GUI QT:
# It allows  users to choose different options such as
# install an application or config some tools and environments.
#
# MPIS-QT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MPIS-QT; If not, see <http://www.gnu.org/licenses/>.
###############################################################################
import atexit
from PyQt4.QtCore import QProcess
from PyQt4.QtCore import QSize
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QX11EmbedContainer
from PyQt4.QtGui import QApplication


class XTerm(QX11EmbedContainer):

    def __init__(self, parent, xterm_cmd="xterm"):
        QX11EmbedContainer.__init__(self, parent)
        self.xterm_cmd = xterm_cmd
        self.process = QProcess(self)
        self.connect(self.process,
                     SIGNAL("finished(int, QProcess::ExitStatus)"),
                     self.on_term_close)
        atexit.register(self.kill)
        self.show_term()

    def kill(self):
        self.process.kill()
        self.process.waitForFinished()

    def sizeHint(self):
        size = QSize(400, 300)
        return size.expandedTo(QApplication.globalStrut())

    def show_term(self):
        args = [
            "-into",
            str(self.winId()),
            "-bg",
            "#000000",  # self.palette().color(QPalette.Background).name(),
            "-fg",
            "#f0f0f0",  # self.palette().color(QPalette.Foreground).name(),
            # border
            "-b", "0",
            "-w", "0",
            # blink cursor
            "-bc",
            '-e', 'tmux', 'new', '-s', 'my_session'
        ]
        self.process.start(self.xterm_cmd, args)
        if self.process.error() == QProcess.FailedToStart:
            print("xterm not installed")

    def on_term_close(self, exit_code, exit_status):
        print("close", exit_code, exit_status)
        self.close()