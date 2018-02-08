from setuptools import setup

setup(
    name='worktimecalc',
    version='1.1.0',
    py_modules=['worktimecalc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        worktimecalc=worktimecalc:cli
    ''',
)