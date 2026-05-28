# 📅 Curriculum — Seed Germination pH Simulator
### Advanced coding

---

## Overview

| Session | Focus | File | Branch name |
|---------|-------|------|-------------|
| 1 | Setup — template repo, Codespaces, project tour | — | `setup-yourname` |
| 2 | Mission 01 — pH input & classification | `backend/mission_01.py` | `mission-01-yourname` |
| 3 | Mission 02 — Germination logic | `backend/mission_02.py` | `mission-02-yourname` |
| 4 | Mission 03 — 7-day simulation loop | `backend/mission_03.py` | `mission-03-yourname` |
| 5 | Mission 04A — HTML + CSS frontend | `frontend/index.html` + `style.css` | `mission-04-yourname` |
| 6 | Mission 04B — JavaScript logic | `frontend/app.js` | `mission-04-yourname` |
| 7 | Mission 05 — Testing & bug fixes | `backend/mission_05.py` | `mission-05-yourname` |
| 8 | Final demo + peer presentations | All files | — |

---

## Session 1 — Setup & Orientation
**Goal:** Everyone has their own copy of the project, a working Codespace, and understands what they're building.

### What to do

**Part 1 — Create your own copy of the project**
1. Create a GitHub account at [github.com](https://github.com) if you don't have one
2. Go to the repository link your teacher shared
3. Click the green **"Use this template"** button → **"Create a new repository"**
4. Name it `seed-germination-simulator`, make sure it's under **your own account**
5. Click **"Create repository"** ✅

> 💡 Only one person per pair does steps 2–5. The other partner gets added as a collaborator next.

**Part 2 — Add your partner as a collaborator**
1. In your new repo, go to **Settings → Collaborators**
2. Click **"Add people"** and type your partner's GitHub username
3. Your partner accepts the invite from their email or GitHub notifications

**Part 3 — Open in Codespaces**
1. Click the green **`<> Code`** button in your repo
2. Click the **Codespaces** tab
3. Click **"Create codespace on main"**
4. Wait ~30 seconds — a full VS Code editor opens in your browser ✅

**Part 4 — Explore and make your first commit**
1. Open the terminal inside Codespaces (`` Ctrl+` ``)
2. Run `python --version` to confirm Python is ready
3. Explore the folder structure — find `backend/` and `frontend/`
4. Create your first branch:
```bash
git checkout -b setup-yourname
```
5. Open `README.md` and fill in your name and GitHub username in the Team table
6. Save, commit, and push:
```bash
git add .
git commit -m "Setup: added team names to README"
git push origin setup-yourname
```
7. Go to your GitHub repo in the browser, open a Pull Request, and ask your partner to review it
8. Partner approves → merge to `main`

### By the end of Session 1 you will have
- ✅ Your own independent copy of the project from the template
- ✅ Your partner added as a collaborator
- ✅ A working Codespace — browser-based VS Code with Python ready
- ✅ Your first branch, commit, push, pull request, and merge

---

## Session 2 — Mission 01: What's Your Water?
**File:** `backend/mission_01.py`
**Branch:** `git checkout -b mission-01-yourname`

### Science connection
Remember measuring the pH of your detergent before watering the seeds?
This mission does exactly that in code — it takes a pH value and tells the user what kind of water it is.

### What you'll build
A Python program that:
- Asks the user to enter a pH value
- Classifies it as acidic, neutral, or alkaline
- Predicts what will happen to the seed
- Handles errors gracefully (no crashing!)

### How to run it
In the Codespaces terminal:
```bash
python backend/mission_01.py
```

### Python concepts you'll learn
`input()` · `float()` · `if/elif/else` · `functions` · `f-strings` · `try/except`

### End of session checklist
- [ ] `classify_ph()` returns the correct label for at least 5 different pH values
- [ ] `predict_growth()` returns a clear, helpful message
- [ ] Program doesn't crash when you type a word instead of a number
- [ ] Committed and pushed to your branch
- [ ] Pull request opened and partner has reviewed

---

## Session 3 — Mission 02: Will It Grow?
**File:** `backend/mission_02.py`
**Branch:** `git checkout -b mission-02-yourname`

### Science connection
Your experiment showed that some seeds grew well and others didn't, depending on the pH.
This mission writes the actual rules — the logic that decides what happens to the seed.

### What you'll build
Three functions that power your simulation:
- `will_germinate(ph)` — True or False
- `daily_growth_rate(ph)` — how many cm per day
- `health_status(ph)` — Healthy, Struggling, or Failed

### How to run it
```bash
python backend/mission_02.py
```

### Python concepts you'll learn
`boolean` · `return values` · `comparison operators` · `nested conditions` · `testing functions`

### End of session checklist
- [ ] All three functions return correct values for test pH values: 4.0, 5.5, 6.5, 7.0, 9.0
- [ ] Test table prints cleanly with correct output for each
- [ ] Committed and pushed to your branch
- [ ] Pull request opened and partner has reviewed

---

## Session 4 — Mission 03: Watch It Grow!
**File:** `backend/mission_03.py`
**Branch:** `git checkout -b mission-03-yourname`

### Science connection
You measured your real plant every day for 7 days and wrote it in your notebook.
This mission brings that table to life — the program simulates each day automatically.

### What you'll build
- A `simulate_growth()` function with a 7-day loop
- Daily output: day number, height in cm, health status
- A short delay between days using `time.sleep()` — it feels alive!
- A final comparison between two pH experiments

### How to run it
```bash
python backend/mission_03.py
```

### Python concepts you'll learn
`for loops` · `range()` · `lists of dictionaries` · `time.sleep()` · `import`

### The magic moment 🌟
Run your simulation with the same pH your real experiment used.
Does the simulated height match what you actually measured?
If not — that's a great debugging challenge!

### End of session checklist
- [ ] 7-day loop runs and prints each day correctly
- [ ] `time.sleep()` added — it feels like watching the plant grow
- [ ] Comparison between two pH values is printed
- [ ] Committed and pushed to your branch
- [ ] Pull request opened and partner has reviewed

---

## Session 5 — Mission 04A: Build the Interface
**Files:** `frontend/index.html` + `frontend/style.css`
**Branch:** `git checkout -b mission-04-yourname`

### What's happening here
The Python logic is done. Now you build what users actually see.
HTML is the structure (like the skeleton), CSS is the styling (like the clothes).

### What you'll build
- A pH slider (1–14) that shows the current value
- A "Run Simulation" button
- A plant visual that will grow on screen (the stem grows via JS next session)
- A results table with columns: Day | Height (cm) | Status

### How to preview your page
In the Codespaces terminal:
```bash
cd frontend
python -m http.server 5500
```
Codespaces will show a notification — click **"Open in Browser"** to see your page live.

### HTML/CSS concepts you'll learn
`HTML structure` · `input type="range"` · `CSS flexbox` · `CSS transitions` · `table styling`

### End of session checklist
- [ ] Slider shows and updates the displayed pH number
- [ ] Button exists and is styled
- [ ] Plant container and stem div are in the HTML
- [ ] Results table has correct column headers
- [ ] Page looks good — at least some CSS styling applied
- [ ] Committed and pushed to `mission-04-yourname`

---

## Session 6 — Mission 04B: Bring It to Life
**File:** `frontend/app.js`
**Branch:** same `mission-04-yourname` branch

### What's happening here
JavaScript is the brain of your frontend.
It reads the slider, runs the simulation logic, grows the plant on screen, and fills the table — all in real time.

### What you'll build
- Slider event listener — updates display and background color live
- `classifyPH()` — mirrors your Python logic from Mission 01
- `getDailyRate()` — mirrors your Python logic from Mission 02
- `runSimulation()` — 7-day async loop that animates the plant and fills the table

### The coolest part 🌟
`async/await` with `setTimeout` — each day appears one at a time, 600ms apart.
The plant stem grows taller on screen. Your science experiment is now alive in the browser!

### JavaScript concepts you'll learn
`functions` · `DOM manipulation` · `event listeners` · `async/await` · `setTimeout` · `for loops`

### End of session checklist
- [ ] Slider updates pH display and background color in real time
- [ ] Clicking Run fills the table row by row
- [ ] Plant stem animates and grows taller
- [ ] Health status cells are color-coded (green / yellow / red)
- [ ] Committed, pushed, PR opened, partner reviewed, merged to `main` ✅

### 🌟 Bonus (if you finish early)
Replace the plain growing stem with a real SVG illustrated plant that changes shape day by day — sprouting leaves on day 3, a bud on day 5, a full plant on day 7, and a wilted brown plant if the pH was too extreme. The bonus TODO in `app.js` walks you through exactly how to do it.

---

## Session 7 — Mission 05: Break It & Fix It
**File:** `backend/mission_05.py`
**Branch:** `git checkout -b mission-05-yourname`

### What's happening here
Real developers break their own code on purpose to make it stronger.
Swap computers with another pair and try to crash their simulator. Then fix your own bugs.

### The challenge list — try every single one
- Enter pH = 0 — crash or handled?
- Enter pH = 14 — what message appears?
- Type `hello` instead of a number — crash or handled?
- Enter pH = 6.5 — does the output match your real experiment data?
- Run with pH = -1 — is that even possible?

### What you'll add
- `safe_input()` — never crashes, always asks again politely
- `try/except` error handling around all risky code
- A real vs simulated comparison using your actual notebook data

### End of session checklist
- [ ] All 5 test cases handled without crashing
- [ ] `safe_input()` works correctly
- [ ] Real vs simulated comparison table prints
- [ ] Committed, pushed, PR opened, partner reviewed

---

## Session 8 — Final Demo Day 🎉
**No new code — show what you built!**

### Each pair presents (5 minutes)
1. **Run the Python simulation** — show it in the Codespaces terminal
2. **Open the frontend** — demonstrate the slider and plant animation
3. **Show your GitHub** — show your branches, PRs, and commit history
4. **One thing you're proud of** — any line of code, any feature
5. **One thing you'd add next** — what would Mission 06 be?

### Reflection questions
- What was the hardest bug you fixed?
- What moment felt most satisfying?
- How does the code connect to what you did in science class?
- What would you build next?

---

## Branch naming convention

Always follow this pattern — replace `yourname` with your actual first name:
```
setup-alice
mission-01-alice
mission-02-alice
mission-04-alice
```

One branch per mission per person. Never commit directly to `main`.

---

## Peer review guide

When reviewing your partner's Pull Request, check:

- [ ] Does the code run without errors?
- [ ] Do the functions return the right values?
- [ ] Are there comments explaining what the code does?
- [ ] Are variable names clear and readable?
- [ ] Is there anything you don't understand? (Ask in a comment!)
- [ ] Is there a better or simpler way to do something? (Suggest it kindly!)

Leave at least **2 comments** on every PR — one thing you liked, one suggestion.

---


