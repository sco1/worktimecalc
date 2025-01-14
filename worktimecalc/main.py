import datetime as dt
import sys
import typing as t

import click


@click.command()
@click.option("--interactive", "-i", is_flag=True, help="Enable interactive mode")
@click.option("--starttime", "-s", default="0700", help="Start time, 'HHMM'")
@click.option("--endtime", "-e", default="1530", help="End time, 'HHMM'")
@click.option("--workday", "-wd", default=8.5, help="Length of workday, decimal hours")
@click.option("--startend", "-se", nargs=2, help="Shortcut for standard workday, 'HHMM' 'HHMM'")
@click.option(
    "--nonstandard", "-ns", nargs=3, help="Shortcut for nonstandard workday, 'HHMM' 'HHMM' x.x"
)
@click.version_option()
def cli(
    starttime: t.Union[str, dt.datetime],
    endtime: t.Union[str, dt.datetime],
    interactive: bool,
    workday: float,
    nonstandard: tuple[str, str, str],
    startend: tuple[str, str],
) -> None:
    """Calculate leave/premium time based on start and end times."""
    if nonstandard:
        starttime, endtime, new_workday = nonstandard
        workday = float(new_workday)

    if startend:
        starttime, endtime = startend

    if interactive:
        starttime = click.prompt("Enter Start Time", default=starttime)
        endtime = click.prompt("Enter End Time", default=endtime)
        workday = click.prompt("Enter workday length (decimal hours)", default=workday)

    if isinstance(starttime, str):
        starttime = dt.datetime.strptime(starttime, "%H%M")

    if isinstance(endtime, str):
        endtime = dt.datetime.strptime(endtime, "%H%M")

    tdelta = endtime - starttime
    decimalhours = (tdelta.total_seconds() / 3600) - workday

    if decimalhours < 0:
        click.echo("Request ", nl=False)
        click.secho(f"{abs(decimalhours)} ", nl=False, fg="green")
        click.echo("hours of leave")

        click.echo("Request time: ", nl=False)
        click.secho(
            f"{endtime.strftime('%H%M')} - {(starttime + dt.timedelta(hours=workday)).strftime('%H%M')}",  # noqa: E501
            fg="green",
        )
    elif decimalhours > 0:
        click.echo("Request ", nl=False)
        click.secho(f"{decimalhours} ", nl=False, fg="green")
        click.echo("premium hours")

        click.echo("Request time: ", nl=False)
        click.secho(
            f"{(starttime + dt.timedelta(hours=workday)).strftime('%H%M')} - {endtime.strftime('%H%M')}",  # noqa: E501
            fg="green",
        )
    else:
        click.echo("You worked exactly ", nl=False)
        click.secho("one ", nl=False, fg="green")
        click.echo("full workday!")


if len(sys.argv) == 1:
    # If called without inputs, automatically enter interactive mode
    cli(["--interactive"])
else:
    # Otherwise pass everything straight through
    cli(sys.argv[1:])
