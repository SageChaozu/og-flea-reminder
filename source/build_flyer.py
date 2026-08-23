#!/usr/bin/env python3
import base64, pathlib

HERE = pathlib.Path(__file__).resolve().parent

def b64(p):
    return base64.b64encode(p.read_bytes()).decode()

YESEVA = b64(HERE / "fonts" / "YesevaOne.ttf")
PATRICK = b64(HERE / "fonts" / "PatrickHand.ttf")
CAND_LEFT = b64(HERE / "photos" / "final_cand_left.jpg")
CAND_RIGHT = b64(HERE / "photos" / "final_cand_right.jpg")

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OG's Flea-Free Mission</title>
<style>
@font-face{font-family:'Yeseva One';src:url(data:font/ttf;base64,%%YESEVA%%) format('truetype');font-weight:400;font-style:normal;}
@font-face{font-family:'Patrick Hand';src:url(data:font/ttf;base64,%%PATRICK%%) format('truetype');font-weight:400;font-style:normal;}

:root{
  --paper:#FFFFFF; --card:#FFFFFF; --panel:#FFFFFF; --white:#ffffff;
  --paper-2:#FFFFFF;
  --ink:#3B2A20; --ink-soft:#77604F;
  --sage:#7F9A6E; --sage-deep:#5E7A50;
  --rose:#C88793; --rose-deep:#A85E6C;
  --honey:#E2A950; --honey-deep:#A9781F; --mulberry:#9E5A66;
  --line:#E7D6BF;
  --display:'Yeseva One',Georgia,serif;
  --hand:'Patrick Hand','Comic Sans MS',cursive;
  --body:Georgia,'Times New Roman',serif;
}
*{box-sizing:border-box;}
@page{size:letter;margin:0;}
html,body{margin:0;padding:0;}
body{font-family:var(--body);color:var(--ink);background:var(--paper);
  width:8.5in;height:11in;padding:0.2in;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;}

.card{position:relative;height:100%;background:var(--card);
  border:2.5px solid var(--sage-deep);border-radius:8px;
  padding:0.30in 0.34in 0.26in;overflow:hidden;}
.card::before{content:"";position:absolute;top:6px;left:6px;right:6px;bottom:6px;
  border:1px solid var(--rose);opacity:.5;border-radius:5px;pointer-events:none;z-index:1;}
.inner{position:relative;height:100%;z-index:3;display:flex;flex-direction:column;justify-content:space-between;}

.corner{position:absolute;width:1.2in;height:auto;z-index:2;}
.corner.tl{top:6px;left:6px;}
.corner.tr{top:6px;right:6px;transform:scaleX(-1);}
.corner.bl{bottom:6px;left:6px;transform:scaleY(-1);}

/* header */
header{text-align:center;padding:2px 0 0;}
.eyebrow{font-family:var(--hand);font-size:17px;color:var(--rose-deep);margin:0;letter-spacing:.3px;}
h1{font-family:var(--display);font-size:37px;line-height:1;color:var(--mulberry);
  margin:4px 0 5px;letter-spacing:.4px;}
.subtitle{font-style:italic;font-size:13px;color:var(--ink-soft);margin:0;}
.flourish{display:flex;align-items:center;justify-content:center;gap:9px;margin:9px auto 0;}
.flourish .ln{height:1px;width:1.7in;background:linear-gradient(90deg,transparent,var(--line));}
.flourish .ln.r{background:linear-gradient(90deg,var(--line),transparent);}

/* photos */
.photos{display:flex;flex-direction:column;align-items:center;gap:0.16in;margin:0;}
.photo-row{display:flex;justify-content:center;align-items:flex-start;gap:0.44in;}
.photo-wrap{width:3.7in;position:relative;}
.polaroid{background:var(--white);border:1px solid #e6d5bd;border-radius:3px;
  padding:0.15in 0.15in 0.1in;box-shadow:0 1px 3px rgba(94,66,46,.13);position:relative;}
.tape{position:absolute;top:-0.15in;left:50%;margin-left:-0.55in;width:1.1in;height:0.36in;
  background:rgba(226,169,80,.45);border:1px solid rgba(168,94,108,.30);
  transform:rotate(-3deg);border-radius:2px;}
.tape::after{content:"";position:absolute;inset:0;
  background:repeating-linear-gradient(45deg,rgba(255,255,255,.4) 0 5px,transparent 5px 10px);}
