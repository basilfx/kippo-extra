# Copyright (c) 2013-2015 Bas Stottelaar <basstottelaar [AT] gmail [DOT] com>

from kippo.core.honeypot import HoneyPotCommand

import optparse


class ExtendedHoneyPotCommand(HoneyPotCommand):
    """
    Extend the HoneyPotCommand class with some commonly used methods.
    """

    def __init__(self, *args, **kwargs):
        super(ExtendedHoneyPotCommand, self).__init__(*args, **kwargs)

        # Override default writeln
        def _writeln(data):
            """
            Write data to the honeypot terminal. Data can be a string, but also
            an iterable
            """

            # If data is iterable, then write line for line
            if type(data) in (type([]), type(())):
                for line in data:
                    self.honeypot.writeln(line)
            else:
                self.honeypot.writeln(data)
        self.writeln = _writeln

    def writeln_and_exit(self, data):
        """
        Write data and exit. Useful for more complicated commands that need to
        display help, version e.g.
        """

        # Write data and quit
        self.writeln(data)
        self.exit()

    def user_is_root(self):
        return self.honeypot.user.username == 'root'


class OptionParsingError(RuntimeError):
    def __init__(self, msg):
        self.msg = msg


class OptionParsingExit(Exception):
    def __init__(self, status, msg):
        self.msg = msg
        self.status = status


class ModifiedOptionParser(optparse.OptionParser):
    def error(self, msg):
        raise OptionParsingError(msg)

    def exit(self, status=0, msg=None):
        raise OptionParsingExit(status, msg)
