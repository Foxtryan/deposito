# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Coding\\jogo-da-forca-dev\\jogo-forca-dev'],
             binaries=[],
             datas=[
			 ('C:\\Coding\\jogo-da-forca-dev\\jogo-forca-dev\\data\\*', 'data'),
			 ('C:\\Coding\\jogo-da-forca-dev\\jogo-forca-dev\\image\\*.png', 'image'),
			 ('C:\\Coding\\jogo-da-forca-dev\\jogo-forca-dev\\image\\base\\*.jpg', 'image\\base'),
			 ('C:\\Coding\\jogo-da-forca-dev\\jogo-forca-dev\\image\\um\\*.jpg', 'image\\um')
			 ],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
			   *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
