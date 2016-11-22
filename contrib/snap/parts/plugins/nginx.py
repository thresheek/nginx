import os
import logging
import shutil
import re
import subprocess

import snapcraft
from snapcraft.plugins import autotools

logger = logging.getLogger(__name__)

class NGINXPlugin(autotools.AutotoolsPlugin):

    def build(self):
        super(autotools.AutotoolsPlugin, self).build()

        configure_command = ['./auto/configure']
        make_install_command = ['make', 'install']

        configure_command.append('--prefix=' + self.installdir)
        self.run(configure_command + self.options.configflags)
        self.run(['make', '-j{}'.format(self.parallel_build_count)])
        self.run(make_install_command)
