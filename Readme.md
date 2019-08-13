# Yeelight Script

# Requirements

* python3.X
* module `yeelight`

```
$ pip3 install yeelight
```

# Scripts

## Turn on

**Description :** Turn the bulb on.

```
$ python3 turn_on.py <address>
```

## Turn off

**Description :** Turn the bulb off.

```
$ python3 turn_off.py <address>
```

## Turn off

**Description :** Toggle the bulb on or off.

```
$ python3 toggle.py <address>
```

## Set Brightness

**Description :** Set the bulb's brightness.

```
$ python3 set_brightness.py <address> <brightness>
```

## Set RGB

**Description :** Set the bulb's RGB value.

```
$ python3 set_rgb.py <address> <red> <green> <blue>
```

## Set HSV

**Description :** Set the bulb's HSV value.

```
$ python3 set_hsv.py <address> <hue> <saturation> [-v value] [-t light_type]
```

## Set Color Temp

**Description :** Set the bulb's color temperature.

```
$ python3 set_adjust.py <address> <degrees>
```

## Set Adjust

**Description :** Adjust a parameter.

```
$ python3 set_adjust.py <address> {bright|ct} {increase|decrease|circle}
```

## Documentations

* https://yeelight.readthedocs.io/en/latest/
