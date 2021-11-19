import random  
import time
import datetime

# =============================================================================
# alphabet = 'abcdefghijklmnopqrstuvwxyz' 
# result = ''.join((random.choice(alphabet)) for x in range(3))  
# print(result)  
# =============================================================================


# =============================================================================
# random_cislo = int("".join(str(random.randint(0, 9)) for x in range(4)))
# print(random_cislo)
# =============================================================================


# =============================================================================
# random_hour = str(random.randint(0, 24))
# random_min = str(random.randint(0, 60))
# random_sec = str(random.randint(0, 60))
# 
# if int(random_hour) < 10:
#     random_hour = "0" + random_hour
# if int(random_min) < 10:
#     random_min = "0" + random_min
# if int(random_sec) < 10:
#     random_sec = "0" + random_sec
# print(random_hour, random_min, random_sec, sep=":")
# =============================================================================


# =============================================================================
# while 1:
#     year = random.randint(1500, 2500)
#     month = random.randint(0, 12)
#     day = random.randint(0, 31)
#     try:
#         datetime.datetime(year, int(month), int(day))
#         break
#     except ValueError:
#         pass
#         
# print(f"""Tvé náhodé datum je {day}.{month}.{year}""")
# =============================================================================


# =============================================================================
# character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# code = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','-.-','...','-','..-','...-','.--','-..-','-.--','--..']
# pismeno = "".join(random.choice(character))
# pismeno_v_morzeovce = code[character.index(pismeno)]
# print(f"""Písmeno {pismeno} je v morzeovce {pismeno_v_morzeovce}""")
# =============================================================================












