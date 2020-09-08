# -*- coding: utf-8 -*-
'''
Stage: "$ishiの部屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def yuna_and_game(w: World):
    return w.scene("$yunaとゲーム",
            w.plot_note("$yunaは子どもの頃に全然ゲームとかで遊ばなかったと言った"),
            w.plot_note("実際操作すらおぼつかなく、まともにゲームができずに実況どころではなかった"),
            w.plot_note("それでも感がよく、すぐに操作や配信などに慣れていく"),
            w.plot_note("$ishiが持っていたのはどれもFPSやTPSといった３Ｄゲームだった"),
            w.plot_note("$yunaにやりたいものを聞くとホラーゲームだった"),
            w.plot_note("次々に遅い来るゾンビを倒す"),
            w.plot_note("操作に癖があり、なかなか楽しめない"),
            w.plot_note("それでも一日、ほうっておいたらご飯も食べずにずっと$yunaはゲームをやっていた"),
            w.plot_note("そののめり込みようは異常に映った"),
            )


def yunas_streaming(w: World):
    return w.scene("$yunaと実況配信",
            w.plot_note("ある程度ゲーム操作になれたらそれを配信してみたいと$yunaが言い出す"),
            w.plot_note("$mumeは配信することで不必要に他人と繋がり嫌なことがあるかもしれないと忠告はする"),
            w.plot_note("顔出しもせず、声も変えることにした"),
            w.plot_note("セッティングはしてやり、配信が始まる"),
            w.plot_note("全然人が集まらないのを見て、$mumeは安心した"),
            w.plot_note("一週間もすると$mumeが手伝わなくても基本的な配信ができるようになった"),
            w.plot_note("$yunaが一人で配信して遊べるようになり、$mumeにも時間が生まれた"),
            )


def famous_streamer(w: World):
    return w.scene("人気配信者",
            w.plot_note("一月もすると$yunaの配信には人が集まるようになっていた"),
            w.plot_note("傍で見ていると彼女は人を喜ばせることをよく理解しているようで、それも無意識にそのリアクションをしているようだった"),
            w.plot_note("$mumeは$yunaにそのことについて聞いてみた"),
            w.plot_note("彼女は別に意識をしていないと答えた"),
            w.plot_note("$mumeは徐々に$yunaの人気が羨ましくなってきて、あまり部屋に入らないようになった"),
            )
