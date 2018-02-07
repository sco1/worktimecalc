import datetime as dt

import click

@click.command()
def cli():
    """
    Calculate leave/premium time based on start and end times.

    Time is input as HHMM
    """
    workday = 8.5  # Workday length, in hours
    starttime = dt.datetime.strptime(click.prompt('Enter Start Time', default='0700'), '%H%M')
    endtime = dt.datetime.strptime(click.prompt('Enter End Time', default='1530'), '%H%M')

    tdelta = endtime - starttime
    decimalhours = (tdelta.total_seconds() / 3600) - workday
    
    if decimalhours < 0:
        click.echo('Request ', nl=False)
        click.secho(f'{abs(decimalhours)} ', nl=False, fg='green')
        click.echo('hours of leave')
    elif decimalhours > 0:
        click.echo('Request ', nl=False)
        click.secho(f'{abs(decimalhours)} ', nl=False, fg='green')
        click.echo('premium hours')
    else:
        click.echo('You worked exactly ', nl=False)
        click.secho('one ', nl=False, fg='green')
        click.echo('full workday!')

if __name__ == '__main__':
    cli()