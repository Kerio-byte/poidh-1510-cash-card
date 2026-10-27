#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Тик 390 (v2): листовка-визитка «PAID IN CASH. ON PURPOSE.» — лот base #1510.

Печатные размеры в пунктах: 1 pt = 300/72 px при 300 dpi.
Ничего мельче 5 pt: на настоящей карточке 3.5 x 2 дюйма это уже не читается.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1050, 600
M = 58
INK, PAPER = 0, 255
OUT = '/home/jar/.hermes/state/money/lot1510'

NB = '/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf'
SB = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
MO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
MOB = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'


def px(pt):
    return int(round(pt * 300 / 72))


def f(path, pt):
    return ImageFont.truetype(path, px(pt))


def tw(d, text, font, tracking=0.0):
    if not tracking:
        return d.textlength(text, font=font)
    return sum(d.textlength(c, font=font) + tracking for c in text) - tracking


def tracked(d, xy, text, font, fill=INK, tracking=0.0, right=False, center=False):
    x, y = xy
    w = tw(d, text, font, tracking)
    if right:
        x -= w
    elif center:
        x -= w / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textlength(c, font=font) + tracking
    return w


def fit(d, text, path, start_pt, maxw, tracking=0.0, floor=4.0):
    pt = start_pt
    while pt >= floor:
        fo = f(path, pt)
        if tw(d, text, fo, tracking) <= maxw:
            return fo
        pt -= 0.5
    return f(path, floor)


def rule(d, y, x0=M, x1=W - M, h=3):
    d.rectangle([x0, y, x1, y + h - 1], fill=INK)


def fine(d, y, text, pt=5.0, tracking=2.0):
    fo = fit(d, text, MO, pt, W - 2 * M, tracking, floor=4.0)
    tracked(d, (W / 2, y), text, fo, INK, tracking, center=True)


# ------------------------------------------------------------------ FRONT
def front():
    img = Image.new('L', (W, H), PAPER)
    d = ImageDraw.Draw(img)

    fo = f(MOB, 6)
    tracked(d, (M, 40), 'SERIES C · 2026', fo, INK, 3)
    tracked(d, (W - M, 40), 'Nº 004 182', fo, INK, 2, right=True)
    rule(d, 74)

    f1 = fit(d, 'THIS NOTE', NB, 34, W - 2 * M, -1.0)
    d.text((M - 2, 104), 'THIS NOTE', font=f1, fill=INK)
    y2 = 104 + f1.getbbox('THIS NOTE')[3] + 14

    f2 = fit(d, 'LEAVES NO TRACE.', NB, 34, W - 2 * M - 40, -1.0)
    x0, y0, x1, y1 = d.textbbox((0, 0), 'LEAVES NO TRACE.', font=f2)
    band = [M, y2 + y0 - 8, M + 40 + (x1 - x0), y2 + y1 + 8]
    d.rectangle(band, fill=INK)
    d.text((M + 20 - x0, y2), 'LEAVES NO TRACE.', font=f2, fill=PAPER)

    yy = band[3] + 24
    for line in ('No bank. No app. No record of you.',
                 'Works when power, network or banks are down.'):
        fl = fit(d, line, MO, 7.5, W - 2 * M, 0, floor=6.0)
        d.text((M, yy), line, font=fl, fill=INK)
        yy += int(px(7.5) * 1.35)

    by0, by1 = H - 136, H - 76
    d.rectangle([M, by0, W - M, by1], fill=INK)
    f4 = f(MOB, 6.5)
    ty = by0 + (by1 - by0) // 2 - px(4.5)
    tracked(d, (W - M - 20, ty), 'TURN OVER →', f4, PAPER, 2, right=True)
    cta_x = W - M - 20 - tw(d, 'TURN OVER →', f4, 2) - 26
    tracked(d, (M + 20, ty), 'PRIVATE · OFFLINE · FINAL · YOURS', f4, PAPER, 2)
    if tw(d, 'PRIVATE · OFFLINE · FINAL · YOURS', f4, 2) + M + 20 > cta_x:
        tracked(d, (M + 20, ty), 'PRIVATE · OFFLINE · FINAL · YOURS', f4, PAPER, 0)

    # строчка «от кого» — визитку передают из рук в руки, имя вписывают от руки
    f5 = f(MO, 6.5)
    d.text((M, H - 56), 'FROM', font=f5, fill=INK)
    fx = M + tw(d, 'FROM', f5) + 16
    base = H - 56 + px(6.5) + 6
    d.rectangle([fx, base, fx + 300, base + 2], fill=INK)
    tracked(d, (W - M, H - 56), 'KEEP CASH ALIVE', f5, INK, 2, right=True)
    return img


# ------------------------------------------------------------------- BACK
ITEMS = [
    ('01', 'PRIVATE', 'No bank, no app, no name.'),
    ('02', 'OFFLINE', 'Still pays with the power out.'),
    ('03', 'FINAL', 'Settled at once. No chargeback.'),
    ('04', 'YOURS', 'No account, no limit, no asking.'),
]


def back():
    img = Image.new('L', (W, H), PAPER)
    d = ImageDraw.Draw(img)

    fo = f(MOB, 6.5)
    tracked(d, (M, 40), 'WHY I PAID YOU IN CASH', fo, INK, 3)
    tracked(d, (W - M, 40), 'Nº 004 182', fo, INK, 2, right=True)
    rule(d, 74)

    fh = f(NB, 13)
    d.text((M - 1, 92), "What a card can't do", font=fh, fill=INK)

    y = 172
    row = 86
    for num, label, body in ITEMS:
        d.rectangle([M, y + 4, M + 32, y + 36], fill=INK)
        fn = f(MOB, 6)
        tracked(d, (M + 16, y + 11), num, fn, PAPER, 0.5, center=True)
        fl = f(SB, 9)
        tracked(d, (M + 48, y + 4), label, fl, INK, 2)
        fb = f(MO, 8)
        body_x = M + 48 + max(178, tw(d, label, fl, 2) + 20)
        d.text((body_x, y + 8), body, font=fb, fill=INK)
        if num != '04':
            d.rectangle([M + 48, y + 64, W - M, y + 65], fill=INK)
        y += row

    by0, by1 = H - 124, H - 56
    d.rectangle([M, by0, W - M, by1], fill=INK)
    fc = f(NB, 10.5)
    d.text((M + 20, by0 + (by1 - by0) // 2 - px(7)), 'NEXT TIME: ASK FOR YOUR CHANGE IN CASH.',
           font=fc, fill=PAPER)
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    fr, bk = front(), back()
    fr.save(f'{OUT}/card_front.png', dpi=(300, 300))
    bk.save(f'{OUT}/card_back.png', dpi=(300, 300))
    gap = 40
    prev = Image.new('L', (W * 2 + gap * 3, H + gap * 2), 232)
    prev.paste(fr, (gap, gap))
    prev.paste(bk, (gap * 2 + W, gap))
    prev.save(f'{OUT}/preview.png')
    fr.save(f'{OUT}/card_print.pdf', 'PDF', resolution=300.0, save_all=True,
            append_images=[bk])
    print('OK; front ink%%: %.1f' % (sum(1 for p in fr.getdata() if p < 128) / (W * H) * 100))


if __name__ == '__main__':
    main()
