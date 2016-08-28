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

import mpislib
from mpislib import core
from mpisqtlib.gui.dialogs import about_dialog
from mpisqtlib.gui.misc import terminal
from mpisqtlib.gui.misc import tab_menu
from mpisqtlib import resource


class MpisQt(QMainWindow):

    def __init__(self, parent=None):
        super(MpisQt, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):

        self.setWindowTitle("Manjaro Post Installation Script (MPIS)")

        self._processes = []
        self._Tabs = []
        self._mpis_cli = mpislib.core.Mpis()
        # Actions
        action_report_bug = QAction('&Report Bug!', self)
        action_report_bug.setShortcuts(resource.get_shortcut("Report-bug"))
        action_report_bug.setStatusTip('Report Bug')
        action_report_bug.triggered.connect(self.report_bug)

        action_about_mpisqt = QAction('&About Mpis-Qt', self)
        action_about_mpisqt.setShortcut(resource.get_shortcut("About-MpisQt"))
        action_about_mpisqt.setStatusTip('Show Dialog About Mpis-Qt')
        action_about_mpisqt.triggered.connect(self.show_about_mpisqt)

        action_about_qt = QAction('About &Qt', self)
        action_about_qt.setShortcut(resource.get_shortcut("About-Qt"))
        action_about_qt.setStatusTip('Show Dialog About Qt')
        action_about_qt.triggered.connect(self.show_about_qt)

        # Menus
        menu_about = self.menuBar().addMenu('&About')
        menu_about.addAction(action_report_bug)
        menu_about.addSeparator()
        menu_about.addAction(action_about_mpisqt)
        menu_about.addAction(action_about_qt)

        self.statusBar()

        self._vbox = QVBoxLayout()
        self._hbox = QHBoxLayout()
        self._central_widget = QWidget()
        self._grublayout = QWidget()

        self._run_qpb = QPushButton("Run")
        self._run_qpb.clicked.connect(self._exe_command)
        self._cancel_qpb = QPushButton("Cancel")
        self._buttonlayout = QHBoxLayout()
        self._buttonlayout.addStretch(1)
        self._buttonlayout.addWidget(self._run_qpb)
        self._buttonlayout.addWidget(self._cancel_qpb)

        self._TabPanel = QTabWidget()
        for category in self._mpis_cli.categorys:
            if category != "Main Menu":
                new_tab = tab_menu.TabMenu(
                    self._mpis_cli.get_app_by_category(category)
                )
                new_tab.setMouseTracking(True)
                new_tab.installEventFilter(self)
                new_tab.communicate.clickedQCheckBox.connect(
                    self._update_list_cmds
                )
                self._Tabs.append(new_tab)
                self._TabPanel.addTab(new_tab, category)

        self._terminal_dock = QDockWidget("Xterm", self)
        self._terminal = terminal.XTerm(self._terminal_dock)
        self._terminal_dock.setWidget(self._terminal)
        self._terminal_dock.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self._terminal_dock)
        self._terminal_dock.setFixedHeight(150)

        self._list_cmds_dock = QDockWidget("command list")
        self._list_cmd = QListWidget()
        self._vbox.addWidget(self._list_cmd)
        self._vbox.addLayout(self._buttonlayout)
        self._grublayout.setLayout(self._vbox)
        self._list_cmds_dock.setWidget(self._grublayout)
        self.addDockWidget(Qt.RightDockWidgetArea, self._list_cmds_dock)
        self._list_cmds_dock.setFixedWidth(250)

        self._hbox.addWidget(self._TabPanel)

        self._central_widget.setLayout(self._hbox)

        self.setCentralWidget(self._central_widget)

    @pyqtSlot()
    def report_bug(self):
        webbrowser.open(resource.BUGS_PAGE)

    @pyqtSlot()
    def show_about_mpisqt(self):
        about = about_dialog.AboutMpisQT(self)
        about.show()

    @pyqtSlot()
    def show_about_qt(self):
        QMessageBox.aboutQt(self, self.tr("About Qt"))

    def _update_list_cmds(self):
        self._list_cmd.clear()
        for tab in self._Tabs:
            if tab.flag_clickedCkeckbox:
                for cmd in tab.listCommands:
                    self._list_cmd.addItem(cmd)
            tab.flag_clickedCkeckbox = False

    def _start_process(self, prog, args):
        child = QProcess()
        self._processes.append(child)
        child.start(prog, args)
        child.waitForFinished()

    def _exe_command(self):
        __list_command = []

        for i in range(self._list_cmd.count()):
            __list_command.append(self._list_cmd.item(i).text())

        self._list_cmd.clear()

        for _cmd in __list_command:
            self._start_process(
                'tmux', ['send-keys',
                         '-t',
                         'my_session:0',
                         str(_cmd), 'Enter']
            )

    def _kill_terminal_process(self):
        self._start_process(
            'tmux', ['send-keys',
                     '-t',
                     'my_session:0',
                     'exit',
                     'Enter']
        )

    def closeEvent(self, event):
        self._kill_terminal_process()
        event.accept()