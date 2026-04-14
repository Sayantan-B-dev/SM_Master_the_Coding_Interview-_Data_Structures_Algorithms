## GitHub Contribution Graph Customization – Tool Documentation

### Overview
Three open-source tools that allow you to artificially generate or manipulate your GitHub contribution history (the green squares graph).  
**Use for fun, learning Git automation, or artistic expression – not to misrepresent actual work.**

---

### 1. Commit‑Bot  
**Repo:** [theshteves/commit-bot](https://github.com/theshteves/commit-bot)

**Purpose:** Automatically creates regular fake commits to fill out your calendar.

**How it works:**  
- Uses a cron job (or GitHub Actions) to make commits with backdated timestamps.  
- Commits can be empty or contain dummy content.

**Basic setup:**  
```bash
git clone https://github.com/theshteves/commit-bot
cd commit-bot
# Edit config file (set repo path, commit frequency, date range)
./commit-bot.sh
```

**Cron example (daily at 10 AM):**  
`0 10 * * * /path/to/commit-bot/commit-bot.sh`

**Note:** Changes may take a few hours to appear on GitHub.

---

### 2. GitHub Calendar Customizer  
**Repo:** [ZachSaucier/github-calendar-customizer](https://github.com/ZachSaucier/github-calendar-customizer)

**Purpose:** “Draw” patterns, text, or logos onto your contribution graph by backdating commits.

**How it works:**  
- Generates a script that creates commits on specific past dates matching a user‑defined grid pattern.  
- Each cell = a commit on a particular day.

**Basic usage:**  
```bash
git clone https://github.com/ZachSaucier/github-calendar-customizer
cd github-calendar-customizer
python draw.py   # interactive pattern designer
# Follow prompts: set pattern size, commit message, repo path
```

**Output:** A shell script that creates the commits. Run it, then `git push`.

**Limitations:**  
- Cannot modify dates older than your GitHub account creation.  
- Pushing many backdated commits can be slow.

---

### 3. Gitfiti  
**Repo:** [gelstudios/gitfiti](https://github.com/gelstudios/gitfiti)

**Purpose:** Similar to Calendar Customizer but with more artistic presets (e.g., logos, large text, pixel art).

**How it works:**  
- Python script that maps an ASCII art or bitmap to your contribution graph.  
- Each pixel = a commit on a specific date.

**Basic setup:**  
```bash
git clone https://github.com/gelstudios/gitfiti
cd gitfiti
python gitfiti.py   # interactive menu of designs
```

**Example – draw a rocket:**  
Choose preset → provide GitHub username & repo name → script generates commits → `git push`

**Warning:** Overwrites any existing commit history in the target repo if not careful. Use a fresh repository.

---

### Common Notes for All Tools

| Item | Detail |
|------|--------|
| **Effect visibility** | Changes may take **a few hours** to reflect on GitHub’s graph. |
| **Repo requirement** | Each tool needs a dedicated repository (create a new one, e.g., `github-art`). |
| **Push command** | After script runs: `git push origin main` (or `--force` if rewriting history). |
| **Undo** | Deleting the repository or using `git push --force` with a clean history removes the fake commits. |
| **Recruiters** | Real contribution quality matters more than graph density. Use sparingly. |

---

### Troubleshooting
- **No green squares after 6+ hours** – Check that commits have correct author email (must match GitHub account).  
- **Commits show but wrong dates** – Ensure your system clock and Git timezone are correctly set.  
- **Git push rejected** – Use `--force` only if you are the sole contributor to that repo.

---

### Final Reminder
This exercise is **completely optional** and intended for fun. If you have technical questions, visit the course’s private Discord `#helpme` channel.