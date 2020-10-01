# -*- coding: utf-8 -*-
'''
Stage: "本屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def about_famous(w: World):
    mume = w.get("mume")
    woman = w.get("woman")
    return w.scene('有名とは',
            w.cmd.change_stage("BookShop"),
            mume.be("本屋を見ている"),
            woman.be("#書店員"),
            mume.do("駅に隣接する商業施設内に入っているチェーン店の本屋"),
            mume.do("平積みされているよく知る名前"),
            mume.do("そこには有名しか並んでいない"),
            mume.do("その中に○○賞受賞！という帯で、$full_akaiの名前があった"),
            mume.do("$akaiは中学のときの同級生で本なんて読むタイプじゃなかった"),
            mume.do("サッカーをやり、モデル事務所にスカウトされ、今では俳優をこなすマルチタレント"),
            mume.do("向こうは全然知らないだろうが、こちらは知っている"),
            mume.do("苦々しく思いながらもその本を購入する$S"),
            )

