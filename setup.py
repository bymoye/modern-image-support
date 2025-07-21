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
    name="modern-image-support",
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
    author="bymoye",
    author_email="s3moye@gmail.com",
    version="0.4.0",
    url="https://github.com/bymoye/modern-image-support",
    description="Fast WebP and AVIF image format support detection from User-Agent strings.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Cython",
        "Programming Language :: C",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    packages=["modern_image_support"],
    keywords=["webp", "avif", "image", "user-agent", "browser-detection"],
)
