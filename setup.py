from setuptools import setup

setup(
    name='worktimecalc',
    version='1.1.0',
    py_modules=['worktimecalc'],
    python_requires=">=3.6",
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        worktimecalc=worktimecalc:cli
    ''',
)