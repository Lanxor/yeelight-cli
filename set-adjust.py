#! /usr/bin/python3

import sys
import os
import argparse
import logging as log
import yeelight

log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

def do_set_adjust(address, action, prop):
  try:
    bulb = yeelight.Bulb(address)
    bulb.set_adjust(action, prop)
  except Exception as e:
    log.error(e)

def main():
  parser = argparse.ArgumentParser(
    usage="%(prog)s address [bright|ct] [increase|decrease|circle]",
    description="Adjust a parameter.",
    epilog='''I don't know what this is good for. I don't know how to use it, or why. I'm just
              including it here for completeness, and because it was easy, but it won't get any
              particular love.''')
  parser.add_argument('address',
    help="IP address of bulb.")
  parser.add_argument('prop', choices=['bright', 'ct', ],
    help="The direction of adjustment. Can be 'increase', 'decrease' or 'circle'.")
  parser.add_argument('action', choices=['increase', 'decrease', 'circle'],
    help='''The property to adjust. Can be 'bright' for brightness, 'ct' for color temperature and
            'color' for color. The only action fo'color' can be 'circle'. Why? Who knows.''')
  args = parser.parse_args()

  do_set_adjust(args.address, args.action, args.prop)

if __name__ == '__main__':
  main()
