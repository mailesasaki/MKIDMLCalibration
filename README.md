# MKIDMLCalibration

A repository for training machine learning models and using them to find and tune MKID resonators.

The mlDict.yml file can also be replaced with ones that the user may create, with different settings, data files, and directories.

train_model.py is a script that takes an mlDict file (yaml format) and creates a machine learning model from it. 

findResonatorsWPS.py is a script that takes an ML model and inference data.

For help with running these scripts and the ML procedure, refer to HELP.md
