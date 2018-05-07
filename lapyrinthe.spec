# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/ashmonger/projets/lapyrinthe'],
             binaries=[],
             datas=[
             ('/home/ashmonger/projets/lapyrinthe/img/*.ttf','img'),
             ('/home/ashmonger/projets/lapyrinthe/img/*.png','img'),
             ('/home/ashmonger/projets/lapyrinthe/img/items/*.png','img/items'),
             ('/home/ashmonger/projets/lapyrinthe/img/path/*.png','img/path'),
             ('/home/ashmonger/projets/lapyrinthe/img/player/*.png','img/player')
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
          exclude_binaries=True,
          name='lapyrinthe',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='lapyrinthe')
