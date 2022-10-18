from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="Brain-Stroke-Predictor"
VERSION="0.0.1"
AUTHOR="Mujeeb Subhani"
DESRCIPTION="Developed a model to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status."

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), 
install_requires=get_requirements_list()
)