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
import webbrowser

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

import mpislib
import mpisqtlib
from mpisqtlib import resource


class AboutMpisQT(QDialog):

    def __init__(self, parent=None):
        super(AboutMpisQT, self).__init__(parent)

        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle(self.tr("About MPIS-QT"))
        self.setMaximumSize(QSize(0, 0))

        vbox = QVBoxLayout(self)

        self.lblIcon = QLabel()
        self.lblIcon.setPixmap(
            QPixmap(resource.get_image("banner"), 'png')
        )

        hbox = QHBoxLayout()
        hbox.addWidget(self.lblIcon)

        title_qlbl = QLabel(
            '<h1>MPIS-QT</h1>'
            '<i>QT GUI to Manjaro Post Install scritp<i>\n'
        )
        title_qlbl.setTextFormat(Qt.RichText)
        title_qlbl.setAlignment(Qt.AlignLeft)
        hbox.addWidget(title_qlbl)

        vbox.addLayout(hbox)

        vbox.addWidget(
            QLabel(self.tr(
"""MPIS-QT ("Manjaro Post Install scritp" QT GUI), is a script
allows to configure the system, install some applications
for a regular work day designed for developers, gamers,
musicians and more...
""")))
        vbox.addWidget(
            QLabel(self.tr("MPIS Version: %s") % mpislib.__version__)
        )
        vbox.addWidget(
            QLabel(self.tr("MPIS-QT Version: %s") % mpisqtlib.__version__)
        )
        link_kernelpanicblog = QLabel(
            self.tr('Website: <a href="%s"><span style=" '
                    'text-decoration: underline; color:#ff9e21;">'
                    '%s</span></a>') % (mpisqtlib.__url__, mpisqtlib.__url__))

        vbox.addWidget(link_kernelpanicblog)

        link_source = QLabel(
            self.tr('Source Code: <a href="%s"><span style=" '
            'text-decoration: underline; color:#ff9e21;">%s</span></a>') %
            (mpisqtlib.__source__, mpisqtlib.__source__))
        vbox.addWidget(link_source)

        self.connect(link_kernelpanicblog,
                     SIGNAL("linkActivated(QString)"),
                     self.link_activated)
        self.connect(link_source,
                     SIGNAL("linkActivated(QString)"),
                     self.link_activated)

    def link_activated(self, link):
        webbrowser.open(str(link))
