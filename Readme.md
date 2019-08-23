# Yeelight Command Line Interface

# Requirements

* python3.X
* module `yeelight`

```
$ pip3 install yeelight
```

## Documentations

* https://yeelight.readthedocs.io/en/latest/

# Usage

List of available command :
`turn_on`, `turn_off`, `toogle`,
`set_brightness`, `set_color_temp`,
`set_rgb`, `set_hsv`,
`set_adjust`

```
$ python3 yeelight-cli.py toogle <address>
$ python3 yeelight-cli.py set_brightness <address> 55
```

Tap `--help` for more information of one command.
