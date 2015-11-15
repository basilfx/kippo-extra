# Copyright (c) 2013-2015 Bas Stottelaar <basstottelaar [AT] gmail [DOT] com>

from kippo_extra.utils import ExtendedHoneyPotCommand

commands = {}


class command_which(ExtendedHoneyPotCommand):
    # Do not resolve args
    resolve_args = False

    def call(self):
        """ Look up all the arguments on PATH and print each (first) result """

        # No arguments, just exit
        if not len(self.args) or 'PATH' not in self.env:
            return

        # Look up each file
        for f in self.args:
            for path in self.env['PATH'].split(':'):
                resolved = self.fs.resolve_path(f, path)

                if self.fs.exists(resolved):
                    self.writeln("%s/%s" % (path, f))
                    continue

# Definition
commands['/bin/which'] = command_which
