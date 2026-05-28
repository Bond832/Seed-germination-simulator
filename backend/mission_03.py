# ═══════════════════════════════════════════════════════
# MISSION 03 — Watch It Grow!
# Branch: mission-03-yourname
# ═══════════════════════════════════════════════════════
#
# SCIENCE CONNECTION:
# You measured your real plant every day for 7 days and
# wrote it in your notebook. This mission simulates those
# exact 7 days in code — day by day, height by height.
# At the end, you'll compare your simulation to your
# real data. Do they match?
#
# BY THE END OF THIS MISSION YOU WILL HAVE:
# → A fully working Python simulation of your experiment
# → A dramatic day-by-day printout with time delays
# → A comparison between two different pH experiments
# ═══════════════════════════════════════════════════════

import time

# ── Copy your functions from Mission 02 here ─────────
# (will_germinate, daily_growth_rate, health_status)
# These are the building blocks — Mission 03 uses all three.

def will_germinate(ph):
    return 5.5 <= ph <= 7.5          # ← replace with your Mission 02 answer

def daily_growth_rate(ph):
    if 6.0 <= ph <= 7.0:
        return 1.2
    elif 5.5 <= ph < 6.0:
        return 0.7
    elif 7.0 < ph <= 8.0:
        return 0.5
    else:
        return 0.0

def health_status(ph):
    pass                             # ← paste your Mission 02 answer here


# ───────────────────────────────────────────────────────
# TODO 1: Build the 7-day simulation loop
#
# WHAT: Write a function that simulates 7 days of plant
#       growth at a given pH. Each day, the plant grows
#       by the daily rate and prints its current state.
#
# WHY: This is the core of the entire project. Every
#      button click in the JavaScript frontend (Mission 04)
#      is recreating this exact logic — but visually.
#      Getting this right in Python first makes Mission 04
#      much easier to build.
#
# YOUR FUNCTION MUST:
#   1. Check will_germinate() — if False, print a message and return []
#   2. Start with height = 0.0
#   3. Loop through days 1 to 7
#   4. Each day: add daily_growth_rate() to height
#   5. Print: day number, current height (1 decimal), health status
#   6. Append {"day": day, "height": height, "status": status} to a list
#   7. Use time.sleep(0.5) between days — makes it feel dramatic!
#   8. Return the list of results
#
# AFTER THIS TODO: You have a fully working science
# experiment simulator. Type in any pH and watch it grow.
# ───────────────────────────────────────────────────────
def simulate_growth(ph, days=7):
    print(f"\n🌱 Starting experiment at pH {ph}")
    print("=" * 45)

    if not will_germinate(ph):
        print("❌ Seed did not germinate at this pH level.")
        print(f"   pH {ph} is outside the safe range (5.5 – 7.5)")
        return []

    print("✅ Seed germinated! Simulating growth...\n")
    print(f"{'Day':<5} | {'Height (cm)':<12} | Health")
    print("-" * 35)

    height = 0.0
    rate = daily_growth_rate(ph)
    results = []

    # YOUR LOOP HERE ↓
    # for day in range(1, days + 1):
    #     ...

    return results


# ───────────────────────────────────────────────────────
# TODO 2: Run two experiments and compare
#
# WHAT: Call simulate_growth() twice — once with plain
#       water (pH 6.5) and once with strong detergent
#       (use the pH value you actually measured in class).
#
# WHY: This mirrors your real experiment exactly.
#      Seeing both results side by side — just like your
#      notebook — is what makes this simulator meaningful.
#
# AFTER THIS TODO: Your simulator produces a full
# comparison, just like your science lab report.
# ───────────────────────────────────────────────────────

print("🔬 EXPERIMENT A — Plain water (pH 6.5)")
results_a = simulate_growth(6.5)

print("\n🔬 EXPERIMENT B — Detergent water (change this pH!)")
results_b = simulate_growth(3.0)      # ← replace 3.0 with your actual detergent pH


# ───────────────────────────────────────────────────────
# TODO 3 (BONUS): Print a final comparison summary
#
# WHAT: After both experiments, print a clean summary
#       showing the final height of each experiment.
#
# WHY: This is what a scientist would write in the
#      conclusion of their lab report. "At pH 6.5 the
#      plant reached X cm. At pH Y it reached Z cm."
#
# AFTER THIS TODO: Your simulation has a proper scientific
# conclusion — just like your real experiment did.
# ───────────────────────────────────────────────────────

print("\n📊 FINAL COMPARISON")
print("=" * 45)
# YOUR SUMMARY CODE HERE ↓
# Hint: the last item in results_a has the day 7 height
# if len(results_a) > 0:
#     print(f"Experiment A final height: {results_a[-1]['height']} cm")



# ════════════════════════════════════════════════════
# 🧪 MISSION 03 — CHECK YOUR WORK
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

# ── simulate_growth checks ────────────────────────────
print("\n📌 Testing simulate_growth():")

# Test 1: returns a list
result_65 = simulate_growth(6.5)
total += 1
if isinstance(result_65, list):
    print(f"  ✅  simulate_growth(6.5) returns a list")
    passed += 1
else:
    print(f"  ❌  simulate_growth(6.5) should return a list, got: {type(result_65)}")

# Test 2: returns 7 days
total += 1
if len(result_65) == 7:
    print(f"  ✅  simulate_growth(6.5) returns 7 days of results")
    passed += 1
else:
    print(f"  ❌  expected 7 days, got {len(result_65)}")

# Test 3: day 7 height is correct (7 × 1.2 = 8.4)
total += 1
if result_65 and round(result_65[-1]["height"], 1) == 8.4:
    print(f"  ✅  Day 7 height at pH 6.5 → 8.4 cm")
    passed += 1
else:
    got_h = result_65[-1]["height"] if result_65 else "no results"
    print(f"  ❌  Day 7 height should be 8.4 cm, got: {got_h}")

# Test 4: failed experiment returns empty list
result_bad = simulate_growth(3.0)
total += 1
if result_bad == []:
    print(f"  ✅  simulate_growth(3.0) returns [] — seed didn't germinate")
    passed += 1
else:
    print(f"  ❌  simulate_growth(3.0) should return [], got: {result_bad}")

# Test 5: each result has day, height, status keys
total += 1
if result_65 and all(k in result_65[0] for k in ["day", "height", "status"]):
    print(f"  ✅  Each result has 'day', 'height', and 'status' keys")
    passed += 1
else:
    print(f"  ❌  Each result dict should have 'day', 'height', 'status' keys")

# ── Final score ───────────────────────────────────────
print("\n" + "─" * 45)
if passed == total:
    print(f"  🎉 {passed}/{total} passed — Mission 03 Complete!")
    print("  Your simulator is alive! The plant grows day by day 🌱🚀")
    print("\n  git add backend/mission_03.py")
    print("  git commit -m \"Mission 03: 7-day simulation loop complete\"")
    print("  git push origin mission-03-yourname")
elif passed >= total // 2:
    print(f"  🔥 {passed}/{total} passed — Almost! Check the ❌ above.")
else:
    print(f"  💪 {passed}/{total} passed — Keep going!")
    print("  Tip: make sure your loop appends a dict to results each day.")
print("─" * 45)
