# # 1 - heslo
# input_password = input("Zadejte heslo: ")
# password = "monitor"
# attempt = 1
#
# while True:
#     if input_password == password:
#         print(f"""Heslo zadáno správně a to na {attempt}. pokus!""")
#         break
#
#     attempt += 1
#     input_password = input("Heslo bylo zadáno špatně, zadejte ho znovu: ")


# # 2 - součet n hodnot
# n = int(input("Zadejte číslo n: "))
# i = 1
# total = 0
#
# while i <= n:
#     total += i
#     i += 1
#
# print(f"""Součet je {total}!""")


# # 3 - tabulka hodnot gon fcí
# import math as m
#
# angle = 0
# print("uhel\t\tsin \t\t\tcos \t\t\ttg  \t\t\tcotg")
# while angle <= 90:
#     angle_rad = m.radians(angle)
#     value_sin = "%0.3f" % m.sin(angle_rad)
#     value_cos = "%0.3f" % m.cos(angle_rad)
#     if angle == 90:
#         value_tg = "UD   "
#     else:
#         value_tg = "%0.3f" % m.tan(angle_rad)
#
#     if angle == 0:
#         value_cotg = "UD   "
#     else:
#         value_cotg = "%0.3f" % m.sin(angle_rad)
#     print(f"""{angle}°\t\t\t{value_sin}\t\t\t{value_cos}\t\t\t{value_tg}\t\t\t{value_cotg}""")
#     angle += 5
