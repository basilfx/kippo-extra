# kippo-commands
Set of extra commands for the kippo SSH honeypot daemon (http://code.google.com/p/kippo/).

## Provided commands
* `/usr/bin/env` - current environment variables
* `/usr/bin/gcc` - fake compiler with file output
* `/sbin/iptables` - fake firewall management, supports flush and list for different tables/chains
* `/bin/which` - path of binary
* `/bin/netstat` - work in progress

The commands are based on the x64 build of Debian 5.


## Installation
Please read the full installation part.

Kippo does not have an easy way to add commands via the `kippo.cfg` file. Therefore, you will have to copy the folder `basilfx` to the `KIPPO_ROOT/kippo/commands/` directory. You will also have to edit the file `KIPPO_ROOT/kippo/commands/__init__.py` file and add the following after the last command in the list:

```
# Custom
'basilfx.gcc',
'basilfx.iptables',
'basilfx.netstat',
'basilfx.env',
'basilfx.which',
```

Make sure you put it in the list. Remove a line to remove a command.

### Note 1
Since kippo does not pass the environment variables (yet), you'll have apply a patch to the kippo source for now. By default, kippo also resolves command line arguments. For example, if you execute `gcc testfile.c -o test` and there exists a file/program called test, it would resolve it to `/path/to/test`. But in this case, `test` is the name of the output file you want to create in the current directory directory!

The patch is included in the `patch` directory and makes this behavior selectable. Change directory to `KIPPO_ROOT/kippo/core` and execute `patch -p0 < /path/to/honeypot.py.patch`. The patch should be successfully applied. Patch is created against revision 220 of the source.

This issue has been reported. See https://code.google.com/p/kippo/issues/detail?id=59 for more information.

### Note 2
The commands require you have a fake filesystem ready with fake links to the commands. Therefore, make sure the `/path/to/command` is in your fake filesystem. If a command does not work in a session, try to `touch /path/to/command` and then try again. If it works now, then you do not have the fake links in your fake filesystem.

## Known issues
Probably a lot ;)

I'm not a Unix guru, so I have no advanced knowledge of all commands and possible options. I have implemented the basic options to make an honeypot session more realistic.

Feel free to fork or submit issues!

## License
See the `LICENSE` file (MIT license).
