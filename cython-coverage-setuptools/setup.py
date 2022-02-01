from setuptools import setup, Extension

setup(
    name="tasket",
    version="0.0.1.dev0",
    description="A sample project that uses Cython-generated extensions",
    license="Apache 2.0",
    ext_modules=[
        Extension(
            name="tasket._comp",
            sources=["tasket/_comp.pyx"],
            libraries=["m",],
            define_macros=[("CYTHON_TRACE",1),],
            language="c++"
        ),
    ],
)
