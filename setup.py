from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in twonkfms/__init__.py
from twonkfms import __version__ as version

setup(
	name="twonkfms",
	version=version,
	description="A Fleet Management System for 2NK SACCO Transport Limited. The system will be used by 2NK SACCO management to oversee the management of vehicle routing, timetable scheduling, maintenace scheduling, driver monitoring and costs control.",
	author="George Kiirithio Waweru",
	author_email="gkdevs50@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
