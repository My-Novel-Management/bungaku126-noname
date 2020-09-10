# -*- coding: utf-8 -*-
'''
Stage: "$mumeの部屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def his_dream(w: World):
    mume = w.get("mume")
    return w.scene('$mumeの夢',
            w.cmd.change_stage("MumeRoom"),
            w.cmd.change_time("night"),
            w.cmd.change_date("FirstMeet"),
            w.plot_note("$mumeは自室にこもり、小説のプロットを書く"),
            w.plot_note("インターネット黎明期なら自分でホームページを作り、そこに駄文を掲載した"),
            w.plot_note("それを小学生の$Sはよく読んでいた"),
            w.plot_note("最近は投稿サイトにみんな小説を出す"),
            w.plot_note("多くはウェブ小説と呼ばれるものだが、文芸作品を書いている人も多い"),
            w.plot_note("公募などでよく見かける名前もあった"),
            w.plot_note("一定のファンがついている人たち"),
            w.plot_note("しかし$mumeは無風。無名で、たまに読んでくれる人がいても、コメントも何もなく、分からない"),
            w.plot_note("その他大勢の投稿者の一人だった"),
            mume.come("自室に入ってくる"),
            mume.do("明かりをつけて、荷物をベッドの上に置く"),
            mume.do("六畳程度の部屋にベッドとテーブル、パソコン、小物ケースが三段"),
            mume.do("ここが$mumeの生活のほとんどで、書斎でもあった"),
            mume.do("小さな冷蔵庫から取り出したペットボトルから、水をコップに移して飲む"),
            mume.do("パソコンを立ち上げ、その間にスマホを確認する"),
            mume.do("$mutsuから「今日はありがとう」というメッセージ付きイラストが送られていた"),
            mume.think("そんな気軽に自分のコンテンツを使える彼女が、正直羨ましかった"),
            mume.do("ブラウザを開き、ウェブ小説投稿サイトを確認する"),
            mume.do("自分の投稿した作品にいったいいくら$pvがついているかとか、レビューはないかとか、そういった諸々を確認する"),
            mume.do("でもほとんど変動がなく、がっかりするばかり"),
            mume.do("そしてサイトトップには「書籍化します」といった言葉をタイトル脇につけている作品ばかりが目立つ"),
            mume.do("自分はどこでも無名なままだと思う"),
            mume.do("そのサイトを閉じて、書きかけている小説の続きを書こうとする"),
            mume.do("タイトルは無題のままだった"),
            )


def popular_mutsu(w: World):
    mume = w.get("mume")
    return w.scene("$mutsuの人気",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("一方イラストという違いはあれど$mutsuは少しずつファンを増やしていた"),
            w.plot_note("その差を歯がゆく思う"),
            )


def this_blog(w: World):
    mume = w.get("mume")
    return w.scene("あるブログ",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("ネットで情報を探している中で「$theblog」というブログを見つける"),
            w.plot_note("そこにはかつて有名になったことで周囲の人間関係がおかしくなり、やがて逃げ出したことが書かれていた"),
            w.plot_note("コメントには嫉妬や称賛、ただの悪口、悪戯と様々な人間の感情がうずまいていた"),
            w.plot_note("$mumeはそれでも有名になりたい、と考えていた"),
            )


def depart_mutsu(w: World):
    mume = w.get("mume")
    return w.scene("$mutsuとの別れ",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("ある日彼女から別れたいと連絡があった"),
            w.plot_note("$mumeはその話し合いとブッキングしてしまった仕事の締切を優先してしまった"),
            w.plot_note("結局そのまま別れることになった"),
            )


def wasted_time(w: World):
    mume = w.get("mume")
    return w.scene("無駄な時間",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("$mutsuと別れてから、不思議と時間が生まれた"),
            w.plot_note("仕事もなく、小説執筆に時間が使えるのに、なかなか書く気になれなかった"),
            w.plot_note("埃をかぶったギターを引っ張り出して、昔書いた曲を弾く"),
            w.plot_note("音楽も俳優もイラストも何もかも、売れない無名のまま"),
            )


def writing_novels(w: World):
    mume = w.get("mume")
    return w.scene("小説を書く時間",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("中途半端だった小説に時間をかける$mume"),
            w.plot_note("いろいろな人の言葉に振り回される$mume"),
            w.plot_note("書き方や文章、物語の構築の仕方、流行を考えること、様々やってみたが、全部成果が出ないまま"),
            w.plot_note("$mumeはとにかく書いた"),
            w.plot_note("$yunaはたまにそれを読んでいたようだが、何も言わない"),
            )


def researching_streamer(w: World):
    mume = w.get("mume")
    return w.scene("実況配信の研究",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("色々な実況や配信、動画を見て回る"),
            w.plot_note("そこもまた小説と同じで、何かしら元から有名な人間が多く人気を集めていたが、それでも中には$yunaのようなぽっと出の新人もいた"),
            w.plot_note("人気がある人はやはり何かしら特徴がある"),
            w.plot_note("でも$mume自身がそれになれるかといったら無理だとしか思えなかった"),
            w.plot_note("かつて自分が投稿した動画を発掘して見直した"),
            w.plot_note("自己満足、といってよかった"),
            w.plot_note("大半のものは自己満足でしかないのだ、と理解して、その動画を削除した"),
            )


def notfound_myname(w: World):
    mume = w.get("mume")
    return w.scene("名前が見つからない",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("自分の作品を読んでくれていた人の名が、公募の最終選考にあるのを見つけた"),
            w.plot_note("SNSでずっと駄目だとか才能はないと$mumeと同じようにぼやいていた人が急に脚光を浴びたり、選考突破して喜んだりしている"),
            w.plot_note("$mumeはその人たちの作品に目を通して、自分と大きな差があるようには思えなかった"),
            w.plot_note("才能も小説も何もかもが分からなくなる"),
            )


def sns_words(w: World):
    mume = w.get("mume")
    return w.scene("$SNSの言葉たち",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("別の公募の結果も出て、全滅なことが判明する"),
            w.plot_note("そんな$mumeにSNSで流れてきた有名編集者の言葉が突き刺さる"),
            w.plot_note("結局凡庸な無名の人間の悪あがきでしかなかったのだ"),
            w.plot_note("処女作でデビューする新人。それは有名作家の孫娘だった"),
            w.plot_note("文芸雑誌にも芸人やアイドルの小説の掲載が増え始める"),
            w.plot_note("自分でファンを持っていない、平均値の作家志望者はよっぽどいいアイデアを見つけてものにするしか方法はないと"),
            w.plot_note("今や文芸の世界ですら「有名人」でないと厳しいのだった"),
            )


def deleting_novels(w: World):
    mume = w.get("mume")
    return w.scene("そして小説を消した",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("徹夜して今まで自分が書いたものに、本当に才能はないのかと探した"),
            w.plot_note("けれど朝になっても何も感動は見つからず、そのデータ全てを$mumeは削除した"),
            )


def contact_from_publisher(w: World):
    mume = w.get("mume")
    return w.scene("出版社からの連絡",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("引っ越しも考え始めた頃、$mumeに出版社から連絡がある"),
            w.plot_note("一度話をすることになった"),
            )


def yuna_blog(w: World):
    mume = w.get("mume")
    return w.scene("$yunaのブログ",
            w.cmd.change_stage("MumeRoom"),
            w.plot_note("話の中でライターの仕事をしていると言った流れから$yunaのことが話題にでる"),
            w.plot_note("編集者は$yunaが「$theblog」の主だと分かって声をかけていたとおもらしする"),
            w.plot_note("$mumeは帰ってから再度あのブログを読み返す"),
            w.plot_note("そこに書かれたコメントの中に$yunaが書いたらしきものを見つける"),
            w.plot_note("そこには何度も死を選ぼうとして選べなかったけれど、今度こそはというようなことが書かれていた"),
            )
