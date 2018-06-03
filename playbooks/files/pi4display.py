#!/usr/bin/env python3

import os
import re
import time
import fourletterphat as flp

import constants


last_state = None


def get_device_instructions(rpi_id, dir_file_list):
    pattern = 'info_{:03}_(....)_Z\.txt'.format(rpi_id)
    instructions = []
    for somefile in dir_file_list:
        m = re.match(pattern, somefile)
        if m:
            instructions.append(m.group(1))
    return instructions


def display_state(rpi_id, pidi_status_dir):
    global last_state

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
        if last_state is None:
            flp.scroll_print('ERROR - FILE FOR THIS RASPBERRY NOT FOUND!')
            return
        else:
            instructions = [last_state]

    if len(instructions) > 1:
        flp.scroll_print('ERROR - TOO MANY INSTRUCTIONS')
        return

    instr = instructions[0]
    flp.print_str(instr)
    flp.show()

    rename_instruction(rpi_id, instr, pidi_status_dir)
    last_state = instr


def rename_instruction(rpi_id, code, pidi_status_dir):
    pattern = 'info_{:03}_{}_{}.txt'
    src = pattern.format(rpi_id, code, 'Z')
    dst = pattern.format(rpi_id, code, 'K')

    src = os.path.join(pidi_status_dir, src)
    dst = os.path.join(pidi_status_dir, dst)

    if os.path.exists(src):
        os.rename(src, dst)


def main():
    global last_state
    last_state = None

    rpi_id = constants.rpi_id
    pidi_status_dir = constants.pidi_status_dir

    flp.clear()

    flp.scroll_print("START")
    time.sleep(2)

    while True:
        display_state(rpi_id, pidi_status_dir)
        time.sleep(2)


if __name__ == '__main__':
    main()
