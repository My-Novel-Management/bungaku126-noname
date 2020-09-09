# -*- coding: utf-8 -*-
'''
Stage: "イタリアンバー"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def about_yuna_inbar(w: World):
    return w.scene('$yunaのことを聞く',
            w.cmd.change_stage("ItalianBar"),
            w.plot_note("バーで$yunaのことを聞く"),
            w.plot_note("よく一人で飲みに来ていて、数日前にも一人できたと"),
            w.plot_note("居場所は知らないと言われた"),
            w.plot_note("子役時代のことを知る人を当たる"),
            w.plot_note("ライターのツテを頼って引退した芸能マネージャーを知る"),
            w.plot_note("配達屋をやったりして日銭を稼いでいた男は子役時代について語る"),
            w.plot_note("有名であることがその人や周囲を壊していく姿を色々見てきたと言う"),
            w.plot_note("男は言う。有名っていうのは自分の人生を千切って投げ売りしているようなものだと"),
            w.plot_note("そこまでしても有名なんて大半が一時的なもので、後にはその名前をなんとかやりくりして生きていくしかないと"),
            w.plot_note("彼女は早く引退してよかったと語る"),
            w.plot_note("彼女の元マネージャーに連絡がついた"),
            )

