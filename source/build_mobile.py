#!/usr/bin/env python3
import base64, pathlib

HERE = pathlib.Path(__file__).resolve().parent

def b64(p):
    return base64.b64encode(p.read_bytes()).decode()

YESEVA = b64(HERE / "fonts" / "YesevaOne.ttf")
PATRICK = b64(HERE / "fonts" / "PatrickHand.ttf")
ICON = b64(HERE / "icon" / "apple_touch_icon.png")
CAND_LEFT = b64(HERE / "photos" / "final_cand_left.jpg")
CAND_RIGHT = b64(HERE / "photos" / "final_cand_right.jpg")

# build the 14 day-circle buttons
day_buttons = "\n".join(
    f'<button class="day-circle" data-i="{i}" aria-label="Day {i+1}">{i+1}</button>'
    for i in range(14)
)

# build the 7 program rows
program_rows = [
    ("MON", "d-feature", "Double Feature", "Vacuum thoroughly, then a light mist over the carpets."),
    ("TUE", "d-quick",   "Quick Clean",    "Vacuum up yesterday&rsquo;s stragglers &amp; stir out the hiders."),
    ("WED", "d-quick",   "Quick Clean",    "A fresh pass to keep the floors happy."),
    ("THU", "d-feature", "Double Feature", "Vacuum thoroughly, then a light mist over the carpets."),
    ("FRI", "d-quick",   "Quick Clean",    "Sweep up the week&rsquo;s last stragglers."),
    ("SAT&middot;SUN", "d-weekend", "Intermission", "Easy daily vacuum, then feet up and enjoy your shows."),
]
program_html = "\n".join(
    f'''<div class="prow">
      <div class="pill {cls}">{label}{' <svg class="drop" viewBox="0 0 12 16"><path d="M6 0C6 0 11.2 7.4 11.2 11 A5.2 5.2 0 0 1 0.8 11C0.8 7.4 6 0 6 0Z" fill="#9E5A66"/></svg>' if cls=="d-feature" else ''}</div>
      <div class="ptext"><b>{title}</b> &mdash; {desc}</div>
    </div>''' for label, cls, title, desc in program_rows
)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>OG's Flea-Free Mission</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="OG Mission">
<meta name="mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#9E5A66">
<link rel="apple-touch-icon" href="data:image/png;base64,%%ICON%%">
<link rel="manifest" href="manifest.json">
<style>
@font-face{font-family:'Yeseva One';src:url(data:font/ttf;base64,%%YESEVA%%) format('truetype');font-display:swap;}
@font-face{font-family:'Patrick Hand';src:url(data:font/ttf;base64,%%PATRICK%%) format('truetype');font-display:swap;}
:root{
  --paper:#FFFFFF; --panel:#FDF9F3;
  --ink:#3B2A20; --ink-soft:#6b5847;
  --sage:#7F9A6E; --sage-deep:#5E7A50;
  --rose:#C88793; --rose-deep:#A85E6C;
  --honey:#E2A950; --honey-deep:#A9781F; --mulberry:#9E5A66;
  --line:#E7D6BF;
  --display:'Yeseva One',Georgia,serif;
  --hand:'Patrick Hand','Comic Sans MS',cursive;
  --body:Georgia,'Times New Roman',serif;
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
html,body{margin:0;padding:0;background:var(--paper);}
body{font-family:var(--body);color:var(--ink);font-size:17px;line-height:1.5;
  max-width:480px;margin:0 auto;padding:22px 18px 44px;
  -webkit-text-size-adjust:100%;}
header{text-align:center;padding-top:4px;}
.eyebrow{font-family:var(--hand);font-size:16px;color:var(--rose-deep);margin:0;}
h1{font-family:var(--display);font-size:30px;line-height:1.08;color:var(--mulberry);margin:6px 0 4px;}
.subtitle{font-style:italic;font-size:14.5px;color:var(--ink-soft);margin:0;}
.flourish{display:flex;align-items:center;justify-content:center;margin:12px 0 20px;}
.flourish .ln{flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--honey),transparent);max-width:80px;}
.flourish span.heart{font-size:15px;margin:0 8px;}

.photos{margin-bottom:8px;}
.photo-card{background:var(--paper);border:1px solid var(--line);border-radius:12px;
  padding:8px;box-shadow:0 2px 8px rgba(94,66,46,.08);margin-bottom:18px;}
