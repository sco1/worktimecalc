from setuptools import setup

setup(
    name='worktimecalc',
    version='0.1',
    py_modules=['worktimecalc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        worktimecalc=worktimecalc:cli
    ''',
)