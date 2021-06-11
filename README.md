[![GitHub release](https://img.shields.io/github/release/sco1/worktimecalc.svg)](https://github.com/sco1/worktimecalc/releases/latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sco1/worktimecalc/main.svg)](https://results.pre-commit.ci/latest/github/sco1/worktimecalc/main)
[![lint-and-test](https://github.com/sco1/worktimecalc/actions/workflows/lint_test.yml/badge.svg?branch=main)](https://github.com/sco1/worktimecalc/actions/workflows/lint_test.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
# Worktime Calculator
Helper CLI for calculating leave & premium hour based on the start & end of the workday.

Because I got sick of doing this in my head.

Built using the [Click command line utility](https://github.com/pallets/click). Yay!

## Installation
### Windows executable
Windows users can download a standalone executable from the [latest GitHub release](https://github.com/sco1/worktimecalc/releases/latest)

An executable can also be generated from the source with [PyInstaller](https://github.com/pyinstaller/pyinstaller):

```
$ pip install pyinstaller
$ pyinstaller --onefile ./src/worktimecalc.py
```

### poetry
`worktime` is intended to be installed in a virtual environment using [Poetry](https://python-poetry.org/).

After cloning or downloading this repository, `cd` to the repository directory and use `poetry` to install the `worktimecalc` CLI:

```
$ poetry install --no-dev
```

## Usage
### Arguments
| Short Flag | Long Flag       | Description                                | Default                  |
| :---:      | :---            | :---                                       | :---:                    |
| `-i`       | `--interactive` | Enable interactive mode                    | Flag not set<sup>1</sup> |
| `-s`       | `--starttime`   | Start time, 24H, str                       | `'0700'`                 |
| `-e`       | `--endtime`     | End time, 24H, str                         | `'1530'`                 |
| `-wd`      | `--workday`     | Workday length, decimal hours, float       | `8.5`                    |
| `-se`      | `--startend`    | Shortcut, specify start/end time           |                          |
| `-ns`      | `--nonstandard` | Shortcut, specify start/end time & workday |                          |
|            | `--version`     | Show version information and exit          |                          |
|            | `--help`        | Show help message and exit                 |                          |

1: The interactive mode flag is implicitly set when `worktimecalc` called without any inputs

### Examples
Note: Unless otherwise stated, all examples assume `worktimecalc` has been installed with `pip`

#### Interactive Mode
```
$ worktimecalc -i
Enter Start Time [0700]: 0700
Enter End Time [1530]: 1530
Enter workday length (decimal hours) [8.5]: 8.5
You worked exactly one full workday!
```

```
$ worktimecalc -i
Enter Start Time [0700]: 0700
Enter End Time [1530]: 1430
Enter workday length (decimal hours) [8.5]: 8.5
Request 1.0 hours of leave
Request time: 1430 - 1530
```

```
$ worktimecalc -i
Enter Start Time [0700]: 0700
Enter End Time [1530]: 1630
Enter workday length (decimal hours) [8.5]: 8.5
Request 1.0 premium hours
Request time: 1530 - 1630
```

#### Using flags
```
$ worktimecalc -s 0730 -e 1500
Request 1.0 hours of leave
Request time: 1500 - 1600
```

```
$ worktimecalc -se 0730 1500
Request 1.0 hours of leave
Request time: 1500 - 1600
```

```
$ worktimecalc -ns 0500 1730 1
Request 11.5 premium hours
Request time: 0600 - 1730
```
