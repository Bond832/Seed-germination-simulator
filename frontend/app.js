// ═══════════════════════════════════════════════════════
// MISSION 04B — JavaScript Simulation Logic
// Session 6 | Branch: mission-04-yourname (same branch!)
// ═══════════════════════════════════════════════════════
//
// WHAT IS JAVASCRIPT DOING HERE?
// Your HTML is the structure. Your CSS is the style.
// JavaScript is the brain — it reads the slider, runs
// the simulation logic, grows the plant, and fills the
// table. Everything interactive on this page is JS.
//
// NOTICE: The logic here mirrors your Python exactly.
// classifyPH() is the same as classify_ph().
// getDailyRate() is the same as daily_growth_rate().
// This is intentional — you're rebuilding your Python
// logic so it runs in the browser.
//
// BY THE END OF THIS FILE YOU WILL HAVE:
// → A fully interactive pH slider with live color feedback
// → A plant that visibly grows on screen day by day
// → A color-coded results table filled automatically
// → BONUS: A real illustrated SVG plant with growth stages
// ═══════════════════════════════════════════════════════


// ───────────────────────────────────────────────────────
// TODO 1: Connect the pH Slider to the page
//
// WHAT: Add an event listener to the slider so that when
//       the user moves it, the pH display updates and the
//       page background color changes to match the pH type.
//
// WHY: Without this, moving the slider does nothing visible.
//      Real apps give instant feedback to every user action.
//      This is called "reactivity" — the page reacts to input.
//      After this, every slider movement will feel alive.
//
// HOW:
//   slider.addEventListener('input', function() {
//     const ph = parseFloat(this.value);
//     phDisplay.textContent = ph.toFixed(1);
//     const info = classifyPH(ph);
//     phLabel.textContent = info.label;
//     document.body.style.backgroundColor = info.bgColor;
//   });
//
// AFTER THIS TODO: Moving the slider instantly updates
// the pH number, the label, and the background color.
// ───────────────────────────────────────────────────────
const slider = document.getElementById('phSlider');
const phDisplay = document.getElementById('phDisplay');
const phLabel = document.getElementById('phLabel');

// YOUR EVENT LISTENER HERE ↓


// ───────────────────────────────────────────────────────
// TODO 2: classifyPH(ph)
//
// WHAT: Return an object with a label and a background color.
//       Example: { label: "Neutral", bgColor: "#d8f3dc" }
//
// WHY: This function is called every time the slider moves
//      (TODO 1 above) and also at the start of runSimulation().
//      It tells the app two things: what to display as text,
//      and what background color to show.
//      Without it, there's no live color feedback.
//
// RANGES:
//   pH < 6.0    → label: "Acidic"   bgColor: "#fde8e8" (light red)
//   pH ≤ 7.5    → label: "Neutral"  bgColor: "#d8f3dc" (light green)
//   pH > 7.5    → label: "Alkaline" bgColor: "#dbeafe" (light blue)
//
// AFTER THIS TODO: The page background changes color live
// as the user moves the slider — acidic turns red, neutral
// stays green, alkaline goes blue.
// ───────────────────────────────────────────────────────
function classifyPH(ph) {
    // YOUR CODE HERE ↓
}


// ───────────────────────────────────────────────────────
// TODO 3: getDailyRate(ph)
//
// WHAT: Return how many cm the plant grows per day.
//       This is the JavaScript version of daily_growth_rate()
//       from your Python mission_02.py.
//
// WHY: runSimulation() (TODO 5) calls this once and uses
//      the result every day in the loop to add to height.
//      If this is wrong, every day of the simulation is wrong.
//      It must match your Python logic exactly.
//
// RATES (same as Python):
//   pH 6.0 – 7.0  → 1.2 cm/day
//   pH 5.5 – 6.0  → 0.7 cm/day
//   pH 7.0 – 8.0  → 0.5 cm/day
//   anything else → 0.0 cm/day
//
// AFTER THIS TODO: The simulation knows exactly how fast
// to grow the plant for any pH value.
// ───────────────────────────────────────────────────────
function getDailyRate(ph) {
    // YOUR CODE HERE ↓
}


// ───────────────────────────────────────────────────────
// TODO 4: getHealthStatus(ph)
//
// WHAT: Return an object with a label and a CSS color.
//       Example: { label: "Healthy 🟢", color: "#2d6a4f" }
//
// WHY: runSimulation() uses this to color-code each row
//      of the results table. Green rows, yellow rows, red
//      rows — exactly like a color-coded lab report.
//      Without it, every row looks the same.
//
// STATUSES:
//   Healthy 🟢   → color: "#2d6a4f" (dark green)
//   Struggling 🟡 → color: "#b45309" (amber)
//   Failed 🔴    → color: "#dc2626" (red)
//
// AFTER THIS TODO: Each table row will be color-coded
// automatically based on the plant's health status.
// ───────────────────────────────────────────────────────
function getHealthStatus(ph) {
    // YOUR CODE HERE ↓
}


