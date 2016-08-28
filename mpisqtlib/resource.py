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

import os
from PyQt4.QtCore import QDir
from PyQt4.QtGui import QKeySequence
from PyQt4.QtCore import Qt

###############################################################################
# PATHS
###############################################################################

HOME_PATH = QDir.toNativeSeparators(QDir.homePath())

LIB_PATH = os.path.abspath(os.path.dirname(__file__))

IMG_PATH = os.path.join("/user", "share", "mpisqt")

###############################################################################
# URLS
###############################################################################

BUGS_PAGE = "https://github.com/KernelPanicBlog/MPIS/issues"

HOME_PAGE = "https://kernelpanicblog.wordpress.com"

###############################################################################
# IMAGES
###############################################################################

IMAGES = {
    "splash": os.path.join(IMG_PATH, "img", "splash.png"),
    "icon": os.path.join(IMG_PATH, "img", "icon.png"),
    "banner": os.path.join(IMG_PATH, "img", "banner.png")
}

###############################################################################
# SHORTCUTS
###############################################################################

SHORTCUTS = {
    "About-MpisQt": QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_A),
    "About-Qt": QKeySequence(Qt.ALT + Qt.SHIFT + Qt.Key_Q),
    "Show-readme": QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_R),
    "Show-changelog": QKeySequence(Qt.ALT + Qt.Key_C),
    "Report-bug": QKeySequence(Qt.ALT + Qt.Key_R)
}

###############################################################################
# FUNCTIONS
###############################################################################


def get_image(image_name):

    global IMAGES

    return IMAGES.get(image_name)


def get_shortcut(shortcut_name):

    global SHORTCUTS

    return SHORTCUTS.get(shortcut_name)
