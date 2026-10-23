
from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Một bức thư dành cho em</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=Dancing+Script:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
:root {
    --night: #111b2b;
    --paper: #f8f0df;
    --ink: #4b352f;
    --rose: #a34f63;
    --gold: #b58a55;
}

* { box-sizing: border-box; }

body {
    margin: 0;
    min-height: 100vh;
    overflow-x: hidden;
    color: #f8eee3;
    font-family: 'Be Vietnam Pro', sans-serif;
    background:
        radial-gradient(ellipse at 50% 15%, #30415a, transparent 48%),
        radial-gradient(ellipse at 15% 85%, #243047, transparent 42%),
        linear-gradient(145deg, #0b1321, var(--night) 55%, #101a29);
    display: grid;
    place-items: center;
    padding: 34px 16px;
    position: relative;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    opacity: .34;
    background-image:
        radial-gradient(1px 1px at 8% 15%, #fff 98%, transparent),
        radial-gradient(1px 1px at 22% 72%, #fff 98%, transparent),
        radial-gradient(1.5px 1.5px at 78% 19%, #fff 98%, transparent),
        radial-gradient(1px 1px at 88% 66%, #fff 98%, transparent),
        radial-gradient(1px 1px at 48% 8%, #fff 98%, transparent),
        radial-gradient(1px 1px at 63% 83%, #fff 98%, transparent);
    background-size: 270px 240px;
    animation: stars 28s linear infinite;
}

.ambient-glow {
    position: fixed;
    width: 340px;
    height: 340px;
    border-radius: 50%;
    background: #d1a56a;
    opacity: .045;
    filter: blur(70px);
    top: 12%;
    left: 50%;
    transform: translateX(-50%);
    pointer-events: none;
}

.page-shell {
    width: min(100%, 790px);
    position: relative;
    z-index: 1;
    text-align: center;
    animation: fadeUp 1s ease both;
}

.eyebrow {
    color: #d6b990;
    font-size: 10px;
    letter-spacing: .34em;
    text-transform: uppercase;
    margin-bottom: 14px;
}

h1 {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 400;
    font-size: clamp(38px, 7vw, 58px);
    line-height: 1.04;
    margin: 0;
    color: #fff5e7;
    text-shadow: 0 4px 25px #0005;
}

.subtitle {
    color: #d4c5b2;
    font-size: 13px;
    font-weight: 300;
    margin: 15px auto 0;
    line-height: 1.8;
}

.ornament {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin: 23px auto 27px;
    color: #c8a16f;
}

.ornament::before, .ornament::after {
    content: "";
    height: 1px;
    width: 54px;
    background: linear-gradient(90deg, transparent, #c8a16f);
}

.ornament::after { transform: scaleX(-1); }

.ornament span {
    font-size: 17px;
    animation: pulse 2.4s ease-in-out infinite;
}

.envelope-wrap {
    width: min(330px, 82vw);
    margin: 0 auto;
    perspective: 1000px;
    filter: drop-shadow(0 24px 35px #0005);
}

.envelope {
    height: 218px;
    position: relative;
    cursor: pointer;
    outline: none;
    transform-style: preserve-3d;
    transition: transform .5s ease;
}

.envelope:hover { transform: translateY(-5px) rotate(-.6deg); }

.envelope:focus-visible {
    outline: 2px solid #d6b990;
    outline-offset: 8px;
    border-radius: 6px;
}

.envelope-back {
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, #ead4b3, #c49b71);
    border-radius: 5px 5px 8px 8px;
    border: 1px solid #f0d9b8;
}

.envelope-paper {
    position: absolute;
    left: 7%;
    right: 7%;
    bottom: 9px;
    height: 78%;
    border-radius: 3px;
    background: linear-gradient(135deg, #fff9ec, #eadcc2);
    box-shadow: 0 2px 12px #4a2c1b22;
    transition: transform .8s cubic-bezier(.2,.75,.25,1);
}

.envelope-paper::before {
    content: "Pour toi";
    position: absolute;
    top: 22px;
    left: 0;
    right: 0;
    font-family: 'Dancing Script', cursive;
    font-size: 28px;
    color: #9d5361;
    transform: rotate(-4deg);
}

.envelope-front {
    position: absolute;
    inset: 0;
    border-radius: 5px 5px 8px 8px;
    overflow: hidden;
    background: linear-gradient(145deg, #d8b58a, #b8875e);
    clip-path: polygon(0 0, 50% 54%, 100% 0, 100% 100%, 0 100%);
}

.envelope-front::before, .envelope-front::after {
    content: "";
    position: absolute;
    bottom: 0;
    width: 0;
    height: 0;
    border-style: solid;
}

.envelope-front::before {
    left: 0;
    border-width: 0 0 218px 50%;
    border-color: transparent transparent #c69a6b transparent;
}

.envelope-front::after {
    right: 0;
    border-width: 218px 0 0 50%;
    border-color: transparent transparent transparent #d2a779;
}

.envelope-flap {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 60%;
    background: linear-gradient(145deg, #f0d8b2, #c69a6b);
    clip-path: polygon(0 0, 100% 0, 50% 100%);
    transform-origin: top center;
    transition: transform .65s ease, opacity .35s ease;
    z-index: 3;
    backface-visibility: hidden;
}

.wax-seal {
    position: absolute;
    z-index: 4;
    left: 50%;
    top: 48%;
    transform: translate(-50%, -50%);
    width: 42px;
    height: 42px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    color: #f4d9b5;
    font-family: 'Cormorant Garamond', serif;
    font-size: 24px;
    background: radial-gradient(circle at 35% 25%, #bd6574, #7e2f43 70%);
    box-shadow: 0 3px 10px #51202b55, inset 0 0 0 1px #e7a0a6aa, inset 0 0 0 4px #8c3c4e;
    transition: opacity .3s ease, transform .4s ease;
}

.envelope.open .envelope-flap {
    transform: rotateX(180deg);
    opacity: 0;
}

.envelope.open .wax-seal {
    opacity: 0;
    transform: translate(-50%, -50%) scale(.5);
}

.envelope.open .envelope-paper { transform: translateY(-105px); }

.open-hint {
    margin: 20px auto 0;
    color: #d9cbb8;
    font-size: 12px;
    letter-spacing: .04em;
}

.open-button {
    border: 1px solid #c5a174;
    color: #f8e9d3;
    background: linear-gradient(135deg, #6e3e4b, #482b3a);
    border-radius: 999px;
    padding: 13px 25px;
    margin-top: 21px;
    font: 500 12px 'Be Vietnam Pro', sans-serif;
    letter-spacing: .04em;
    cursor: pointer;
    box-shadow: 0 8px 25px #0003, inset 0 1px #ffffff1a;
    transition: transform .25s ease, box-shadow .25s ease;
}

.open-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px #0005;
}

.letter-overlay {
    position: fixed;
    inset: 0;
    z-index: 10;
    display: grid;
    place-items: center;
    padding: 22px 12px;
    background: #090f19d9;
    backdrop-filter: blur(9px);
    opacity: 0;
    visibility: hidden;
    transition: opacity .45s ease, visibility .45s ease;
    overflow-y: auto;
}

.letter-overlay.visible { opacity: 1; visibility: visible; }

.letter-card {
    width: min(100%, 670px);
    max-height: calc(100vh - 44px);
    overflow-y: auto;
    position: relative;
    text-align: left;
    color: var(--ink);
    padding: clamp(27px, 5vw, 48px) clamp(22px, 6vw, 55px) 34px;
    background:
        radial-gradient(ellipse at 15% 10%, #fffdf2 0%, transparent 34%),
        radial-gradient(ellipse at 90% 85%, #e8d4b6 0%, transparent 35%),
        repeating-linear-gradient(0deg, #795b3710 0, #795b3710 1px, transparent 1px, transparent 4px),
        linear-gradient(135deg, #fff9ed, var(--paper) 60%, #f0e0c7);
    border: 1px solid #c5a06b;
    box-shadow: 0 25px 80px #0008, inset 0 0 0 5px #f9efd9, inset 0 0 0 6px #c7a477;
    transform: translateY(25px) scale(.97);
    transition: transform .6s cubic-bezier(.2,.8,.2,1);
    scrollbar-color: #c5a477 transparent;
    scrollbar-width: thin;
}

.letter-overlay.visible .letter-card { transform: translateY(0) scale(1); }

.letter-card::before, .letter-card::after {
    content: "❧";
    position: absolute;
    color: #b58a55;
    font-family: 'Cormorant Garamond', serif;
    font-size: 28px;
    opacity: .75;
    pointer-events: none;
}

.letter-card::before { top: 14px; left: 19px; }
.letter-card::after { bottom: 10px; right: 20px; transform: rotate(180deg); }

.paper-topline {
    text-align: center;
    color: #a0784d;
    font-size: 9px;
    letter-spacing: .28em;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.letter-heading {
    text-align: center;
    margin: 0;
    color: #75414b;
    font: 500 clamp(30px, 6vw, 43px)/1.1 'Dancing Script', cursive;
}

.letter-subheading {
    text-align: center;
    margin: 8px 0 0;
    color: #a17a64;
    font: italic 14px 'Cormorant Garamond', serif;
    letter-spacing: .06em;
}

.tiny-divider {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 9px;
    color: #ad7c5b;
    margin: 22px auto 23px;
    font-size: 12px;
}

.tiny-divider::before, .tiny-divider::after {
    content: "";
    height: 1px;
    width: 48px;
    background: linear-gradient(90deg, transparent, #bd9b70);
}

.tiny-divider::after { transform: scaleX(-1); }

.letter-body {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(18px, 2.6vw, 21px);
    font-weight: 500;
    line-height: 1.75;
    letter-spacing: .005em;
    color: #4d3932;
}

.letter-body p { margin: 0 0 17px; }

.letter-body .highlight {
    color: #874657;
    font-style: italic;
    font-weight: 600;
}

.letter-closing {
    text-align: center;
    margin: 23px auto 5px;
    color: #945365;
    font: italic 19px/1.55 'Cormorant Garamond', serif;
}

.closing-heart {
    display: block;
    color: #a9576a;
    font-size: 17px;
    margin-top: 8px;
    animation: pulse 2.2s ease-in-out infinite;
}

.signature {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-top: 17px;
    padding: 5px 4px 7px;
    color: #a45f79;
    font-family: 'Dancing Script', cursive;
    font-weight: 600;
    text-shadow: 0 2px 6px #d9aab922;
}

.signature-first {
    font-size: 31px;
    line-height: 1.15;
    transform: rotate(-4deg);
}

.signature-last {
    font: italic 13px 'Cormorant Garamond', serif;
    letter-spacing: .08em;
    margin-top: 5px;
    color: #8c665c;
}

.signature::after {
    content: "♡";
    display: block;
    margin-top: 1px;
    font-family: 'Be Vietnam Pro', sans-serif;
    font-size: 12px;
    color: #c18a9e;
}

.letter-footer {
    border-top: 1px solid #c9aa7d88;
    margin-top: 20px;
    padding-top: 13px;
    text-align: center;
    color: #987d68;
    font: italic 13px 'Cormorant Garamond', serif;
}

.close-button {
    position: sticky;
    top: 0;
    float: right;
    z-index: 5;
    width: 31px;
    height: 31px;
    margin: -13px -15px 0 10px;
    border: 1px solid #c9aa7d;
    border-radius: 50%;
    background: #f7ecd7;
    color: #865564;
    font-size: 19px;
    line-height: 1;
    cursor: pointer;
}

.petal {
    position: fixed;
    top: -30px;
    z-index: 8;
    pointer-events: none;
    color: #d9a3a6;
    opacity: 0;
    animation: petalFall linear forwards;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes stars {
    from { background-position: 0 0; }
    to { background-position: 270px 240px; }
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: .8; }
    50% { transform: scale(1.16); opacity: 1; }
}

@keyframes petalFall {
    0% { opacity: 0; transform: translate3d(0,-10px,0) rotate(0deg); }
    10% { opacity: .85; }
    90% { opacity: .7; }
    100% { opacity: 0; transform: translate3d(var(--drift),110vh,0) rotate(500deg); }
}

@media (max-width: 600px) {
    body { padding: 28px 15px; }
    .eyebrow { font-size: 9px; letter-spacing: .24em; }
    .subtitle { max-width: 290px; font-size: 12px; }
    .envelope { height: 190px; }
    .envelope-front::before { border-width: 0 0 190px 50%; }
    .envelope-front::after { border-width: 190px 0 0 50%; }
    .envelope-paper::before { font-size: 25px; }
    .letter-overlay { padding: 12px 8px; align-items: start; }
    .letter-card {
        max-height: calc(100dvh - 24px);
        padding: 34px 23px 29px;
        box-shadow: 0 20px 60px #0008, inset 0 0 0 4px #f9efd9, inset 0 0 0 5px #c7a477;
    }
    .letter-card::before { top: 13px; left: 15px; font-size: 23px; }
    .letter-card::after { bottom: 7px; right: 15px; font-size: 23px; }
    .paper-topline { font-size: 8px; letter-spacing: .2em; }
    .letter-body { font-size: 19px; line-height: 1.7; }
    .letter-body p { margin-bottom: 15px; }
    .letter-closing { font-size: 18px; }
    .signature { margin-top: 13px; }
    .signature-first { font-size: 28px; }
    .signature-last { font-size: 12px; }
    .close-button { margin: -20px -10px 0 8px; }
}

@media (max-width: 360px) {
    .letter-card { padding-left: 19px; padding-right: 19px; }
    .letter-body { font-size: 18px; }
    .signature-first { font-size: 26px; }
    .signature-last { font-size: 11px; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
        scroll-behavior: auto !important;
        transition-duration: .01ms !important;
    }
}
</style>
</head>

<body>
<div class="ambient-glow"></div>

<main class="page-shell">
    <div class="eyebrow">A little letter, just for you</div>
    <h1>Một bức thư dành cho em</h1>
    <p class="subtitle">Có vài điều anh muốn gửi em, bằng tất cả sự chân thành.</p>

    <div class="ornament"><span>♡</span></div>

    <div class="envelope-wrap">
        <div class="envelope" id="envelope" role="button" tabindex="0" aria-label="Mở phong bì thư">
            <div class="envelope-back"></div>
            <div class="envelope-paper"></div>
            <div class="envelope-front"></div>
            <div class="envelope-flap"></div>
            <div class="wax-seal">Đ</div>
        </div>
    </div>

    <p class="open-hint">Một lá thư nhỏ, dành riêng cho em.</p>
    <button class="open-button" id="openButton" type="button">Mở lá thư ♡</button>
</main>

<div class="letter-overlay" id="letterOverlay" aria-hidden="true">
    <article class="letter-card" role="dialog" aria-modal="true" aria-labelledby="letterTitle">
        <button class="close-button" id="closeButton" type="button" aria-label="Đóng thư">×</button>

        <div class="paper-topline">A letter from the heart</div>
        <h2 class="letter-heading" id="letterTitle">Gửi em,</h2>
        <p class="letter-subheading">một vài điều anh vẫn muốn nói</p>
        <div class="tiny-divider">❦</div>

        <div class="letter-body">
            <p>Anh không biết sau này chúng ta sẽ đi cùng nhau được bao lâu. Có thể sẽ còn rất nhiều chuyện để kể nhau nghe, cũng có thể đến một ngày nào đó, chúng ta chẳng còn nói chuyện với nhau nữa.</p>

            <p>Nếu ngày đó thật sự đến, anh chỉ mong em vẫn luôn vui vẻ, vẫn gặp được những điều tốt đẹp và vẫn nở nụ cười trên môi như bây giờ.</p>

            <p>Anh không biết em có nhận ra không, nhưng mỗi lần em cười, <span class="highlight">trông em thật sự rất xinh.</span> Có lẽ sau này anh sẽ không còn là người được nhìn thấy nụ cười ấy thường xuyên nữa, nhưng anh vẫn mong sẽ luôn có những người khiến em cười thật nhiều.</p>

            <p>Anh không viết những dòng này để khiến em buồn, cũng chẳng mong em phải hứa hẹn điều gì. Chỉ là anh nghĩ, nếu đã có cơ hội gặp một người khiến mình thấy vui vẻ, thì dù sau này kết quả ra sao, mình vẫn nên trân trọng khoảng thời gian ấy.</p>

            <p>Vậy nên, nếu một ngày anh không còn xuất hiện trong những tin nhắn của em nữa, em cũng đừng quên cười nhé. Vì thật lòng mà nói, anh thấy khi cười nhìn em xinh hơn rất nhiều.</p>

            <p>Mong em luôn vui, không chỉ khi có anh, mà cả trong những ngày chẳng có anh bên cạnh.</p>
        </div>

        <div class="letter-closing">
            Mong những ngày của em luôn có điều gì đó đáng để mỉm cười.
            <span class="closing-heart">♡</span>
        </div>

        <div class="signature">
            <span class="signature-first">Đăng</span>
            <span class="signature-last">Ngô Văn Đăng</span>
        </div>

        <div class="letter-footer">được viết bằng một chút nhớ thương</div>
    </article>
</div>

<script>
const envelope = document.getElementById('envelope');
const openButton = document.getElementById('openButton');
const overlay = document.getElementById('letterOverlay');
const closeButton = document.getElementById('closeButton');

function openLetter() {
    envelope.classList.add('open');
    overlay.classList.add('visible');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    createPetals(13);
    window.setTimeout(() => closeButton.focus(), 350);
}

function closeLetter() {
    overlay.classList.remove('visible');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    envelope.classList.remove('open');
    openButton.focus();
}

function createPetals(count) {
    const symbols = ['✦', '♡', '❀', '·'];

    for (let i = 0; i < count; i++) {
        const petal = document.createElement('span');
        petal.className = 'petal';
        petal.textContent = symbols[Math.floor(Math.random() * symbols.length)];
        petal.style.left = (Math.random() * 100) + 'vw';
        petal.style.fontSize = (10 + Math.random() * 12) + 'px';
        petal.style.setProperty('--drift', (Math.random() * 160 - 80) + 'px');
        petal.style.animationDuration = (4 + Math.random() * 4) + 's';
        petal.style.animationDelay = (Math.random() * 1.3) + 's';
        document.body.appendChild(petal);
        window.setTimeout(() => petal.remove(), 9000);
    }
}

envelope.addEventListener('click', openLetter);

envelope.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        openLetter();
    }
});

openButton.addEventListener('click', openLetter);
closeButton.addEventListener('click', closeLetter);

overlay.addEventListener('click', (event) => {
    if (event.target === overlay) closeLetter();
});

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && overlay.classList.contains('visible')) {
        closeLetter();
    }
});
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
