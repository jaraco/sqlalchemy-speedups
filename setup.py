
import setuptools

setup_params = dict(
    name="SQLAlchemy-speedups",
    version="1.0",
    description="Database Abstraction Library C Extensions",
    author="Mike Bayer",
    author_email="mike_mp@zzzcomputing.com",
    url="http://www.sqlalchemy.org",
    packages=['sqlalchemy_speedups'],
    license="MIT License",
    ext_modules = [
        setuptools.Extension('sqlalchemy_speedups.cprocessors',
            sources=['lib/processors.c']),
        setuptools.Extension('sqlalchemy_speedups.cresultproxy',
            sources=['lib/resultproxy.c']),
        setuptools.Extension('sqlalchemy_speedups.cutils',
            sources=['lib/utils.c']),
        ]
    )

if __name__ == '__main__':
    setuptools.setup(**setup_params)
