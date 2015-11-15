# Copyright (c) 2013-2015 Bas Stottelaar <basstottelaar [AT] gmail [DOT] com>

from kippo_extra.utils import ExtendedHoneyPotCommand
from twisted.internet import reactor

commands = {}


class command_sleep(ExtendedHoneyPotCommand):
    def start(self):
        """ Sleep for n seconds, or display help """

        if len(self.args) == 1:
            _time = int(self.args[0])
            self.scheduled = reactor.callLater(_time, self.exit)
        else:
            self.writeln_and_exit('usage: sleep seconds')

commands['/bin/sleep'] = command_sleep
