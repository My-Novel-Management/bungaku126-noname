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
def bignews(w: World):
    return w.scene('$mutsuのビッグニュース',
            w.cmd.change_stage("Cafe"),
            w.plot_note("$mutsuから話したいことがあると連絡がある"),
            w.plot_note("仕事でその日は会えなかった"),
            w.plot_note("ネットのコンテストで優秀賞に$mutsuの名前を見つける"),
            w.plot_note("おめでとうと送るが、内心ではどうして自分は駄目なのだろうとばかり"),
            w.plot_note("互いの時間がちぐはぐでなかなか出会えない"),
            )


def nohas_talent(w: World):
    return w.scene("才能がない",
            w.cmd.change_stage("Cafe"),
            w.plot_note("ライターの仕事先の人から「あれってどういう話だったんですか？」と言われる"),
            w.plot_note("ウェブサイトで読んでみたけれど面白くなかったと"),
            w.plot_note("普通の文章は書けても小説は書けないんじゃないか、と言われてしまう"),
            )


def support_talent(w: World):
    return w.scene("才能の提案",
            w.cmd.change_stage("Cafe"),
            w.plot_note("$mumeは編集者と出会う"),
            w.plot_note("一次選考で落選した作品を見て、書き直してキャラ文芸の方の公募に出してみないかと誘われる"),
            w.plot_note("$mumeは自分の作品のどこがよかったのか聞いたが、編集者はうまく言えない"),
            w.plot_note("話を考えさせてほしいと、一旦持ち帰ることにした"),
            )
