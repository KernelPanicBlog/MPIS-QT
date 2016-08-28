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
from PyQt4.QtCore import QObject
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QCheckBox

from mpislib import core


class Communicate(QObject):
    clickedQCheckBox = pyqtSignal()


class TabMenu(QWidget):
    """docstring for TabMenu"""

    def __init__(self, list_apps, parent=None):
        super(TabMenu, self).__init__(parent)
        self.flag_clickedCkeckbox = False
        self._columm = None
        self._itemxcolumm = None
        self._max_itemxcolumm = None
        self.communicate = Communicate()
        self._list_apps = list_apps
        self.listCommands = []
        self._calculate_distribution()
        self._init_ui()

    def _init_ui(self):
        self.list_items = []

        if self._columm == 2:
            self._box = QGridLayout()
        else:
            self._box = QVBoxLayout()
        j, i, x = 0, 0, 0

        for item in self._list_apps:
            if self.objectName() != item.category.name:
                self.setObjectName(item.category.name)
            new_qcb = QCheckBox(item.title)
            new_qcb.setObjectName(item.name)
            new_qcb.clicked.connect(self._addcommand)

            if isinstance(self._box, QGridLayout):

                if i == 0:
                    self._box.addWidget(new_qcb, j, i)
                    i = 1
                    x += 1
                else:
                    self._box.addWidget(new_qcb, j, i)
                    i = 0
                    x += 1

                if x == 2:
                    j += 1
                    x = 0

            elif isinstance(self._box, QVBoxLayout):
                self._box.addWidget(new_qcb)

        self.setLayout(self._box)

    def _calculate_distribution(self):

        items = len(self._list_apps)
        resultado = items // 2
        resto = items % 2

        if resultado > 5 <= 10:
            self._columm = 2
        else:
            self._columm = 1

        self._itemxcolumm = resultado

    def _addcommand(self):
        var = self.sender().objectName()
        if self.sender().isChecked():
            _app = core.search_commands(var, self._list_apps)
            for cmd in _app.commands:
                self.listCommands.append(cmd)
        else:
            _app = core.search_commands(var, self._list_apps)
            for item in _app.commands:
                for cmd in range(len(self.listCommands)-1, -1, -1):
                    if self.listCommands[cmd] == item:
                        del self.listCommands[cmd]
        self.flag_clickedCkeckbox = True
        self.communicate.clickedQCheckBox.emit()
