from distutils.core import setup
import py2exe

setup(name="Cuadratica",
 version="1.1",
 description="funcion cuadratica",
 author="Fabri Juncal",
 author_email="juncalfabri@gmail.com",
 url="url del proyecto",
 license="reserva los derechos del autor",
 scripts=["cuadratica.py"],
 console=["cuadratica.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)
