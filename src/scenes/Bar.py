# -*- coding: utf-8 -*-
'''
Stage: "母親の飲み屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def yuna_mother(w: World):
    return w.scene('彼女の母親',
            w.cmd.change_stage("Bar"),
            w.plot_note("彼女の母親は飲み屋をやっていた"),
            w.plot_note("金を色々使い込んで、借金をして、なんとか店をやっていた"),
            w.plot_note("彼女とは全然似ていないようで、料理ができないとか似ている部分もあった"),
            w.plot_note("有名子役の母親という立場になったのに、あの子には可愛そうなことをしたと言う"),
            w.plot_note("全然連絡が取れず、今も謝りたい、会いたいと言い出す"),
            w.plot_note("$mumeは居場所が分かったら連絡すると約束をした"),
            )

