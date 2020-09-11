# -*- coding: utf-8 -*-
'''
Stage: "コンビニ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def thought_of_famous(w: World):
    mume = w.get("mume")
    rin = w.get("rin")
    return w.scene('有名への思い',
            w.cmd.change_stage("Conveni"),
            w.cmd.change_time("evening"),
            mume.be("帰りにコンビニに立ち寄っている"),
            mume.do("店内の本棚には漫画誌が並ぶ"),
            mume.do("有名になってください、と言われたことがひっかかっている"),
            mume.do("弁当と飲み物を買ってレジに並ぶ"),
            rin.be("アジア系の顔立ちの店員がレジにいて、さばさばした素振りで客対応している"),
            mume.do("店員の名札に『$rin』と書かれている"),
            mume.think("それを見てなんと読むのだろうか考えている",
                "りん、なのか、はやし、なのか",
                "ずっと利用しているけれど未だに読み方が分からない",
                "それはひょっとしたら無名と大差ないのではないだろうか、と考えたり"),
            )