// ───────────────────────────────────────────────────────
// TODO 5: runSimulation()
//
// WHAT: This is the main function — it runs when the user
//       clicks the Run button. It loops through 7 days,
//       adds a table row for each day, and grows the plant.
//
// WHY: This is where Python logic meets a visual interface.
//      The same 7-day loop you built in mission_03.py is
//      now animated on screen with a growing plant stem.
//      This is the payoff of all the previous missions.
//
// THIS FUNCTION MUST:
//   1. Read the current pH from the slider
//   2. Clear the previous results (tbody.innerHTML = '')
//   3. Reset the plant stem height to 0
//   4. Get the daily rate using getDailyRate()
//   5. Loop days 1 to 7:
//      a. Add rate to total height
//      b. Create a <tr> with 3 <td> cells: day, height, status
//      c. Color the status cell using getHealthStatus().color
//      d. Append the row to the table body
//      e. Grow the plant stem: stem.style.height = (height * 12) + 'px'
//      f. Wait 600ms before the next day (see hint below)
//
// HINT — how to wait 600ms in JavaScript:
//   Make the function async and use:
//   await new Promise(resolve => setTimeout(resolve, 600));
//   Add "async" before "function" for this to work.
//
// AFTER THIS TODO: Clicking Run animates the plant growing
// day by day, fills the table row by row, and shows
// color-coded health status for every day — your complete
// interactive science experiment simulator is done!
// ───────────────────────────────────────────────────────
async function runSimulation() {
    const ph = parseFloat(slider.value);
    const rate = getDailyRate(ph);
    const tbody = document.getElementById('resultsBody');
    const stem = document.getElementById('plantStem');

    // Clear previous results
    tbody.innerHTML = '';
    stem.style.height = '0px';

    let height = 0;

    // YOUR 7-DAY LOOP HERE ↓
    // for (let day = 1; day <= 7; day++) {
    //     ...
    // }
}


// ── Initialize on page load ───────────────────────────
// Set the slider to pH 7.0 and fire the display update
// so the page looks correct when it first opens.
// YOUR CODE HERE ↓


// ───────────────────────────────────────────────────────
// 🌟 BONUS TODO: Make the plant look alive with SVG
//
// WHAT: Replace the plain growing stem div with a real
//       illustrated plant built from SVG shapes.
//       The plant should visually change as it grows —
//       showing a sprout on day 1, small leaves on day 3,
//       and a full plant with multiple leaves by day 7.
//
// WHY: Right now the plant is just a green rectangle
//      getting taller. That works, but it doesn't feel
//      like a real plant. SVG lets you draw shapes directly
//      in the browser — stems, leaves, roots — all in code.
//      This bonus makes your simulator look like a real
//      science app, not just a homework project.
//
// HOW IT WORKS:
//   SVG is like HTML but for drawing. You add it inside
//   your HTML file and control it with JavaScript.
//   Each "stage" of growth shows different shapes.
//
// SUGGESTED GROWTH STAGES:
//   Day 1 → tiny sprout poking out of soil (just a curve)
//   Day 2 → short stem, no leaves yet
//   Day 3 → stem + 1 small leaf on the left
//   Day 4 → stem + 1 leaf left + 1 leaf right
//   Day 5 → taller stem + 2 leaves + a bud at the top
//   Day 6 → full stem + 3 leaves
//   Day 7 → full plant with flower or seed pod at the top
//
//   If the plant FAILED (pH too extreme):
//         → show a wilted brown drooping stem instead
//
// STEPS TO IMPLEMENT:
//   1. In index.html, replace #plantStem with an <svg> tag:
//      <svg id="plantSvg" width="120" height="180"
//           viewBox="0 0 120 180"></svg>
//
//   2. Write a function updatePlantStage(day, ph) that
//      uses innerHTML to draw different SVG shapes
//      depending on the day number and health status.
//      Example for day 1:
//        document.getElementById('plantSvg').innerHTML = `
//          <line x1="60" y1="180" x2="60" y2="150"
//                stroke="#2d6a4f" stroke-width="4"/>
//          <ellipse cx="60" cy="145" rx="6" ry="10"
//                   fill="#52b788" transform="rotate(-20 60 145)"/>
//        `;
//
//   3. Call updatePlantStage(day, ph) inside your 7-day
//      loop in runSimulation(), after each await.
//
//   4. For a failed/wilted plant, use brown colors (#8B4513)
//      and rotate the shapes to droop downward.
//
// AFTER THIS BONUS TODO: Your simulator has a real animated
// plant that visibly sprouts, grows leaves, and either
// thrives or wilts depending on the pH — just like your
// real experiment, but alive on screen.
// ───────────────────────────────────────────────────────
