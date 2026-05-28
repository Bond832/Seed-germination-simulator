# 🌱 Seed Germination pH Simulator
### Advanced coding

---

## What are we building?

In science class, you ran a real experiment testing how water pH affects seed germination.
You used detergent and plain water, measured plant height every day, and recorded your results.

**Now you're rebuilding that experiment in code** — so anyone in the world can run it
virtually, change the pH, and see what happens to the plant.

- 🐍 **Python** handles all the logic (calculations, simulations, data)
- 🌐 **JavaScript** builds the interactive interface users see and click
- 🐙 **GitHub** tracks every change you make — just like real developers

---

## How to open this project (No installation needed!)

This project runs fully in the browser using **GitHub Codespaces**.

### Step 1 — Open in Codespaces
1. Go to this project's GitHub repository
2. Click the green **`<> Code`** button
3. Click the **Codespaces** tab
4. Click **"Create codespace on main"**
5. Wait ~30 seconds — a full VS Code editor opens in your browser ✅

### Step 2 — Run Python files
Open the terminal inside Codespaces (`` Ctrl + ` ``) and type:
```bash
python backend/mission_01.py
```

### Step 3 — Run the frontend
In the terminal:
```bash
cd frontend
python -m http.server 5500
```
Codespaces will pop up a notification — click **"Open in Browser"** to see your app.

---

## Project structure

```
seed-germination-simulator/
│
├── backend/
│   ├── mission_01.py      ← Session 2: pH input & classification
│   ├── mission_02.py      ← Session 3: germination logic
│   ├── mission_03.py      ← Session 4: 7-day simulation loop
│   └── mission_05.py      ← Session 7: testing & bug fixes
│
├── frontend/
│   ├── index.html         ← Session 5: app structure
│   ├── style.css          ← Session 5: styling
│   └── app.js             ← Session 6: simulation logic in JS
│
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md   ← PR checklist for peer reviews
│
├── CURRICULUM.md          ← Full session-by-session guide
└── README.md              ← You are here
```

---

## GitHub workflow — do this every session

### 1. Create your branch at the start of each mission
```bash
git checkout -b mission-01-yourname
```
> 💡 Replace `yourname` with your actual name. Example: `mission-01-alice`

### 2. Write your code, save often

### 3. Stage and commit your work
```bash
git add .
git commit -m "Mission 01: completed pH classification"
```
> 💡 Write a real commit message — describe what you actually did.

### 4. Push your branch to GitHub
```bash
git push origin mission-01-yourname
```

### 5. Open a Pull Request
1. Go to the GitHub repo in your browser
2. You'll see a yellow banner — click **"Compare & pull request"**
3. Fill in the PR template (what you did, what you struggled with)
4. Assign your **partner** as a reviewer

### 6. Peer Review
- Your partner reads your code and leaves comments
- They click **"Approve"** or **"Request changes"**
- Once approved, merge to `main`

---

## Team

| Name | GitHub username |
|------|----------------|
| Partner 1: | |
| Partner 2: | |

---


