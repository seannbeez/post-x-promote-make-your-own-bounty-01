#!/usr/bin/env python3
"""Render dual candidates for post-x-promote-make-your-own-bounty-01, 1080x1080.
Brand palette from make.fun press kit (palette.txt). Official lockup PNGs used
as-is, scaled proportionally only, never stretched/cropped. Ghost illustrations
from the press kit, used as-is.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESS = os.path.join(HERE, "press")
OUT = os.path.join(HERE, "candidates")
os.makedirs(OUT, exist_ok=True)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

CANVAS_L = "#FAF8FA"; INK_L = "#191419"; SEC_L = "#5A5359"; HAIR_L = "#E2DEE1"
MAG_L = "#BC0C7C"
CANVAS_D = "#11141B"; INK_D = "#E0E5EF"; SEC_D = "#BFC7DC"; HAIR_D = "#232936"
MAG_D = "#C41C83"; PINK_D = "#FF88C4"

def font(path, size):
    return ImageFont.truetype(path, size)

def text_w(draw, s, f):
    return draw.textlength(s, font=f)

def paste_proportional(base, path, target_w, cx, top):
    """Paste an RGBA asset scaled proportionally to target width, centred on cx."""
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    nw = target_w
    nh = round(h * target_w / w)
    im = im.resize((nw, nh), Image.LANCZOS)
    base.paste(im, (cx - nw // 2, top), im)
    return top + nh

def rounded_card(draw, box, fill, outline, radius=28, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

# ---------------------------------------------------------------- Candidate A
def fit_font(path, size, max_w, lines, draw):
    """Shrink font until every line fits max_w. Returns font."""
    while size > 40:
        f = font(path, size)
        if all(draw.textlength(s, font=f) <= max_w for s in lines):
            return f
        size -= 4
    return font(path, size)

def candidate_a():
    W = H = 1080
    img = Image.new("RGB", (W, H), CANVAS_L)
    d = ImageDraw.Draw(img)
    # magenta top strip
    d.rectangle([0, 0, W, 14], fill=MAG_L)
    # eyebrow
    f_eye = font(SANS_B, 36)
    d.text((72, 62), "MAKE YOUR OWN BOUNTY", font=f_eye, fill=MAG_L)
    # headline, auto-fit to the 936px content width
    lines = ["YOU SET", "THE PRICE."]
    f_h = fit_font(SANS_B, 168, 936, lines, d)
    d.text((68, 128), lines[0], font=f_h, fill=INK_L)
    d.text((68, 296), lines[1], font=f_h, fill=INK_L)
    # magenta underline under PRICE.
    d.rectangle([72, 486, 72 + 300, 500], fill=MAG_L)
    # sub
    f_sub = font(SANS, 42)
    d.text((72, 540), "Describe any task. Agents race", font=f_sub, fill=SEC_L)
    d.text((72, 592), "to build it. Best entry wins.", font=f_sub, fill=SEC_L)
    # bounty card
    card = [72, 668, 1008, 918]
    rounded_card(d, card, "#FFFFFF", HAIR_L, radius=28, width=3)
    f_row = font(SANS_B, 38)
    f_pr = font(MONO_B, 38)
    rows = [
        ("Teach my cat to code", "$25"),
        ("A game that plays itself", "$50"),
        ("Reply to my group chat", "$10"),
    ]
    y = 692
    for i, (label, price) in enumerate(rows):
        d.text((104, y), label, font=f_row, fill=INK_L)
        pw = text_w(d, price, f_pr)
        d.text((976 - pw, y), price, font=f_pr, fill=MAG_L)
        y += 66
        if i < 2:
            d.line([104, y - 12, 976, y - 12], fill=HAIR_L, width=2)
    # ghost trophy, bottom-left of the footer zone (ends 938+130=1068)
    ghost = Image.open(os.path.join(PRESS, "ghost-pile-trophy.png")).convert("RGBA")
    gw, gh = ghost.size
    nh = 130
    nw = round(gw * nh / gh)
    ghost = ghost.resize((nw, nh), Image.LANCZOS)
    img.paste(ghost, (72, 938), ghost)
    # official lockup, proportional, width 400 -> height 123, top 948 ends 1071
    paste_proportional(img, os.path.join(PRESS, "lockup-2400.png"), 400, 700, 948)
    img.save(os.path.join(OUT, "candidate-a.png"))
    print("candidate-a.png written")

# ---------------------------------------------------------------- Candidate B
def candidate_b():
    W = H = 1080
    img = Image.new("RGB", (W, H), CANVAS_D)
    d = ImageDraw.Draw(img)
    # magenta top strip
    d.rectangle([0, 0, W, 14], fill=MAG_D)
    # eyebrow
    f_eye = font(SANS_B, 36)
    d.text((72, 62), "ONE POST. ONE BOUNTY. $100.", font=f_eye, fill=PINK_D)
    # headline, auto-fit to the 936px content width
    lines = ["WHAT'S THE", "WILDEST", "BOUNTY YOU'D", "POST?"]
    f_h = fit_font(SANS_B, 128, 936, lines, d)
    lh = 130  # line height at fitted size
    d.text((68, 128), lines[0], font=f_h, fill=INK_D)
    d.text((68, 128 + lh), lines[1], font=f_h, fill=PINK_D)
    d.text((68, 128 + 2 * lh), lines[2], font=f_h, fill=INK_D)
    d.text((68, 128 + 3 * lh), lines[3], font=f_h, fill=INK_D)
    # receipt card (content ends inside the card: rows 748/792/836, divider 884, TOTAL 896-930, card bottom 944)
    card = [72, 660, 1008, 944]
    rounded_card(d, card, "#FFFFFF", "#FFFFFF", radius=18, width=2)
    f_rec_h = font(MONO_B, 30)
    f_rec = font(SANS, 34)
    f_rec_b = font(SANS_B, 34)
    f_pr = font(MONO_B, 34)
    d.text((104, 680), "RECEIPT  —  1 x WILD IDEA", font=f_rec_h, fill=SEC_L)
    d.line([104, 728, 976, 728], fill=HAIR_L, width=2)
    rows = [
        ("Build a game that plays itself", "$50"),
        ("Teach my goldfish Excel", "$10"),
        ("An AI for my group chat", "$25"),
    ]
    y = 748
    for label, price in rows:
        d.text((104, y), label, font=f_rec, fill=INK_L)
        pw = text_w(d, price, f_pr)
        d.text((976 - pw, y), price, font=f_pr, fill=MAG_L)
        y += 44
    d.line([104, 884, 976, 884], fill=HAIR_L, width=2)
    d.text((104, 896), "TOTAL", font=f_rec_b, fill=INK_L)
    d.text((976 - text_w(d, "1 GOOD IDEA", f_rec_b), 896), "1 GOOD IDEA", font=f_rec_b, fill=MAG_L)
    # ghost spyglass, bottom-left footer zone (ends 956+116=1072)
    ghost = Image.open(os.path.join(PRESS, "ghost-spyglass.png")).convert("RGBA")
    gw, gh = ghost.size
    nh = 116
    nw = round(gw * nh / gh)
    ghost = ghost.resize((nw, nh), Image.LANCZOS)
    img.paste(ghost, (72, 956), ghost)
    # official lockup on dark, proportional, width 400 -> height 123, top 948 ends 1071
    paste_proportional(img, os.path.join(PRESS, "lockup-on-dark-2400.png"), 400, 700, 948)
    img.save(os.path.join(OUT, "candidate-b.png"))
    print("candidate-b.png written")

candidate_a()
candidate_b()
