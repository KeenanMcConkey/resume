# Job Search Subagent Prompt Template

Use this as the prompt when spawning a general-purpose subagent for job searching.
Customize the [SEARCH PARAMETERS] section before each run.

---

## TASK

Search for software engineering job openings matching the candidate profile below.
Return a curated shortlist — do NOT include full JD text, just the key fields per job.
Use WebSearch and WebFetch. Prefer jobs.lever.co, jobs.ashbyhq.com, and job-boards.greenhouse.io.

---

## CANDIDATE PROFILE

**Name:** Keenan McConkey
**Experience:** ~4 years (2021 grad, Engineering Physics UBC)
**Current role:** Operations Engineer, Brock Solutions (SFO, 2025–present)
**Prior:** Software Engineer Brock (2023–2025), Sanctuary AI robotics co-op (2022), Voltsafe embedded (2020), CARIS Lab ML/robotics (2019)
**Stack:** Python, C++, C#, Rust, TypeScript/JavaScript, SQL
**Backend:** Microservices, REST/gRPC, Docker, Kubernetes, Terraform, CI/CD, Azure/GCP
**ML/Robotics:** PyTorch, ROS, Isaac Sim, SLAM, sensor fusion, GPU inference, ML pipelines
**Databases:** PostgreSQL, MS SQL Server, MySQL, MongoDB, Redis
**Projects:** BarPath (iOS app + ML pipeline), TrashBot (autonomous robot, Jetson TX2), CLIDAW (Rust CLI DAW)
**Publication:** IEEE EMBC 2020

---

## [SEARCH PARAMETERS] — edit before each run

**Target locations:** SF Bay Area, Vancouver BC, Los Angeles, Seattle, London UK, Berlin Germany
**Role types:** Backend SWE, ML/AI SWE, Robotics SWE, Full-Stack SWE
**Experience level:** 0–3 years required, NOT roles requiring 4+ years of experience, NOT new grad/intern
**Salary range:** $120K–$220K USD or CAD $100K–$160K
**Company types:** AI/ML startups, robotics, AV, fintech, infrastructure — NOT defense contractors

**NEVER suggest:** Anduril, Shield AI, Palantir, Lockheed, Raytheon, Northrop, Joby, L3Harris, SAIC, Booz Allen, Leidos, General Dynamics, BAE Systems

**Visa/sponsorship check (IMPORTANT):** Candidate has Canadian and German citizenship and is NOT authorized to work in the US without sponsorship. When fetching each JD, check for language like:
- "US citizen or Green Card only" → EXCLUDE
- "must be a US citizen" → EXCLUDE
- "security clearance required" → EXCLUDE
- "authorized to work without sponsorship" / "no visa sponsorship" / "must be authorized to work in the US" → EXCLUDE

Canadian roles (EarnIn Vancouver, etc.) do not have this restriction — include freely.
London and Berlin roles have no citizenship/sponsorship issues (EU/UK citizen via German passport).
For remote roles, check whether they accept international workers or Canada-based applicants.

**Already applied:** Nuro, Plaid, Orb, Hive AI, Anara, CodeRabbit, EarnIn, Skild AI (update this list each run)
**Resume ready (don't re-search):** Skild AI, EarnIn, CodeRabbit

---

## OUTPUT FORMAT

Return a markdown table for each tier. For each job include:
- Company name
- Role title
- Location + remote/hybrid/onsite
- Salary range (if listed)
- Key stack/skills required
- Years of experience required
- Apply URL (direct Lever/Ashby/Greenhouse link)
- 1-sentence fit note

### Tier 1 — Strong match (4+ of these: Python/C++/C#, microservices, Docker/K8s, ML/robotics background valued, 2–4 yrs exp, right salary)

### Tier 2 — Decent match or slight stretch

### Skip — explain briefly why anything promising was ruled out (citizenship restriction, defense contractor, too senior, posting removed, etc.)

---

## SEARCH STRATEGY (batch to minimize token usage)

Run exactly 4 searches total, each covering multiple locations and role types at once:

1. `site:jobs.lever.co OR site:jobs.ashbyhq.com software engineer backend Python C++ "San Francisco" OR "Vancouver" OR "Seattle" OR "Los Angeles" 2025 2026`
2. `site:jobs.lever.co OR site:jobs.ashbyhq.com software engineer backend Python C++ "London" OR "Berlin" 2025 2026`
3. `site:jobs.lever.co OR site:jobs.ashbyhq.com software engineer robotics OR "AI inference" OR "machine learning" Python C++ Rust 2025 2026`
4. `site:job-boards.greenhouse.io software engineer backend Python robotics ML inference 2025 2026`

**WebFetch rules (minimize calls):**
- From all search results, shortlist the 6–8 most promising by title/company alone
- WebFetch only those — do not fetch every result
- If a JD page returns only CSS/JS (Lever/Ashby dynamic pages), skip the fetch and note "JD unconfirmed" — use search snippet to infer stack
- Stop fetching once you have 6 confirmed Tier 1+2 candidates

**Do not return** jobs requiring 4+ years of experience, internships, new grad roles, or already-applied companies.
