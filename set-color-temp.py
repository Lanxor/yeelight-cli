#! /usr/bin/python3

import sys
import os
import argparse
import logging as log
import yeelight

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

def do_set_color_temp(address, degrees):
  try:
    bulb = yeelight.Bulb(address)
    bulb.set_color_temp(degrees)
  except Exception as e:
    log.error(e)

def main():
  parser = argparse.ArgumentParser(
    usage="%(prog)s address value",
    description="Set the bulb's color temperature.")
  parser.add_argument('address',
    help="")
  parser.add_argument('degrees', type=int,
    help="""The degrees to set the color temperature to (min/max are specified by the
            model's capabilities, or 1700-6500).""")
  args = parser.parse_args()

  do_set_color_temp(args.address, args.degrees)

if __name__ == '__main__':
  main()
