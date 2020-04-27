# -*- mode: python ; coding: utf-8 -*-
from kivy.deps import sdl2, glew

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Gabriel\\Desktop\\jogo-forca\\dev-code'],
             binaries=[],
             datas=[
			 ('C:\\Users\\Gabriel\\Desktop\\jogo-forca\\dev-code\\image\\*.png','image'),
			 ('C:\\Users\\Gabriel\\Desktop\\jogo-forca\\dev-code\\image\\base\\*','image\\base'),
			 ('C:\\Users\\Gabriel\\Desktop\\jogo-forca\\dev-code\\image\\um\\*','image\\um'),
			 ('C:\\Users\\Gabriel\\Desktop\\jogo-forca\\dev-code\\data\\*','data'),
			 ],
             hiddenimports=[],
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
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
			   *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
