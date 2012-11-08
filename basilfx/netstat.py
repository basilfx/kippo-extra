# Copyright (c) 2012 Bas Stottelaar <basstottelaar [AT] gmail [DOT] com>

from utils import ExtendedHoneyPotCommand
from twisted.internet import reactor

import time, re, getopt, random

commands = {}

class command_netstat(ExtendedHoneyPotCommand):
    def call(self):
        pass

    def show_version(self):
        self.writeln_and_exit([
            'netstat 1.42 (2001-04-15)',
            'Fred Baumgarten, Alan Cox, Bernd Eckenfels, Phil Blundell, Tuan Hoang and others',
            '+NEW_ADDRT +RTF_IRTT +RTF_REJECT +FW_MASQUERADE +I18N',
            'AF: (inet) +UNIX +INET +INET6 +IPX +AX25 +NETROM +X25 +ATALK +ECONET +ROSE',
            'HW:  +ETHER +ARC +SLIP +PPP +TUNNEL +TR +AX25 +NETROM +X25 +FR +ROSE +ASH +SIT +FDDI +HIPPI +HDLC/LAPB +EUI64'
        ])

    def show_help(self):
        self.writeln_and_exit([
            'usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}',
            '       netstat [-vWnNcaeol] [<Socket> ...]',
            '       netstat { [-vWeenNac] -i | [-cWnNe] -M | -s }',
            '',
            '        -r, --route              display routing table',
            '        -i, --interfaces         display interface table',
            '        -g, --groups             display multicast group memberships',
            '        -s, --statistics         display networking statistics (like SNMP)',
            '        -M, --masquerade         display masqueraded connections',
            '',
            '        -v, --verbose            be verbose',
            '        -W, --wide               don\'t truncate IP addresses',
            '        -n, --numeric            don\'t resolve names',
            '        --numeric-hosts          don\'t resolve host names',
            '        --numeric-ports          don\'t resolve port names',
            '        --numeric-users          don\'t resolve user names',
            '        -N, --symbolic           resolve hardware names',
            '        -e, --extend             display other/more information',
            '        -p, --programs           display PID/Program name for sockets',
            '        -c, --continuous         continuous listing',
            '',
            '        -l, --listening          display listening server sockets',
            '        -a, --all, --listening   display all sockets (default: connected)',
            '        -o, --timers             display timers',
            '        -F, --fib                display Forwarding Information Base (default)',
            '        -C, --cache              display routing cache instead of FIB',
            '',
            '  <Socket>={-t|--tcp} {-u|--udp} {-w|--raw} {-x|--unix} --ax25 --ipx --netrom',
            '  <AF>=Use \'-6|-4\' or \'-A <af>\' or \'--<af>\'; default: inet',
            '  List of possible address families (which support routing):',
            '    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25) ',
            '    netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP) ',
            '    x25 (CCITT X.25) ',
        ])

# Definitions
commands['/bin/netstat'] = command_netstat