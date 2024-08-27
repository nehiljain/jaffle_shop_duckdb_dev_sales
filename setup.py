from setuptools import setup

setup(
    name='dev-sell',
    version='0.1.0',
    py_modules=['main','generate_brewery_shop_ai','execution_plan'],  # This is your CLI script file without the .py extension
    install_requires=[
        'Click',  # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'dev-sell=main:cli',  # 'mycli' is the command name, 'cli:cli' is the module and function to call
        ],
    },
)
