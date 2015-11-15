# Copyright (c) 2013-2015 Bas Stottelaar <basstottelaar [AT] gmail [DOT] com>

from kippo_extra.utils import ExtendedHoneyPotCommand

commands = {}


class command_env(ExtendedHoneyPotCommand):
    def call(self):
        """ Print the current environment variables """

        if self.env and len(self.env) > 0:
            for key, value in self.env.iteritems():
                self.writeln("%s=%s" % (key, value))

# Definition
commands['/usr/bin/env'] = command_env