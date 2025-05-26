#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, (
    "This project requires Python 3.6 or higher."
)

setup(
    name='my_safety_gym_project',
    description='Safe RL project using OpenAI Safety Gym, PyTorch, and CleanRL.',
    packages=find_packages(),
    install_requires=[
        'gym==0.23.1',
        'mujoco_py==2.0.2.7',
        'numpy~=1.17.4',
        'xmltodict~=0.12.0',
        'joblib~=0.14.0',
        'torch>=1.12.0',
        'stable-baselines3>=1.6.2',
        'opencv-python',
        'tyro>=0.5.10',
        'tensorboard',
        'cleanrl @ git+https://github.com/vwxyzjn/cleanrl.git',
    ],
    python_requires='>=3.6',
)
