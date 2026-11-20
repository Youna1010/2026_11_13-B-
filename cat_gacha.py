import os
import random
import tkinter as tk
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cats_data = [
    {"file": "a.jpg", "name": "白猫", "rarity": "N", "weight": 30},
    {"file": "b.jpg", "name": "ラグドール", "rarity": "SSR", "weight": 10},
    {"file": "c.jpg", "name": "三毛猫", "rarity": "SR", "weight": 15},
    {"file": "d.jpg", "name": "シャム", "rarity": "SR", "weight": 15},
    {"file": "e.jpg", "name": "キジトラ", "rarity": "N", "weight": 30},
]

RARITY_COLORS = {
    "N": "#5C4033",
    "SR": "#E67E22",
    "SSR": "#E91E63",
}

BG_COLOR = "#FFF8E7"
TEXT_COLOR = "#5C4033"
BTN_COLOR = "#FF85A1"
collected_cats = set()


def draw_gacha():
    weights = [cat["weight"] for cat in cats_data]
    chosen_cat = random.choices(cats_data, weights=weights, k=1)[0]

    image_path = os.path.join(BASE_DIR, chosen_cat["file"])
    img = Image.open(image_path)
    img = img.resize((250, 250))
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo, bg="white", width=0, height=0)
    image_label.photo = photo

    rarity = chosen_cat["rarity"]
    color = RARITY_COLORS[rarity]

    if rarity == "SSR":
        msg = f'✨【{rarity}】「{chosen_cat["name"]}」が当たりました！✨'
    else:
        msg = f'【{rarity}】「{chosen_cat["name"]}」が当たりました！'

    result_label.config(text=msg, fg=color)
    collected_cats.add(chosen_cat["name"])


def open_zukan():
    zukan_win = tk.Toplevel(root)
    zukan_win.title("猫図鑑")
    zukan_win.geometry("620x480")
    zukan_win.configure(bg=BG_COLOR)

    count = len(collected_cats)
    total = len(cats_data)
    header_text = f"📖 集めた猫図鑑（{count} / {total} 種類）"
    if count == total:
        header_text += "\n🎉 コンプリートおめでとう！ 🎉"

    header = tk.Label(
        zukan_win,
        text=header_text,
        font=("メイリオ", 14, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR,
    )
    header.pack(pady=12)

    grid_frame = tk.Frame(zukan_win, bg=BG_COLOR)
    grid_frame.pack(pady=5)

    zukan_win.photos = []

    for index, cat in enumerate(cats_data):
        row = index // 3
        col = index % 3

        card = tk.Frame(grid_frame, bg="#FFF0D6", padx=12, pady=10)
        card.grid(row=row, column=col, padx=10, pady=10)

        if cat["name"] in collected_cats:
            image_path = os.path.join(BASE_DIR, cat["file"])
            img = Image.open(image_path).resize((110, 110))
            photo = ImageTk.PhotoImage(img)
            zukan_win.photos.append(photo)

            pic_label = tk.Label(card, image=photo, bg="white")
            pic_label.pack()

            rarity = cat["rarity"]
            name_text = f"[{rarity}] {cat['name']}"
            label_color = RARITY_COLORS[rarity]
        else:
            pic_label = tk.Label(
                card,
                text="？",
                font=("メイリオ", 28, "bold"),
                bg="#FFE4E1",
                fg=TEXT_COLOR,
                width=5,
                height=2,
            )
            pic_label.pack()
            name_text = "？？？"
            label_color = TEXT_COLOR

        name_label = tk.Label(
            card,
            text=name_text,
            font=("メイリオ", 10, "bold"),
            bg="#FFF0D6",
            fg=label_color,
        )
        name_label.pack(pady=(6, 0))


root = tk.Tk()
root.title("猫ガチャガチャゲーム")
root.geometry("500x580")
root.configure(bg=BG_COLOR)

title = tk.Label(
    root,
    text="🐾 猫ガチャガチャ 🐾",
    font=("メイリオ", 20, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
title.pack(pady=15)

image_label = tk.Label(root, bg="#FFE4E1", width=32, height=15)
image_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="ボタンを押してガチャを引こう！",
    font=("メイリオ", 13, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
result_label.pack(pady=10)

btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=10)

gacha_button = tk.Button(
    btn_frame,
    text="ガチャを引く！",
    font=("メイリオ", 15, "bold"),
    bg=BTN_COLOR,
    fg="white",
    activebackground="#FF5C8A",
    activeforeground="white",
    padx=18,
    pady=6,
    command=draw_gacha,
)
gacha_button.pack(side="left", padx=8)

zukan_button = tk.Button(
    btn_frame,
    text="📖 図鑑を見る",
    font=("メイリオ", 15, "bold"),
    bg="#FFB347",
    fg="white",
    activebackground="#FFA07A",
    activeforeground="white",
    padx=18,
    pady=6,
    command=open_zukan,
)
zukan_button.pack(side="left", padx=8)

root.mainloop()