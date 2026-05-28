# ═══════════════════════════════════════════════════════
# MISSION 01 — What's Your Water?
# Branch: mission-01-yourname
# ═══════════════════════════════════════════════════════
#
# SCIENCE CONNECTION:
# In your experiment, you measured the pH of detergent
# before watering the seeds. This mission does the same
# thing in code — it takes a pH value and tells the user
# exactly what kind of water it is and what will happen
# to their seed.
#
# BY THE END OF THIS MISSION YOU WILL HAVE:
# → A working Python program that reads input and makes decisions
# → Your first real functions that other missions will use
# ═══════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────
# TODO 1: classify_ph(ph)
#
# WHAT: Write a function that takes a pH number and returns
#       a string describing what type of water it is.
#
# WHY: Every other mission depends on this. Mission 02 uses
#      it to decide if a seed survives. Mission 04 uses it
#      to color the background of the app.
#
# RULES:
#   pH < 6.0          → return "acidic"
#   pH 6.0 up to 7.5  → return "neutral"
#   pH > 7.5          → return "alkaline"
#
# AFTER THIS TODO: You can tell any pH value apart — the
# foundation of your entire simulator is in place.
# ───────────────────────────────────────────────────────
def classify_ph(ph):
    # YOUR CODE HERE ↓
    pass


# ───────────────────────────────────────────────────────
# TODO 2: predict_growth(ph)
#
# WHAT: Write a function that returns a helpful message
#       predicting what will happen to the seed at this pH.
#
# WHY: This is the first time your program "talks" to the
#      user like a scientist. It makes the simulator feel
#      real and informative, not just a number cruncher.
#
# HINT: Think about what you observed in science class.
#   - What happened to seeds watered with strong detergent?
#   - What happened to seeds watered with plain water?
#   Use that knowledge to write your messages.
#
# EXAMPLE return values:
#   "The seed will germinate well! 🌱 pH is in the optimal range."
#   "The seed may struggle. 🟡 Water is too acidic."
#   "The seed will likely fail. 🔴 This pH is too extreme."
#
# AFTER THIS TODO: Your program doesn't just classify —
# it actually gives useful scientific advice.
# ───────────────────────────────────────────────────────
def predict_growth(ph):
    # YOUR CODE HERE ↓
    pass


# ───────────────────────────────────────────────────────
# TODO 3: Get input safely from the user
#
# WHAT: Ask the user to type a pH value. Convert it to a
#       float (decimal number). If they type a word like
#       "hello", catch the error and ask again.
#
# WHY: Real programs never crash on bad input. A user
#      typing the wrong thing should get a helpful message,
#      not a scary error. This is called "input validation"
#      and every professional developer does it.
#
# TOOLS TO USE:
#   input("Enter pH: ")   ← asks the user to type something
#   float(...)            ← converts text to a decimal number
#   try / except          ← catches errors before they crash
#
# AFTER THIS TODO: Your program is bulletproof — it handles
# mistakes gracefully and keeps running no matter what.
# ───────────────────────────────────────────────────────

print("🌱 Seed Germination pH Simulator")
print("=" * 35)

# Replace this fixed value with your input() code:
ph = 6.5

# Call your functions and print the results
water_type = classify_ph(ph)
prediction = predict_growth(ph)

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
