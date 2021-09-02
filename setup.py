import setuptools

setuptools.setup(
    name="mkidmlcalibration",
    version="0.1",
    author="MazinLab",
    author_email="mazinlab@ucsb.edu",
    description="An UVOIR MKID ML Calibration Package",
    long_description_content_type="text/markdown",
    url="https://github.com/mailesasaki/mkidmlcalibration",
    scripts=['mkidmlcalibration/findResonatorsWPS.py',
             'mkidmlcalibration/train_model.py'],
    packages=setuptools.find_packages(),
)
