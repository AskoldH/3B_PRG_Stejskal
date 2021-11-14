directions = {
    "north": ["sever", "s"],
    "south": ["jih", "j"],
    "est": ["východ", "v", "vychod"],
    "west": ["západ", "z", "zapad"]
}

game_on = 1
north_block_on = 1

death = f"""
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\\
       ::::::;       ;          OOOOO\\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#"""

tiger = f"""
                       __,,,,_
   _   _ ___.--'''`--''// ,-o `-.
   \\`)' o |  \\  \\ o\\/ /.// / ,-  o,_
  /_`  \\   |o )  | O|. /o// / -.,_o `-.
 /<0\\    ) \\  |  | ||/ //o| \\/ O  |`-.o`-._
/  _.-.  .-\\,O__|  _-| /o\\ \\/|_/  |    `-._)
`-\\  \\/ |       /o__/ \\__O / |o_/ |
     `-'       |  -| -|\\__ \\  |-' |
 (✘_✘)     __/ o /__,-o    ),'o |'
 /( )\\    ((__.-'((____..-' \\__,'
  / \\    """

start_block = f"""  
                  ▁▁▁▁▁▁▁▏   ▕▁▁▁▁▁▁
                  ▌                ▌
                  ▌                ▌
                ▔▔▔                ▔▔▔
                         START             
                ▁▁▁                ▁▁▁
                  ▌                ▌
                  ▌▁▁▁▁▁▁     ▁▁▁▁▁▌
                         ▏   ▕ """

now_in_block = f""" 
                  ▁▁▁▁▁▁▁▏ S ▕▁▁▁▁▁▁
                  ▌                ▌
                  ▌                ▌
                ▔▔▔      (._.)     ▔▔▔
                Z        /( )\\       V
                ▁▁▁       / \\      ▁▁▁
                  ▌                ▌
                  ▌▁▁▁▁▁▁     ▁▁▁▁▁▌
                         ▏ J ▕ """

middle_block = f""" 
                  ▁▁▁▁▁▁▁▏   ▕▁▁▁▁▁▁
                  ▌                ▌
                  ▌                ▌
                ▔▔▔                ▔▔▔
                                    
                ▁▁▁                ▁▁▁
                  ▌                ▌
                  ▌▁▁▁▁▁▁     ▁▁▁▁▁▌
                         ▏   ▕ """

empty_from_start_block = f"""   
                  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁    ▁▁▁▁▁▁▁▏   ▕▁▁▁▁▁▁
                  ▌                ▌    ▌                ▌
                  ▌                ▌    ▌                ▌
                  ▌      (._.)     ▔▔▔▔▔▔                ▔▔▔
                  ▌      /( )z       V         START        
                  ▌       / \\      ▁▁▁▁▁▁                ▁▁▁
                  ▌                ▌    ▌                ▌
                  ▌▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▌    ▌▁▁▁▁▁▁     ▁▁▁▁▁▌
                                               ▏   ▕"""

empty_from_middle_block = f"""   
                  ▁▁▁▁▁▁▁▏   ▕▁▁▁▁▁▁    ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
                  ▌                ▌    ▌                ▌ 
                  ▌                ▌    ▌                ▌
                ▔▔▔                ▔▔▔▔▔▔      (._.)     ▌
                                      Z        /( )z     ▌
                ▁▁▁                ▁▁▁▁▁▁       / \\      ▌
                  ▌                ▌    ▌                ▌
                  ▌▁▁▁▁▁▁     ▁▁▁▁▁▌    ▌▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▌
                         ▏   ▕"""

with_sand_block = f"""   
                  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
                  ▌................▌
                  ▌................▌
                  ▌.....\\(._.)/....▔▔▔
                  ▌.......( ).......V
                  ▌......./ \\ ......▁▁
                  ▌................▌
                  ▌▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▌
                          """

win_block = f"""   
                  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
                  ▌     $$$$$$     ▌
                  ▌    $$$$$$$$    ▌
                  ▌     \\(._.)/    ▌
                  ▌       ( )      ▌
                  ▌       / \\      ▌
                  ▌                ▌
                  ▌▁▁▁▁▁▁     ▁▁▁▁▁▌
                         ▏   ▕ """

welcome_text = f"""Vítej v mé hře, tvým úkolem je dostat se až k pokladu, věřím že se tí to povede, nebude to ale jednoduché.
Přeji hodně štěstí, pohybovat se můžeš příkazy sever, jih, východ nebo západ (nebo s, j, v, z)!
Resetuj hru pomocí "reset" a vypni pomocí "off".
                   {now_in_block}
Tvůj první směr bude: """

user_input = input(welcome_text).lower()