.photo-card img{width:100%;height:auto;display:block;border-radius:8px;}
.photo-cap{font-family:var(--hand);text-align:center;color:var(--mulberry);
  font-size:16px;margin-top:8px;}

.panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;
  padding:16px 16px 14px;margin-bottom:20px;}
.panel-title{font-family:var(--display);font-size:19px;color:var(--sage-deep);margin:0 0 10px;
  display:flex;align-items:center;}
.dot{width:9px;height:9px;border-radius:50%;background:var(--honey);display:inline-block;margin-right:8px;}

.rules{list-style:none;margin:0;padding:0;}
.rules li{position:relative;padding:0 0 13px 34px;font-size:15.5px;}
.rules li:last-child{padding-bottom:0;}
.rnum{position:absolute;left:0;top:1px;width:23px;height:23px;border-radius:50%;
  background:var(--sage);color:#fff;font-family:var(--display);font-size:13px;
  text-align:center;line-height:23px;}
.rules b{color:var(--rose-deep);}

.prow{display:flex;align-items:flex-start;padding:9px 0;border-bottom:1px solid var(--line);}
.prow:last-child{border-bottom:none;}
.pill{flex:0 0 auto;min-width:60px;text-align:center;font-family:var(--display);
  font-size:11.5px;letter-spacing:.3px;padding:5px 8px;border-radius:5px;border:1.5px solid;
  background:#fff;margin-right:12px;}
.d-feature{border-color:var(--mulberry);color:var(--mulberry);}
.d-quick{border-color:var(--sage-deep);color:var(--sage-deep);}
.d-weekend{border-color:var(--honey);color:var(--honey-deep);}
.ptext{font-size:14.5px;line-height:1.4;padding-top:3px;}
.ptext b{color:var(--ink);}
.legend{font-family:var(--hand);font-size:13.5px;color:var(--rose-deep);margin:-4px 0 12px;}
.drop{width:9px;height:12px;vertical-align:-1px;}

.rem-sub{font-size:14.5px;color:var(--ink-soft);margin:0 0 14px;line-height:1.4;}
.rem-row{display:flex;align-items:center;justify-content:space-between;
  background:#fff;border:1px solid var(--line);border-radius:8px;
  padding:10px 14px;margin-bottom:14px;}
.rem-label{font-size:14.5px;color:var(--ink);}
.rem-row input[type=time]{font-size:16px;font-family:var(--body);color:var(--mulberry);
  border:none;background:transparent;}
.rem-btn{display:block;width:100%;background:var(--mulberry);color:#fff;border:none;
  border-radius:8px;padding:13px;font-family:var(--display);font-size:15.5px;
  letter-spacing:.3px;}
.rem-btn:active{background:var(--rose-deep);}
.rem-status{text-align:center;font-size:13.5px;color:var(--sage-deep);min-height:18px;margin:10px 0 2px;}
.rem-help{font-family:var(--hand);text-align:center;font-size:13px;color:var(--rose-deep);margin:2px 0 0;}
.rem-panel{margin-top:26px;border-style:dashed;}

.count-sub{font-family:var(--hand);text-align:center;color:var(--sage-deep);
  font-size:15px;margin:-2px 0 14px;}
.day-grid{display:flex;flex-wrap:wrap;justify-content:center;margin:0 0 8px;}
.day-circle{width:44px;height:44px;border-radius:50%;border:2px solid var(--rose);
  background:#fff;color:var(--rose-deep);font-family:var(--display);font-size:15px;
  display:flex;align-items:center;justify-content:center;cursor:pointer;
  margin:5px;transition:transform .12s ease;}
.day-circle:active{transform:scale(0.92);}
.day-circle.done{background:var(--sage);border-color:var(--sage-deep);color:#fff;}
.progress-wrap{background:#fff;border:1px solid var(--line);border-radius:8px;
  height:10px;overflow:hidden;margin:4px 0 8px;}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--sage),var(--honey));
  width:0%;transition:width .25s ease;}
#progressText{text-align:center;font-size:14px;color:var(--ink-soft);margin:0 0 4px;}
.reset-row{text-align:center;}
.reset-row button{background:none;border:none;color:var(--rose-deep);font-family:var(--hand);
  font-size:14px;text-decoration:underline;padding:6px;cursor:pointer;}

