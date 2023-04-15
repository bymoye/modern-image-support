from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "webp_support",
        sources=["webp_support.pyx", "webp_support_c.c"],
        extra_compile_args=["-O3"],
        extra_link_args=["-O3"],
    ),
]

setup(
    name="webp_support",
    ext_modules=cythonize(
        ext_modules,
        language_level=3,
        compiler_directives={
            "language_level": 3,
            "boundscheck": False,
            "wraparound": False,
        },
    ),
    package_data={'webp_support': ['*.pyi', "*.pyx"]},
    author="bymoye",
    author_email="s3moye@gmail.com",
    version="0.2.2",
    url="https://github.com/bymoye/webp_support",
    description="A Quickly determine whether Webp is supported from UserAgent.",
    long_description="A Quickly determine whether Webp is supported from UserAgent.",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Cython",
        "Programming Language :: C",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
)
