# Copyright (c) 2012 Bas Stottelaar <basstottelaar [AT] gmail [DOT] com>

from utils import ExtendedHoneyPotCommand

commands = {}

class command_env(ExtendedHoneyPotCommand):
    def call(self):
        """ Print the current environment variables """
        
        if self.env and len(self.env) > 0:
            for key, value in self.env.iteritems():
                self.writeln("%s=%s" % (key, value))

# Definition
commands['/usr/bin/env'] = command_env