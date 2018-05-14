# -*- mode: python -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['.'],
             binaries=[],
             datas=[
              ('./img/*.png','img'),
              ('./img/*.ttf','img'),
              ('./img/items/*.png','img/items'),
              ('./img/path/*.png','img/path'),
              ('./img/player/*.png','img/player'),
              ('./sfx','sfx'),
            ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
