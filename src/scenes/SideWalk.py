# -*- coding: utf-8 -*-
'''
Stage: "歩道"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def her_contact(w: World):
    return w.scene('彼女の連絡',
            w.plot_note("スマホにはこの半年ばかり付き合っている$mutsuから連絡"),
            )

