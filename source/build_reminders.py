#!/usr/bin/env python3
"""
Generates the 14-day OG Flea-Free Mission reminders .ics file.

By default, starts on the next Monday from today so the schedule lines up
with the Mon/Thu spray-day pattern. Pass a different start date if needed:

    python3 build_reminders.py 2026-09-14
"""
import datetime, uuid, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "reminders" / "OG_Flea_Free_Reminders.ics"

schedule = {
    0: ("Double Feature", "Vacuum thoroughly, then a light mist over the carpets."),   # Mon (spray day)
    1: ("Quick Clean", "Vacuum up yesterday's stragglers and stir out the hiders."),    # Tue
    2: ("Quick Clean", "A fresh pass to keep the floors happy."),                       # Wed
    3: ("Double Feature", "Vacuum thoroughly, then a light mist over the carpets."),    # Thu (spray day)
    4: ("Quick Clean", "Sweep up the week's last stragglers."),                         # Fri
    5: ("Intermission", "Easy daily vacuum, then feet up and enjoy your shows."),       # Sat
    6: ("Intermission", "Easy daily vacuum, then feet up and enjoy your shows."),       # Sun
}

def esc(t):
    return t.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;").replace("\n", "\\n")

def fmt_dt(d, hour, minute):
    return f"{d.year:04d}{d.month:02d}{d.day:02d}T{hour:02d}{minute:02d}00"

def fold(line):
    """RFC5545 line folding at 75 octets, safe for multi-byte UTF-8."""
    b = line.encode("utf-8")
    if len(b) <= 75:
        return line
    out = []
    start_i = 0
    limit = 75
    while start_i < len(b):
        end = min(start_i + limit, len(b))
        while end < len(b) and (b[end] & 0xC0) == 0x80:
            end -= 1
        out.append(b[start_i:end])
        start_i = end
        limit = 74
    return ("\r\n ").join(chunk.decode("utf-8") for chunk in out)

def next_monday(d):
    days_ahead = (0 - d.weekday()) % 7
    days_ahead = days_ahead or 7  # always the *next* Monday, not today if today is Monday
    return d + datetime.timedelta(days=days_ahead)

def build(start):
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0",
             "PRODID:-//OG Flea-Free Mission//EN", "CALSCALE:GREGORIAN"]
    dtstamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    for i in range(14):
        d = start + datetime.timedelta(days=i)
        title, desc = schedule[d.weekday()]
        day_num = i + 1
        summary = f"Flea Mission - Day {day_num}/14: {title}"
        if day_num == 14:
            desc = desc + " Mission complete after today - you did it!"
        full_desc = f"Day {day_num} of 14. {desc}"

        lines += [
            "BEGIN:VEVENT",
            f"UID:{uuid.uuid4()}@og-flea-mission",
            f"DTSTAMP:{dtstamp}",
            f"DTSTART:{fmt_dt(d, 9, 0)}",
            f"DTEND:{fmt_dt(d, 9, 30)}",
            fold(f"SUMMARY:{esc(summary)}"),
            fold(f"DESCRIPTION:{esc(full_desc)}"),
            "BEGIN:VALARM", "ACTION:DISPLAY",
            fold(f"DESCRIPTION:{esc(summary)}"),
            "TRIGGER:PT0M", "END:VALARM", "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    return "\r\n".join(lines) + "\r\n"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start = datetime.date.fromisoformat(sys.argv[1])
    else:
        start = next_monday(datetime.date.today())
    ics_text = build(start)
    OUT.write_text(ics_text, encoding="utf-8", newline="")
    print(f"wrote {OUT}")
    print(f"first day: {start}  last day: {start + datetime.timedelta(days=13)}")
