#!/usr/bin/env python3

import os
import re
import time
import fourletterphat as flp

import constants


def get_device_instructions(rpi_id, dir_file_list):
    pattern = 'info_{:03}_(....)_Z\.txt'.format(rpi_id)
    instructions = []
    for somefile in dir_file_list:
        m = re.match(pattern, somefile)
        if m:
            instructions.append(m.group(1))
    return instructions


def display_state(rpi_id, pidi_status_dir):
    try:
        dir_file_list = os.listdir(pidi_status_dir)
    except FileNotFoundError:
        flp.scroll_print('ERROR - REMOTE DIR NOT FOUND!')
        return
    except PermissionError:
        flp.scroll_print('ERROR - REMOTE DIR NOT PERMITTED!')
        return

    instructions = get_device_instructions(rpi_id, dir_file_list)
    if not instructions:
        flp.scroll_print('ERROR - FILE FOR THIS RASPBERRY NOT FOUND!')
        return

    if len(instructions) > 1:
        flp.scroll_print('ERROR - TOO MANY INSTRUCTIONS')
        return

    instr = instructions[0]
    flp.print_str(instr)
    flp.show()

    rename_instruction(rpi_id, instr)


def rename_instruction(rpi_id, code):
    pattern = 'info_{:03}_{}_{}.txt'
    src = pattern.format(rpi_id, code, 'Z')
    dst = pattern.format(rpi_id, code, 'K')
    os.rename(src, dst)


def main():
    rpi_id = constants.rpi_id
    pidi_status_dir = constants.pidi_status_dir

    flp.clear()

    flp.scroll_print("START")
    time.sleep(2)

    while True:
        display_state(rpi_id, pidi_status_dir)
        sleep(2)


if __name__ == '__main__':
    main()
