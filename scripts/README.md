# Binedit Scripts

This directory contains different bash script to ease the use of the binedit tool for common needed functions for working with 32 bits microcontrollers memory and firmware files.

## Usage

Create an empty (0xFFs) binary file of 256KB:

```bash
binedit_create firmware.bin
```

Show content of a binary file in Hexadecimal and ASCII:

```bash
# Show full file content
binedit_show firmware.bin

# Show 64 bytes from 0x08008000 address
binedit_show firmware.bin 0x08008000 64
```

Join Bootloader and Application files into a single Firmware file of 256KB:

```bash
# Add boot.bin and app.bin into a firmware.bin file
binedit_add_boot_app firmware.bin boot.bin app.bin
```

Extract Bootloader or Application from a Firmware file:

```bash
# Get Bootloader
binedit_get_boot firmware.bin boot.bin

# Get Application
binedit_get_app firmware.bin app.bin
```

Extract Bootloader and Application from a Firmware file:

```bash
# Get Bootloader and Application
binedit_split_boot_app firmware.bin boot.bin app.bin
```
