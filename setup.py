from setuptools import setup

with open('README.md') as f:
    readme = f.read()
with open('CHANGES.md') as f:
    changes = f.read()

setup(
    name="vgkits-vanguard",
    version="0.2.0_rc4",
    description='Tools to support VGkits Vanguard ESP8266 python-programmable board.',
    long_description='{}\n\n{}'.format(readme, changes),
    long_description_content_type="text/markdown",
    url='https://vgkits.org',
    download_url = 'https://github.com/vgkits/vgkits-vanguard/archive/0.2.0_rc4.tar.gz',
    author='@cefn',
    author_email='github.com@cefn.com',
    license='GPL3',
    packages=[
        'vgkits.vanguard',
        'vgkits.vanguard.shell',
        'vgkits.vanguard.brainwash',
        'vgkits.vanguard.braindump',
    ],
    package_data={'vgkits.vanguard': ['data/firmware']},
    install_requires=[
        "click>=6.7",
        "pyserial>=3.4",
        "esptool>=2.3.1",
        "adafruit-ampy>=1.0.3",
        "rshell>=0.0.12",
        "six>=1.11.0",
    ],
    include_package_data=True,
    zip_safe=False,
    keywords = ['vgkits', 'vanguard', 'esp8266', 'micropython', 'circuitpython', 'iot', 'gcse', 'computer science',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Education',
        'Topic :: Software Development :: Embedded Systems',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    entry_points={
        'console_scripts': [
            "vanguard = vgkits.vanguard:main",
            "vanguard-shell = vgkits.vanguard.shell:main",
            "vanguard-brainwash = vgkits.vanguard.brainwash:main",
            "vanguard-braindump = vgkits.vanguard.braindump:main",
        ],
    }
)
