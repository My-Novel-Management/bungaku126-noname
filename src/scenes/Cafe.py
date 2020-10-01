# -*- coding: utf-8 -*-
'''
Stage: "喫茶店"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sub_work(w: World):
    mume = w.get("mume")
    taka = w.get("taka")
    return w.scene("$mumeの収入源",
            w.cmd.change_stage("Cafe"),
            w.cmd.change_time("afternoon"),
            w.cmd.change_date("MeetingDay1"),
            mume.be("駅から少し歩いたところにある喫茶店（コメダ珈琲）"),
            mume.do("チェーン店で安定した味", "店内はそこそこ混んでいる"),
            taka.be("対面に座る$S"),
            taka.do("眼鏡とスーツ姿", "スマホを常にいじっている"),
            taka.talk("大丈夫すね", "じゃあこれで"),
            taka.do("校正済の原稿を受け取る$S"),
            taka.talk("そういえば小説、最近書いてますか？"),
            mume.talk("ええ、一応"),
            taka.talk("最近はみんなコレで書くんですってね"),
            taka.do("スマホを見せる"),
            taka.talk("この春にうちに入ってきた新人も最初は全然パソコン使えなくて",
                "文字なんてこっちで打ったほうが早いっつうんですから"),
            taka.talk("結構読みやすくて好きな文章なんですけど、小説の方じゃ結果出ないんですか？"),
            mume.talk("はあ、まあ"),
            taka.talk("最近はウェブ小説が流行ってるみたいですが、投稿も手軽で、小説家未満の素人もいっぱいいるんでしょうね",
                "誰もが印税生活を夢に見る",
                "けど実際新人作家の売上なんて知れてるし副業作家のほうがずっと多くて、現実知ると夢のない業界ですよ",
                "そう思いません？"),
            mume.do("何とも言えない"),
            mume.do("アイスコーヒーをちびちびやる"),
            taka.do("痩せているのに生クリームがいっぱいのったパンケーキを既に半分食べ終えている"),
            taka.talk("いつか有名になって$meのことインタビューとかで話して下さいよ"),
            mume.do("苦笑するだけ"),
            )


def bignews(w: World):
    mume = w.get("mume")
    taka = w.get("taka")
    return w.scene('$mutsuのビッグニュース',
            w.cmd.change_stage("Cafe"),
            w.plot_note("$mutsuから話したいことがあると連絡がある"),
            w.plot_note("仕事でその日は会えなかった"),
            w.plot_note("ネットのコンテストで優秀賞に$mutsuの名前を見つける"),
            w.plot_note("おめでとうと送るが、内心ではどうして自分は駄目なのだろうとばかり"),
            w.plot_note("互いの時間がちぐはぐでなかなか出会えない"),
            mume.be("仕事の打ち合わせにきている"),
            taka.be("$Sは資料を見ながら「これでいきましょう」と"),
            taka.talk("そういえばご存知ですよね、$mutsuさん",
                "うちではないんですけど、今度ゲームのデザインするそうですね"),
            mume.talk("え？"),
            mume.do("寝耳に水な情報に戸惑う"),
            taka.talk("なかなか可愛い絵でうちでも使えたらって思ってたんですけど、売れちゃうと厳しくなっちゃうなあ"),
            # TODO
            )


def nohas_talent(w: World):
    mume = w.get("mume")
    return w.scene("才能がない",
            w.cmd.change_stage("Cafe"),
            w.plot_note("ライターの仕事先の人から「あれってどういう話だったんですか？」と言われる"),
            w.plot_note("ウェブサイトで読んでみたけれど面白くなかったと"),
            w.plot_note("普通の文章は書けても小説は書けないんじゃないか、と言われてしまう"),
            )


def support_talent(w: World):
    mume = w.get("mume")
    return w.scene("才能の提案",
            w.cmd.change_stage("Cafe"),
            w.plot_note("$mumeは編集者と出会う"),
            w.plot_note("一次選考で落選した作品を見て、書き直してキャラ文芸の方の公募に出してみないかと誘われる"),
            w.plot_note("$mumeは自分の作品のどこがよかったのか聞いたが、編集者はうまく言えない"),
            w.plot_note("話を考えさせてほしいと、一旦持ち帰ることにした"),
            )
