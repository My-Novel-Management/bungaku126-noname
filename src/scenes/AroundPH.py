# -*- coding: utf-8 -*-
'''
Stage: "実家跡地周辺"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def redevelop_area(w: World):
    return w.scene('再開発エリア',
            w.cmd.change_stage("AroundPH"),
            w.plot_note("周囲も開発が進み、古い店舗はどんどん看板を下ろしていく"),
            w.plot_note("人間だけでなく、街も有名なものたちに無名が虐げられていた"),
            w.plot_note("おまけに財布には金が数百円しか残っていなかった"),
            )

