# -*- coding: utf-8 -*-
import os
import logging
import subprocess
import shlex

logger = logging.getLogger(__name__)

curdir = os.path.dirname(os.path.realpath(__file__))

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %I:%M:%S %p"
)

h = logging.StreamHandler()
h.setFormatter(formatter)
logger.addHandler(h)

h = logging.FileHandler(os.path.join(curdir, "kak_plug.log"), "w")
h.setFormatter(formatter)
logger.addHandler(h)
logger.setLevel(logging.DEBUG)

logger.debug("Current directory: {}".format(curdir))

DIRECTORY = os.path.expanduser("~/.config/kak/autoload/kak-plug/")


def install_github(username, repo):
    plugin = os.path.join(DIRECTORY, "plugins", "{}_{}".format(username, repo))
    if not os.path.exists(plugin):
        p = subprocess.Popen(
            shlex.split(
                "git clone https://github.com/{}/{} {}".format(username, repo, plugin)
            )
        )
        p.wait()


def install(argument):
    """
    Install kak plugin
    """
    if len(argument.split("/")) == 2:
        username, repo = argument.split("/")
        install_github(username, repo)
    else:
        raise NotImplementedError("Please contact the developer")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="kak-plug manager")
    parser.add_argument("--install", dest="install")
    parser.add_argument("--kak-dir", dest="kak_dir")

    args = parser.parse_args()

    install(args.install)
    return 0


if __name__ == "__main__":

    main()
