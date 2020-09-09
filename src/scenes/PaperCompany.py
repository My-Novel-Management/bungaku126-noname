# -*- coding: utf-8 -*-
'''
Stage: "元マネージャーの会社"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def talk_manager(w: World):
    return w.scene('元マネージャーの話',
            w.cmd.change_stage("PaperCompany"),
            w.plot_note("彼女の元マネージャーはフリーペーパーを作っていた"),
            w.plot_note("街の小さな話題やちょっとした話題の人を掲載する"),
            w.plot_note("もう芸能界は懲り懲りだと言っていた"),
            w.plot_note("最近は全然連絡を取っていないが留学から帰ってきた時に一度だけ連絡があったと"),
            w.plot_note("彼女は自分の名前を酷く気にしていて、町中から完全に名前が消えることを願っていた"),
            w.plot_note("そして壊れた家族とは縁を切ってしまったと"),
            w.plot_note("しかし彼女の母親だけは探し出して連絡をつけたと聞いた"),
            w.plot_note("彼女の母親の連絡先を教えてもらう"),
            )

