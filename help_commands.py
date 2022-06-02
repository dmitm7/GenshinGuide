from discord_components import Button, ButtonStyle


def open_files():
    with open("mond/mond.txt", "r", encoding="utf-8") as mond, \
            open("liyue/liyue.txt", "r", encoding="utf-8") as liuye, \
            open("inazuma/inazuma.txt", "r", encoding="utf-8") as inazuma, \
            open("mond/noelle/noelle.txt", "r", encoding="utf-8") as noelleD, \
            open("mond/noelle/talants.txt", "r", encoding="utf-8") as noelleT, \
            open("mond/noelle/weapons.txt", "r", encoding="utf-8") as noelleW, \
            open("mond/noelle/artifacts.txt", "r", encoding="utf-8") as noelleA, \
            open("mond/noelle/stars.txt", "r", encoding="utf-8") as noelleS, \
            open("mond/diluc/diluc.txt", "r", encoding="utf-8") as dilucD, \
            open("mond/diluc/talants.txt", "r", encoding="utf-8") as dilucT, \
            open("mond/diluc/weapons.txt", "r", encoding="utf-8") as dilucW, \
            open("mond/diluc/artifacts.txt", "r", encoding="utf-8") as dilucA, \
            open("mond/diluc/stars.txt", "r", encoding="utf-8") as dilucS:
        mond = mond.read()
        liuye = liuye.read()
        inazuma = inazuma.read()

        noelleD = noelleD.read()
        noelleT = noelleT.read()
        noelleW = noelleW.read()
        noelleA = noelleA.read()
        noelleS = noelleS.read()

        dilucD = dilucD.read()
        dilucT = dilucT.read()
        dilucW = dilucW.read()
        dilucA = dilucA.read()
        dilucS = dilucS.read()

    return mond, liuye, inazuma, \
           noelleD, noelleT, noelleW, noelleA, noelleS, \
           dilucD, dilucT, dilucW, dilucA, dilucS


mond, liuye, inazuma, \
noelleD, noelleT, noelleW, noelleA, noelleS, \
dilucD, dilucT, dilucW, dilucA, dilucS = open_files()

weapons, artifacts, stars, talants, back = Button(style=ButtonStyle.gray, label="Оружие", emoji="⚔"), \
                                           Button(style=ButtonStyle.gray, label="Артефакты", emoji="🏆"), \
                                           Button(style=ButtonStyle.gray, label="Созвездия", emoji="💫"), \
                                           Button(style=ButtonStyle.gray, label="Таланты", emoji="📚"), \
                                           Button(style=ButtonStyle.gray, label="Назад")
mond_btn, liuye_btn, inazuma_btn = Button(style=ButtonStyle.gray, label="Мондштадт"), \
                                   Button(style=ButtonStyle.gray, label="Ли Юэ"), \
                                   Button(style=ButtonStyle.gray, label="Инадзума")
