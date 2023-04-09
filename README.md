# Binedit

Binary files editor tool to manipulate binary files and it content.

## Features

It supports the next features:
- Create empty binary files full of 0xFF to specified size.
- Show binary file's content in hexadecimal and ascii (hexdump).
- Clear bytes (set to 0xFF) on given binary file address.
- Extract binary file data from address range into a binary file.
- Join binary files by insert bytes from one to another.
- Split a single binary file into two binary files.

## Installation

A Makefile is provided to ease installation of the tool on a linux system:

```bash
# Get the tool
git clone https://github.com/J-Rios/binedit
cd binedit

# Install the tool
sudo make install
```

Note: Installation place the binedit tool in `/opt/binedit` and create a symbolic link in `/usr/local/bin/binedit`.

In case you want to uninstall the tool from the system:

```bash
cd /opt/binedit
sudo make uninstall
```

## Usage

Example on how to "hexdump" a binary file:

```bash
# Show the full content of a binary file
binedit --show --input fw.bin

# Show a section of bytes from a binary file
binedit --show --input fw.bin --base_address 0x08000000 --address 0x08007C00
```

Example on how to join and create a firmware file that contains Bootloader and Application:

```bash
# Create an empty binary file of 256KB
binedit --create --input fw.bin --size 262144

# Add a Bootloader binary file content to 0x08000000 address (at the beginning of the file)
binedit --add --input boot.bin --output fw.bin --base_address 0x08000000 --output_address 0x08000000

# Add an Application binary file content to 0x08008000 address (after 32KB of Bootloader)
binedit --add --input app.bin --output fw.bin --base_address 0x08000000 --output_address 0x08008000
```

Example on how to extract a byte section from a binary file:

```bash
# Extract Application Section from a full Firmware file
binedit --get --input fw.bin --output app.bin --base_address 0x08000000 --address 0x08008000
```

Note: the `--base_address` argument allows to set a base address corresponding to address 0x00000000 (like an offset for use that base in `--address` and `--output_address` argument values).

Example on how to clear (set to 0xFF) specific bytes from a binary file:

```bash
# Clear 4 bytes at 0x08007C00 address
binedit --clear --input fw.bin --base_address 0x08000000 --address 0x08007C00 --size 4
```
