import datetime as dt

import click

@click.command()
@click.option('--interactive' ,'-i', is_flag=True, help='Enable interactive mode')
@click.option('--starttime', '-s', default='0700', help="Start time, 'HHMM'")
@click.option('--endtime', '-e', default='1530', help="End time, 'HHMM'")
@click.option('--workday', '-wd', default=8.5, help='Length of workday, decimal hours')
@click.option('--timetuple', '-tt', nargs=3, type=(str, str, float), help="Short circuit tuple, 'HHMM' 'HHMM' x.x")
def cli(starttime, endtime, interactive, workday, timetuple):
    """
    Calculate leave/premium time based on start and end times.
    """
    if timetuple:
        starttime, endtime, workday = timetuple

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
    elif decimalhours > 0:
        click.echo('Request ', nl=False)
        click.secho(f'{decimalhours} ', nl=False, fg='green')
        click.echo('premium hours')
    else:
        click.echo('You worked exactly ', nl=False)
        click.secho('one ', nl=False, fg='green')
        click.echo('full workday!')
