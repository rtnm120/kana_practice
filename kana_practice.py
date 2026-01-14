#!/usr/bin/env python3
# Generates a randomized list of romaji to practice writing kana

import os
import time
import cursor
import random
import shutil

cursor.hide()

hiragana_base = [
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

katakana_base = [
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

romaji_base = [
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

kana_selection = []
kana_randomized = []

romaji_selection = []
romaji_randomized = []

console_width = shutil.get_terminal_size().columns
console_height = shutil.get_terminal_size().lines
half_console_height = int((console_height - 1) / 2)

kana_input = None
routine_input = None

while kana_input is None:
    os.system("clear")

    for x in range(0, half_console_height - 2):
        print()

    print("Select Kana".center(console_width))
    print("1: Hiragana".center(console_width))
    print("2: Katakana".center(console_width))
    print("3. Challenge Mode".center(console_width))

    kana_input = input()

    try:
        kana_input = int(kana_input)
        
        if kana_input >= 1 and kana_input <= 3:
            break
        else:
            kana_input = None
    except:
        kana_input = None

if kana_input != 3:
    while routine_input is None:
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
            routine_input = int(routine_input)
            if routine_input >= 1 and routine_input <= 4:
                break
            else:
                routine_input = None

        except:
            routine_input = None

match kana_input:
    case 1:
        match routine_input:
            case 1:
                kana_selection = hiragana_base
                romaji_selection = romaji_base
            case 2:
                kana_selection = hiragana_diacritics
                romaji_selection = romanji_diacritics
            case 3:
                kana_selection = hiragana_digraphs
                romaji_selection = romaji_digraphs
            case 4:
                kana_selection = hiragana_base + hiragana_diacritics + hiragana_digraphs
                romaji_selection = romaji_base + romanji_diacritics + romaji_digraphs
    case 2:
        match routine_input:
            case 1:
                kana_selection = katakana_base
                romaji_selection = romaji_base
            case 2:
                kana_selection = katakana_diacritics
                romaji_selection = romanji_diacritics
            case 3:
                kana_selection = katakana_digraphs
                romaji_selection = romaji_digraphs
            case 4:
                kana_selection = katakana_base + katakana_diacritics + katakana_digraphs
                romaji_selection = romaji_base + romanji_diacritics + romaji_digraphs
    case 3:
        hiragana = hiragana_base + hiragana_diacritics + hiragana_digraphs
        katakana = katakana_base + katakana_diacritics + katakana_digraphs
        romaji_selection = romaji_base + romanji_diacritics + romaji_digraphs

        for kana in range(len(hiragana)):
            kana_selection.append([hiragana[kana], katakana[kana]])
                
while kana_selection:
    rand = random.randint(0, len(kana_selection) - 1)

    kana_randomized.append(kana_selection[rand])
    romaji_randomized.append(romaji_selection[rand])
    
    kana_selection.pop(rand)
    romaji_selection.pop(rand)

for kana in romaji_randomized:
    os.system("clear")

    for clear_lines in range(0, half_console_height):
        print()

    input(kana.center(console_width))

for kana in range(len(kana_randomized)):
    os.system("clear")
    
    for clear_lines in range(0, half_console_height):
        print()

    print(f"{romaji_randomized[kana]}".center(console_width))

    if kana_input == 3:
        input(f"{kana_randomized[kana][0]} {kana_randomized[kana][1]}".center(console_width)) 

    else:
        input(f"{kana_randomized[kana]}".center(console_width)) 
