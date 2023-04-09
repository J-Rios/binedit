#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script:
    binedit.py
Description:
    Tool to create or edit binary files.
    It supports the next features:
      - Create empty binary files full of 0xFF to specified size.
      - Show binary file's content in hexadecimal and ascii (hexdump).
      - Clear bytes (set to 0xFF) on given binary file address.
      - Extract binary file data from address range into a binary file.
Author:
    Jose Miguel Rios Rubio
Creation date:
    09/04/2023
Last modified date:
    09/04/2023
Version:
    1.0.0
'''

###############################################################################
# Application Version Information
###############################################################################

NAME = "binedit"
VERSION = "1.0.0"
DATE = "06/04/2023"


###############################################################################
# Standard Libraries
###############################################################################

# Logging Library
import logging

# Argument Parser Library
from argparse import ArgumentParser

# Operating System Library
from os import path as os_path

# System Library
from sys import argv as sys_argv
from sys import exit as sys_exit

# BinEdit Library
from bineditlib import BinEdit

###############################################################################
# Logger Setup
###############################################################################

logging.basicConfig(
    #format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    format="%(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


###############################################################################
# Texts
###############################################################################

class TEXT():

    OPT_CREATE = \
        "Create a binary file."

    OPT_SHOW = \
        "Read and show hexadecimal and ascii of a binary file."

    OPT_CLEAR = \
        "Clear data bytes from a binary file."

    OPT_GET = \
        "Extract data from a binary file address to a new binary file."

    OPT_INPUT = \
        "Input binary file to use."

    OPT_OUTPUT = \
        "Output binary file to use."

    OPT_ADDRESS_INPUT = \
        "Specify input binary address."

    OPT_SIZE = \
        "Specify size of bytes to manipulate."


###############################################################################
# Auxiliary Function
###############################################################################

def auto_int(x):
    return int(x, 0)


def parse_options():
    '''Get and parse program input arguments.'''
    parser = ArgumentParser()
    parser.version = VERSION
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument("--create", help=TEXT.OPT_CREATE, action="store_true")
    parser.add_argument("--show", help=TEXT.OPT_SHOW, action="store_true")
    parser.add_argument("--clear", help=TEXT.OPT_CLEAR, action="store_true")
    parser.add_argument("--get", help=TEXT.OPT_GET, action="store_true")
    parser.add_argument("--input", help=TEXT.OPT_INPUT,
                        action="store", type=str)
    parser.add_argument("--output", help=TEXT.OPT_OUTPUT,
                        action="store", type=str)
    parser.add_argument("--address", help=TEXT.OPT_ADDRESS_INPUT,
                        action="store", type=auto_int, default=0)
    parser.add_argument("-s", "--size", help=TEXT.OPT_SIZE,
                        action="store", type=auto_int, default=0)
    args = parser.parse_args()
    # Check required options combinations
    if (args.create) and \
    ( (args.input is None) or (args.size is None) ):
        parser.error("Arguments Required: --input, --size")
    if (args.show) and (args.input is None):
        parser.error("Arguments Required: --input")
    if args.clear and ( (args.input is None) or (args.address is None)
                     or (args.size == 0) ):
        parser.error("Arguments Required: --input, --address, --size")
    if args.get and ( (args.input is None) or (args.output is None)
                     or (args.address is None) ):
        parser.error("Arguments Required: --input, --output, --address")
    return args


###############################################################################
# Main Function
###############################################################################

def main(argc, argv):
    binedit = BinEdit()
    args = parse_options()
    if args.create:
        logger.debug("Creating binary file...")
        binedit.create_file(args.input, args.size)
    elif args.show:
        logger.debug("Showing binary file...")
        binedit.show_file(args.input, args.address, args.size,
                          args.base_address)
    elif args.clear:
        logger.debug("Clearing data from binary file...")
        binedit.clear_data(args.input, args.address, args.size)
    elif args.get:
        logger.debug("Getting data from binary file...")
        binedit.extract_data(args.input, args.address, args.size, args.output)
    return 0


###############################################################################
# Runnable Main Script Detection
###############################################################################

if __name__ == '__main__':
    logger.debug("{} v{} {}\n".format(os_path.basename(NAME), VERSION, DATE))
    return_code = main(len(sys_argv) - 1, sys_argv[1:])
    sys_exit(return_code)
