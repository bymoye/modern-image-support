from setuptools import setup, Extension
from Cython.Build import cythonize


def readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


ext_modules = [
    Extension(
        "modern_image_support.modern_image_support",
        sources=["modern_image_support/modern_image_support.pyx"],
        extra_compile_args=["-O3"],
        extra_link_args=["-O3"],
    ),
]

setup(
    ext_modules=cythonize(
        ext_modules,
        language_level=3,
        compiler_directives={
            "language_level": 3,
            "boundscheck": False,
            "wraparound": False,
        },
    ),
    package_data={
        "modern_image_support": [
            "*.pyi",
            "*.pyx", 
            "*.h",
            "*.pxd",
        ]
    },
    include_package_data=True,
    packages=["modern_image_support"],
)
