from setuptools import setup


setup(
    name='mozilla-addon-signer',
    version='0.1.0',
    py_modules=[
        'mozilla_addon_signer',
    ],
    install_requires=[
        'boto3',
        'Click',
        'colorama',
        'requests',
        'untangle',
    ],
    entry_points={
        'console_scripts': [
            'mozilla-addon-signer = mozilla_addon_signer.cli:cli',
        ],
    },
)
