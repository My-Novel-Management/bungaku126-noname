# -*- coding: utf-8 -*-
'''
Stage: "タワーマンション"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def yuna_place(w: World):
    return w.scene('$yunaの居場所',
            w.plot_note("それは$mumeが生まれた場所の、再開発地域に新しく建ったタワーマンションの一つだった"),
            w.plot_note("$mumeはインタフォンで$yunaのことを確認して、そこに入る"),
            w.plot_note("$yunaは$mumeを出迎えてくれたが、やつれていた"),
            )

