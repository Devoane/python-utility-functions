from setuptools import setup, find_packages

setup(
    name="Library_Task3",  # Nazwa projektu
    version="0.1",  # Wersja projektu
    packages=find_packages(),  # Automatyczne wykrywanie pakietów
    install_requires=[],  # Zewnętrzne zależności (jeśli jakieś są)
    test_suite="tests",  # Katalog z testami
    author="Devoane",    # Autor projektu
    description="A collection of utility functions for various tasks.",
)
