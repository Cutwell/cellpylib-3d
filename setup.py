from setuptools import setup
import re

INIT_FILE = "cellpylib3d/__init__.py"

with open(INIT_FILE) as fid:
    file_contents = fid.read()
    match = re.search(r"^__version__\s?=\s?['\"]([^'\"]*)['\"]", file_contents, re.M)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s" % INIT_FILE)

setup(name="cellpylib3d",
      version=version,
      description="An extension of CellPyLib, enabling 3d cellular automata.",
      long_description="An extension of CellPyLib, enabling 3d cellular automata. Adds support for 3-dimensional k-colour cellular automata, with 3d helper and plot functions.",
      license="Apache License 2.0",
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.7',
      ],
      url='https://github.com/Cutwell/cellpylib-3d',
      author="Z. Smith",
      author_email="zachsmith.dev@gmail.com",
      packages=["cellpylib3d"],
      keywords=["cellular automata", "complexity", "complex systems", "computation", "non-linear dynamics"],
      python_requires='>3.7',
      install_requires=["numpy >= 1.15.4", "matplotlib >= 3.0.2"])
