#! /usr/bin/python3

import sys
import os
import argparse
import logging as log
import yeelight

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

def do_set_hsv(address, hue, saturation, value, lighttype):
  try:
    bulb = yeelight.Bulb(address)
    if value and lighttype:
      bulb.set_hsv(hue, saturation, value, lighttype)
    elif value:
      bulb.set_hsv(hue, saturation, value)
    elif lighttype:
      bulb.set_hsv(hue, saturation, None, lighttype)
    else:
      bulb.set_hsv(hue, saturation)
  except Exception as e:
    log.error(e)
        
def main():
  parser = argparse.ArgumentParser(
    usage="%(prog)s address hue saturation [-v value] [-t light_type]",
    description="Set the bulb's HSV value.")
  parser.add_argument('address',
    help="IP address of bulb.")
  parser.add_argument('hue', type=int,
    help="The hue to set (0-359).")
  parser.add_argument('saturation', type=int,
    help="The saturation to set (0-100).")
  parser.add_argument('-v', '--value', type=int,
    help="The value to set (0-100). If omitted, the bulb's brightness will remain the same as before the change.")
  parser.add_argument('-t', '--light-type', type=int)
  args = parser.parse_args()

  do_set_hsv(args.address, args.hue, args.saturation, args.value, args.light_type)

if __name__ == '__main__':
  main()
