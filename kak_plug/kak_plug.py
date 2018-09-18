# -*- coding: utf-8 -*-
import os
import logging
import subprocess
import shlex

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

logger = logging.getLogger(__name__)

curdir = os.path.dirname(os.path.realpath(__file__))

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %I:%M:%S %p"
)

h = logging.StreamHandler()
h.setFormatter(formatter)
logger.addHandler(h)

logger.debug("Current directory: {}".format(curdir))

DIRECTORY = os.path.expanduser("~/.config/kak/autoload/kak-plug/")


def clone(username, repo, hostname, kak_dir=None):
    if kak_dir is None:
        plugin = os.path.join(
            DIRECTORY, "plugins", "{}_{}_{}".format(hostname, username, repo)
        )
    else:
        raise NotImplementedError("directory not customizable, contact the developer")
    if not os.path.exists(plugin):
        url = "https://{}/{}/{}.git".format(hostname, username, repo)
        p = subprocess.Popen(shlex.split("git clone {} {}".format(url, plugin)))
        p.wait()


def install(argument, kak_dir, hostname):
    """
    Install kak plugin
    """
    if hostname is None:
        hostname = "github.com"
    if len(argument.split("/")) == 2:
        username, repo = argument.split("/")
        clone(username, repo, hostname, kak_dir)
    else:
        raise NotImplementedError("Please contact the developer")


def update(arguments):
    p_list = []
    for plugin in arguments:
        hostname = "github.com"
        username, repo = plugin.replace("'", "").replace('"', "").split("/")
        folder = os.path.join(
            DIRECTORY, "plugins", "{}_{}_{}".format(hostname, username, repo)
        )
        p = subprocess.Popen(shlex.split("git pull"), cwd=os.path.join(folder))
        p_list.append(p)
    for p in p_list:
        p.wait()


def main():
    import argparse

    h = logging.FileHandler(os.path.join(curdir, "kak_plug.log"), "w")
    h.setFormatter(formatter)
    logger.addHandler(h)
    logger.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser(description="kak-plug manager")

    subparsers = parser.add_subparsers(dest="command")

    install_parser = subparsers.add_parser("install", help="kak-plug install manager")
    install_parser.add_argument("install")
    install_parser.add_argument("--kak-dir", dest="kak_dir")
    install_parser.add_argument("--hostname", dest="hostname")

    # begin_parser = subparsers.add_parser("begin", help="kak-plug begin manager")
    # end_parser = subparsers.add_parser("end", help="kak-plug end manager")

    update_parser = subparsers.add_parser("update", help="kak-plug update manager")
    update_parser.add_argument("update", nargs="+")

    logger.info("Parsing command line arguments ...")

    args = parser.parse_args()

    logger.info(args)

    if args.command == "install":
        install(args.install, args.kak_dir, args.hostname)
    if args.command == "update":
        update(args.update)

    return 0


if __name__ == "__main__":

    main()
