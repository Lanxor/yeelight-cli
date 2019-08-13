#! /usr/bin/python3

import sys
import os
import argparse
import logging as log
import yeelight

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

def do_set_brightness(address, value):
  try:
    bulb = yeelight.Bulb(address)
    bulb.set_brightness(value)
  except Exception as e:
    log.error(e)

def main():
  parser = argparse.ArgumentParser(
    usage="%(prog)s address value",
    description="Set the bulb's brightness.")
  parser.add_argument('address',
    help="IP address of bulb.")
  parser.add_argument('value', type=int,
    help="The brightness value to set (1-100).")
  args = parser.parse_args()

  do_set_brightness(args.address, args.value)

if __name__ == '__main__':
  main()
