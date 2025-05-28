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
    "numpy==1.23.5",
    "joblib~=0.14.0",
    "xmltodict~=0.12.0",
    "gym~=0.23.1", 
    "gymnasium>=0.28.1",
    "stable-baselines3==2.0.0",
    "huggingface-hub>=0.8.0",
    "torch>=1.12.1",
    "pygame==2.1.0",
    "tensorboard==2.10.0",
    "tyro",
    "wandb==0.13.11",
    "moviepy",
    "opencv-python",
    "matplotlib",
    "seaborn",
    "cleanrl @ git+https://github.com/vwxyzjn/cleanrl.git",
]

setup(
    name="openai-safety-gym",
    packages=['safety_gym'],
    python_requires=">=3.6",
    install_requires=install_requires,
)