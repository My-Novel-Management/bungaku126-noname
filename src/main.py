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
from scenes import AroundPH
from scenes import Bar
from scenes import BookShop
from scenes import Cafe
from scenes import Conveni
from scenes import Famires
from scenes import House
from scenes import IshiRoom
from scenes import ItalianBar
from scenes import Living
from scenes import MumeRoom
from scenes import PaperCompany
from scenes import ParentHouse
from scenes import PostOffice
from scenes import SideWalk
from scenes import TenantBuilding
from scenes import TowerManshion
from scenes import YunaHome


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
MAJOR, MINOR, MICRO = 0, 7, 0
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
RELEASED = (8, 31, 2020)


# Episodes
def ep_annoymous_man(w: World):
    return w.episode("無名な男",
            "主人公の名前は最後まで書かないこと",
            "自動的に「一人称」作品となる",
            w.plot_setup("$mumeは名前を呼ばれない、無名の男だった"),
            "郵便局：自分の名前",
            PostOffice.my_name(w),
            w.plot_setup("$mumeはイラストレーター志望の$mutsuと付き合っていた"),
            "歩道：彼女の連絡",
            SideWalk.her_contact(w),
            "本屋：有名とは",
            BookShop.about_famous(w),
            w.plot_setup("$mumeは$mutsuとよく「有名」について討論した"),
            "ファミレス：彼女",
            Famires.girlfriend(w),
            )

def ep_share_house(w: World):
    return w.episode("シェアハウス",
            w.plot_setup("$mumeはシェアハウスで$ishiと暮らしていた"),
            "シェアハウス：住人",
            House.resident(w),
            Living.introduction_house(w),
            w.plot_setup("$ishiは芸人で新しい彼女$yunaをよく連れ込んでいた"),
            w.plot_setup("$yunaは$ishiと付き合っている", about="yuna"),
            "シェアハウス：$ishiの彼女",
            Living.ishi_girlfriend(w),
            )

def ep_want_famous(w: World):
    return w.episode("有名になりたい",
            w.plot_setup("$mumeは色々とやって売れることを目指していた"),
            "自室：$mumeの夢",
            MumeRoom.his_dream(w),
            Cafe.sub_work(w),
            w.plot_setup("人気になりつつある$mutsu"),
            "自室：$mutsuの人気",
            MumeRoom.popular_mutsu(w).omit(),
            Conveni.thought_of_famous(w),
            w.plot_setup("$mumeはブログ「$theblog」を読んで、それでも有名に憧れを抱いていた"),
            "自室：あるブログ",
            MumeRoom.this_blog(w),
            w.plot_setup("$mutsuが公募に通り、プロの道が開ける"),
            "喫茶店：仕事とビッグニュース",
            Cafe.bignews(w),
            w.plot_setup("$mumeは$mutsuから別れると連絡を受ける"),
            "自室：$mutsuとの別れ",
            MumeRoom.depart_mutsu(w),
            )

def ep_nothing_any(w: World):
    return w.episode("何もない男",
            w.plot_setup("$mumeは再び大切なものを失った"),
            "自室：無駄な時間",
            MumeRoom.wasted_time(w),
            w.plot_setup("$mumeはいつも「無」になってしまう"),
            "実家跡地：何もない場所",
            ParentHouse.nothing_place(w),
            "跡地周辺：再開発地区",
            AroundPH.redevelop_area(w),
            )

def ep_catch_her(w: World):
    return w.episode("彼女を拾う",
            w.plot_turnpoint("$ishiが$yunaを捨て、有名タレントと付き合い始める"),
            w.plot_turnpoint("$ishiに捨てられる", about="yuna"),
            "シェアハウス：帰らない$ishi",
            House.nohome_ishi(w),
            w.plot_turnpoint("$mumeは捨てられた$yunaを拾う"),
            "シェアハウス：$yunaを助けた",
            House.help_yuna(w),
            )

def ep_yuna_parting(w: World):
    return w.episode("$yunaの別れ話",
            w.plot_develop("$yunaと$ishiが別れた事情を聞く"),
            "シェアハウス：$yunaと話す",
            House.talk_with_yuna(w),
            w.plot_develop("$mumeは$ishiの気持ちも分からないではなかった"),
            "シェアハウス：$yunaと$ishi",
            House.yuna_and_ishi(w),
            w.plot_develop("$mumeは口論の内容を聞く"),
            w.plot_develop("$ishiが戻ってくるまでこの部屋を使えばいいと提案した"),
            "シェアハウス：$mumeの提案",
            House.mume_suggestion(w),
            )

def ep_yuna_life(w: World):
    return w.episode("$yunaの暮らし",
            w.plot_develop("$yunaと$mumeはシェアハウスで暮らし始める"),
            "シェアハウス：$yunaの何もない一日",
            House.yunas_nothing_day(w),
            )

