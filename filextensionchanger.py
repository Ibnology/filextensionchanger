import os

print("-"*45)
print("""
  ___ _               _     _           ____  
 |_ _| |__  _ __ __ _| |__ (_)_ __ ___ | __ ) 
  | || '_ \| '__/ _` | '_ \| | '_ ` _ \|  _ \ 
  | || |_) | | | (_| | | | | | | | | | | |_) |
 |___|_.__/|_|  \__,_|_| |_|_|_| |_| |_|____/ 
                                                        
""")
print("-"*45)
uzanti = input("Dosyalarin suanki uzantisi (Örnek: .txt): ")
duzanti = input("Degistirmek istediginiz uzanti: (Örnek: .selco)")
os.system('cmd /c ren *{iuzanti} *{iduzanti}' .format(iuzanti = uzanti, iduzanti = duzanti))
print('{uz} uzantili dosyalar basarili bir sekilde {duz} uzantili dosyalara cevrildi !' .format(uz = uzanti, duz = duzanti))
