# -*- coding: utf-8 -*-
import os
import logging

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


def main():
    return 0


if __name__ == "__main__":

    main()