def ep_streamer(w: World):
    return w.episode("ゲーム実況者",
            w.plot_develop("$mumeは$yunaにゲーム実況配信のやり方を教えた"),
            "石脇の部屋：$yunaとゲーム",
            IshiRoom.yuna_and_game(w),
            w.plot_develop("$yunaはゲーム配信を始める"),
            "石脇の部屋：$yunaと配信",
            IshiRoom.yunas_streaming(w),
            w.plot_develop("$yunaはゲームを楽しむようになり、日々に笑顔が戻る"),
            )

def ep_dontwork_mume(w: World):
    return w.episode("うまくいかない$mume",
            w.plot_develop("$mumeは小説の才能がないと言われる"),
            "自室：小説を書く",
            MumeRoom.writing_novels(w),
            "喫茶店：才能がない",
            Cafe.nohas_talent(w),
            )

def ep_popular_streamer(w: World):
    return w.episode("人気実況者",
            w.plot_develop("$yunaは人気実況者となる"),
            "石脇の部屋：人気配信者",
            IshiRoom.famous_streamer(w),
            w.plot_develop("$mumeは実況で人気になることについて考えた"),
            "自室：実況配信の研究",
            MumeRoom.researching_streamer(w),
            )

def ep_lose_days(w: World):
    return w.episode("失敗の日々",
            w.plot_develop("一方$mumeは相変わらず成功から遠ざかっていた"),
            "自室：not found",
            MumeRoom.notfound_myname(w),
            w.plot_develop("$mumeは公募に出していた小説が次々落選する"),
            "自室：SNSの言葉",
            MumeRoom.sns_words(w),
            w.plot_develop("$mumeは小説を諦めた"),
            "自室：デリート",
            MumeRoom.deleting_novels(w),
            )

def ep_her_name(w: World):
    return w.episode("彼女の名前",
            w.plot_develop("ある日、$yunaから実況のコメントに恐い人が出ると相談される"),
            "シェアハウス：$yunaの相談",
            House.yuna_need_advice(w),
            w.plot_turnpoint("$yunaがかつて有名子役だったことがバレる"),
            )

def ep_losther(w: World):
    return w.episode("$yunaの失踪",
            w.plot_develop("$yunaはシェアハウスに戻ってこなくなった"),
            "シェアハウス：姿を消す彼女",
            House.vanishing_yuna(w),
            w.plot_develop("シェアハウスのオーナーから$ishiから入金がないが知らないかと連絡がある"),
            w.plot_turnpoint("$mumeに落選した公募の主催出版社の編集から一度会いませんかと連絡がある"),
            "自室：出版社からの連絡",
            MumeRoom.contact_from_publisher(w),
            )

def ep_selection(w: World):
    return w.episode("$mumeの選択",
            w.plot_develop("$mumeは出版社の人間から声をかけてもらい会う予定になっていた"),
            "喫茶店：才能の提案",
            Cafe.support_talent(w),
            w.plot_turnpoint("$mumeは$yunaも同じ出版社からブログの書籍化の話を持ちかけられていたと知る"),
            "自室：$yunaのブログ",
            MumeRoom.yuna_blog(w),
            w.plot_resolve("$mumeは触れようとしなかった彼女の過去と、過去の繋がりを調べる"),
            "シェアハウス：$ishiの帰還",
            House.comeback_ishi(w),
            )

def ep_yuna_info(w: World):
    return w.episode("$yunaの情報",
            w.plot_resolve("$yunaの過去について知る人間を巡って、彼女の居場所を探す"),
            "イタリアンバー：$yunaのことを",
            ItalianBar.about_yuna_inbar(w),
            )

def ep_yuna_old_manager(w: World):
    return w.episode("$yunaの元マネージャー",
            w.plot_resolve("$yunaの元マネージャーに出会う"),
            "元マネージャー会社：元マネージャーの話",
            PaperCompany.talk_manager(w),
            )

def ep_yuna_mother(w: World):
    return w.episode("$yunaの母親",
            w.plot_resolve("$yunaの母親に出会う"),
            "飲み屋：彼女の母親",
            Bar.yuna_mother(w),
            )

def ep_ishiwaki(w: World):
    return w.episode("$ishiの情報",
            w.plot_resolve("$ishiから$yunaの居場所を教わる"),
            "シェアハウス：出ていく$ishi",
            House.goout_ishi(w),
            )

def ep_yuna_home(w: World):
    return w.episode("$yunaの居場所",
            w.plot_resolve("初めて訪れた$yunaの住まいは全てが揃った高級住宅だった"),
            "タワーマンション：彼女の居場所",
            TowerManshion.yuna_place(w),
            )

