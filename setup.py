from setuptools import find_packages, setup


setup(
    name='openrectorch',
    version='0.1.0',
    packages=find_packages(exclude=("tutorials",)),
    description="An open-source and modular library for neural network-inspired recommendation algorithms",
    license='MIT',
    author='Corey Smith',
    author_email='coreys@uchicago.edu',
    install_requires=[
        'tqdm>=4.15.0',
        'numpy>=1.13.0',
        'termcolor>=1.1.0'
          ],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'License :: OSI Approved :: MIT',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence'],
)
