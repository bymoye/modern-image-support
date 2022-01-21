from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name="supportWebp",
    ext_modules=cythonize(
        Extension(
            name="supportWebp",
            sources=["supportWebp.pyx"],
            language=["c++"],
            extra_compile_args=["-O2"],
        ),
        compiler_directives={
            'language_level': 3,
            'boundscheck': False,
            'wraparound': False
        },
    ),
    author="bymoye",
    author_email="s3moye@gmail.com",
    version="0.0.1",
    description="Quickly determine whether Webp is supported from UserAgent.",
    license="MIT",
    classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Cython",
    "Programming Language :: C++",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6'
)