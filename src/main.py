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
MAJOR, MINOR, MICRO = 0, 3, 0
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
def ep_anonymous(w: World):
    return w.episode("無名",
            w.plot_setup("無名の男がいた"),
            w.plot_setup("$mumeは色々なことをして有名になろうとしていたが、全て失敗していた"),
            w.plot_note("作家だけじゃない、音楽も、絵も、ゲームやシナリオ、果ては動画制作まで、",
                "いろいろとチャレンジしたが全く芽が出なかった"),
            w.plot_note("$mumeは現在は作家に挑戦していたが、公募もネットでもぱっとせず、苦悩していた"),
            w.plot_note("ある日、SNSですり寄っていたプロ作家から、才能がないと強いダメ出しを受けてしまい、酷く落ち込む"),
            w.plot_setup("$mumeは付き合っていた彼女($mutsu)に愛想をつかされ、失恋した"),
            w.plot_note("$mutsuが応募していたイラストコンテストで入賞したときに、$mumeは素直に喜べなかった"),
            w.plot_note("それをきっかけに徐々に距離を離れ、やがて$mutsuから一方的に別れると$lineがきて、関係が終わった"),
            "いつも必要以上に追いかけない$mumeは、チャンスを逃してしまう",
            "あと一歩、を出さない。ここも彼女に声をかけていれば、理由をきいていれば、復縁はあったかも知れない",
            w.plot_setup("$mumeとシェアハウスをして暮らしていた芸人$ishiがいた"),
            w.plot_note("$ishiは芸人をしていて、ほとんど$mumeとは交流がなかったが、",
                "時折ネタの相談にきたり、知りたいことを聞きに来たり、といった程度の関係はあった"),
            w.plot_note("たまに仕事で気持ちよくなって飲んで帰ってきた時、$mumeにお土産をくれたりした（自慢話つき）"),
            w.plot_note("$mumeは相手の話をなんだかんだ意見せずに聞いてしまうので、そのあたりは人として$ishiは気に入っていた"),
            w.plot_setup("$ishiには半同棲の彼女$yunaがいた", about="yuna"),
            w.plot_note("$ishiを玄関前で待っていた女性（$yuna）と出会う$mume",
                "これが初対面"),
            w.plot_setup("$ishiは彼女を部屋に連れ込み、ほぼ半同棲生活だった"),
            w.plot_turnpoint("$yunaは$ishiにふられてしまう", about="yuna"),
            w.plot_turnpoint("$mumeは家の前で泣きつかれていた$yunaを拾った"),
            )

def ep_alternate(w: World):
    return w.episode("代替",
            w.plot_develop("$mumeは出ていった$ishiが帰ってくるまでシェアハウスで暮せばいいと提案する"),
            w.plot_develop("$mumeと$yunaの同棲のような生活が始まる"),
            w.plot_develop("$yunaは自発性がなく、一日ぼーっとしていた"),
            w.plot_develop("掃除していて$ishiが楽しそうにやっていた人殺しのゲームをやってみるが、恐くて一人ではできなかった", about="yuna"),
            w.plot_turnpoint("$yunaは$ishiがやっていたゲーム実況をしてみたいと言うので、$mumeが準備をして配信方法を教えてやった"),
            w.plot_develop("$yunaはゲーム実況配信をし始める"),
            w.plot_note("$yunaは視聴者とのやり取りが面白く、どんどん人気が高まっていく"),
            w.plot_develop("$yunaは人気実況者になった"),
            w.plot_develop("$mumeも彼女を真似て実況配信してみたが、全然人気は出なかった"),
            w.plot_turnpoint("コメントでリアルの$yunaを知ってそうな人が現れて恐くなった", about="yuna"),
            w.plot_turnpoint("$mumeは$yunaと実況の中の人を交代し、人気実況者としての生活を始めることになった"),
            w.plot_note("$theblogというブログを見つけて、それを読む$mume"),
            w.plot_note("そこには元子役で芸能界でメンタルを傷つけられてさっさと逃げ出した、ある女性の独白が書かれていた"),
            "これが$yunaの過去の姿。基本的に最後まで読者以外はそれに気づけない作りにしておくが、ちょくちょく引用したりするようになる",
            w.plot_note("有名になりたい、と色々がんばっていた日常の方がずっと楽しく、充実していたこと"),
            w.plot_note("いざ有名になっても制約が多く、また自分ではない自分が独り歩きしてしまって、",
                "それが悪さをしたりする。誰かに傷つけられたりする"),
            )

def ep_famous(w: World):
    return w.episode("有名",
            w.plot_develop("$mumeは人気の彼女になりきろうと必死に彼女のことを勉強する"),
            w.plot_develop("ストーカー気質なコメントをする人物を炙り出そうと考える"),
            w.plot_develop("$ishiから連絡が入る", about="yuna"),
            w.plot_develop("$ishiと久しぶりにデートする、と$mumeに報告する", about="yuna"),
            w.plot_develop("$ishiには既に別の女がいると知る（その女からの連絡）", about="yuna"),
            w.plot_develop("彼女は更に人気となる"),
            w.plot_develop("男は彼女の中の人として人気になる"),
            w.plot_note("徐々に酷いコメントが目につくようになる"),
            w.plot_turnpoint("中の人が男だとばれる"),
            )

