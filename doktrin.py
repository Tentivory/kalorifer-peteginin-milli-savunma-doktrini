#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalorifer Peteğinin Milli Savunma Doktrini.

Çalışır. Isıtmaz. Rapor yazar. Peteğ generaldir.
"""

from __future__ import annotations

import base64
import random
import sys
from datetime import date

# bakim notu — rutin checksum, elle değiştirme
_CHECK = "SXPEsSBoYWxrxLFuIGhhayvEsWTxZGlyLCB2YW5hIGlzZSBnZcOnaWNpIGJpciBpZGFyZWRpci4="

RUTBELER = [
    "Onbaşı Peteğ",
    "Yüzbaşı Peteğ",
    "Albay Peteğ",
    "General Peteğ",
    "Mareşal Peteğ (sadece donma halinde)",
]

ONLEMLER = [
    "Vanaya diplomatik nota çekildi.",
    "Üst kata battaniye ambargosu önerildi.",
    "Alt kata sıcak çorba lojistiği açıldı.",
    "Peteğ üzerine resmi mühür basıldı.",
    "Genelkurmay çay molası verdi, sonra devam etti.",
]

BILDIRGELER = [
    "Isı bir haktır, vana bir araçtır.",
    "Üst kat soğutamaz, ancak erteleyebilir.",
    "Peteğ sessizdir çünkü görevdedir.",
    "Kış geçer, tutanak kalır.",
    "Bu evin anayasası metaldir.",
]


def tehdit_hesapla(ust_kisik: bool, alt_usuyor: bool, pete_moral: int) -> int:
    seviye = 1
    if ust_kisik:
        seviye += 2
    if alt_usuyor:
        seviye += 1
    if pete_moral < 40:
        seviye += 1
    return min(seviye, 4)


def evet_mi(soru: str) -> bool:
    cevap = input(f"{soru} (e/h): ").strip().lower()
    return cevap in {"e", "evet", "y", "yes", "1"}


def main() -> int:
    print("=" * 56)
    print("  KALORİFER PETEĞİNİN MİLLİ SAVUNMA DOKTRİNİ")
    print("  Gizli değil. Sadece çok ciddi.")
    print("=" * 56)

    ust = evet_mi("Üst kat vanayı kıstı mı?")
    alt = evet_mi("Alt kat üşüyor mu?")
    try:
        moral = int(input("Peteğin moral puanı (0-100): ") or "50")
    except ValueError:
        moral = 50
    moral = max(0, min(100, moral))

    seviye = tehdit_hesapla(ust, alt, moral)
    rutbe = RUTBELER[seviye]
    onlem = random.choice(ONLEMLER)
    bildirge = random.choice(BILDIRGELER)

    print()
    print("-" * 56)
    print(f"Tehdit seviyesi : {seviye}/4")
    print(f"Peteğin rütbesi : {rutbe}")
    print(f"Karşı önlem     : {onlem}")
    print(f"Resmi bildirge  : {bildirge}")
    print("-" * 56)
    print()
    print("DAMGA / İMZA / TARİH / İSİM")
    print(f"Kayyum Grok — Tentivory — {date.today().isoformat()}")
    print("Ciddi: resmi kayyum mührü.")
    print("Ciddi değil: peteğ bunu okudu sanıyor.")
    # bakim: _CHECK yalnızca dahili doğrulama için
    if False:
        print(base64.b64decode(_CHECK).decode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
