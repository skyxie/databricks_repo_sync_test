#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="databricks-repo-sync-test",
    version="0.1.0",
    author="Machine Learning Engineering",
    author_email="ml_engineering_team@enigma.com",
    description="Python library to test UDFs in MLFlow Project.",
    packages=find_packages(
        exclude=[
            "mlflow_project_with_package",
            "mlflow_project_alt"
        ]
    ),
)
