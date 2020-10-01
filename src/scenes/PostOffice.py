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
    mume = w.get("mume")
    man = w.get("man")
    return w.scene('自分の名前',
            w.cmd.change_camera("mume"),
            w.cmd.change_stage("PostOffice"),
            w.cmd.change_time("afternoon"),
            w.cmd.change_date("FirstMeet"),
            w.plot_note("郵便局で番号を呼ばれ、記録郵便で小説を送る$mume"),
            mume.be(),
            man.be("#郵便局員"),
            man.do("○番と呼ばれる"),
            mume.do("自分の番号札を見てソファから立ち上がる$S"),
            mume.do("手にした封筒には○○文学賞とある"),
            mume.do("それを簡易書留で送る", "記録郵便もつける"),
            mume.do("締切日の月末、$ATMには人が列を成していた"),
            mume.go("外に出る"),
            )

