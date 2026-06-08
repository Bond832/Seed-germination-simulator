# ═══════════════════════════════════════════════════════
# MISSION 01 — What's Your Water?
# Branch: mission-01-yourname
# ═══════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────
# TODO 1: classify_ph(ph)
# ───────────────────────────────────────────────────────
def classify_ph(ph):

    if ph < 6.0:
        return "acidic"
    elif ph <= 7.5:
        return "neutral"
    else:
        return "alkaline"


# ───────────────────────────────────────────────────────
# TODO 2: predict_growth(ph)
# ───────────────────────────────────────────────────────
def predict_growth(ph):

    if ph < 4.5 or ph > 8.5:
        return "The seed will likely fail. 🔴 This pH is too extreme."
    elif ph < 6.0 or ph > 7.5:
        return "The seed may struggle. 🟡 Water is outside the optimal range."
    else:
        return "The seed will germinate well! 🌱 pH is in the optimal range."


# ───────────────────────────────────────────────────────
# TODO 3: Get input safely from the user
# ───────────────────────────────────────────────────────

print("🌱 Seed Germination pH Simulator")
print("=" * 35)

while True:
    try:
        user_input = input("Enter pH value (0.0 - 14.0): ")
        ph = float(user_input)
        break
    except ValueError:
        print("❌ Invalid input. Please enter a valid decimal number (e.g., 7.0).")

# Call your functions and print the results
water_type = classify_ph(ph)
prediction = predict_growth(ph)

print("-" * 35)
print(f"pH entered  : {ph}")
print(f"Water type  : {water_type}")
print(f"Prediction  : {prediction}")

# ════════════════════════════════════════════════════
# 🧪 MISSION 01 — CHECK YOUR WORK
# Run this file to see if your functions are correct.
# Every ✅ means you got it right!
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
        print(f"       expected: '{expected}'")
        print(f"       got:      '{got}'")

def check_contains(label, got, keyword):
    global passed, total
    total += 1
    if got is not None and keyword.lower() in str(got).lower():
        print(f"  ✅  {label}")
        print(f"       got: '{got}'")
        passed += 1
    else:
        print(f"  ❌  {label}")
        print(f"       expected your message to mention: '{keyword}'")
        print(f"       got: '{got}'")

# ── classify_ph checks ───────────────────────────────
print("\n📌 Testing classify_ph():")
check("classify_ph(3.0)  → 'acidic'",   classify_ph(3.0),  "acidic")
check("classify_ph(5.9)  → 'acidic'",   classify_ph(5.9),  "acidic")
check("classify_ph(6.0)  → 'neutral'",  classify_ph(6.0),  "neutral")
check("classify_ph(6.5)  → 'neutral'",  classify_ph(6.5),  "neutral")
check("classify_ph(7.5)  → 'neutral'",  classify_ph(7.5),  "neutral")
check("classify_ph(9.0)  → 'alkaline'", classify_ph(9.0),  "alkaline")
check("classify_ph(12.0) → 'alkaline'", classify_ph(12.0), "alkaline")

# ── predict_growth checks ────────────────────────────
print("\n📌 Testing predict_growth():")
check_contains("predict_growth(6.5) → mentions germinate",   predict_growth(6.5),  "germinate")
check_contains("predict_growth(3.0) → mentions fail/acidic", predict_growth(3.0),  "fail")
check_contains("predict_growth(10.0) → mentions fail/alkaline", predict_growth(10.0), "fail")

# ── Final score ──────────────────────────────────────
print("\n" + "─" * 45)
if passed == total:
    print(f"  🎉 {passed}/{total} passed — Mission 01 Complete!")
    print("  You crushed it! Time to push to GitHub 🚀")
    print("\n  git add backend/mission_01.py")
    print("  git commit -m \"Mission 01: pH classification done\"")
    print("  git push origin mission-01-yourname")
elif passed >= total // 2:
    print(f"  🔥 {passed}/{total} passed — So close! Check the ❌ lines above.")
else:
    print(f"  💪 {passed}/{total} passed — Keep going, you're learning!")
    print("  Tip: re-read the TODO comments carefully.")
print("─" * 45)