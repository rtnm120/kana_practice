#!/usr/bin/env python3
# Generates a randomized list of romaji to practice writing kana

import os
import time
import cursor
import random
import shutil

cursor.hide()

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
]
         
hiragana_diacritics = [
    "が","ぎ","ぐ","げ","ご",
    "ざ","じ","ず","ぜ","ぞ",
    "だ","ぢ","づ","で","ど",
    "ば","び","ぶ","べ","ぼ",
    "ぱ","ぴ","ぷ","ぺ","ぽ",
]

hiragana_digraphs = [
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

katakana = [
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
]

katakana_diacritics = [
    "ガ","ギ","グ","ゲ","ゴ",
    "ザ","ジ","ズ","ゼ","ゾ",
    "ダ","ヂ","ヅ","デ","ド",
    "バ","ビ","ブ","ベ","ボ",
    "パ","ピ","プ","ペ","ポ",
]          

katakana_digraphs = [
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

romaji = [
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
]

romanji_diacritics = [
    "ga","gi","gu","ge","go",
    "za","ji (zi)","zu","ze","zo",
    "da","ji (di)","zu (du)","de","do",
    "ba","bi","bu","be","bo",
    "pa","pi","pu","pe","po",
]

romaji_digraphs = [
    "kya","kyu","kyo",
    "sha","shu","sho",
    "cha","chu","cho",
    "nya","nyu","nyo",
    "hya","hyu","hyo",
    "mya","myu","myo",
    "rya","ryu","ryo",
    "gya","gyu","gyo",
    "ja (zya)","ju (zyu)","jo (zyo)",
    "ja (dya)","ju (dyu)","jo (dyo)",
    "bya","byu","byo",
    "pya","pyu","pyo"
]

hiragana_randomized = []
katakana_randomized = []
romaji_randomized = []

console_width = shutil.get_terminal_size().columns
console_height = shutil.get_terminal_size().lines
half_console_height = int((console_height - 1) / 2)

kana_selection = None
routine_selection = None

while kana_selection is None:
    os.system("clear")

    for x in range(0, half_console_height - 3):
        print()

    print("Select Kana".center(console_width))
    print("1: Hiragana".center(console_width))
    print("2: Katakana".center(console_width))

    kana_input = input()

    try:
        kana_selection = int(kana_input)
        
        if kana_selection == 1 or kana_selection == 2:
            break
        else:
            kana_selection = None
    except:
        kana_selection = None

while routine_selection is None:
    os.system("clear")

    for clear_lines in range(0, half_console_height - 5):
        print()
    
    print("Select a practice routine".center(console_width))
    print("1: Kana".center(console_width))
    print("2: Diacritics".center(console_width))
    print("3: Digraphs".center(console_width))
    print("4: All".center(console_width))
    print()

    routine_input = input()
    
    try:
        routine_selection = int(routine_input)
        if routine_selection >= 1 and routine_selection <= 4:
            break
        else:
            routine_selection = None

    except:
        routine_selection = None

while hiragana:
    rand = random.randint(0, len(hiragana) - 1)

    hiragana_randomized.append(hiragana[rand])
    katakana_randomized.append(katakana[rand])
    romaji_randomized.append(romaji[rand])
    
    hiragana.pop(rand)
    katakana.pop(rand)
    romaji.pop(rand)

for kana in romaji_randomized:
    os.system("clear")

    for clear_lines in range(0, half_console_height):
        print()

    input(kana.center(console_width))

for kana in range(len(hiragana_randomized)):
    os.system("clear")
    
    for clear_lines in range(0, half_console_height - 1):
        print()

    print(f"{romaji_randomized[kana]}".center(console_width))
    input(f"{hiragana_randomized[kana]} {katakana_randomized[kana]}".center(console_width)) 
