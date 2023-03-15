import sys
import platform

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    'llvmlite',
    'numpy',
    'requests',
    'fairseq',

    "torch>=1.6",
]

if platform.machine() == 'aarch64' and sys.platform == 'linux':
    install_requires.append(
        "torch==1.12.0;sys_platform=='linux' and platform_machine=='aarch64' and python_version<'3.11'"
    )

if platform.machine() == 'arm64':
    install_requires.append("torch>=1.13.0; platform_machine == 'arm64'")

setup(
    name='ablang',
    version='0.2.2',
    description='AbLang: A language model for antibodies.',
    license='BSD 3-clause license',
    maintainer='Tobias Hegelund Olsen',
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer_email='tobias.olsen@stats.ox.ac.uk',
    include_package_data=True,
    packages=find_packages(include=('ablang', 'ablang.*')),
    install_requires=install_requires,
)
