from kippo_extra.utils import ExtendedHoneyPotCommand, ModifiedOptionParser, \
    OptionParsingError, OptionParsingExit

commands = {}


class command_uname(ExtendedHoneyPotCommand):
    def call(self):
        """ Add uname command to identify server """

        # Initialize options
        parser = ModifiedOptionParser(add_help_option=False)
        parser.add_option("--help", dest="help", action="store_true")
        parser.add_option("--version", dest="version", action="store_true")
        parser.add_option("-a", "--all", dest="all", action="store_true")
        parser.add_option(
            "-s", "--kenel-name", dest="name", action="store_true")
        parser.add_option(
            "-r", "--kernel-release", dest="release", action="store_true")
        parser.add_option(
            "-v", "--kernel-version", dest="kernel", action="store_true")
        parser.add_option(
            "-m", "--machine", dest="machine", action="store_true")
        parser.add_option(
            "-p", "--processor", dest="processor", action="store_true")
        parser.add_option(
            "-i", "--hardware-platform", dest="hardware", action="store_true")
        parser.add_option(
            "-o", "--operating-system", dest="os", action="store_true")

        try:
            (opts, args) = parser.parse_args(list(self.args))
        except OptionParsingError, e:
            self.bad_argument(self.args[0])
            return
        except OptionParsingExit, e:
            self.bad_argument(e)
            return

        if opts.help:
            self.help()
        elif opts.version:
            self.writeln("#1 SMP Wed Nov 4 23:40:10 UTC 2009")
        elif opts.all:
            self.writeln(
                "Linux %s 2.6.26-2-686 #1 SMP Wed Nov 4 20:45:37 "
                "UTC 2009 i686 GNU/Linux" % self.honeypot.hostname)
        else:
            parts = []

            # Actually, the order matters, e.g. '-s -r -v' gives another output
            # as '-r -v -s'.
            if opts.name:
                parts.append("Linux")
            if opts.release:
                parts.append("2.6.26-2-686")
            if opts.kernel:
                parts.append("#1 SMP Wed Nov 4 20:45:37 UTC 2009")
            if opts.machine:
                parts.append("i686")
            if opts.processor:
                parts.append("i686")
            if opts.hardware:
                parts.append("i686")
            if opts.os:
                parts.append("GNU/Linux")

            # No command given, disply the name only.
            if parts:
                self.writeln(" ".join(parts))
            else:
                self.writeln("Linux")

    def bad_argument(self, argument):
        self.writeln("""uname: invalid option -- '%s'
Try 'uname --help' for more information.""" % argument)

    def help(self):
        self.writeln("""Usage: uname [OPTION]...
Print certain system information.  With no OPTION, same as -s.

  -a, --all                print all information, in the following order,
                             except omit -p and -i if unknown:
  -s, --kernel-name        print the kernel name
  -n, --nodename           print the network node hostname
  -r, --kernel-release     print the kernel release
  -v, --kernel-version     print the kernel version
  -m, --machine            print the machine hardware name
  -p, --processor          print the processor type or "unknown"
  -i, --hardware-platform  print the hardware platform or "unknown"
  -o, --operating-system   print the operating system
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/uname>
or available locally via: info '(coreutils) uname invocation'""")

commands['/bin/uname'] = command_uname