def ep_yuna_history(w: World):
    return w.episode("$yunaの人生",
            w.plot_resolve("$yunaは$mumeに自分の子役時代のことを語る"),
            "$yunaの部屋：彼女の話",
            YunaHome.her_talk(w),
            "同：$yunaの過去",
            YunaHome.her_backhistory(w),
            w.plot_resolve("両親が芸能関係者だったことから、物心ついた頃には既に片足を芸能界に突っ込んでいた"),
            w.plot_resolve("赤ん坊でテレビデビューし、その後順調に子役として育つ"),
            w.plot_resolve("連続テレビドラマで人気になり、子役として毎日テレビに出るという忙しさになる"),
            w.plot_resolve("両親はプロデュース専業に鞍替えし、自分の事務所を設立し、グッズ販売なども手がけるようになった"),
            w.plot_resolve("$yunaは普通の生活が送りたかったが小学校はまともに行けず、中学は通信教育だった"),
            w.plot_resolve("芸能界を引退したまま復帰する気のない娘と、残った会社を巡り、両親が対立。離婚調停になった"),
            w.plot_resolve("高校には入らず、カナダに留学をする"),
            w.plot_resolve("日本に帰ってきたのは二十歳を過ぎてからで、その頃には街からかつての自分の名前は消えていた"),
            )

def ep_hisname(w: World):
    return w.episode("$yunaは彼の名を呼んだ",
            w.plot_resolve("有名というのは自分の人生を売り渡す行為だと$yunaは言う"),
            w.plot_resolve("無名なのは人生がないのと同じじゃないかと$mumeは言う"),
            w.plot_resolve("$yunaは$mumeの人生が無意味でも無駄でも空虚でもないと反論する"),
            w.plot_resolve("$mumeは真面目で面倒見がよく、他人のことに色々と気付ける人間で"),
            w.plot_resolve("$yunaは$mumeによって助けられた"),
            w.plot_resolve("この世界には無名の人の方がずっと多く、そういう無名の人によって世界は支えられている"),
            w.plot_resolve("日々の生活では名前じゃなく、人の繋がりによって支えられていると"),
            w.plot_resolve("いつ折れてもおかしくなかった自分を支えたのは、$mumeだったと"),
            w.plot_resolve("$yunaは$mumeにプロポーズする", about="yuna"),
            "実家跡地：プロポーズ",
            ParentHouse.proposed(w),
            w.plot_resolve("$mumeは$yunaに「名前」を呼ばれた"),
            w.plot_resolve("その時本当は「無名」じゃなかったと分かった"),
            )


