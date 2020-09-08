# -*- coding: utf-8 -*-
'''
Stage: "$yunaの部屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def her_talk(w: World):
    return w.scene('$yunaの話',
            )



def her_backhistory(w: World):
    return w.scene("$yunaの過去",
            )
