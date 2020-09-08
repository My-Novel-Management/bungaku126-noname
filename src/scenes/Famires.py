# -*- coding: utf-8 -*-
'''
Stage: "ファミレス"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def girlfriend(w: World):
    return w.scene('$mumeの彼女',
            w.plot_note("帰りにファミレスで合流して、互いの進捗を話し合う"),
            w.plot_note("有名になりたい、と話す$mumeと、いい作品を作りたいという$mutsu"),
            w.plot_note("$mutsuは自分が有名になることは「ついで」だと言った。作品の方がずっと大事だと"),
            w.plot_note("$mutsuはイラストレーターでプロを目指して活動していた"),
            )

