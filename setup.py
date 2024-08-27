from setuptools import setup

setup(
    name='demodrive',  # Updated project name
    version='0.1.0',
    py_modules=['main','generate_brewery_shop_ai','execution_plan'],  # This is your CLI script file without the .py extension
    install_requires=[
        'Click',  # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'demodrive=main:cli',  # Updated command name
        ],
    },
)
