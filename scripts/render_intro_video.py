from __future__ import annotations

import math
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH = 1280
HEIGHT = 720
FPS = 24


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUTPUT = ASSETS / "review-intro-zh.mp4"


SOCIAL = Image.open(ASSETS / "social-preview-zh-CN.png").convert("RGBA")
OVERVIEW = Image.open(ASSETS / "overview-zh-CN.png").convert("RGBA")


FONT_CANDIDATES = {
    "regular": [
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ],
    "bold": [
        Path("C:/Windows/Fonts/msyhbd.ttc"),
        Path("C:/Windows/Fonts/segoeuib.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf"),
    ],
    "mono": [
        Path("C:/Windows/Fonts/consola.ttf"),
        Path("C:/Windows/Fonts/cour.ttf"),
    ],
}


def load_font(size: int, kind: str = "regular") -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES.get(kind, []):
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


TITLE = load_font(64, "bold")
SUBTITLE = load_font(30, "regular")
BODY = load_font(25, "regular")
BODY_BOLD = load_font(25, "bold")
SMALL = load_font(18, "regular")
MONO = load_font(26, "mono")


def ease_out_cubic(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return 1 - pow(1 - x, 3)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def gradient_background(top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    arr = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    for y in range(HEIGHT):
        t = y / max(1, HEIGHT - 1)
        color = [int(lerp(top[i], bottom[i], t)) for i in range(3)]
        arr[y, :, :] = color
    return Image.fromarray(arr, "RGB").convert("RGBA")


def draw_soft_glow(base: Image.Image, center: tuple[int, int], radius: int, color: tuple[int, int, int, int]) -> None:
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    x, y = center
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=40))
    base.alpha_composite(overlay)


def wrap_text(text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        candidate = current + ch
        width = font.getbbox(candidate)[2]
        if current and width > max_width:
            lines.append(current.rstrip())
            current = ch
        else:
            current = candidate
    if current:
        lines.append(current.rstrip())
    return lines


def draw_text_block(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], font: ImageFont.ImageFont, fill: tuple[int, int, int], max_width: int, line_gap: int = 10) -> int:
    x, y = xy
    lines = wrap_text(text, font, max_width)
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        bbox = font.getbbox(line)
        y += (bbox[3] - bbox[1]) + line_gap
    return y


def rounded_card(size: tuple[int, int], fill: tuple[int, int, int, int], radius: int = 28, outline: tuple[int, int, int, int] | None = None) -> Image.Image:
    w, h = size
    card = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle((0, 0, w, h), radius=radius, fill=fill, outline=outline, width=2 if outline else 0)
    return card


def card_with_shadow(size: tuple[int, int], fill: tuple[int, int, int, int], radius: int = 28, outline: tuple[int, int, int, int] | None = None) -> Image.Image:
    w, h = size
    shadow = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((20, 20, 20 + w, 20 + h), radius=radius, fill=(0, 0, 0, 110))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=16))
    card = rounded_card(size, fill, radius, outline)
    shadow.alpha_composite(card, (20, 20))
    return shadow


def paste_panel(base: Image.Image, panel: Image.Image, box: tuple[int, int, int, int], offset_x: int = 0, offset_y: int = 0) -> None:
    x0, y0, x1, y1 = box
    target_w = x1 - x0
    target_h = y1 - y0
    ratio = min(target_w / panel.width, target_h / panel.height)
    resized = panel.resize((int(panel.width * ratio), int(panel.height * ratio)), Image.Resampling.LANCZOS)
    px = x0 + (target_w - resized.width) // 2 + offset_x
    py = y0 + (target_h - resized.height) // 2 + offset_y
    base.alpha_composite(resized, (px, py))


def add_footer(draw: ImageDraw.ImageDraw) -> None:
    footer = "wxmb01/review-skill  •  Evidence-based review for PRs, projects, and technical artifacts"
    draw.text((52, HEIGHT - 40), footer, font=SMALL, fill=(220, 232, 240))


