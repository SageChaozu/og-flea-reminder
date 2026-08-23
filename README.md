# OG's Flea-Free Mission

A keepsake project made for OG: a printable fridge flyer, a mobile Home Screen
page, and daily calendar reminders, all covering the same two-week
flea-elimination routine.

## What's in here

| Path | What it is |
|---|---|
| `index.html` | The mobile page. Deploy this repo with GitHub Pages and it becomes the site's homepage — the one to Add to Home Screen on her iPhone. Now includes an in-page "Set Her Daily Reminders" tool and works offline as a PWA (see below). |
| `manifest.json` | PWA manifest — lets the page register as an installable app. |
| `sw.js` | Service worker — caches the page so it still opens if she's offline after the first visit. |
| `icons/` | Home Screen / app icons in the sizes browsers expect for installability (192px, 512px). |
| `print/OG_Flea-Free_Mission.html` | The printable flyer (Letter size, 8.5x11), same content as the HTML source. |
| `print/OG_Flea-Free_Mission.pdf` | The print-ready PDF — print at 100%/Actual Size, margins None, Background graphics on. |
| `reminders/OG_Flea_Free_Reminders.ics` | A pre-made 14-day reminders file (9am), in case you want to just send this directly without going through the page. The mobile page now also generates one of these on the fly — see below. |
| `source/` | The Python scripts and raw assets used to generate everything above — see below if you want to make future edits. |

## The mobile page is now a PWA

- **Works offline.** After she opens the page once (while online), a service
  worker caches it, so it keeps opening from her Home Screen icon even with
  no signal or wifi.
- **Daily reminders, generated on the spot.** A new panel lets her (or you)
  pick a reminder time and download a fresh 14-day `.ics` file that starts
  from *that day* — not a fixed date baked in ahead of time. Tapping the
  downloaded file in Files adds all 14 to Calendar, syncing to a paired
  Apple Watch automatically. That panel sits at the very bottom of the
  page, below the sign-off, so it can't be tapped by accident while she's
  scrolling to the countdown.

One honest caveat: getting a browser-generated `.ics` file to hand off
cleanly to the Calendar app has a history of being inconsistent across iOS
versions (this is a known iOS quirk, not specific to this page). The button
downloads the file via the browser's normal download mechanism, which is
the most reliable current approach — but if tapping the download doesn't
prompt Calendar automatically, open the **Files app → Downloads** and tap
it there, which always works.

## Hosting the mobile page on GitHub Pages

**Already set this up before?** Just replace `index.html` in your existing
repo and add the three new items (`manifest.json`, `sw.js`, `icons/`) —
same repo, same URL, no need to redo the Pages setup below.

**Starting fresh?**
1. Make sure this repo is **Public** (required for free GitHub Pages).
2. Go to **Settings → Pages**.
3. Under "Build and deployment," set Source to **Deploy from a branch**,
   branch **main**, folder **/(root)** → **Save**.
4. After a minute, GitHub shows the live URL at the top of that page —
   something like `https://yourusername.github.io/og-flea-mission/`.
5. Send that link to her. She opens it in Safari → Share icon →
   **Add to Home Screen**.

Because `index.html` sits at the repo root, that URL loads the mobile page
directly — no extra path needed.

## Making edits later

Both builders are self-contained — run them from inside `source/` and they
read their own assets and write straight back into the repo:

```bash
cd source
pip install pillow numpy weasyprint --break-system-packages

python3 build_flyer.py
# writes print/OG_Flea-Free_Mission.html
# then, to get the PDF:
python3 -c "import weasyprint; weasyprint.HTML('../print/OG_Flea-Free_Mission.html').write_pdf('../print/OG_Flea-Free_Mission.pdf')"

python3 build_mobile.py
# writes index.html, manifest.json, sw.js, and icons/*.png -- all in one run
```

To change wording, photos, colors, or the schedule, edit the HTML/CSS
template strings inside `build_flyer.py` / `build_mobile.py` directly, then
re-run.

### Source assets

- `source/fonts/` — Yeseva One (display) and Patrick Hand (handwriting),
  embedded as base64 in both builds.
- `source/photos/img3_fixed.jpg`, `img4_fixed.jpg` — the two grandkid photos,
  cropped and orientation-corrected, *before* the pencil-sketch filter.
- `source/photos/final_cand_left.jpg`, `final_cand_right.jpg` — the same
  photos *after* the ink-light pencil-sketch treatment (what's actually
  embedded in both builds today).
- `source/icon/apple_touch_icon.png` — the "OG" heart Home Screen icon.

If you ever want to redo the sketch filter (lighter/darker, different tone),
regenerate from the `_fixed.jpg` originals rather than re-processing the
already-sketched versions.

## Regenerating the reminders file

```bash
cd source
python3 build_reminders.py                # starts next Monday from today
python3 build_reminders.py 2026-09-14     # or pick a specific start date
```

Writes straight into `reminders/OG_Flea_Free_Reminders.ics`, 14 days from
whatever start date you give it, keeping the Mon/Thu spray-day pattern
aligned to real weekdays.
