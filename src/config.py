# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('mume', '無門', '無門,健義', 35,(1,1), 'male', '無職', "me:私"),# 無門で「かどなし」と呼ぶ
            ("yuna", "有奈", "冴喜,有奈", 28,(1,1), "female", "動画配信者", "me:わたし"),
            ("ishi", "石脇", "石脇,和優", 35,(1,1), "male", "芸人", "me:俺"),
            ("hashi", "橋本", "", 40,(1,1), "male", "記者", "me:俺:k_me:私"),
            ("mutsu", "睦美", "奈良,睦美", 30,(1,1), "female", "イラストレータ", "me:うち"),
            ("akai", "赤井", "赤井,圭助", 34,(1,1), "male", "小説家", "me:俺"),
            ("taka", "高橋", "高橋,弘之", 30,(1,1), "male", "編集者", "me:オレ"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Tabata", "田端", "Tokyo"),
            ("Station", "田端駅", "Tabata"),
            ("House", "名無荘", "Tabata"),
            ("MumeRoom", "無名の部屋", "House"),
            ("IshiRoom", "石脇の部屋", "House"),
            ("Living", "共用スペース", "House"),
            ("YunaHome", "有奈の家", "Tabata"),
            ("ParentHouse", "無名の実家", "Tabata"),
            ("Cafe", "喫茶店", "Tabata"),
            ("Conveni", "コンビニ", "Tabata"),
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
            ("FirstMeet", "初対面の日", 8,31, 2020),
            ("MeetingDay1", "打ち合わせ日１", 9,1, 2020),
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
            ("ATM", "ＡＴＭ"),
            ("pv", "ＰＶ"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