while game_on:
    if user_input == "reset":
        user_input = input(welcome_text).lower()
        north_block_on = 1

    elif user_input == "off":
        game_on = 0

    elif user_input in directions["north"]:
        north_block_on = 1
        user_input = input(now_in_block + start_block + "\n\nKde ni tu nic, pokračuj.\nTvůj další směr bude: ").lower()
        while north_block_on:
            if user_input in directions["north"]:
                user_input = input(win_block + middle_block + "\n$$$ POKLAD $$$ "
                                                              "\nNo way!! Ty jsi ho našel, ty, ty jsi našel "
                                                              "poklad!\nNašel jsi zlaté pruty, tak se můžeš "
                                                              "vrátit.\nUžívej ho ve zdraví, kdyby jsi "
                                                              "nevěděl co s tolika penězi,\ntak mi kup kakajíčko v "
                                                              "automatu, dík.\n"
                                                              "Pro reset hry napiš \"reset\", pro konec \"off\": ")
                north_block_on = 0

            elif user_input in directions["south"]:
                user_input = input(middle_block + now_in_block + "\n\nJsi na začátku a tvůj další směr bude: ").lower()
                north_block_on = 0

            elif user_input in directions["est"]:
                user_input = input(
                    empty_from_middle_block + "\n\nVypadá to že to nikam nevede! Tak to je nůůůda!\nVrať se a zkus to "
                                              "jinudy: ").lower()
                while True:
                    if user_input in directions["west"]:
                        user_input = input(now_in_block + "\n\nJsi zpět a tvůj další směr bude: ").lower()
                        break

                    elif (user_input in directions["north"]) or (user_input in directions["south"]) or (
                            user_input in directions["est"]):
                        user_input = input(
                            empty_from_middle_block + "\nZdí neprojdeš, vrať se na zpět na západ : ").lower()
                    else:
                        user_input = input(
                            f"""Jajx, {user_input} neodpovídá příkazu!\nZkus to prosím znova: """).lower()

            elif user_input in directions["west"]:
                while True:
                    user_input = input(
                        with_sand_block + "\nRychle se vrať, místnost je "
                                          "plná tekutého písku, snad to zvládneš!!\nUtíkej: ").lower()

                    if user_input in directions["est"]:
                        user_input = input(
                            now_in_block + "\n\nJsi zpět a pořád kde nic tu nic, pokračuj."
                                           "\nTvůj další směr bude: ").lower()
                        break
                    elif user_input in directions["north"] or user_input in directions["south"] or user_input in \
                            directions["west"]:
                        user_input = input(
                            death + "\n\n✞✞ RIP ✞✞\nGame over!!\nTy jsi ale loupák. vážne jsi se rozběhl proti "
                                    "špatné zdi, vysílil se a zůstal v písku na věky?"
                                    "\nPro reset hry napiš \"reset\", pro konec \"off\": ")
                        north_block_on = 0
                        break

                    else:
                        user_input = input(
                            f"""Jajx, {user_input} neodpovídá příkazu!\nZkus to prosím znova: """).lower()
            else:
                user_input = input(f"""Jajx, {user_input} neodpovídá příkazu!\nZkus to prosím znova: """).lower()

    elif user_input in directions["south"]:
        user_input = input(
            "\nSkrz malou chodbičku vidíš v další místnosti tygra, jsi si jistý, že chceš pokračovat? (y/n): ").lower()
        while True:
            if (user_input != "y") and (user_input != "n"):
                user_input = input("Zadej y pro pokračování, n pro vrácení se: ").lower()

            elif user_input == "y":
                user_input = input(tiger + "\n\n✞✞ RIP ✞✞\nGame over, jsi se nechal sežrat troubo, lul."
                                           "\nPro reset hry napiš \"reset\", pro konec \"off\": ")
                reset_loop = 0
                break

            elif user_input == "n":
                user_input = input(now_in_block + "\n\nJsi na začátku a tvůj další směr bude: ").lower()
                break

    elif user_input in directions["est"]:
        user_input = input(
            death + "\n\n✞✞ RIP ✞✞\nGame over, jako vážne jsi právě uklouzl a zlomil si vaz? To jsem teda "
                    "čekal,\n"
                    "že si budeš dávat větší pozor hrdino!\nPro reset hry napiš \"reset\", pro konec \"off\": ")
        reset_loop = 0

    elif user_input in directions["west"]:
        user_input = input(
            empty_from_start_block + "\n\nVypadá to že to nikam nevede!\nVrať se a zkus to jinudy: ").lower()
        while True:
            if user_input in directions["est"]:
                user_input = input(now_in_block + "\n\nJsi na začátku a tvůj další směr bude: ").lower()
                break

            elif (user_input in directions["north"]) or (user_input in directions["south"]) or (
                    user_input in directions["west"]):
                user_input = input(empty_from_start_block + "\nZdí neprojdeš, vrať se na začátek: ").lower()

            else:
                user_input = input(f"""Jajx, {user_input} neodpovídá příkazu!\nZkus to prosím znova: """).lower()

    else:
        user_input = input(f"""Jajx, {user_input} neodpovídá příkazu!\nZkus to prosím znova: """).lower()
