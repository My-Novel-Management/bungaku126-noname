# -*- coding: utf-8 -*-
'''
Stage: "郵便局"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def my_name(w: World):
    return w.scene('自分の名前',
            w.cmd.change_camera("mume"),
            w.cmd.change_stage("PostOffice"),
            w.cmd.change_time("afternoon"),
            w.plot_note("郵便局で番号を呼ばれ、記録郵便で小説を送る$mume"),
            )

