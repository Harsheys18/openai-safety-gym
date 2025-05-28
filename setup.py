#!/usr/bin/env python3
"""Setup script for PPO Safety Gym project."""

import os
from setuptools import setup, find_packages
import sys
from setuptools.command.install import install  # NEW

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "Safety Gym is designed to work with Python 3.6 and greater. " \
    + "Please install it before proceeding."

# Core dependencies
install_requires = [
    "numpy~=1.17.4",
    "joblib~=0.14.0",
    "mujoco_py==2.0.2.7",
    "xmltodict~=0.12.0", 
    "gym~=0.15.3",
    "stable-baselines3>=1.6.0",
    "huggingface-hub>=0.8.0",
    "torch",
    "pygame",
    "tensorboard",
    "tyro",
    "wandb",
    "moviepy",
    "opencv-python",
    "matplotlib",
    "seaborn",
]

setup(
    name="openai-safety-gym",
    packages=['safety_gym'],
    python_requires=">=3.6",
    install_requires=install_requires,
)