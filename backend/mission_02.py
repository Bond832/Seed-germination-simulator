# ═══════════════════════════════════════════════════════
# MISSION 02 — Will It Grow?
# Branch: mission-02-yourname
# ═══════════════════════════════════════════════════════
#
# SCIENCE CONNECTION:
# Your experiment showed that some seeds germinated and
# others didn't — depending on what they were watered with.
# This mission writes the exact rules that decide that
# outcome. You're coding the biology of your experiment.
#
# BY THE END OF THIS MISSION YOU WILL HAVE:
# → Three core functions that power the entire simulation
# → A printed test table that proves your logic works
# ═══════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────
# TODO 1: will_germinate(ph)
#
# WHAT: Return True if the seed will germinate at this pH,
#       False if it won't.
#
# WHY: Mission 03 calls this first before starting the
#      7-day loop. If the seed won't germinate, there's
#      no point simulating 7 days of growth — the program
#      should tell the user immediately and stop.
#
# RULE: Seeds germinate between pH 5.5 and 7.5.
#       Outside that range → False.
#
# HINT: You can check a range in one line:
#       return 5.5 <= ph <= 7.5
#
# AFTER THIS TODO: Your simulator can make a yes/no
# decision about whether an experiment will work.
# ───────────────────────────────────────────────────────
def will_germinate(ph):
    # YOUR CODE HERE ↓
    pass


# ───────────────────────────────────────────────────────
# TODO 2: daily_growth_rate(ph)
#
# WHAT: Return how many centimetres the plant grows per day
#       at the given pH level.
#
# WHY: Mission 03 uses this number every day in the loop
#      to calculate the total height. If this is wrong,
#      every single day of the simulation will be wrong.
#      Getting this right is critical.
#
# GROWTH RATES (from your science experiment data):
#   pH 6.0 – 7.0  →  1.2 cm/day   ← optimal, best growth
#   pH 5.5 – 6.0  →  0.7 cm/day   ← slightly acidic, slower
#   pH 7.0 – 8.0  →  0.5 cm/day   ← slightly alkaline, slower
#   anything else →  0.0 cm/day   ← too extreme, no growth
#
# AFTER THIS TODO: Your simulation knows exactly how fast
# the plant grows at any pH — day by day.
# ───────────────────────────────────────────────────────
def daily_growth_rate(ph):
    # YOUR CODE HERE ↓
    pass


# ───────────────────────────────────────────────────────
# TODO 3: health_status(ph)
#
# WHAT: Return a string describing the plant's health.
#
# WHY: The frontend (Mission 04) uses this to color-code
#      the results table — green rows, yellow rows, red rows.
#      It also makes the simulation feel like a real lab report.
#
# STATUSES:
#   "Healthy 🟢"     → pH 6.0 to 7.0
#   "Struggling 🟡"  → pH 5.5–6.0 or 7.0–8.0
#   "Failed 🔴"      → anything outside those ranges
#
# AFTER THIS TODO: Every day of the simulation will have
# a clear, color-coded health label — just like a real
# experiment log.
# ───────────────────────────────────────────────────────
def health_status(ph):
    # YOUR CODE HERE ↓
    pass


# ── Test all three functions ──────────────────────────
# Run this and check every row makes scientific sense.
# If a result looks wrong, go back and fix your function!

test_values = [3.0, 5.5, 6.0, 6.5, 7.0, 8.0, 11.0]

print("pH    | Germinates? | Growth/day  | Health")
print("-" * 55)
for ph in test_values:
    g = will_germinate(ph)
    r = daily_growth_rate(ph)
    h = health_status(ph)
    print(f"{ph:<5} | {str(g):<11} | {r} cm/day   | {h}")


# ════════════════════════════════════════════════════
# 🧪 MISSION 02 — CHECK YOUR WORK
# ════════════════════════════════════════════════════

print("\n" + "─" * 45)
print("🧪 CHECKING YOUR WORK...")
print("─" * 45)

passed = 0
total = 0

def check(label, got, expected):
    global passed, total
    total += 1
    if got == expected:
        print(f"  ✅  {label}")
        print(f"       got: '{got}'")
        passed += 1
    else:
        print(f"  ❌  {label}")
        print(f"       expected: '{expected}'  |  got: '{got}'")

# ── will_germinate checks ─────────────────────────────
print("\n📌 Testing will_germinate():")
check("will_germinate(6.5)  → True",  will_germinate(6.5),  True)
check("will_germinate(5.5)  → True",  will_germinate(5.5),  True)
check("will_germinate(7.5)  → True",  will_germinate(7.5),  True)
check("will_germinate(3.0)  → False", will_germinate(3.0),  False)
check("will_germinate(10.0) → False", will_germinate(10.0), False)

# ── daily_growth_rate checks ──────────────────────────
print("\n📌 Testing daily_growth_rate():")
check("daily_growth_rate(6.5) → 1.2", daily_growth_rate(6.5), 1.2)
check("daily_growth_rate(5.7) → 0.7", daily_growth_rate(5.7), 0.7)
check("daily_growth_rate(7.5) → 0.5", daily_growth_rate(7.5), 0.5)
check("daily_growth_rate(3.0) → 0.0", daily_growth_rate(3.0), 0.0)
check("daily_growth_rate(11.0)→ 0.0", daily_growth_rate(11.0), 0.0)

# ── health_status checks ──────────────────────────────
print("\n📌 Testing health_status():")
check("health_status(6.5)  → 'Healthy 🟢'",    health_status(6.5),  "Healthy 🟢")
check("health_status(5.7)  → 'Struggling 🟡'", health_status(5.7),  "Struggling 🟡")
check("health_status(7.3)  → 'Struggling 🟡'", health_status(7.3),  "Struggling 🟡")
check("health_status(3.0)  → 'Failed 🔴'",     health_status(3.0),  "Failed 🔴")
check("health_status(11.0) → 'Failed 🔴'",     health_status(11.0), "Failed 🔴")

# ── Final score ───────────────────────────────────────
print("\n" + "─" * 45)
if passed == total:
    print(f"  🎉 {passed}/{total} passed — Mission 02 Complete!")
    print("  Three functions, all working. You're building a real simulator! 🚀")
    print("\n  git add backend/mission_02.py")
    print("  git commit -m \"Mission 02: germination logic complete\"")
    print("  git push origin mission-02-yourname")
elif passed >= total // 2:
    print(f"  🔥 {passed}/{total} passed — Nearly there! Fix the ❌ above.")
else:
    print(f"  💪 {passed}/{total} passed — Keep going!")
    print("  Tip: check your pH ranges in each function carefully.")
print("─" * 45)
