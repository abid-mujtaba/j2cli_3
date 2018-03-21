#! /usr/bin/env python

""" j2cliPy3 main file """
import pkg_resources

__author__ = "Samuel Windall"
__email__ = "samuel.windall@gmail.com"
__version__ = pkg_resources.get_distribution('j2cliPy3').version

from j2cliPy3.cli import main

if __name__ == '__main__':
    main()
