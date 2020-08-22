#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8：3K
#   4. Spec
#   5. Plot         - 1/4：7K
#   6. Scenes
#   7. Conte        - 1/2：15K
#   8. Layout
#   9. Draft        - 1/1：30K
#
################################################################

# Constant
TITLE = "無名"
MAJOR, MINOR, MICRO = 0, 2, 0
COPY = "名前に振り回された人生でした"
ONELINE = "約３万字の文学短編。有名になりたい男と無名になりたい女の人生が、交錯する"
OUTLINE = "有名になりたい男は試行錯誤するけれど、その間にも同居するその界隈で有名な女は更に有名になり、無名になりたいと願う。二人は人生の交換を申し出た"
THEME = "名前によって人生は左右されるのか？"
GENRE = "文学"
TARGET = "20-70years"
SIZE = "原稿70から150枚（20Kから50K）"
CONTEST_INFO = "第126回文學界新人賞"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["文学",]
RELEASED = (1, 1, 2020)


# Episodes
def ep_xxx(w: World):
    return w.episode('episode_title',
            outline="description")


def ch_main(w: World):
    return w.chapter('main',
            "main plot",
            w.plot_setup("無名の男がいた"),
            w.plot_setup("男は色々なことをして有名になろうとしていたが、全て失敗していた"),
            w.plot_setup("その男とルームシェアして暮らす女性がいた"),
            w.plot_turnpoint("彼女はゲーム実況をしてみたいと言うので、手伝った"),
            w.plot_develop("彼女は人気実況者になった"),
            w.plot_develop("彼女をマネていろいろやってみたけれど、男は全然人気が出なかった"),
            w.plot_turnpoint("男は彼女の中の人として交代した"),
            w.plot_develop("彼女は更に人気となる"),
            w.plot_develop("男は彼女の中の人として人気になる"),
            w.plot_turnpoint("中の人が男だとばれる"),
            w.plot_resolve("炎上し、彼女のアカウントだけでなく、男のアカウントも全て削除する"),
            w.plot_resolve("$mumeは彼女にプロポーズされ、そこで初めて自分の名を呼ばれた"),
            "sub plot",
            w.plot_setup("シェアハウスで同居していた彼氏に出ていかれた", about="yuna"),
            w.plot_setup("いつの間にかシェアハウスに$mumeと取り残された", about="yuna"),
            w.plot_develop("（元彼氏がやっていた）ゲーム実況をやってみる", about="yuna"),
            w.plot_develop("実況者として人気になってしまう", about="yuna"),
            w.plot_turnpoint("SNSまで追いかけてきてネットストーカーされる", about="yuna"),
            w.plot_develop("彼に自分の代わりにゲーム実況者になってもらう", about="yuna"),
            w.plot_resolve("何もなくても一緒にいたいと思った$yunaは彼の名を呼びプロポーズをした", about="yuna"),
            w.plot_note("無名な人間がいた"),
            w.plot_note("彼は作家を目指していた"),
            w.plot_note("作家だけじゃない、音楽も、絵も、ゲームやシナリオ、果ては動画制作まで、",
                "いろいろとチャレンジしたが全く芽が出なかった"),
            w.plot_note("一方、同棲している女が、ゲームを実況したいと言い出した"),
            w.plot_note("いろいろと準備して、彼女の実況生活が始まる"),
            w.plot_note("彼女は知らないうちにどんどん名前が売れて、人気者になっていく"),
            w.plot_note("自分はそれを横目に必死に小説を書いたり、SNSで人気な人にすり寄ったり"),
            w.plot_note("人気は出ないばかりか、才能がないと駄目出しされてしまった"),
            w.plot_note("彼女はＶチューバーとして人気者になっていた"),
            w.plot_note("けれど彼女はそれをよしとはせず、引退して、ひっそり暮らしたりと言い出す"),
            w.plot_note("彼は彼女から人気を引き継いだ"),
            w.plot_note("人気者になった彼"),
            w.plot_note("ネット上では自分の知らないところでその名前が出る"),
            w.plot_note("有名になったと錯覚するが、それが自分の才能とは何の関係もないことを知る"),
            w.plot_note("そこでネタバラシをして名前を自分のものにしようと考えたが、",
                "コメントで誰かが「もし〜だったら」という仮定の話を書いていて、",
                "その流れからどう考えてもマイナスにしかならないと判断する"),
            w.plot_note("自分の名前ではない名前が独り歩きし、それを演じ続ける中で、",
                "悪質なもの、悪戯などが増えてくる"),
            w.plot_note("それは「かつて有名だった私へ」と題したブログにかかれていたことと同じ内容だった"),
            w.plot_note("有名になりたい、と色々がんばっていた日常の方がずっと楽しく、充実していたこと"),
            w.plot_note("いざ有名になっても制約が多く、また自分ではない自分が独り歩きしてしまって、",
                "それが悪さをしたりする。誰かに傷つけられたりする"),
            w.plot_note("最後に書かれていたのは「わたしは無名になりたい」だった"),
            w.plot_note("そのブログの主は自殺した"),
            w.plot_note("有名が彼女を殺したのだ"),
            w.plot_note("無名を手に入れた同棲の彼女が言う",
                "有名ってさ結局自分の人生を削ることじゃないの？と"),
            w.plot_note("それでも空虚な名にしがみつこうとした主人公"),
            w.plot_note("けれど徐々にその名も保てなくなり、ネタバレされ、",
                "没落していく"),
            w.plot_note("男はふたたび無名に戻った"),
            w.plot_note("そんな無名な男に、同棲している彼女はプロポーズしてその名を呼んだ",
                "それが男にとって初めて呼ばれた名前だった"),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )


