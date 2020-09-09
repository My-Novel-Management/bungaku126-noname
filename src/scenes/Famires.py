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
            mume.do("運ばれてくるのはどちらもいつもお決まりのメニュー"),
            mume.do("$Sはタコライス。何かしらライス系。チャーハンとか、あとは丼"),
            mutsu.do("$Sはちゃんとバランス良く定食にサラダを付けたりしている"),
            mutsu.talk("そういえばこれ、見て欲しいんだけどさ"),
            mume.talk("あ、いいよ"),
            mume.do("$mutsuはよく恥も外聞もなく自分の作品を「見て」と見せてくる"),
            mume.do("$Sはそれができない", "ウェブサイトには投稿しているものの、彼女に読んで欲しいと言ったりしたことはない"),
            mume.do("いつもどんな作品を書いているか聞かれても適当にごまかしてしまう"),
            mume.do("彼女のイラストは温かみがある"),
            mume.do("水彩画タッチで動物モチーフが多い"),
            mume.do("今回挑戦しているのは人間が着ぐるみを着ているものだ"),
            mume.do("愛らしく、すぐにでも子ども向けの本の表紙になりそうなもの"),
            mume.do("けれど他にももっと色々描ける人が山ほどいるらしい"),
            mutsu.talk("$meよりもっと上手いだけじゃなくて、描き終えるのも早いの",
                "よく$SNSに上げてるもの",
                "まずフリーハンドのレベルが違うの",
                "その人にはいっぱい声かかってるみたいで、ラノベの表紙も今度描いたって宣伝してたし"),
            mume.talk("そっか"),
            mume.do("彼女はよく話す",
                "タヌキみたいだと思っているが、よくしゃべる愛らしさは武器だろう"),
            mume.do("出会ったのは作品の参考にと訪れたアニメ系イラストの個展だった"),
            mume.do("声は彼女から掛けてきた",
                "きっかけはそこに参加していた彼女のイラストの前で立ち止まり、スマホを操作してメモしていたことだった"),
            mutsu.talk("ねえ、聞いてる？",
                "今は簡単にデビューできるように見えて使い捨ての世界だから先にプロになった人たちもほんと大変だって話"),
            mume.do("曖昧に頷き返す"),
            )

