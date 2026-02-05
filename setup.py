import sys
from setuptools import setup, Extension

setup_kwargs = {
    "ext_modules": [
        Extension(
            "tgcryptomax",
            sources=[
                "tgcryptomax/tgcryptomax.c",
                "tgcryptomax/aes256.c",
                "tgcryptomax/ige256.c",
                "tgcryptomax/ctr256.c",
                "tgcryptomax/cbc256.c"
            ]
        )
    ]
}

if sys.version_info >= (3, 9):
    setup_kwargs["license_files"] = ["COPYING", "COPYING.lesser", "NOTICE"]

setup(**setup_kwargs)
