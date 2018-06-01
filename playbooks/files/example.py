#!/usr/bin/env python3

import os
import re
import time
import fourletterphat as flp

import constants


def main():
    rpi_id = constants.rpi_id
    pidi_status_dir = constants.pidi_status_dir
    rpi_string = "rpi_id = " + str(rpi_id)
    infofile_string = "pidi_status_dir = " + pidi_status_dir


    flp.clear()

    flp.scroll_print("STAR")
    # flp.scroll_print(rpi_string.upper())
    # flp.scroll_print(infofile_string.upper())

    try:
        dir_files = os.listdir(pidi_status_dir)
        pattern = 'info_{}_(....)_(.)\.txt'.format(rpi_id)
        for somefile in dir_files:
            m = re.match(pattern, somefile)
            if m:
                flp.print_str(m.group(1))
                flp.show()
                time.sleep(5)
                break
        else:
            flp.scroll_print('ERROR - FILE FOR THIS RASPBERRY NOT FOUND!')
    except FileNotFoundError:
        flp.scroll_print('ERROR - REMOTE DIR NOT FOUND!')
    except PermissionError:
        flp.scroll_print('ERROR - REMOTE DIR NOT PERMITTED!')

    flp.scroll_print("END.")
    time.sleep(1)


if __name__ == '__main__':
    main()
