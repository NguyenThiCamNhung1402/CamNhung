# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:47:28 2024

@author: Nguyễn Thị Cẩm Nhung- 23712471
"""
chuoi = "i'm a cat"
in_hoa= chuoi.upper()
print(in_hoa)
hoa_dau_moi_tu = chuoi.title()
print(hoa_dau_moi_tu)
hoa_chu_cai_dau = chuoi[0].upper() + chuoi[1:]
print(hoa_chu_cai_dau)
moi = list(chuoi)
moi[2]= moi[2].upper()
moi[5]= moi[5].upper()
moi[7]= moi[7].upper()
moi[8]= moi[8].upper()
moi="".join(moi)
print(moi)