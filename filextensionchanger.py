# -*- coding: cp1254 -*-
import sys
import os

req_version = (3,0)
cur_version = sys.version_info
if cur_version >= req_version:
    print("-"*45)
    print("""
      ___ _               _     _           ____  
     |_ _| |__  _ __ __ _| |__ (_)_ __ ___ | __ ) 
      | || '_ \| '__/ _` | '_ \| | '_ ` _ \|  _ \ 
      | || |_) | | | (_| | | | | | | | | | | |_) |
     |___|_.__/|_|  \__,_|_| |_|_|_| |_| |_|____/ 
                                                        
    """)
    print("-"*45)
    uzanti = input("Dosyalarin suanki uzantisi (Ornek: .txt): ")
    duzanti = input("Degistirmek istediginiz uzanti (Ornek: .selco):")
    os.system('cmd /c ren *{iuzanti} *{iduzanti}' .format(iuzanti = uzanti, iduzanti = duzanti))
    print('{uz} uzantili dosyalar basarili bir sekilde {duz} uzantili dosyalara cevrildi !' .format(uz = uzanti, duz = duzanti))
else:
    print("Programi calıstirmak icin Python surumunun en az 3.x.x olmasi gerekiyor.")
