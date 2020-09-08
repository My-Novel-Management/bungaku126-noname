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
    return w.scene('有名とは',
            )

