#! /usr/bin/python3

import sys
import os
import argparse
import logging as log
import yeelight

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

def do_set_rgb(address, red, green, blue):
  try:
    bulb = yeelight.Bulb(address)
    bulb.set_rgb(red, green, blue)
  except Exception as e:
    log.error(e)

def main():
  parser = argparse.ArgumentParser(
    usage="%(prog)s address red green blue",
    description="Set the bulb's RGB value.")
  parser.add_argument('address',
    help="IP address of bulb.")
  parser.add_argument('red', type=int,
    help="The red value to set (0-255).")
  parser.add_argument('green', type=int,
    help="The green value to set (0-255).")
  parser.add_argument('blue', type=int,
    help="The blue value to set (0-255).")
  args = parser.parse_args()

  do_set_rgb(args.address, args.red, args.green, args.blue)

if __name__ == '__main__':
  main()
