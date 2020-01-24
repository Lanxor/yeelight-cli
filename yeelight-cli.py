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

def do_set_brightness(address, value):
  try:
    bulb = yeelight.Bulb(address)
    bulb.set_brightness(value)
  except Exception as e:
    log.error(e)

def do_set_color_temp(address, degrees):
  try:
    bulb = yeelight.Bulb(address)
    bulb.set_color_temp(degrees)
  except Exception as e:
    log.error(e)

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
        
def do_set_rgb(address, red, green, blue):
  try:
    bulb = yeelight.Bulb(address)
    bulb.set_rgb(red, green, blue)
  except Exception as e:
    log.error(e)

def do_toggle(address):
  try:
    bulb = yeelight.Bulb(address)
    bulb.toggle()
  except Exception as e:
    log.error(e)

def do_turn_off(address):
  try:
    bulb = yeelight.Bulb(address)
    bulb.turn_off()
  except Exception as e:
    log.error(e)

def do_turn_on(address):
  try:
    bulb = yeelight.Bulb(address)
    bulb.turn_on()
  except Exception as e:
    log.error(e)

def main():
  parser = argparse.ArgumentParser(description="Yeelight Command Line Interface",
    epilog="See documentation : https://yeelight.readthedocs.io/en/latest/")
  subparsers = parser.add_subparsers(dest='action')
  
  # Parser turn_on command
  parser_turnon = subparsers.add_parser('turn_on', description="Turn the bulb on.")
  parser_turnon.add_argument('address',
    help="IP address of bulb.")
  
  # Parser turn_off command
  parser_turnoff = subparsers.add_parser('turn_off', description="Turn the bulb off.")
  parser_turnoff.add_argument('address',
    help="IP address of bulb.")
  
  # Parser toggle command
  parser_toggle = subparsers.add_parser('toggle', description="Toggle the bulb on or off.")
  parser_toggle.add_argument('address',
      help="IP address of bulb.")

  # Parser set_rgb command
  parser_setrgb = subparsers.add_parser('set_rgb', description="Set the bulb's RGB value.")
  parser_setrgb.add_argument('address',
    help="IP address of bulb.")
  parser_setrgb.add_argument('red', type=int,
    help="The red value to set (0-255).")
  parser_setrgb.add_argument('green', type=int,
    help="The green value to set (0-255).")
  parser_setrgb.add_argument('blue', type=int,
    help="The blue value to set (0-255).")

  # Parser set_hsv command
  parser_sethsv = subparsers.add_parser('set_hsv', description="Set the bulb's HSV value.")
  parser_sethsv.add_argument('address',
    help="IP address of bulb.")
  parser_sethsv.add_argument('hue', type=int,
    help="The hue to set (0-359).")
  parser_sethsv.add_argument('saturation', type=int,
    help="The saturation to set (0-100).")
  parser_sethsv.add_argument('-v', '--value', type=int,
    help="The value to set (0-100). If omitted, the bulb's brightness will remain the same as before the change.")
  parser_sethsv.add_argument('-t', '--light-type', type=int)
  
  # Parser set_color_temp command
  parser_setcolortemp = subparsers.add_parser('set_color_temp', description="Set the bulb's color temperature.")
  parser_setcolortemp.add_argument('address',
    help="IP address of bulb.")
  parser_setcolortemp.add_argument('degrees', type=int,
    help="""The degrees to set the color temperature to (min/max are specified by the
            model's capabilities, or 1700-6500).""")
  
  # Parser set_brightness command
  parser_setbrightness = subparsers.add_parser('set_brightness', description="Set the bulb's brightness.")
  parser_setbrightness.add_argument('address',
    help="IP address of bulb.")
  parser_setbrightness.add_argument('value', type=int,
    help="The brightness value to set (1-100).")

  # Parser set_adjust command
  parser_setadjust = subparsers.add_parser('set_adjust', description="Adjust a parameter.")
  parser_setadjust.add_argument('address',
    help="IP address of bulb.")
  parser_setadjust.add_argument('prop', choices=['bright', 'ct', ],
    help="The direction of adjustment. Can be 'increase', 'decrease' or 'circle'.")
  parser_setadjust.add_argument('action', choices=['increase', 'decrease', 'circle'],
    help='''The property to adjust. Can be 'bright' for brightness, 'ct' for color temperature and
            'color' for color. The only action fo'color' can be 'circle'. Why? Who knows.''')

  args = parser.parse_args()

  if args.action == 'turn_on':
    do_turn_on(args.address)
  elif args.action == 'turn_off':
    do_turn_off(args.address)
  elif args.action == 'toggle':
    do_toggle(args.address)
  elif args.action == 'set_rgb':
    do_set_rgb(args.address, args.red, args.green, args.blue)
  elif args.action == 'set_hsv':
    do_set_hsv(args.address, args.hue, args.saturation, args.value, args.light_type)
  elif args.action == 'set_color_temp':
    do_set_color_temp(args.address, args.degrees)
  elif args.action == 'set_brightness':
    do_set_brightness(args.address, args.value)
  elif args.action == 'set_adjust':
    do_set_adjust(args.address, args.action, args.prop)

if __name__ == '__main__':
  main()