footer{text-align:center;margin-top:8px;}
.quote{font-style:italic;font-size:14.5px;color:var(--ink);line-height:1.45;margin:0 0 10px;}
.signoff{font-family:var(--display);font-size:19px;color:var(--mulberry);margin:0 0 10px;}
.seal-line{font-family:var(--hand);font-size:14px;color:var(--rose-deep);}
</style>
</head>
<body>

<header>
  <p class="eyebrow">a little note for the strongest lady we know &mdash;</p>
  <h1>OG&rsquo;s Flea&ndash;Free Mission</h1>
  <p class="subtitle">Two weeks, one spotless house, and a whole lot of love.</p>
  <div class="flourish"><span class="ln"></span><span class="heart">&#128156;</span><span class="ln"></span></div>
</header>

<div class="photos">
  <div class="photo-card">
    <img src="data:image/jpeg;base64,%%CAND_LEFT%%" alt="">
  </div>
  <div class="photo-card">
    <img src="data:image/jpeg;base64,%%CAND_RIGHT%%" alt="">
  </div>
</div>

<div class="panel">
  <div class="panel-title"><span class="dot"></span>The Golden Rules</div>
  <ul class="rules">
    <li><span class="rnum">1</span><b>Spray only on spray days.</b> Monday and Thursday are the only spray days &mdash; vacuum the whole carpet first, then mist, so it isn&rsquo;t wasted on dirt still in the carpet.</li>
    <li><span class="rnum">2</span><b>Empty the canister outside.</b> Tip it straight into the outdoor trash so nothing can crawl back in.</li>
    <li><span class="rnum">3</span><b>Shake well, mist light.</b> Shake hard, then mist an even coat until the carpet is barely damp &mdash; never soaked.</li>
    <li><span class="rnum">4</span><b>Trust the process.</b> New eggs keep hatching for about two weeks. Vacuuming daily coaxes them out so the spray can finish the job.</li>
  </ul>
</div>

<div class="panel">
  <div class="panel-title"><span class="dot"></span>This Week&rsquo;s Program</div>
  <p class="legend"><svg class="drop" viewBox="0 0 12 16"><path d="M6 0C6 0 11.2 7.4 11.2 11 A5.2 5.2 0 0 1 0.8 11C0.8 7.4 6 0 6 0Z" fill="#9E5A66"/></svg> spray day &mdash; every other day is vacuum only</p>
  %%PROGRAM_ROWS%%
</div>

<div class="panel">
  <div class="panel-title"><span class="dot"></span>14&ndash;Day Countdown</div>
  <p class="count-sub">tap a circle each night you finish!</p>
  <div class="day-grid">
    %%DAY_BUTTONS%%
  </div>
  <div class="progress-wrap"><div class="progress-fill" id="progressFill"></div></div>
  <p id="progressText">0 of 14 days complete</p>
  <div class="reset-row"><button id="resetBtn">reset countdown</button></div>
</div>

<div class="panel rem-panel">
  <div class="panel-title"><span class="dot"></span>Set Her Daily Reminders</div>
  <p class="rem-sub"><b>One&ndash;time setup.</b> Pick a time, then download 14 days of calendar alerts starting today &mdash; syncs to a paired Apple Watch too.</p>
  <div class="rem-row">
    <label for="remTime" class="rem-label">Reminder time</label>
    <input type="time" id="remTime" value="09:00">
  </div>
  <button id="remBtn" class="rem-btn" type="button">Download Reminders (.ics)</button>
  <p id="remStatus" class="rem-status"></p>
  <p class="rem-help">Opens in Files &mdash; tap it there to add to Calendar. If it doesn&rsquo;t prompt automatically, check Files &rarr; Downloads.</p>
</div>

<footer>
  <p class="quote">You finish what you start, you keep a loving home, and you always look after your family. That&rsquo;s just who you are &mdash; and those little pests picked the wrong house.</p>
  <p class="signoff">We love you, OG &mdash; you&rsquo;ve got this! &#128149;</p>
  <p class="seal-line">O.G. &middot; Flea&ndash;Fighting Champion &#11088;&#11088;&#11088;</p>
</footer>