def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "名前はまだない。という出だし",
            "有名になることが人生の目標だったと書いている",
            "残っていたブログを記者が読んでいる、というてい",
            "無名でなくなった時に、主人公は後悔していた",
            "「俺の名はない」とインタビュアーに答えて終わり",
            "作中での「有名」は主にネット上でのこと",
            "それが現実にも侵食してくるから恐怖になる",
            "誰しも名を知ってもらいたい。それが多くの人にとっての人生の意味だろう",
            "けれど名を知られるというのは古来から恐れられてきた",
            "だから通り名を使っていた。本名、真の名前は教えなかった",
            "名前はいつの間にか安売りされ、人の価値も安くなってしまった",
            )


def chara_note(w: World):
    return w.writer_note("人物メモ",
            "・有名になりたい男",
            "・有名になってしまった女",
            "・彼女の元恋人で、同棲していたが逃げ出した男",
            "特に稼ぐとか有名になりたいとかの気持ちはなくゲームの実況配信を行っていたら、知らない間に有名になっていた",
            "有名事件を追う記者",
            "依頼されて事件の調査をし始めた。そこである動画配信者に辿り着く",
            "？　人物が三人では少なくないか。それも一人は記者なので語り手にしかならない",
            "記者は削除してもいい。ただ他に二人を第三者的に見られる、主人公の友人か、誰かが必要",
            "人間関係が同棲者とネット上でのみ完結している、とかの方が現代っぽいか",
            )


def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "有名と無名",
            "有名というのは多くの人に名が知れているということ",
            "言い換えれば有名であるとは知られてしまっている、ということ",
            "知られていることのメリットは人気をベースとした商売に活用できる",
            "デメリットは私生活に他人が侵食しやすい",
            "また有象無象の色々な人間が近づいてくる",
            "人生の防衛が難しくなる点か",
            "本当にすごい人は、無名なんだ。無名の中にこそ英雄はいる。そういう世界観を描く",
            "だからこそ、$yunaの存在は、無名の本当にすごいところを見せる為の存在である",
            )


def motif_note(w: World):
    return w.writer_note("モチーフメモ",
            "有名", "無名",
            "名前", "名刺",
            "炎上",
            "SNS",
            "メディア", "テレビ", "CM",
            "本を出す",
            "ポスター",
            "名刺",
            "顔出し",
            "ストーカー",
            "過保護な擁護者", "信者", "イエスマン", "宗教",
            "自分の番組", "youtube",
            "課金", "スパチャ", "ユーチューバー", "違法行為",
            "お金", "紙幣",
            "豪華な食事",
            "豪華な衣装", "広い部屋",
            "高級機材", "大型モニタ",
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            plot_note(w),
            chara_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

