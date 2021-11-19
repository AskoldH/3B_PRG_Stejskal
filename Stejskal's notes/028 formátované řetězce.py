# -*- coding: utf-8 -*-
"""
Formátovaný řetězec
- do řetězce vkládáme pomocí indexů hodnoty
  z n-tice
- obecný tvar je:
  retězec="{index:specifikátor}".format(n-tice)

https://www.sallyx.org/sally/python/python3b.php#format3
https://docs.python.org/3/library/string.html#format-specification-mini-language
"""

#indexy parametrů lze vynechat :)
#ret = "Dnes je {0}.{1}.{2}".format(8,5,2020)
#print(ret)

#vložení desetinného čísla (dochází k mat. zaokr.)
#ret = "Číslo pí má hodnotu {0:.3f}".format(3.14159)
#print(ret)

#lze vkládat hodnoty z různých struktur
#seznam=["Chleba","stojí",28.50,"Kč"]
#ret="{0[0]} {0[1]} {0[2]:10.2f} {0[3]}".format(seznam)
#print(ret)

#pozor, u slovníků se nepíší uvozovky u klíče!!!

#lze uvádět různé podoby celého čísla
#ret = "Dnes je {0:b}.{1:b}.{2:b}".format(8,5,2020)
#print(ret)
#ret = "Dnes je {0:x}.{1:x}.{2:x}".format(8,5,2020)
#print(ret)
#ret = "Toto je znak zavináč {0:c}".format(64)
#print(ret)


#v rámci volného prostoru můžeme zarovnávat
ret="Číslo {0:<15} zarovnané doleva".format(28)
print(ret)
ret="Číslo {0:>15} zarovnané doprava".format(28)
print(ret)
ret="Číslo {0:^15} zarovnané na střed".format(28)
print(ret)
ret="Číslo {0:*^15} zarovnané na střed".format(28)
print(ret)