<script>
(function(){
  var KEY = 'ogFleaDays_v1';
  function loadState(){
    try{
      var raw = localStorage.getItem(KEY);
      if(raw) return JSON.parse(raw);
    }catch(e){}
    return Array(14).fill(false);
  }
  function saveState(state){
    try{ localStorage.setItem(KEY, JSON.stringify(state)); }catch(e){}
  }
  var state = loadState();
  var circles = document.querySelectorAll('.day-circle');
  var progressText = document.getElementById('progressText');
  var progressFill = document.getElementById('progressFill');
  function render(){
    circles.forEach(function(el,i){
      el.classList.toggle('done', !!state[i]);
    });
    var count = state.filter(Boolean).length;
    progressText.textContent = count + ' of 14 days complete';
    progressFill.style.width = (count/14*100) + '%';
  }
  circles.forEach(function(el,i){
    el.addEventListener('click', function(){
      state[i] = !state[i];
      saveState(state);
      render();
    });
  });
  document.getElementById('resetBtn').addEventListener('click', function(){
    state = Array(14).fill(false);
    saveState(state);
    render();
  });
  render();
})();

// --- Daily reminders: build a fresh 14-day .ics starting today, at the chosen time ---
(function(){
  var scheduleByDow = { // JS Date.getDay(): 0=Sun,1=Mon,...6=Sat
    0: ["Intermission", "Easy daily vacuum, then feet up and enjoy your shows."],
    1: ["Double Feature", "Vacuum thoroughly, then a light mist over the carpets."],
    2: ["Quick Clean", "Vacuum up yesterday's stragglers and stir out the hiders."],
    3: ["Quick Clean", "A fresh pass to keep the floors happy."],
    4: ["Double Feature", "Vacuum thoroughly, then a light mist over the carpets."],
    5: ["Quick Clean", "Sweep up the week's last stragglers."],
    6: ["Intermission", "Easy daily vacuum, then feet up and enjoy your shows."]
  };
  function pad(n){ return (n<10?'0':'')+n; }
  function esc(t){ return t.replace(/\\/g,'\\\\').replace(/,/g,'\\,').replace(/;/g,'\\;'); }
  function fmtDT(dt){
    return '' + dt.getFullYear() + pad(dt.getMonth()+1) + pad(dt.getDate()) + 'T' +
           pad(dt.getHours()) + pad(dt.getMinutes()) + '00';
  }
  function buildIcs(startDate, hh, mm){
    var lines = ['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//OG Flea-Free Mission//EN','CALSCALE:GREGORIAN'];
    var now = new Date();
    var dtstamp = now.getUTCFullYear()+pad(now.getUTCMonth()+1)+pad(now.getUTCDate())+'T'+
                  pad(now.getUTCHours())+pad(now.getUTCMinutes())+pad(now.getUTCSeconds())+'Z';
    var rand = Math.random().toString(36).slice(2,8);
    for(var i=0;i<14;i++){
      var startDt = new Date(startDate.getFullYear(), startDate.getMonth(), startDate.getDate()+i, hh, mm, 0);
      var endDt = new Date(startDt.getTime() + 30*60000);
      var info = scheduleByDow[startDt.getDay()];
      var title = info[0], desc = info[1];
      var dayNum = i+1;
      if(dayNum===14){ desc = desc + ' Mission complete after today - you did it!'; }
      var summary = 'Flea Mission - Day ' + dayNum + '/14: ' + title;
      var fullDesc = 'Day ' + dayNum + ' of 14. ' + desc;
      lines.push('BEGIN:VEVENT');
      lines.push('UID:' + Date.now() + '-' + i + '-' + rand + '@og-flea-mission');
      lines.push('DTSTAMP:' + dtstamp);
      lines.push('DTSTART:' + fmtDT(startDt));
      lines.push('DTEND:' + fmtDT(endDt));
      lines.push('SUMMARY:' + esc(summary));
      lines.push('DESCRIPTION:' + esc(fullDesc));
      lines.push('BEGIN:VALARM');
      lines.push('ACTION:DISPLAY');
      lines.push('DESCRIPTION:' + esc(summary));
      lines.push('TRIGGER:PT0M');
      lines.push('END:VALARM');
      lines.push('END:VEVENT');
    }
    lines.push('END:VCALENDAR');
    return lines.join('\r\n') + '\r\n';
  }
  var btn = document.getElementById('remBtn');
  var status = document.getElementById('remStatus');
  btn.addEventListener('click', function(){
    var timeVal = (document.getElementById('remTime').value) || '09:00';
    var parts = timeVal.split(':');
    var hh = parseInt(parts[0],10), mm = parseInt(parts[1],10);
    if(isNaN(hh) || isNaN(mm)){ hh = 9; mm = 0; }
    var today = new Date();
    try{
      var ics = buildIcs(today, hh, mm);
      var blob = new Blob([ics], {type:'text/calendar;charset=utf-8'});
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'OG_Flea_Free_Reminders.ics';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(function(){ URL.revokeObjectURL(url); }, 4000);
      status.textContent = 'Downloaded! Open it from Files to add to Calendar.';
    }catch(e){
      status.textContent = "This browser can't generate the file — try opening this page in Safari.";
    }
  });
})();