def scene_hero(t: float, duration: float) -> Image.Image:
    p = ease_out_cubic(t / duration)
    frame = gradient_background((9, 22, 45), (4, 70, 86))
    draw_soft_glow(frame, (1050, 160), 240, (56, 189, 248, 70))
    draw_soft_glow(frame, (180, 560), 220, (16, 185, 129, 75))
    draw = ImageDraw.Draw(frame)

    title_x = int(72 - 40 * (1 - p))
    draw.text((title_x, 86), "Review", font=TITLE, fill=(250, 252, 255))
    draw_text_block(
        draw,
        "一个面向 PR、项目与技术文档的证据驱动型评审 skill",
        (title_x, 168),
        SUBTITLE,
        (220, 235, 242),
        480,
        8,
    )
    chip_y = 274
    for idx, label in enumerate(["PR 审查", "项目评审", "上线准备度"]):
        cx = title_x + idx * 150
        chip = rounded_card((132, 42), (255, 255, 255, 24), radius=20, outline=(255, 255, 255, 50))
        frame.alpha_composite(chip, (cx, chip_y))
        draw.text((cx + 18, chip_y + 10), label, font=SMALL, fill=(240, 248, 252))

    panel = card_with_shadow((520, 330), (6, 18, 33, 230), radius=32, outline=(255, 255, 255, 20))
    panel_x = int(694 + 30 * (1 - p))
    panel_y = 110
    frame.alpha_composite(panel, (panel_x, panel_y))
    paste_panel(frame, SOCIAL, (panel_x + 22, panel_y + 24, panel_x + 538, panel_y + 326), offset_y=int(12 * math.sin(t * 1.4)))
    add_footer(draw)
    return frame


def scene_questions(t: float, duration: float) -> Image.Image:
    p = ease_out_cubic(t / duration)
    frame = gradient_background((10, 24, 47), (7, 43, 59))
    draw_soft_glow(frame, (1120, 120), 180, (34, 197, 94, 55))
    draw = ImageDraw.Draw(frame)
    draw.text((70, 70), "它帮你回答什么问题？", font=TITLE, fill=(250, 252, 255))
    draw_text_block(draw, "从“代码能不能合并”到“项目到底完没完成”，都能给出结构化结论。", (70, 150), SUBTITLE, (217, 232, 240), 900)

    cards = [
        ("PR 能安全合并吗？", "给出严重级别、回归风险和合并建议"),
        ("项目真的完成了吗？", "给出完成度判断、证据缺口和下一步优先级"),
        ("现在能发布或提交吗？", "给出 readiness gates、风险和 caveats"),
    ]
    for idx, (title, body) in enumerate(cards):
        card = card_with_shadow((350, 205), (255, 255, 255, 20), radius=28, outline=(255, 255, 255, 36))
        x = 70 + idx * 386
        y = int(290 + (1 - p) * 32 * (idx + 1))
        frame.alpha_composite(card, (x, y))
        draw.text((x + 34, y + 34), title, font=BODY_BOLD, fill=(248, 252, 255))
        draw_text_block(draw, body, (x + 34, y + 88), BODY, (218, 232, 239), 280)
    add_footer(draw)
    return frame


def scene_scopes(t: float, duration: float) -> Image.Image:
    p = ease_out_cubic(t / duration)
    frame = gradient_background((8, 19, 37), (19, 44, 77))
    draw_soft_glow(frame, (180, 110), 150, (59, 130, 246, 70))
    draw = ImageDraw.Draw(frame)
    draw.text((70, 70), "三种范围，一套工作流", font=TITLE, fill=(250, 252, 255))
    scopes = [
        ("change", "PR、diff、commit", "回归风险、影响范围、合并建议"),
        ("project", "完整仓库或交付状态", "完成度、准备度、整改路线图"),
        ("artifact", "文档、设计稿、计划", "需求缺口、歧义、取舍分析"),
    ]
    for idx, (name, audience, result) in enumerate(scopes):
        box = card_with_shadow((280, 160), (255, 255, 255, 16), radius=26, outline=(255, 255, 255, 28))
        x = 70
        y = 182 + idx * 170
        frame.alpha_composite(box, (x, y))
        draw.text((x + 28, y + 28), name, font=BODY_BOLD, fill=(255, 255, 255))
        draw_text_block(draw, audience, (x + 28, y + 64), BODY, (211, 228, 238), 220)
        draw_text_block(draw, result, (x + 28, y + 104), SMALL, (172, 205, 219), 220, 6)

    panel = card_with_shadow((660, 460), (8, 18, 32, 228), radius=32, outline=(255, 255, 255, 24))
    px = int(536 + 28 * (1 - p))
    py = 170
    frame.alpha_composite(panel, (px, py))
    paste_panel(frame, OVERVIEW, (px + 22, py + 24, px + 638, py + 436), offset_y=int(10 * math.sin(t)))
    add_footer(draw)
    return frame