def ch_main(w: World):
    return w.chapter('main',
            ep_annoymous_man(w),
            ep_share_house(w),
            ep_want_famous(w),
            ep_nothing_any(w),
            ep_catch_her(w),
            ep_yuna_parting(w),
            ep_yuna_life(w),
            ep_streamer(w),
            ep_dontwork_mume(w),
            ep_popular_streamer(w),
            ep_lose_days(w),
            ep_her_name(w),
            ep_losther(w),
            ep_selection(w),
            ep_yuna_info(w),
            ep_yuna_old_manager(w),
            ep_yuna_mother(w),
            ep_ishiwaki(w),
            ep_yuna_home(w),
            ep_yuna_history(w),
            ep_hisname(w),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            "現代に限らず、名前というのはその人を代表する言葉である",
            "ネットの普及、SNSの広がりによって、誰でもがある瞬間に「有名」になれる時代",
            "多くの人が功名心を刺激され、日夜何かしらで有名になろう、人気を得てやろうと必死になっている",
            "またその「知名度」が経済に直結するようになり、他人の功績を奪ってでも有名になろうとする輩も増えている",
            "かつては自分の「真名」を隠すために「源氏名」のようなもの「通り名」のようなものを使って生活していた",
            "真名を知られれば他人にコントロールされてしまうという迷信めいたことが信じられていた名残だが、",
            "情報化社会になり「個人情報」の一つとしての「名前」も本来ならばもっと大切にされなければならない",
            "しかし一旦事件の加害者や被害者になると、それはまたたくまに世間に露呈する",
            "隠すことが困難な時代になってしまっている",
            "だからこそ今「名前」というものをもっと考える必要があるんじゃないだろうか",
            "名前は人を幸福にもするが不幸にもする",
            "その名を、特に「有名」に対する「無名」をめぐる、物語である",
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
            "大学の事務員をしている父と、コンビニにパートタイムで勤務する母の下に生まれる",
            "兄弟はよくできる兄が一人",
            "三つ年上の兄とはいつも比べられながら育った",
            "父の書斎には本が沢山あり、友達に囲まれていつも外で遊び回っていた兄とは違い、",
            "よく本を開いては文字を追っていた",
            "あまり喋らない子で、よくしゃべる母と兄とは違い、父似なんだと親戚のおばさんたちは言っていた",
            "父は物静かな人で、あまり家族サービスなどせず、自分の時間を大切に使っている人だった",
            "小学校に入ると、周囲から孤立しがちになり、一度そのことを父に質問してみたことがあった",
            "父は「小学校時代に同じクラスだった人間は、今ほとんど周囲にいない。それを友達と呼ぶなら、友達というのはその程度のものだ」と語った",
            "子ども心にそれはよく響き、孤立してもあまり悲しいことはなくなった",
            "ただ中学、高校と、多少話せる同級生がいないと困ることが分かり、",
            "質問などはよくするようになった",
            "それをきっかけに同級生からも話しかけられるようになる",
            "ただ親友といった類の人間はできなかった",
            "大学に入り、将来を考えたときに、一人でも可能な仕事というのを列挙した",
            "その多くが創作関連だった",
            "あるいは職人と呼ばれる技術者の領域",
            "$mumeは器用な方ではなかったから、技術者よりはまだ創作関連の技術を磨いた方がいいと考え、",
            "大学に通いながら文章教室の通信講座などを受けた",
            "大学を出るとアルバイトをしながら音楽をやったり、執筆したり、デジタルアートに挑戦したりした",
            "バイトは飲食業が多かった",
            "そこで簡単な料理を覚えたりした",
            "その頃に付き合った女性もいた。バイトの同僚で、新入生歓迎会などがあり、意気投合したからだ",
            "けれど創作に打ち込んでいた彼からすぐに離れていってしまった",
            "彼女はもっと人生に「遊び」が欲しかったのだ。日々楽しければいいじゃないか、と",
            "人生の目標とかどうでもいい、という人種はどうも合わなかった",
            "そのうちに体を壊し、半年入退院を繰り返した",
            "食事などで無理をしてお金を削ったのが悪かった",
            "バイトも休みがちになり、首になる",
            "現在は小説家を目指して小説を書いては公募に出したり、ネットに掲載したりしているが、",
            "全く芽が出ずに自分の才能に失望している日々を送っている",
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
            "町工場に生まれる",
            "五人兄弟の末っ子として兄二人と姉二人にいじめられ育つ",
            "母親が関西の人で、家の中では標準語と関西弁が混在していた為か、",
            "中途半端な関西弁混じりの標準語を話すようになってしまった",
            "小学生の頃から何かといじられキャラで、それを「人気者」と勘違いしたのが$ishiの人生を大きく狂わせた",
            "笑われる才能に恵まれていると思い、彼はお笑いの道を目指す",
            "高校を出るとお笑い学校に入り、バイトをしつつ、お笑いの勉強をする",
            "しかしそこでは自分よりもずっと才能のある人たち、既に名のある二世や三世、",
            "コネもったやつに金持ちと、敵が多すぎて挫折する",
            "お笑い学校を辞め、一人で路上ライブなどしていたが全く人気が出ず、",
            "学生時代の先輩に泣きついて、なんとか飲み屋で営業しつつ働かせてもらったりした",
            "そんなある日、テレビのプロデューサーが酒に酔った勢いで「出てみる？」と言ってしまい、",
            "そこから人生が更に狂う",
            "仕方なく出させてもらったのは、名のない芸人ばかり百人が揃い、自分の名前を売る為に生き残りをかけて様々なアトラクションをクリアするという番組",
            "芸こそ能力がなかったが、身体能力と器用さはあり、なんとかファイナリストになった",
            "$ishiはそこからお笑いの営業も少し回してもらえるようになった",
            "小さな事務所に何とか入らせてもらい、営業をかけつつ、有名になるのを目指した",
            "けれど組んだコンビはすぐ解散し（$ishiのだらしなさから）、",
            "すぐ女優やタレントに手を出すと悪評が立ってしまった（事実だが）",
            "事務所もやめ、どうしようもなくなっていた時に、$yunaと出会う",
            "地味だが顔立ちの整った美人の彼女を得たと気分がよくなっていた",
            "また金づるとしても優秀で、文句も言わないし、他の女みたいに有名になれとか、仕事しろとかも言わなかった",
            "楽しい日々を送っていられればいい、という気分になったが、一方で、有名になっていくやつらに嫉妬していた",
            "特に自分と同期だった芸人がピンでテレビに出始めた時、また芸人としてやりたいという思いが強くなり、",
            "プロデューサーにかけあう",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            "舞台のシェアハウスはカフェだったものを改装してオーナーが貸し出しているものにする",
            "割といい感じのオーナーだが、独り者でちょっと変わった部分もある",
            "高円寺あたりの場所で",
            "場所明記はしない？",
            "田端は山手線で一番無名な駅らしい",
            "イメージする場所は田端にする",
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