// --- PWA: cache the page for offline access after the first visit ---
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function(){
    navigator.serviceWorker.register('sw.js').catch(function(){});
  });
}
</script>
</body>
</html>
"""

HTML = (HTML.replace("%%YESEVA%%", YESEVA)
            .replace("%%PATRICK%%", PATRICK)
            .replace("%%ICON%%", ICON)
            .replace("%%CAND_LEFT%%", CAND_LEFT)
            .replace("%%CAND_RIGHT%%", CAND_RIGHT)
            .replace("%%PROGRAM_ROWS%%", program_html)
            .replace("%%DAY_BUTTONS%%", day_buttons))

OUT = HERE.parent / "index.html"
pathlib.Path(OUT).write_text(HTML, encoding="utf-8")
print("wrote", OUT, len(HTML), "bytes")

# --- PWA manifest ---
MANIFEST = """{
  "name": "OG's Flea-Free Mission",
  "short_name": "OG Mission",
  "start_url": "./index.html",
  "scope": "./",
  "display": "standalone",
  "background_color": "#FFFFFF",
  "theme_color": "#9E5A66",
  "icons": [
    { "src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
"""
manifest_out = HERE.parent / "manifest.json"
manifest_out.write_text(MANIFEST, encoding="utf-8")
print("wrote", manifest_out)

# --- Service worker: minimal offline cache (the page is fully self-contained) ---
SW = """// OG's Flea-Free Mission -- minimal offline cache.
// Everything the page needs (fonts, photos) is inlined in index.html already,
// so caching that single document is enough for full offline access.
const CACHE_NAME = 'og-flea-mission-v2';
const CORE_ASSETS = ['./', './index.html', './manifest.json'];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(CORE_ASSETS))
      .catch(() => {})
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then(cached => {
      const network = fetch(event.request)
        .then(response => {
          if (response && response.status === 200) {
            const copy = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(event.request, copy));
          }
          return response;
        })
        .catch(() => cached);
      return cached || network;
    })
  );
});
"""
sw_out = HERE.parent / "sw.js"
sw_out.write_text(SW, encoding="utf-8")
print("wrote", sw_out)

# --- Manifest icons (real PNG files, needed for cross-browser installability) ---
try:
    from PIL import Image, ImageDraw, ImageFont
    import math

    def make_icon(size, path):
        img = Image.new("RGB", (size, size), (158, 90, 102))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(str(HERE / "fonts" / "YesevaOne.ttf"), int(size * 0.51))
        text = "OG"
        bbox = d.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        tx = (size - tw) / 2 - bbox[0]
        ty = (size - th) / 2 - bbox[1] - size * 0.03
        d.text((tx, ty), text, font=font, fill=(255, 255, 255))

        def heart_points(cx, cy, s):
            pts = []
            for t in [i / 40 * 2 * math.pi for i in range(41)]:
                x = 16 * math.sin(t) ** 3
                y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
                pts.append((cx + x * s, cy - y * s))
            return pts

        scale = size / 180.0
        d.polygon(heart_points(size / 2, 40 * scale, 1.3 * scale), fill=(226, 169, 80))
        img.save(path)
        print("wrote", path, img.size)

    icons_dir = HERE.parent / "icons"
    icons_dir.mkdir(exist_ok=True)
    make_icon(192, icons_dir / "icon-192.png")
    make_icon(512, icons_dir / "icon-512.png")
except ImportError:
    print("Pillow not installed -- skipped icon generation (icons/ files unchanged)")