def scene_languages(t: float, duration: float) -> Image.Image:
    p = ease_out_cubic(t / duration)
    frame = gradient_background((12, 24, 42), (30, 56, 48))
    draw_soft_glow(frame, (1020, 580), 200, (16, 185, 129, 70))
    draw = ImageDraw.Draw(frame)
    draw.text((70, 70), "Code Review 语言专精版", font=TITLE, fill=(250, 252, 255))
    draw_text_block(draw, "不只做通用 code review，还会按技术栈切换更专业的审查视角。", (70, 150), SUBTITLE, (220, 235, 242), 1000)

    cards = [
        ("TypeScript / React", ["类型边界与 runtime 校验", "state / effects / hydration 风险", "前端交互、性能与可访问性"]),
        ("Python", ["异常处理与资源清理", "async / 线程 / worker 安全", "数据模型、时间与事务边界"]),
        ("Java", ["对象语义与 null 安全", "事务、Spring 代理与并发", "集合、Streams 与兼容性"]),
    ]
    for idx, (title, bullets) in enumerate(cards):
        x = 70 + idx * 385
        y = int(272 + 24 * (1 - p) * (idx + 1))
        card = card_with_shadow((350, 300), (255, 255, 255, 18), radius=28, outline=(255, 255, 255, 36))
        frame.alpha_composite(card, (x, y))
        draw.text((x + 28, y + 28), title, font=BODY_BOLD, fill=(250, 252, 255))
        line_y = y + 84
        for bullet in bullets:
            draw.ellipse((x + 30, line_y + 10, x + 40, line_y + 20), fill=(56, 189, 248))
            draw_text_block(draw, bullet, (x + 52, line_y), BODY, (220, 233, 242), 255, 6)
            line_y += 72
    add_footer(draw)
    return frame


def scene_outputs(t: float, duration: float) -> Image.Image:
    p = ease_out_cubic(t / duration)
    frame = gradient_background((9, 21, 39), (14, 58, 79))
    draw_soft_glow(frame, (210, 600), 180, (45, 212, 191, 60))
    draw = ImageDraw.Draw(frame)
    draw.text((70, 70), "最终交付，不只是评论", font=TITLE, fill=(250, 252, 255))
    outputs = [
        "severity-ordered findings",
        "completion verdicts",
        "readiness scorecards",
        "risk registers",
        "requirements gap reports",
        "remediation roadmaps",
    ]
    y = 176
    for item in outputs:
        draw.rounded_rectangle((70, y, 480, y + 54), radius=18, fill=(255, 255, 255, 18))
        draw.text((94, y + 13), item, font=BODY, fill=(240, 247, 250))
        y += 68

    panel = card_with_shadow((640, 420), (8, 18, 32, 230), radius=32, outline=(255, 255, 255, 22))
    px = int(568 + 22 * (1 - p))
    py = 168
    frame.alpha_composite(panel, (px, py))
    paste_panel(frame, OVERVIEW, (px + 22, py + 22, px + 618, py + 398))
    add_footer(draw)
    return frame


def scene_cta(t: float, duration: float) -> Image.Image:
    p = ease_out_cubic(t / duration)
    frame = gradient_background((4, 19, 34), (6, 48, 55))
    draw_soft_glow(frame, (1100, 110), 200, (14, 165, 233, 60))
    draw_soft_glow(frame, (180, 580), 160, (34, 197, 94, 52))
    draw = ImageDraw.Draw(frame)
    draw.text((70, 88), "现在就把它装进你的工作流", font=TITLE, fill=(250, 252, 255))
    draw_text_block(draw, "适合 GitHub 仓库、PR 审查、课程项目、发布前验收，以及架构和文档评审。", (70, 168), SUBTITLE, (220, 235, 242), 980)

    cmd_card = card_with_shadow((900, 112), (8, 18, 32, 236), radius=30, outline=(255, 255, 255, 22))
    cmd_x = 70
    cmd_y = int(292 + 18 * (1 - p))
    frame.alpha_composite(cmd_card, (cmd_x, cmd_y))
    draw.text((cmd_x + 28, cmd_y + 18), "npx skills add https://github.com/wxmb01/review-skill --skill review -g -y", font=MONO, fill=(133, 233, 193))

    draw.text((70, 466), "GitHub: github.com/wxmb01/review-skill", font=BODY_BOLD, fill=(248, 252, 255))
    draw.text((70, 512), "Review 让“看起来做完了”变成“有证据地判断是否真的做完了”。", font=BODY, fill=(220, 235, 242))
    draw.text((70, 558), "Evidence-based  •  Open source  •  Ready for real review workflows", font=SMALL, fill=(184, 212, 223))
    add_footer(draw)
    return frame


SCENES = [
    (4.0, scene_hero),
    (4.0, scene_questions),
    (4.0, scene_scopes),
    (4.5, scene_languages),
    (4.0, scene_outputs),
    (4.5, scene_cta),
]


def render_video() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    writer = imageio.get_writer(str(OUTPUT), fps=FPS, codec="libx264", quality=7, pixelformat="yuv420p")
    try:
        for duration, scene in SCENES:
            frame_count = int(duration * FPS)
            for frame_index in range(frame_count):
                t = frame_index / FPS
                frame = scene(t, duration).convert("RGB")
                writer.append_data(np.asarray(frame))
    finally:
        writer.close()


if __name__ == "__main__":
    render_video()
    print(f"Rendered {OUTPUT}")
