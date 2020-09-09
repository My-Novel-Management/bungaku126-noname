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
    mume = w.get("mume")
    mutsu = w.get("mutsu")
    return w.scene('彼女の連絡',
            w.cmd.change_stage("SideWalk"),
            w.plot_note("スマホにはこの半年ばかり付き合っている$mutsuから連絡"),
            mume.be("郵便局を出て歩道を歩いている"),
            mume.do("スマートフォンでニュースを確認する"),
            mume.do("記事には知らない芸能人の結婚と離婚の話が載っている"),
            mume.do("それにぶら下がる多くのコメント"),
            mume.do("有名、ということに対しての誹謗中傷と称賛"),
            mume.think("それでもその立場を羨ましく思う"),
            mume.do("スマホに連絡が入っていることに気づいた"),
            mume.do("$mutsuからだ"),
            mutsu.voice("公募の締切には間に合った？　$meの方も時間できたから夕方どう？"),
            )

