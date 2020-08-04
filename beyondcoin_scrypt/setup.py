from distutils.core import setup, Extension

bynd_scrypt_module = Extension('bynd_scrypt',
                               sources = ['scryptmodule.c',
                                          'scrypt.c'],
                               include_dirs=['.'])

setup (name = 'bynd_scrypt',
       version = '1.0',
       description = 'Bindings for scrypt proof of work used by Beyondcoin',
       ext_modules = [bynd_scrypt_module])
