import sys
import datetime as dt

import click

@click.command()
@click.version_option()
@click.option('--interactive' ,'-i', is_flag=True, help='Enable interactive mode')
@click.option('--starttime', '-s', default='0700', help="Start time, 'HHMM'")
@click.option('--endtime', '-e', default='1530', help="End time, 'HHMM'")
@click.option('--workday', '-wd', default=8.5, help='Length of workday, decimal hours')
@click.option('--nonstandard', '-ns', nargs=3, help="Short circuit for nonstandard workday, 'HHMM' 'HHMM' x.x")
@click.option('--startend', '-se', nargs=2, help="Short circuit for standard workday, 'HHMM' 'HHMM'")
def cli(starttime, endtime, interactive, workday, nonstandard, startend):
    """
    Calculate leave/premium time based on start and end times.
    """
    if nonstandard:
        starttime, endtime, workday = nonstandard
        workday = float(workday)

    if startend:
        starttime, endtime = startend

    if interactive:
        starttime = click.prompt('Enter Start Time', default=starttime)
        endtime = click.prompt('Enter End Time', default=endtime)
        workday = click.prompt('Enter workday length (decimal hours)', default=workday)

    starttime = dt.datetime.strptime(starttime, '%H%M')
    endtime = dt.datetime.strptime(endtime, '%H%M')

    tdelta = endtime - starttime
    decimalhours = (tdelta.total_seconds() / 3600) - workday
    
    if decimalhours < 0:
        click.echo('Request ', nl=False)
        click.secho(f'{abs(decimalhours)} ', nl=False, fg='green')
        click.echo('hours of leave')

        click.echo(f"Request time: ", nl=False)
        click.secho(f"{endtime.strftime('%H%M')} - {(starttime + dt.timedelta(hours=workday)).strftime('%H%M')}", fg='green')
    elif decimalhours > 0:
        click.echo('Request ', nl=False)
        click.secho(f'{decimalhours} ', nl=False, fg='green')
        click.echo('premium hours')

        click.echo(f"Request time: ", nl=False)
        click.secho(f"{(starttime + dt.timedelta(hours=workday)).strftime('%H%M')} - {endtime.strftime('%H%M')}", fg='green')
    else:
        click.echo('You worked exactly ', nl=False)
        click.secho('one ', nl=False, fg='green')
        click.echo('full workday!')

if getattr(sys, 'frozen', False):
    cli(sys.argv[1:])