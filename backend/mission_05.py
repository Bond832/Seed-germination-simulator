# ═══════════════════════════════════════════════════════
# MISSION 05 — Break It & Fix It!
# Branch: mission-05-yourname
# ═══════════════════════════════════════════════════════
#
# SCIENCE CONNECTION:
# In science, you repeat experiments to verify results.
# In coding, you test your program with unexpected inputs
# to make sure it never fails. This is called "testing"
# and every professional developer does it before shipping.
#
# BY THE END OF THIS MISSION YOU WILL HAVE:
# → A simulator that handles any input without crashing
# → A real vs simulated comparison using your actual data
# → A fully tested, production-ready Python program
# ═══════════════════════════════════════════════════════

# ── Paste your complete simulate_growth() here ───────
# Include all helper functions: will_germinate,
# daily_growth_rate, health_status, simulate_growth
# ─────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────
# TODO 1: Run all test cases without crashing
#
# WHAT: Loop through the test_cases list, call
#       simulate_growth() for each, and catch any errors
#       with try/except so the program keeps running.
#
# WHY: Right now your program probably crashes on some of
#      these values. The goal is to understand WHY it
#      crashes, then go back and fix your helper functions
#      to handle those edge cases. A program that crashes
#      is never finished — testing is how you find the gaps.
#
# WHAT TO DO WITH EACH RESULT:
#   Print "HANDLES OK ✅" if it ran without errors
#   Print "CRASHED ❌" if the except block was triggered
#
# AFTER THIS TODO: You'll know exactly which pH values
# break your program and what needs to be fixed.
# ───────────────────────────────────────────────────────
test_cases = [0, 14, 6.5, -1, 100]

print("🧪 RUNNING ALL TEST CASES")
print("=" * 50)

for ph in test_cases:
    print(f"\nTesting pH = {ph}...")
    try:
        pass  # ← replace with your simulate_growth(ph) call
    except Exception as e:
        print(f"  ❌ CRASHED: {e}")


# ───────────────────────────────────────────────────────
# TODO 2: Write a safe_input() function
#
# WHAT: A function that keeps asking the user for a pH
#       value until they enter a valid number between 0–14.
#       It should never crash no matter what the user types.
#
# WHY: Your current program crashes if someone types "hello"
#      or enters -5. safe_input() fixes that permanently.
#      Replace any input() calls in your other missions
#      with safe_input() once it's working.
#
# IT MUST HANDLE:
#   - Letters or words (ValueError from float())
#   - Numbers outside 0–14 (custom check)
#   - Keep asking until valid input is received
#
# AFTER THIS TODO: Your simulator is truly bulletproof —
# no input from any user can ever cause it to crash.
# ───────────────────────────────────────────────────────
def safe_input():
    while True:
        try:
            ph = float(input("Enter pH (0–14): "))
            if 0 <= ph <= 14:
                return ph
            else:
                print("⚠️  pH must be between 0 and 14. Try again.")
        except ValueError:
            print("⚠️  Please enter a number, not a word!")


# ───────────────────────────────────────────────────────
# TODO 3: Compare your simulation to your real experiment
#
# WHAT: Fill in the real_data dictionary with the actual
#       plant heights you recorded in your science notebook.
#       Then print a table comparing real vs simulated values.
#
# WHY: This is the most meaningful moment of the project.
#      If your simulation matches your real data closely —
#      your code correctly models the biology.
#      If they don't match — that's a genuine scientific
#      question: why did reality differ from the model?
#      Either way, you're doing real science.
#
# AFTER THIS TODO: You have a complete scientific conclusion
# — a code-generated comparison between your model and
# your real experiment. This is what scientists publish.
# ───────────────────────────────────────────────────────

# Fill in your actual measurements from science class ↓
real_data = {
    "day_1": None,   # replace None with your real cm value
    "day_2": None,
    "day_3": None,
    "day_4": None,
    "day_5": None,
    "day_6": None,
    "day_7": None,
}

# The pH you actually used in your experiment:
real_ph = 6.5   # ← change this to your actual pH

print("\n📊 REAL vs SIMULATED COMPARISON")
print(f"Experiment pH: {real_ph}")
print("=" * 55)
print(f"{'Day':<5} | {'Real (cm)':<12} | {'Simulated (cm)':<16} | Close?")
print("-" * 55)

# YOUR COMPARISON LOOP HERE ↓
# Loop through days 1–7, calculate simulated height,
# compare to real_data["day_X"], print the row.
# Mark "✅ Yes" if difference < 0.5 cm, "⚠️  No" otherwise.



# ════════════════════════════════════════════════════
# 🧪 MISSION 05 — CHECK YOUR WORK
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
        passed += 1
    else:
        print(f"  ❌  {label}")
        print(f"       expected: '{expected}'  |  got: '{got}'")

# ── Test 1: safe_input exists and is callable ─────────
print("\n📌 Testing safe_input() exists:")
total += 1
if callable(globals().get("safe_input")):
    print("  ✅  safe_input() function exists")
    passed += 1
else:
    print("  ❌  safe_input() function not found — did you define it?")

# ── Test 2: simulate_growth doesn't crash on edge cases
print("\n📌 Testing edge cases don't crash:")
edge_cases = [0, 14, -1, 100]
for val in edge_cases:
    total += 1
    try:
        simulate_growth(val)
        print(f"  ✅  simulate_growth({val}) — handled without crashing")
        passed += 1
    except Exception as e:
        print(f"  ❌  simulate_growth({val}) crashed: {e}")

# ── Test 3: real_data has been filled in ──────────────
print("\n📌 Checking real_data:")
total += 1
filled = [v for v in real_data.values() if v is not None]
if len(filled) == 7:
    print(f"  ✅  All 7 days of real data filled in!")
    passed += 1
elif len(filled) > 0:
    print(f"  ⚠️   {len(filled)}/7 days filled in — add the rest from your notebook")
    passed += 1  # partial credit
else:
    print(f"  ❌  real_data is all None — fill in your actual measurements!")

# ── Final score ───────────────────────────────────────
print("\n" + "─" * 45)
if passed == total:
    print(f"  🏆 {passed}/{total} passed — Mission 05 Complete!")
    print("  You finished the whole project! This is real software. 🎉")
    print("\n  git add .")
    print("  git commit -m \"Mission 05: testing and bug fixes complete\"")
    print("  git push origin mission-05-yourname")
elif passed >= total // 2:
    print(f"  🔥 {passed}/{total} passed — So close! Check the ❌ above.")
else:
    print(f"  💪 {passed}/{total} passed — Keep going!")
    print("  Tip: make sure safe_input() is defined and real_data is filled in.")
print("─" * 45)
