# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('mume', '無門', '無門,健義', 30,(1,1), 'male', '無職', "me:私"),# 無門で「かどなし」と呼ぶ
            ("yuna", "有奈", "冴喜,有奈", 30,(1,1), "female", "動画配信者", "me:わたし"),
            ("ishi", "石脇", "石脇,和優", 35,(1,1), "male", "芸人", "me:俺"),
            ("hashi", "橋本", "", 40,(1,1), "male", "記者", "me:俺:k_me:私"),
            ("mutsu", "睦美", "奈良,睦美", 30,(1,1), "female", "イラストレータ", "me:うち"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Tabata", "田端", "Tokyo"),
            ("Station", "田端駅", "Tabata"),
            ("House", "シェアハウス", "Tabata"),
            ("MumeRoom", "無名の部屋", "House"),
            ("IshiRoom", "石脇の部屋", "House"),
            ("Living", "共用スペース", "House"),
            ("YunaHome", "有奈の家", "Tabata"),
            ("ParentHouse", "無名の実家", "Tabata"),
            ("Cafe", "喫茶店", "Tabata"),
            ("Famires", "ファミレス", "Tabata"),
            ("PostOffice", "郵便局", "Tabata"),
            ("AroundPH", "実家跡地周辺", "Tabata"),
            ("ItalianBar", "イタリアンバー", "Tokyo"),
            ("TenantBuilding", "雑居ビル", "Tokyo"),
            ("PaperCompany", "小さな会社", "Tokyo"),
            ("SideWalk", "歩道", "Tokyo"),
            ("BookShop", "本屋", "Tokyo"),
            ("Bar", "飲み屋", "Tokyo"),
            ("TowerManshion", "タワーマンション", "Tabata"),
            ("YunaHome", "有奈の部屋", "TowerManshion"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ("theblog", "かつて有名だった私へ"),
            ("line", "ＬＩＮＥ"),
            ("pc", "ＰＣ"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