def ep_lostname(w: World):
    return w.episode('喪失',
            w.plot_resolve("炎上し、彼女のアカウントだけでなく、男のアカウントも全て削除する"),
            w.plot_note("全てのネットの痕跡を削除したはずなのに、$lineにメッセージがどんどんやってくる"),
            w.plot_note("だがそこに書かれているのは偽物という罵倒"),
            w.plot_note("自分の本名は誰も特定していない。彼女の本名だけが書き連ねられている"),
            w.plot_note("その流れが$theblogの主の騒動を思い起こさせた"),
            w.plot_note("主は最後に死をほのめかして、それ以降更新はされていない"),
            w.plot_note("そのブログサービスが終了することが決まり、彼女のブログも消滅することが分かった"),
            w.plot_note("$mumeは引っ越しを決意する"),
            w.plot_resolve("ネットストーカーの犯人は元彼氏だった", about="yuna"),
            w.plot_note("$yunaが部屋の契約をどうするのか$ishiに相談に行くと、彼は彼女に捨てられ、すがりついてきた"),
            w.plot_note("けれど$yunaは人気にすりよって固執している$ishiが、炎上しているけど有名になってしまった自分の名前に執着しているだけだと見抜き、別れを選択する"),
            w.plot_resolve("元彼氏は彼女の人気に激しく嫉妬していた", about="yuna"),
            w.plot_note("$mumeは全てを失い、自分の才能にも絶望し、名前も失った"),
            w.plot_note("$mumeは$yunaに今後どうするのかと尋ねる"),
            w.plot_resolve("何もなくても一緒にいたいと思った$yunaは彼の名を呼びプロポーズをした", about="yuna"),
            w.plot_note("$yunaは$mumeの不器用だけどそこにある優しさと弱さが愛おしくなり、自分に大切な人間が誰なのか気づいた"),
            w.plot_resolve("$mumeは彼女にプロポーズされ、そこで初めて自分の名を呼ばれた"),
            )


def ch_main(w: World):
    return w.chapter('main',
            ep_anonymous(w),
            ep_alternate(w),
            ep_famous(w),
            ep_lostname(w),
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

def about_charas(w: World):
    return (chara_mume(w),
            chara_yuna(w),
            chara_ishi(w),
            )

def chara_mume(w: World):
    return w.chara_note("$mumeの履歴書",
            )

def chara_yuna(w: World):
    return w.chara_note("$yunaの履歴書",
            "音楽プロデューサーと、芸能事務所の事務をしている女性の下に生まれる",
            "両親ともに顔の偏差値は高くなかったが、何故か$yunaは小さい頃から可愛かった",
            "両親は子役としてデビューさせる",
            "それにはコネを使ったが、それ以上に$yunaが才能に満ちていて、他の子役よりも笑顔や泣き顔の対応が素晴らしかったことが、彼女の子役人生を形作った",
            "子役として成功した$yuna",
            "けれどそれは両親も友人も周囲の人間をどんどん不幸にしていった",
            "街を歩いていてもみんなが自分を見てくる",
            "学校ではとりまきが生まれ、ストーカーも嫌がらせも嫉妬もいじめも、いろいろあった",
            "中学では不登校になり、通信教育でなんとか中卒の資格を得て、もう学校には行かないという選択をした",
            "高校にはいかずにカナダに留学させてもらう",
            "芸能界からは完全に身を引いたが、未だに父を通して話がある",
            "母親はノイローゼになり、病院を行ったり来たりしている",
            "留学から帰ってきた$yunaはまだ自分の名前があることに恐れたが、顔を見て気づく人はいなくなっていた",
            "$yunaのことを知らないままナンパしてきた芸人の$ishiと出会う",
            "彼はいつも$yunaを元気にしてくれて、それだけでよかった",
            "けれど野心が強く、彼は絶対に一番の人気者になってやると言っていた",
            "$yunaは留学している頃にブログを書き残していてるが、そのことは既に忘れ去っていた",
            "$ishiと付き合い始め、料理を覚えたりもした",
            "$ishiが引っ越してシェアハウスで暮らしている$mumeと出会う",
            "$ishiはタレントの彼女ができる",
            "$ishiはその彼女と、彼女の親であるプロデューサーに取り入ろうと必死になっていた",
            "やがて$yunaから離れ、$yunaは捨てられたが、どうしていいかわからなくなっていた",
            "そこを$mumeに拾われた",
            )

def chara_ishi(w: World):
    return w.chara_note("$ishiの履歴書",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            "舞台のシェアハウスはカフェだったものを改装してオーナーが貸し出しているものにする",
            "割といい感じのオーナーだが、独り者でちょっと変わった部分もある",
            "高円寺あたりの場所で",
            "場所明記はしない？",
            )

def about_materials(w: World):
    return (mate_sharehouse(w),
            )

def mate_sharehouse(w: World):
    return w.writer_note("シェアハウス",
            "普通のアパートの各部屋をシェアハウスとして貸し出しているところもある",
            "初期費用が多少安いだけで家賃は変わらなかったり",
            "普通に共益費や光熱費などもかかる",
            "こみこみ物件もある",
            "そのシェアハウスにより条件が設定されている（年齢制限や女性限定など）",
            "最低入居期間の設定など",
            "ルームシェアタイプもある（女性限定など）",
            "名前は「シェアハウス○○」とか「○○ハウス」が多い",
            "国際交流型のものもある。インターナショナルなどと銘打ってある",
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
            "名前にこだわるのは「嫉妬心」から",
            "どう「嫉妬」を描くか、にかかってくる",
            "色々な嫉妬の形があって、でも根源は「自分にないもの」に対する欲求",
            "それは憧れという形を取っているかも知れない",
            "恋愛もまた憧れと嫉妬の間かも知れない",
            "名前のこと、有名になりたい、というのも結局は自分が知っている人たちによく思われたいというだけかも",
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
            *about_charas(w),
            stage_note(w),
            *about_materials(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

