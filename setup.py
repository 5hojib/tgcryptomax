from setuptools import setup, Extension

setup(
    ext_modules=[
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
)
