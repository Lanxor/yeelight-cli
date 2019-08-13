#! /usr/bin/python3

import sys
import os
import argparse
import logging as log
import yeelight

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

def do_turn_off(address):
  try:
    bulb = yeelight.Bulb(address)
    bulb.turn_off()
  except Exception as e:
    log.error(e)

def main():
  parser = argparse.ArgumentParser(
    usage="%(prog)s address",
    description="Turn the bulb off.")
  parser.add_argument('address',
    help="IP address of bulb.")
  args = parser.parse_args()

  do_turn_off(args.address)

if __name__ == '__main__':
  main()
