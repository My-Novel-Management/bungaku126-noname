# -*- coding: utf-8 -*-
'''
Stage: "シェアハウス"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def resident(w: World):
    return w.scene('シェアハウスの住人',
            w.plot_note("$mumeは家賃三万のシェアハウスで何とか暮らしていた"),
            w.plot_note("同じシェアハウスの住人の$ishiが、新しい彼女を連れて帰ってくる"),
            )


def ishi_girlfriend(w: World):
    return w.scene("$ishiの彼女",
            w.plot_note("$ishiは芸人をしているらしいが、あまり外出することもなく、ゲームばかりして暮らしている"),
            w.plot_note("パシリに使われる新しい彼女の$yuna"),
            w.plot_note("前の彼女とは違い、あまり料理はしないタイプだと$mumeは思った"),
            )


def nohome_ishi(w: World):
    return w.scene("帰らない$ishi",
            w.plot_note("しばらく$ishiが家に帰ってこなくなった"),
            w.plot_note("何度か家の前で待つ$yunaとすれ違ったが、声もかけなかった"),
            w.plot_note("$mutsuとは完全に連絡がなくなった"),
            w.plot_note("ときおり外で$yunaが泣きながら電話しているのが聞こえてきたが、話を聞かないようにヘッドフォンで音楽を流した"),
            w.plot_note("$mutsuに一度言われたことを思い出す"),
            w.plot_note("$mumeの作品にはあなたらしさがないと"),
            w.plot_note("読んでいても楽しくないし、特に女性の気持ちが全然理解できていないと"),
            w.plot_note("$mumeは$yunaの声が聞こえなくなったのを確認してから、玄関先を見た"),
            w.plot_note("$yunaが泣きつかれて壁にもたれて寝ていた"),
            )


def help_yuna(w: World):
    return w.scene("$yunaを助けた",
            w.plot_note("$mumeは$yunaを部屋の中に運び、共用リビングのソファに寝かせる"),
            )


def talk_with_yuna(w: World):
    return w.scene("$yunaと話す",
            w.plot_note("夜中に小説を書いていると$yunaが起きてきた"),
            w.plot_note("$yunaは$ishiと別れたという経緯について、一人でぼそぼそと語る"),
            w.plot_note("$ishiは芸人をしていたが、大物プロデューサーの孫娘でタレントをしている彼女ができたらしい"),
            w.plot_note("$ishiは有名になる為に彼女と付き合うと最初から言っていた"),
            w.plot_note("確認したがバーターでやっと出してもらっている感じの女性で、$mumeにとっては他の出演者と見分けがつかない"),
            w.plot_note("$yunaは有名になってもいいことなんてなにもないだろうと言う"),
            )


def yuna_and_ishi(w: World):
    return w.scene("$yunaと$ishiの関係",
            w.plot_note("$mumeは$yunaに$ishiの気持ちを自分なりに解釈して代弁した"),
            w.plot_note("ただちゃんと冷静になって話し合った方がいいとも助言する"),
            w.plot_note("$mumeは$yunaが$ishiのどこに惚れているのかよく分からなかったが、彼女の気持ちを尊重したかった"),
            w.plot_note("内容は彼女ができたことではなく、二人の考え方の違いだった"),
            w.plot_note("$ishiにそのタレントへの恋愛感情はないらしい"),
            w.plot_note("ただ体はいいと言っていた"),
            w.plot_note("$ishiとの出会いは居酒屋で、彼女が一人で飲んでいるところをからまれて、そこから助けられた"),
            w.plot_note("その時$yunaにからんできたのが、その大物プロデューサーらしい"),
            w.plot_note("最近テレビにも顔を出している"),
            w.plot_note("その取り巻きの一人にテレビに顔を出すようになった若い編集者がいた"),
            w.plot_note("有名になれ、と自分で本を出した編集者で、色々もてはやされている"),
            w.plot_note("$mumeは$ishiからもらった映画のチケットが、そのプロデューサーたちが噛んでいる映画だと知る"),
            w.plot_note("$ishiは有名になるから、そうなったら愛人くらいにはしてやると言い残したらしい"),
            )


def mume_suggestion(w: World):
    return w.scene("$mumeの提案",
            w.plot_note("今後どうするのか聞いたが、$yunaは特に何も目標がないと言った"),
            w.plot_note("$ishiと連絡がつくまでここを使えばいいと$mumeは言った"),
            w.plot_note("オーナーはあまり口うるさく言わない人だから、と"),
            w.plot_note("翌日から$yunaは自分の荷物を少し持ち込んで、$ishiの部屋に住み始めた"),
            )


def yunas_nothing_day(w: World):
    return w.scene("$yunaの何もない一日",
            w.plot_note("$yunaは一日何もせずにぼーっとしていることも多かった"),
            w.plot_note("料理はせず、買ってきたものを食べるで済ます"),
            w.plot_note("さすがに心配になり、$mumeは自分が作ったものでいいかと尋ねて、一緒に食べ始める"),
            w.plot_note("$yunaには時々魂が抜けたようになることがあった"),
            w.plot_note("$mumeは$yunaに普段どんな暮らしをしているのか質問する"),
            w.plot_note("$yunaはテレビも見ないし、本もあまり読まない"),
            w.plot_note("付き合った男性の趣味に合わせる感じで、$ishiはゲームばかりしていたからそれを黙って見ていたらしい"),
            w.plot_note("$ishiからの連絡はないまま"),
            w.plot_note("テレビの深夜番組に$ishiが出ていた"),
            w.plot_note("$yunaはゲームをしてみたいと$mumeに申し出た"),
            )


def yuna_need_advice(w: World):
    return w.scene("$yunaの相談",
            w.plot_note("$mumeは$yunaと半同棲のような生活を送っていた"),
            w.plot_note("ライターの仕事をしつつ他の求人を当たってみる$mume"),
            w.plot_note("けれど資格もなく、肉体労働も苦手な$mumeにはできる仕事は限られていた"),
            w.plot_note("かつて$mumeの小説を評価してくれた男が新しい会社を作ったので、そこで仕事をしないかと誘ってくれた"),
            w.plot_note("機械が打ち出した記事の文章を人間が書いたものっぽく修正する仕事だった"),
            w.plot_note("$yunaからコメントに恐い人がいると相談される"),
            w.plot_note("女性配信者には変なコメントしてくる人がよく出るが、実際に見てみると確かに彼女をよく知る人間のよう"),
            w.plot_note("いつの間にかその業界でも有名になりつつある$yuna"),
            w.plot_note("彼女は辞めたいと言い出したが$mumeはもったいないから続ければいいと言う"),
            w.plot_note("ある日ネットの掲示板に実況者の$yunaがかつて有名子役だったと書かれていた"),
            )


def vanishing_yuna(w: World):
    return w.scene("姿を消す$yuna",
            w.plot_note("それが書かれた翌日から$yunaはシェアハウスから姿を消した"),
            w.plot_note("連絡先も知らず、連絡は取れない"),
            w.plot_note("辞めるタイミングだったのかも知れないと、他人のことながら有名を諦めるのを残念に思っていた"),
            w.plot_note("$ishiが家賃滞納していて、連絡がある"),
            w.plot_note("一月待つがそれまでに入金などの連絡がない場合は追い出すことになるらしい"),
            w.plot_note("$yunaとは連絡が取れないまま"),
            w.plot_note("家の付近をうろついている怪しい人間の姿もあった"),
            )


def comeback_ishi(w: World):
    return w.scene("$ishiの帰還",
            w.plot_note("$mumeは$yunaについて調べようと$ishiに連絡を取る"),
            w.plot_note("$ishiと会い、彼女とどこでどういう風に出会ったのか詳しく聞く"),
            w.plot_note("$yunaは居酒屋で、といっていたが、よくプロデューサーが芸能人を連れてくる隠れ家的なイタリアンバーだった"),
            )


def goout_ishi(w: World):
    return w.scene("出ていく$ishi",
            w.plot_note("$mumeはシェアハウスに$ishiが戻ってきて、出ていく準備をしているのを見る"),
            w.plot_note("移住して田舎暮らしをする番組に出演が決まり、引き払うらしい"),
            w.plot_note("$ishiは彼なりに有名になることを模索していた"),
            w.plot_note("彼は「選り好みなんてしてられる立場じゃないんだ」と言う"),
            w.plot_note("$yunaへの未練こそあったが、自分みたいな人間と一緒になることはないと"),
            w.plot_note("$ishiは$yunaが元子役だと薄々感づいていたらしい"),
            w.plot_note("$ishiは$yunaの住所を教えてくれる"),
            )
