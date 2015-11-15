# Copyright (c) 2013-2015 Bas Stottelaar <basstottelaar [AT] gmail [DOT] com>

import importlib
import sys
import imp
import os

# Set to False to disable source patching
PATCH_SOURCE = True

class KippoExtraLoader(object):
    def find_module(self, fullname, path=None):
        # Intercept command imports
        if "kippo.commands.kippo_extra" in fullname:
            return KippoExtraCommandsLoader()

        # Intercept core import
        if PATCH_SOURCE:
            if fullname == "kippo.core.honeypot":
                return KippoPatchingLoader()

        return None

class KippoPatchingLoader(object):
    def load_module(self, name):
        # Check loaded modules first
        if name in sys.modules:
            return sys.modules[name]

        # Create module
        module = imp.new_module(name)

        if name == "kippo.core.honeypot":
            bytecode = self.patch_kippo_core_honeypot()

        # Combine them
        exec bytecode in module.__dict__

        # Add it as loaded
        sys.modules[name] = module

        # Done
        return module

    def get_kippo_root(self):
        _, path, _ = imp.find_module("kippo")
        return path

    def read_file(self, filename):
        with open(filename, "r") as fp:
            result = fp.read()

        return result

    def patch_source(self, source_file, patch_file):
        source_file = os.path.join(self.get_kippo_root(), source_file)
        patch_file = os.path.join(os.path.dirname(__file__), patch_file)

        source = self.read_file(source_file)
        patch = self.read_file(patch_file)

        # Modified from https://github.com/danielmoniz/merge_in_memory/
        diff = patch.split("\n")
        source = source.split("\n")
        hunk = 0
        i = 0

        # Iterate through diff sections
        for line in diff:
            i += 1

            if line.startswith("@"):
                hunk = hunk + 1

                line = line.replace("-", "")
                line = line.replace("+", "")
                line = line.strip("@")
                line = line.strip()

                old_info, new_info = line.split(" ")
                old_info = old_info.split(",")
                new_info = new_info.split(",")

                i = int(new_info[0]) - 1
            elif line.startswith("---") or line.startswith("+++"):
                continue
            elif line.startswith("-"):
                # Delete the line.
                del source[i - 1]
                i = i - 1
            elif line.startswith("+"):
                # Add in a new line.
                line = line[1:]
                source.insert(i - 1, line)
            elif line.startswith(" "):
                # Verify if the line matches, so we know if we are in sync.
                if source[i - 1] != line[1:]:
                    raise Exception("Hunk #%d does not match source." % hunk)

        # Done
        return "\n".join(source), source_file

    def patch_kippo_core_honeypot(self):
        # Read the source
        source, source_file = self.patch_source(
            "core/honeypot.py",
            "patches/kippo_core_honeypot.patch"
        )

        # Compile it
        return compile(source, source_file, "exec")

class KippoExtraCommandsLoader(object):
    def load_module(self, name):
        # Strip namespace
        name = name.replace("kippo.commands.", "")

        # Check loaded modules first
        if name in sys.modules:
            return sys.modules[name]

        # Not loaded, so load it
        return importlib.import_module(name)

def install_hook():
    # Extend kippo's commands
    import kippo.commands
    import kippo_extra.commands

    for command in kippo_extra.commands.__all__:
        module = "%s.%s" % (kippo_extra.commands.__name__, command)
        kippo.commands.__all__.append(module)

    # Add import interceptor
    sys.meta_path.append(KippoExtraLoader())

install_hook()