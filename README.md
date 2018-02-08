[![GitHub release](https://img.shields.io/github/release/sco1/worktimecalc.svg)](https://github.com/sco1/worktimecalc/releases/latest) ![Python version](https://img.shields.io/badge/python-%3E%3D3.6-brightgreen.svg)
# Worktime Calculator
Helper CLI for calculating leave & premium hour based on the start & end of the workday.

Because I got sick of doing this in my head.

Built using the [Click command line utility](https://github.com/pallets/click). Yay!

## Installation
### venv
After cloning or downloading this repository, initialize a virtual environment in the repository and use `pip` to install the `worktime` CLI.

The following example utilizes [`virtualenv`](https://github.com/pypa/virtualenv):

```
$ pip install virtualenv
$ virtualenv venv
$ source ./venv/Scripts/activate
$ pip install .
```

Note that non-Windows users will use `. venv/bin/activate` to activate the virtual environment.

### Windows executable
Windows users can download a standalone executable from the [latest GitHub release](https://github.com/sco1/worktimecalc/releases/latest)

An executable can also be generated from the source with [PyInstaller](https://github.com/pyinstaller/pyinstaller):

```
$ pip install pyinstaller
$ pyinstaller --onefile worktimecalc.py
```

### pip
`worktime` can also be installed to the global Python scope.

After cloning or downloading this repository, `cd` to the repository directory and use `pip` to install the `worktime` CLI:

```
$ pip install .
```

## Usage
### Arguments
| Short Flag | Long Flag       | Description                                | Default         |
| :---:      | :---            | :---                                       | :---:           |
| `-i`       | `--interactive` | Enable interactive mode                    | Flag not set^1^ |
| `-s`       | `--starttime`   | Start time, 24H, str                       | `'0700'`        |
| `-e`       | `--endtime`     | End time, 24H, str                         | `'1530'`        |
| `-wd`      | `--workday`     | Workday length, decimal hours, float       | `8.5`           |
| `-se`      | `--startend`    | Shortcut, specify start/end time           |                 |
| `-ns`      | `--nonstandard` | Shortcut, specify start/end time & workday |                 |
|            | `--version`     | Show version information and exit          |                 |
|            | `--help`        | Show help message and exit                 |                 |

1: The interactive mode flag is set when calling the PyInstaller bundled Windows executable without any inputs

### Examples
Note: Unless otherwise stated, all examples assume `worktime` has been installed with `pip`

#### Interactive Mode
```
$ worktime -i
Enter Start Time [0700]: 0700
Enter End Time [1530]: 1530
Enter workday length (decimal hours) [8.5]: 8.5
You worked exactly one full workday!
```

```
$ worktime -i
Enter Start Time [0700]: 0700
Enter End Time [1530]: 1430
Enter workday length (decimal hours) [8.5]: 8.5
Request 1.0 hours of leave
Request time: 1430 - 1530
```

```
$ worktime -i
Enter Start Time [0700]: 0700
Enter End Time [1530]: 1630
Enter workday length (decimal hours) [8.5]: 8.5
Request 1.0 premium hours
Request time: 1530 - 1630
```

### Using flags
```
$ worktime -s '0730' -e '1500'
Request 1.0 hours of leave
Request time: 1500 - 1600
```

```
$ worktime -se '0730' '1500'
Request 1.0 hours of leave
Request time: 1500 - 1600
```

```
$ worktime -ns '0500' '1730' 1
Request 11.5 premium hours
Request time: 0600 - 1730
```