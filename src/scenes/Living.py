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
            # TODO
            )
