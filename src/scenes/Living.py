# -*- coding: utf-8 -*-
'''
Stage: "共用スペース"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def introduction_house(w: World):
    mume = w.get("mume")
    ishi = w.get("ishi")
    return w.scene("シェアハウスの紹介",
            w.cmd.change_stage("Living"),
            mume.come("入ってくる"),
            mume.do("共用スペースには備え付けのテーブルと椅子がある"),
            mume.do("左手側に今日の台所がある"),
            mume.do("テーブルの上にはもう一人の住人である$ishiの食べ終えたチップスの袋と缶ビールの空き缶が転がったまま"),
            mume.do("見かねて荷物を足元に置いて、それを黙って片付ける"),
            )


def ishi_girlfriend(w: World):
    mume = w.get("mume")
    ishi, yuna = w.get("ishi"), w.get("yuna")
    return w.scene("$ishiの彼女",
            w.cmd.change_stage("House"),
            w.plot_note("$ishiは芸人をしているらしいが、あまり外出することもなく、ゲームばかりして暮らしている"),
            w.plot_note("パシリに使われる新しい彼女の$yuna"),
            w.plot_note("前の彼女とは違い、あまり料理はしないタイプだと$mumeは思った"),
            mume.be(),
            mume.do("そこに玄関の鍵が開けられる音がして"),
            ishi.come("$Sが戻ってくる"),
            yuna.come("一緒に初めて見る女も入ってくる"),
            ishi.talk("あっ、わーりぃ"),
            ishi.do("$mumeが片付けているのを見て口では謝るが、全然悪びれてない"),
            ishi.do("ツーブロックで側面を綺麗に剃り上げ、立っている髪も五センチほどで整えられている"),
            ishi.do("白目が多くて右目がやや大きい"),
            ishi.do("顎の中央にだけ髭を生やしている"),
            ishi.do("タンクトップにジャケットを羽織って、下は七部丈"),
            ishi.do("自称芸人の$ishiだった"),
            yuna.do("付添の女は軽く頭を下げただけ"),
            yuna.do("化粧は薄く、ふわっとした帽子で目元を隠している"),
            yuna.do("髪は長く、肌は白い"),
            yuna.do("薄手のコートを着ている"),
            yuna.do("下はブラウスと白いストレートパンツ"),
            ishi.go("そのまま自分の部屋に入っていく"),
            yuna.go("女もついていく"),
            mume.think("$ishiは気にせずに女を部屋に連れ込む"),
            mume.think("それについてどうこう思わないが、また新しい彼女なのかセフレなのか、知らないけれど口論しなければ何でもいい"),
            mume.do("ゴミ袋を置いて、自室に入る"),
            )


