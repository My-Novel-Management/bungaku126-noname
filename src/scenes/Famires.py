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
    mume = w.get("mume")
    mutsu = w.get("mutsu")
    return w.scene('$mumeの彼女',
            w.cmd.change_stage("Famires"),
            w.plot_note("帰りにファミレスで合流して、互いの進捗を話し合う"),
            w.plot_note("有名になりたい、と話す$mumeと、いい作品を作りたいという$mutsu"),
            w.plot_note("$mutsuは自分が有名になることは「ついで」だと言った。作品の方がずっと大事だと"),
            w.plot_note("$mutsuはイラストレーターでプロを目指して活動していた"),
            mume.be("駅近くのガストにいる"),
            mutsu.come("少し遅れてやってくる$S"),
            mutsu.talk("あ、ごめん", "電車一本遅れちゃって"),
            mume.talk("おう"),
            mutsu.do("対面に座って注文を済ませる"),
            mutsu.talk("で、どう？　自信は"),
            mume.talk("いつもと変わらないよ", "どうしてあんなもの書いたんだろって"),
            mume.talk("$mutsuさんはさ、コンテストに応募する時にいつもそれなりに自信持ってるの？"),
            mutsu.talk("色々だよ", "とにかくイラストは数書かないとあれだし",
                "小説とは違うんじゃないかな", "今はデジタルだから無限に手が入れられる分、どこまでやればいいか分からなくなっちゃう"),
            mume.think("自分の学生時代のスケッチブックを思い出して、そんなに違うのかと"),
            mume.do(""),
            # TODO
            )

