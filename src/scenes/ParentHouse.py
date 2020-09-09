# -*- coding: utf-8 -*-
'''
Stage: "実家跡地"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def nothing_place(w: World):
    return w.scene('何もない場所',
            w.cmd.change_stage("ParentHouse"),
            w.plot_note("落ち込んだ時に$mumeはいつも自分の始まりの場所にやってくる"),
            w.plot_note("$mumeの実家は既に整地され、タワーマンション建設予定地になっている"),
            )


def proposed(w: World):
    return w.scene("プロポーズ",
            w.cmd.change_stage("ParentHouse"),
            )
