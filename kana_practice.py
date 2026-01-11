# Generates a randomized list of romaji to practice writing kana

import os
import random

hiragana = [
              "あ","い","う","え","お",
              "か","き","く","け","こ",
              "さ","し","す","せ","そ",
              "た","ち","つ","て","と",
              "な","に","ぬ","ね","の",
              "は","ひ","ふ","へ","ほ",
              "ま","み","む","め","も",
              "や","ゆ","よ",
              "ら","り","る","れ","ろ",
              "わ","を","ん",
              "が","ぎ","ぐ","げ","ご",
              "ざ","じ","ず","ぜ","ぞ",
              "だ","ぢ","づ","で","ど",
              "ば","び","ぶ","べ","ぼ",
              "ぱ","ぴ","ぷ","ぺ","ぽ",
              "きゃ","きゅ","きょ",
              "しゃ","しゅ","しょ",
              "ちゃ","ちゅ","ちょ",
              "にゃ","にゅ","にょ",
              "ひゃ","ひゅ","ひょ",
              "みゃ","みゅ","みょ",
              "りゃ","りゅ","りょ",
              "ぎゃ","ぎゅ","ぎょ",
              "じゃ","じゅ","じょ",
              "ぢゃ","ぢゅ","ぢょ",
              "びゃ","びゅ","びょ",
              "ぴゃ","ぴゅ","ぴょ"
            ]

katakana =  [
              "ア","イ","ウ","エ","オ",
              "カ","キ","ク","ケ","コ",
              "サ","シ","ス","セ","ソ",
              "タ","チ","ツ","テ","ト",
              "ナ","ニ","ヌ","ネ","ノ",
              "ハ","ヒ","フ","ヘ","ホ",
              "マ","ミ","ム","メ","モ",
              "ヤ","ユ","ヨ",
              "ラ","リ","ル","レ","ロ",
              "ワ","ヲ","ン",
              "ガ","ギ","グ","ゲ","ゴ",
              "ザ","ジ","ズ","ゼ","ゾ",
              "ダ","ヂ","ヅ","デ","ド",
              "バ","ビ","ブ","ベ","ボ",
              "パ","ピ","プ","ペ","ポ",
              "キャ","キュ","キョ",
              "シャ","シュ","ショ",
              "チャ","チュ","チョ",
              "ニャ","ニュ","ニョ",
              "ヒャ","ヒュ","ヒョ",
              "ミャ","ミュ","ミョ",
              "リャ","リュ","リョ",
              "ギャ","ギュ","ギョ",
              "ジャ","ジュ","ジョ",
              "ヂャ","ヂュ","ヂョ",
              "ビャ","ビュ","ビョ",
              "ピャ","ピュ","ピョ",
            ]

romaji =   [ 
              "a","i","u","e","o",
              "ka","ki","ku","ke","ko",
              "sa","shi","su","se","so",
              "ta","chi","tsu","te","to",
              "na","ni","nu","ne","no",
              "ha","hi","fu","he","ho",
              "ma","mi","mu","me","mo",
              "ya","yu","yo",
              "ra","ri","ru","re","ro",
              "wa","w(o)","n",
              "ga","gi","gu","ge","go",
              "za","ji(zi)","zu","ze","zo",
              "da","ji(di)","zu(du)","de","do",
              "ba","bi","bu","be","bo",
              "pa","pi","pu","pe","po",
              "kya","kyu","kyo",
              "sha","shu","sho",
              "cha","chu","cho",
              "nya","nyu","nyo",
              "hya","hyu","hyo",
              "mya","myu","myo",
              "rya","ryu","ryo",
              "gya","gyu","gyo",
              "ja(zya)","ju(zyu)","jo(zyo)",
              "ja(dya)","ju(dyu)","jo(dyo)",
              "bya","byu","byo",
              "pya","pyu","pyo"
            ]

hiragana_randomized = []
katakana_randomized = []
romaji_randomized = []

os.system('clear')

while hiragana:
    x = random.randint(0, len(hiragana) - 1)

    hiragana_randomized.append(hiragana[x])
    katakana_randomized.append(katakana[x])
    romaji_randomized.append(romaji[x])
    
    hiragana.pop(x)
    katakana.pop(x)
    romaji.pop(x)

for x in romaji_randomized:
    input(x)
    os.system('clear')

input("Reveal answers?")
os.system('clear')

for x in range(len(hiragana_randomized)):
    print(f"{romaji_randomized[x]}: {hiragana_randomized[x]} {katakana_randomized[x]}")