.photo-slot{width:3.4in;height:2.73in;border-radius:0;background:var(--paper-2);
  margin:0 auto;overflow:hidden;line-height:0;}
.photo-slot img{width:100%;height:100%;display:block;}
.caption{font-family:var(--hand);text-align:center;color:var(--mulberry);
  font-size:17px;margin-top:8px;line-height:1;}
.heart-sm{width:13px;height:13px;vertical-align:-2px;}

/* two column */
.cols{display:table;width:100%;table-layout:fixed;margin-top:0;border-spacing:0;}
.col{display:table-cell;vertical-align:top;}
.col.left{width:47%;padding-right:0.16in;}
.col.right{width:53%;}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:7px;
  padding:11px 13px 10px;height:100%;}
.panel-title{font-family:var(--display);font-size:16px;color:var(--sage-deep);
  margin:0 0 8px;display:flex;align-items:center;gap:8px;}
.panel-title .dot{width:9px;height:9px;border-radius:50%;background:var(--honey);flex:none;
  box-shadow:0 0 0 3px rgba(226,169,80,.22);}

.rules{list-style:none;margin:0;padding:0;}
.rules li{position:relative;padding:0 0 9px 27px;font-size:11.3px;line-height:1.32;color:var(--ink);}
.rules li:last-child{padding-bottom:0;}
.rules .num{position:absolute;left:0;top:1px;width:19px;height:19px;border-radius:50%;
  background:var(--sage);color:#fff;font-family:var(--display);font-size:11px;text-align:center;line-height:19px;}
.rules b{color:var(--mulberry);}

.sched{width:100%;border-collapse:collapse;}
.sched tr{border-bottom:1px solid #efe2cf;}
.sched tr:last-child{border-bottom:none;}
.cell{padding:2px 0;}
.day{font-family:var(--display);font-size:10px;background:#fff;
  text-transform:uppercase;letter-spacing:.4px;text-align:center;padding:4px 3px;
  width:0.78in;vertical-align:middle;border-radius:3px;border:1.5px solid;}
.d-feature{border-color:var(--mulberry);color:var(--mulberry);}
.d-quick{border-color:var(--sage-deep);color:var(--sage-deep);}
.d-weekend{border-color:var(--honey);color:var(--honey-deep);}
.act{padding:4px 0 4px 9px;font-size:10.3px;line-height:1.25;vertical-align:middle;}
.act b{color:var(--mulberry);}
.act .steps{color:var(--ink-soft);}
.legend{font-family:var(--hand);font-size:11.5px;color:var(--rose-deep);margin:-2px 0 8px;}
.drop{width:8px;height:11px;vertical-align:-1px;}

/* countdown */
.count{margin-top:0;background:var(--panel);border:1px dashed var(--sage);
  border-radius:7px;padding:8px 12px 9px;text-align:center;}
.count .lbl{font-family:var(--hand);font-size:13.5px;color:var(--sage-deep);margin-bottom:6px;}
.count .lbl b{color:var(--mulberry);}
.dots{display:flex;justify-content:space-between;align-items:center;padding:0 2px;}
.chk{width:0.31in;height:0.31in;border:1.5px solid var(--rose);border-radius:50%;
  display:flex;align-items:center;justify-content:center;font-family:var(--display);
  font-size:9.5px;color:var(--rose-deep);background:var(--white);}

/* footer */
footer{margin-top:0;}
.foot{display:table;width:100%;table-layout:fixed;border-spacing:0;
  border-top:1px solid var(--line);padding-top:10px;}
.foot-cell{display:table-cell;vertical-align:middle;}
.foot-bug{width:1.1in;text-align:left;vertical-align:bottom;}
.foot-text{text-align:center;padding:0 6px;}
.foot-seal{width:1.3in;text-align:right;}
.quote{font-style:italic;font-size:12.5px;color:var(--ink);line-height:1.4;margin:0 0 7px;}
.signoff{font-family:var(--display);font-size:18px;color:var(--mulberry);}
.signoff .hh{width:16px;height:16px;vertical-align:-2px;}
.bugwink{width:0.95in;height:auto;}
.seal{width:1.12in;height:1.12in;transform:rotate(8deg);opacity:.9;}
</style>
</head>
<body>
<div class="card">

  <svg class="corner tl" viewBox="0 0 150 120"><g class="sprig">
    <path d="M6 8 C40 18 80 32 122 74" fill="none" stroke="#5E7A50" stroke-width="2.4" stroke-linecap="round"/>
    <g fill="#7F9A6E" stroke="#5E7A50" stroke-width="1">
      <ellipse cx="34" cy="14" rx="12" ry="6" transform="rotate(20 34 14)"/>
      <ellipse cx="58" cy="26" rx="13" ry="6.5" transform="rotate(28 58 26)"/>
      <ellipse cx="82" cy="44" rx="12" ry="6" transform="rotate(36 82 44)"/>
      <ellipse cx="24" cy="26" rx="10" ry="5" transform="rotate(-24 24 26)"/>
      <ellipse cx="48" cy="42" rx="11" ry="5.5" transform="rotate(-16 48 42)"/>
    </g>
    <g transform="translate(108,64)">
      <circle r="11" fill="#C88793" stroke="#A85E6C" stroke-width="1.2"/>
      <circle r="6.5" fill="#DBA6AF"/><circle r="2.6" fill="#A85E6C"/>
    </g>
    <circle cx="18" cy="9" r="3.8" fill="#E2A950"/><circle cx="11" cy="17" r="3.1" fill="#E2A950"/>
  </g></svg>
  <svg class="corner tr" viewBox="0 0 150 120"><g class="sprig">
    <path d="M6 8 C40 18 80 32 122 74" fill="none" stroke="#5E7A50" stroke-width="2.4" stroke-linecap="round"/>
    <g fill="#7F9A6E" stroke="#5E7A50" stroke-width="1">
      <ellipse cx="34" cy="14" rx="12" ry="6" transform="rotate(20 34 14)"/>
      <ellipse cx="58" cy="26" rx="13" ry="6.5" transform="rotate(28 58 26)"/>
      <ellipse cx="82" cy="44" rx="12" ry="6" transform="rotate(36 82 44)"/>
      <ellipse cx="24" cy="26" rx="10" ry="5" transform="rotate(-24 24 26)"/>
      <ellipse cx="48" cy="42" rx="11" ry="5.5" transform="rotate(-16 48 42)"/>
    </g>
    <g transform="translate(108,64)">
      <circle r="11" fill="#C88793" stroke="#A85E6C" stroke-width="1.2"/>
      <circle r="6.5" fill="#DBA6AF"/><circle r="2.6" fill="#A85E6C"/>
    </g>
    <circle cx="18" cy="9" r="3.8" fill="#E2A950"/><circle cx="11" cy="17" r="3.1" fill="#E2A950"/>
  </g></svg>

  <div class="inner">

    <header>
      <p class="eyebrow">a little note for the strongest lady we know &mdash;</p>
      <h1>OG&rsquo;s Flea&ndash;Free Mission</h1>
      <p class="subtitle">Two weeks, one spotless house, and a whole lot of love &mdash; Georgia style.</p>
      <div class="flourish"><span class="ln"></span>
        <svg width="17" height="17" viewBox="0 0 24 24"><path d="M12 21C12 21 3 14.6 3 8.9 3 5.6 5.5 3.4 8.3 3.4c1.9 0 3.1 1 3.7 2 .6-1 1.8-2 3.7-2C21.5 3.4 21 5.6 21 8.9 21 14.6 12 21 12 21Z" fill="#C88793" stroke="#A85E6C" stroke-width="1.1"/></svg>
      <span class="ln r"></span></div>
    </header>

    <div class="photos">
      <div class="photo-row">
        <div class="photo-wrap" style="transform:rotate(-1deg);">
          <div class="polaroid">
            <div class="tape"></div>
            <div class="photo-slot"><img src="data:image/jpeg;base64,%%CAND_LEFT%%" alt=""></div>
          </div>
        </div>
        <div class="photo-wrap" style="transform:rotate(1deg);">
          <div class="polaroid">
            <div class="tape" style="transform:rotate(3deg);"></div>
            <div class="photo-slot"><img src="data:image/jpeg;base64,%%CAND_RIGHT%%" alt=""></div>
          </div>
        </div>
      </div>
    </div>

    <div class="cols">
      <div class="col left">
        <div class="panel">
          <div class="panel-title"><span class="dot"></span>The Golden Rules</div>
          <ul class="rules">
            <li><span class="num">1</span><b>Spray only on spray days.</b> Monday and Thursday are the only spray days &mdash; vacuum the whole carpet first, then mist, so it isn&rsquo;t wasted on dirt still in the carpet.</li>
            <li><span class="num">2</span><b>Empty the canister outside.</b> Tip it straight into the outdoor trash so nothing can crawl back in.</li>
            <li><span class="num">3</span><b>Shake well, mist light.</b> Shake hard, then mist an even coat until the carpet is barely damp &mdash; never soaked.</li>
            <li><span class="num">4</span><b>Trust the process.</b> New eggs keep hatching for about two weeks. Vacuuming daily coaxes them out so the spray can finish the job.</li>
          </ul>
        </div>
      </div>
      <div class="col right">
        <div class="panel">
          <div class="panel-title"><span class="dot"></span>This Week&rsquo;s Program</div>
          <p class="legend"><svg class="drop" viewBox="0 0 12 16"><path d="M6 0C6 0 11.2 7.4 11.2 11 A5.2 5.2 0 0 1 0.8 11C0.8 7.4 6 0 6 0Z" fill="#9E5A66"/></svg> spray day &mdash; every other day is vacuum only</p>
          <table class="sched">
            <tr><td class="cell"><div class="day d-feature">Mon <svg class="drop" viewBox="0 0 12 16"><path d="M6 0C6 0 11.2 7.4 11.2 11 A5.2 5.2 0 0 1 0.8 11C0.8 7.4 6 0 6 0Z" fill="#9E5A66"/></svg></div></td>
              <td class="act"><b>Double Feature</b> <span class="steps">&mdash; 1) vacuum thoroughly&nbsp; 2) light mist over the carpets.</span></td></tr>
            <tr><td class="cell"><div class="day d-quick">Tue</div></td>
              <td class="act"><b>Quick Clean</b> <span class="steps">&mdash; vacuum up yesterday&rsquo;s stragglers &amp; stir out the hiders.</span></td></tr>
            <tr><td class="cell"><div class="day d-quick">Wed</div></td>
              <td class="act"><b>Quick Clean</b> <span class="steps">&mdash; a fresh pass to keep the floors happy.</span></td></tr>
            <tr><td class="cell"><div class="day d-feature">Thu <svg class="drop" viewBox="0 0 12 16"><path d="M6 0C6 0 11.2 7.4 11.2 11 A5.2 5.2 0 0 1 0.8 11C0.8 7.4 6 0 6 0Z" fill="#9E5A66"/></svg></div></td>
              <td class="act"><b>Double Feature</b> <span class="steps">&mdash; 1) vacuum thoroughly&nbsp; 2) light mist over the carpets.</span></td></tr>
            <tr><td class="cell"><div class="day d-quick">Fri</div></td>
              <td class="act"><b>Quick Clean</b> <span class="steps">&mdash; sweep up the week&rsquo;s last stragglers.</span></td></tr>
            <tr><td class="cell"><div class="day d-weekend">Sat&middot;Sun</div></td>
              <td class="act"><b>Intermission</b> <span class="steps">&mdash; easy daily vacuum, then feet up and enjoy your shows.</span></td></tr>
          </table>
        </div>
      </div>
    </div>

    <div class="count">
      <div class="lbl"><b>14&ndash;Day Flea&ndash;Free Countdown</b> &mdash; check a circle each night you finish. Fourteen little wins to a fresh, happy home!</div>
      <div class="dots">
        <div class="chk">1</div><div class="chk">2</div><div class="chk">3</div><div class="chk">4</div>
        <div class="chk">5</div><div class="chk">6</div><div class="chk">7</div><div class="chk">8</div>
        <div class="chk">9</div><div class="chk">10</div><div class="chk">11</div><div class="chk">12</div>
        <div class="chk">13</div><div class="chk" style="border-color:var(--honey);color:#b07d1c;">14</div>
      </div>
    </div>

    <footer>
      <div class="foot">
        <div class="foot-cell foot-bug">
          <svg class="bugwink" viewBox="0 0 120 90"><g>
    <g stroke="#C88793" stroke-width="2" stroke-linecap="round" opacity=".7">
      <line x1="6" y1="42" x2="24" y2="42"/><line x1="2" y1="54" x2="20" y2="54"/></g>
    <g stroke="#5c4433" stroke-width="2" stroke-linecap="round">
      <line x1="52" y1="60" x2="44" y2="78"/><line x1="62" y1="64" x2="58" y2="82"/>
      <line x1="72" y1="64" x2="76" y2="82"/><line x1="82" y1="60" x2="90" y2="76"/></g>
    <ellipse cx="66" cy="52" rx="24" ry="20" fill="#8c6239" stroke="#5c4433" stroke-width="2"/>
    <ellipse cx="60" cy="47" rx="8" ry="9" fill="#b98a5a" opacity=".6"/>
    <circle cx="74" cy="47" r="6" fill="#fff" stroke="#5c4433" stroke-width="1.4"/>
    <circle cx="76" cy="48" r="2.6" fill="#3B2A20"/>
    <path d="M64 60 Q72 65 82 59" fill="none" stroke="#3B2A20" stroke-width="1.8" stroke-linecap="round"/>
    <path d="M50 42 Q40 32 44 22" fill="none" stroke="#5c4433" stroke-width="2.4" stroke-linecap="round"/>
    <g transform="translate(78,8)">
      <rect x="0" y="0" width="40" height="22" rx="8" fill="#fff" stroke="#A85E6C" stroke-width="1.4"/>
      <path d="M10 22 l-6 9 l14 -7 Z" fill="#fff" stroke="#A85E6C" stroke-width="1.4"/>
      <text x="20" y="15.5" text-anchor="middle" font-family="'Patrick Hand',cursive" font-size="13" fill="#A85E6C">bye!</text></g>
  </g></svg>
        </div>
        <div class="foot-cell foot-text">
          <p class="quote">You finish what you start, you keep a loving home, and you always look after your family. That&rsquo;s just who you are &mdash; and those little pests picked the wrong house.</p>
          <div class="signoff">We love you, OG &mdash; you&rsquo;ve got this!
            <svg class="hh" viewBox="0 0 24 24"><path d="M12 21C12 21 3 14.6 3 8.9 3 5.6 5.5 3.4 8.3 3.4c1.9 0 3.1 1 3.7 2 .6-1 1.8-2 3.7-2C21.5 3.4 21 5.6 21 8.9 21 14.6 12 21 12 21Z" fill="#C88793" stroke="#A85E6C" stroke-width="1.1"/></svg></div>
        </div>
        <div class="foot-cell foot-seal">
          <svg class="seal" viewBox="0 0 120 120"><g>
    <circle cx="60" cy="60" r="55" fill="none" stroke="#9E5A66" stroke-width="2.4"/>
    <circle cx="60" cy="60" r="47" fill="none" stroke="#9E5A66" stroke-width="1"/>
    <text x="60" y="27" text-anchor="middle" font-family="'Yeseva One',serif" font-size="8.4" fill="#9E5A66" letter-spacing="1">ORIGINAL</text>
    <text x="60" y="38" text-anchor="middle" font-family="'Yeseva One',serif" font-size="8.4" fill="#9E5A66" letter-spacing="1">GRANDMA</text>
    <text x="60" y="64" text-anchor="middle" font-family="'Yeseva One',serif" font-size="22" fill="#9E5A66">O.G.</text>
    <text x="60" y="81" text-anchor="middle" font-family="'Yeseva One',serif" font-size="7.6" fill="#9E5A66" letter-spacing="0.5">FLEA&#8209;FIGHTING</text>
    <text x="60" y="91" text-anchor="middle" font-family="'Yeseva One',serif" font-size="7.6" fill="#9E5A66" letter-spacing="0.5">CHAMPION</text>
    <text x="60" y="106" text-anchor="middle" font-size="9" fill="#E2A950" letter-spacing="2.5">&#9733;&#9733;&#9733;</text>
  </g></svg>
        </div>
      </div>
    </footer>

  </div>
</div>

</body>
</html>
"""
HTML = HTML.replace("%%YESEVA%%", YESEVA).replace("%%PATRICK%%", PATRICK)
HTML = (HTML.replace("%%CAND_LEFT%%", CAND_LEFT)
            .replace("%%CAND_RIGHT%%", CAND_RIGHT))
OUT = HERE.parent / "print" / "OG_Flea-Free_Mission.html"
pathlib.Path(OUT).write_text(HTML, encoding="utf-8")
print("wrote", OUT, len(HTML), "bytes")
print("Tip: render to PDF with:")
print('  python3 -c "import weasyprint; weasyprint.HTML(\'' + str(OUT) + '\').write_pdf(\'' + str(OUT.with_suffix(".pdf")) + '\')"')
