#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script:
    bineditlib.py
Description:
    Library to create or edit binary files.
    It supports the next features:
      - Create empty binary files full of 0xFF to specified size.
      - Show binary file's content in hexadecimal and ascii (hexdump).
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
# Library Version Information
###############################################################################

NAME = "bineditlib"
VERSION = "1.0.0"
DATE = "09/04/2023"


###############################################################################
# Standard Libraries
###############################################################################

# Logging Library
import logging

# Error Traceback Library
from traceback import format_exc

# Operating System Library
from os import stat as os_stat


###############################################################################
# Logger Setup
###############################################################################

logger = logging.getLogger(__name__)


###############################################################################
# BinEdit Class
###############################################################################

class BinEdit():
    '''
    Binary Files Editor element.
    '''

    def __init__(self):
        '''BinEdit Constructor.'''
        return


    def version(self):
        '''Show library version information.'''
        print(f"{NAME}:")
        print("------------------------")
        print(f"Version: {VERSION}")
        print(f"Date: {DATE}")


    def create_file(self, file_path: str, num_bytes: int):
        '''
        Create a binary file of specified size with full content set to
        0xFF.
        '''
        # Check arguments
        if file_path == "":
            logger.error("File path required to create bin file")
            return False
        if num_bytes == 0:
            logger.error("Number of bytes required to create bin file")
            return False
        # Create the file
        try:
            clear_bytes = bytearray([0xFF] * num_bytes)
            with open(file_path, "wb") as bin_file_writer:
                bin_file_writer.write(clear_bytes)
        except Exception:
            logger.error(format_exc())
            logger.error(f"Fail to create binary file {file_path}\n")
            return False
        return True


    def show_file(self, file_path: str, from_address: int,
                  num_bytes: int, addr_offset: int):
        '''
        Show in hexadecimal and ascii, the content of a binary file
        from given address up to specified size of bytes.
        '''
        # Check arguments
        if file_path == "":
            logger.error("File path required to create bin file")
            return False
        # Read the full file content and check it
        file_bytes = self._read_file(file_path)
        if file_bytes is None:
            print(f"Fail to read binary file {file_path}")
            return False
        file_size = len(file_bytes)
        if from_address >= file_size:
            print(f"Address requested to read from binary file larger "
                  f"than file size (max address: 0x{file_size - 1:02x}")
            return False
        # Limit size of bytes to read if request more than file size
        if num_bytes == 0:
            num_bytes = file_size
        if from_address + num_bytes > file_size:
            num_bytes = file_size - from_address
        # Show the bytes
        show_bytes = file_bytes[from_address:from_address+num_bytes]
        print("\n".join(self.hexdump(show_bytes, addr_offset, 16, 2)))
        return True


    def hexdump(self, src: bytes, addr_offs: int = 0,
                bytes_per_line: int = 16, bytes_per_group: int = 4,
                sep: str = '.'):
        '''
        Convert a byte array into a string that contains an
        hexadecimal and ascii representation format of the bytes.
        '''
        FILTER = "".join([(len(repr(chr(x))) == 3) and chr(x)
                          or sep for x in range(256)])
        lines = []
        max_addr_len = len(hex(len(src)))
        if 8 > max_addr_len:
            max_addr_len = 8
        for addr in range(0, len(src), bytes_per_line):
            hex_str = ""
            ascii_str = ""
            # The chars we need to process for this line
            chars = src[addr : addr + bytes_per_line]
            # Create hex string
            tmp = "".join(["{:02X}".format(x) for x in chars])
            idx = 0
            for c in tmp:
                hex_str = hex_str + c
                idx = idx + 1
                # 2 hex digits per byte
                if idx % bytes_per_group * 2 == 0 and idx < bytes_per_line * 2:
                    hex_str = hex_str + " "
            # Pad out the line to fill up the line to take up the right
            # amount of space to line up with a full line
            hex_str = hex_str.ljust(
                (bytes_per_line * 2)
                + int(bytes_per_line * 2 / bytes_per_group)
                - 1)
            # create ascii_str string
            tmp = "".join(
                ["{}".format((x <= 127 and FILTER[x]) or sep) for x in chars])
            # insert space every bytes_per_group
            idx = 0
            for c in tmp:
                ascii_str = ascii_str + c
                idx = idx + 1
            _addr = addr + addr_offs
            line_str = f"{_addr:0{max_addr_len}X}  {hex_str}  | {ascii_str} |"
            lines.append(line_str)
        return lines


    def _read_file(self, file_path: str):
        '''Read full content of a binary file.'''
        read_bytes = None
        try:
            with open(file_path, "rb") as bin_file_reader:
                read_bytes = bin_file_reader.read()
        except Exception:
            logger.error(format_exc())
            logger.error(f"Fail to read binary file {file_path}\n")
        return read_bytes


    def _write_file(self, file_path: str, data: bytearray):
        '''Write to a binary file.'''
        try:
            with open(file_path, "wb") as bin_file_writer:
                bin_file_writer.write(data)
        except Exception:
            logger.error(format_exc())
            logger.error(f"Fail to write binary file {file_path}\n")
            return False
        return True
