# ═══════════════════════════════════════════════════════
# MISSION 03 — Watch It Grow!
# Branch: mission-03-yourname
# ═══════════════════════════════════════════════════════

import time

# ── Functions from Mission 02 ─────────────────────────

def will_germinate(ph):
    return 5.5 <= ph <= 7.5

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
    if 6.0 <= ph <= 7.0:
        return "Excellent"
    elif 5.5 <= ph < 6.0:
        return "Fair"
    elif 7.0 < ph <= 8.0:
        return "Poor"
    else:
        return "Dead"


# ───────────────────────────────────────────────────────
# TODO 1: Build the 7-day simulation loop
# ───────────────────────────────────────────────────────

def simulate_growth(ph, days=7):
    print(f"\nStarting experiment at pH {ph}")
    print("=" * 45)

    if not will_germinate(ph):
        print("Seed did not germinate at this pH level.")
        print(f"pH {ph} is outside the safe range (5.5 – 7.5)")
        return []

    print("Seed germinated! Simulating growth...\n")
    print(f"{'Day':<5} | {'Height (cm)':<12} | Health")
    print("-" * 35)

    height = 0.0
    rate = daily_growth_rate(ph)
    results = []

    for day in range(1, days + 1):
        height += rate
        status = health_status(ph)

        print(f"{day:<5} | {height:<12.1f} | {status}")

        results.append({
            "day": day,
            "height": height,
            "status": status
        })

        time.sleep(0.5)

    return results


# ───────────────────────────────────────────────────────
# TODO 2: Run two experiments and compare
# ───────────────────────────────────────────────────────

print("EXPERIMENT A — Plain water (pH 6.5)")
results_a = simulate_growth(6.5)

print("\nEXPERIMENT B — Detergent water (change this pH!)")
results_b = simulate_growth(3.0)


# ───────────────────────────────────────────────────────
# TODO 3: Final comparison
# ───────────────────────────────────────────────────────

print("\nFINAL COMPARISON")
print("=" * 45)

if len(results_a) > 0:
    print(f"Experiment A final height: {results_a[-1]['height']:.1f} cm")
else:
    print("Experiment A: Seed did not germinate")

if len(results_b) > 0:
    print(f"Experiment B final height: {results_b[-1]['height']:.1f} cm")
else:
    print("Experiment B: Seed did not germinate")


# ════════════════════════════════════════════════════
# CHECKING YOUR WORK
# ════════════════════════════════════════════════════

print("\n" + "-" * 45)
print("CHECKING YOUR WORK...")
print("-" * 45)

passed = 0
total = 0

def check(label, got, expected):
    global passed, total
    total += 1
    if got == expected:
        print(f"PASS {label}")
        print(f"     got: '{got}'")
        passed += 1
    else:
        print(f"FAIL {label}")
        print(f"     expected: '{expected}' | got: '{got}'")


print("\nTesting simulate_growth():")

# Test 1
result_65 = simulate_growth(6.5)
total += 1
if isinstance(result_65, list):
    print("PASS simulate_growth(6.5) returns a list")
    passed += 1
else:
    print(f"FAIL simulate_growth(6.5) should return list, got {type(result_65)}")

# Test 2
total += 1
if len(result_65) == 7:
    print("PASS returns 7 days of results")
    passed += 1
else:
    print(f"FAIL expected 7 days, got {len(result_65)}")

# Test 3
total += 1
if result_65 and round(result_65[-1]["height"], 1) == 8.4:
    print("PASS correct final height (8.4 cm)")
    passed += 1
else:
    got = result_65[-1]["height"] if result_65 else None
    print(f"FAIL expected 8.4 cm, got {got}")

# Test 4
result_bad = simulate_growth(3.0)
total += 1
if result_bad == []:
    print("PASS failed germination returns empty list")
    passed += 1
else:
    print(f"FAIL expected [], got {result_bad}")

# Test 5
total += 1
if result_65 and all(k in result_65[0] for k in ["day", "height", "status"]):
    print("PASS correct dictionary structure")
    passed += 1
else:
    print("FAIL missing required keys")


print("\n" + "-" * 45)
if passed == total:
    print(f"SUCCESS: {passed}/{total} tests passed — Mission 03 Complete!")
elif passed >= total // 2:
    print(f"{passed}/{total} passed — Almost there!")
else:
    print(f"{passed}/{total} passed — Keep improving!")
print("-" * 45)