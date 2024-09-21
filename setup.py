from setuptools import setup, find_packages

setup(
    name='ml_predictor',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'joblib'
    ],
    entry_points={
        'console_scripts': [
            'ml_predictor=ml_predictor.model:main',
        ],
    },
)
