from distutils.core import setup

NEEDED_MODULES = [
    ("PyQt4",
    "http://www.riverbankcomputing.co.uk/software/pyqt/intro"),
]


setup(
    name='MPIS-QT',
    version='0.1.0-alpha1',
    packages=['mpisqtlib', 'mpisqtlib.gui', 'mpisqtlib.gui.misc',
              'mpisqtlib.gui.dialogs'],
    url='https://kernelpanicblog.wordpress.com',
    keywords="manjaro linux post install script gui qt",
    license='gplv3',
    author='Harrinsoft',
    author_email='harrinsoft@gmail.com',
    description='This script allows to configure the system,'
                'install some applications for a regular work day designed'
                'for developers, gamers, musicians and more...',
    data_files=[("/usr/share/licenses/mpisqt", ["LICENSE"])],
    scripts=['mpis_qt']
)