# Resume Repository — Claude Context

## About Keenan McConkey

**Portfolio:** http://keenanmcconkey.dev
**GitHub:** https://github.com/KeenanMcConkey
**Contact:** k.t.mcconkey@gmail.com • (415) 216-7605 • San Francisco, CA

Engineering Physics grad (UBC, 2021, GPA 3.75) with a background at the intersection of software and physical systems — robotics, embedded systems, ML, and backend infrastructure.

## Education

**University of British Columbia** — BASc Engineering Physics, 2016–2021
- GPA 3.75 (81% avg); Graduated with Distinction; 3× Dean's Honour List (2017, 2019, 2020)
- Specialization in Computer Science

**Langara College** — Engineering Transfer, 2016
- GPA 3.86/4.33; Dean's Honour Roll 2015/16

**Relevant Coursework:** Machine Learning & Data Mining, Computer Vision, Algorithm Design & Analysis, Digital Systems & Microcomputers, Computational Physics, Statistical Mechanics, Electromagnetic Theory I & II, Quantum Mechanics, Applied Optics, Mechanical Design, Electronic Circuits I & II, Control Systems, PDEs I & II, Applied Probability, Applied Complex Analysis

## Publication

M. Khalili, **K. T. McConkey**, K. Ta, L. C. Wu, H. F. M. Van der Loos and J. F. Borisoff, "Development of A Learning-Based Terrain Classification Framework for Pushrim-Activated Power-Assisted Wheelchairs," *2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)*, Montreal, QC, Canada, 2020, pp. 4762–4765, doi: 10.1109/EMBC44109.2020.9175678.

## Full Skills Inventory

**Languages:** Python, C++, Rust, C#, JavaScript/TypeScript, SQL, MATLAB, Java, Assembly, LaTeX, Shell/Bash
**Robotics & Simulation:** ROS, SLAM, physics simulation (Isaac Sim/Omniverse), sensor fusion, Sim-to-Real, PR2
**ML/Data:** PyTorch, scikit-learn, NumPy, pandas, matplotlib, computer vision, YOLO, CNNs, IMU signal processing
**Backend/Web:** Microservices, REST APIs, gRPC, Flask, Django, React, Vue.js, Three.js
**Cloud/DevOps:** Docker, Kubernetes, Terraform, CI/CD (GitHub Actions, Bitbucket/Jira/Confluence), Azure, GCP, DigitalOcean
**Databases:** PostgreSQL, MS SQL Server, MySQL, MongoDB, Redis, BigQuery, NoSQL
**Firmware/Embedded:** C++, ESP32 (Bluetooth/WiFi), Arduino, RTOS, VHDL, FPGA, LTSpice, EAGLE
**Hardware/Mechanical:** SolidWorks, AutoCAD, OnShape, 3D printing, laser cutting, oscilloscopes, soldering, CAD
**Tools:** Git, Postman, SCADA/HMI, Linux/macOS, Agile/Scrum, Jira, Unity

## Work Experience (Chronological, Most Recent First)

| Role | Company | Dates | Location |
|------|---------|-------|----------|
| Operations Engineer | Brock Solutions | 2025–Present | San Francisco, CA |
| Software Engineer | Brock Solutions | 2023–2025 | Vancouver, BC |
| Software Co-op ("Simulation Co-op") | Sanctuary AI | Jan–May 2022 | Vancouver, BC |
| Teaching Assistant | UBC Physics & Astronomy | Jan 2020–Apr 2021 | Vancouver, BC |
| Embedded Systems Co-op | Voltsafe Inc. | Sep–Dec 2020 | Vancouver, BC |
| Mechatronics Co-op | CARIS Lab, UBC Mechanical Engineering | May–Aug 2019 | Vancouver, BC |
| Engineering Intern | Max Planck Institute (MPSD) | May–Dec 2018 | Hamburg, Germany |

### Role Details

**Operations Engineer — Brock Solutions (2025–Present, San Francisco CA)**
- Forward-deployed at SFO airport; manages Azure deployments of real-time baggage sortation software
- Integrates Brock software with industrial PLCs, scanners, scales, cameras, motors from multiple OEMs; validates with SCADA/HMI
- Python data analysis, testing, and monitoring scripts; actionable insights for airport operations management
- Technical interface between software, hardware vendors, manufacturing/installation teams, and airport operations
- Led a team of 3 during a 1-month system upgrade at YYC Airport (hardware debugging and validation)
- 24/7 operational environment with strict uptime and safety requirements

**Software Engineer — Brock Solutions (2023–2025, Vancouver BC)**
- Full-stack development (C#, React, MS SQL Server) for net-new client-facing customs clearance software suite
- Docker-based distributed microservices architecture in Azure; Terraform IaC
- CI/CD pipeline with GitHub Actions (compilation, unit testing, code analysis, release)
- Led YYC Airport system upgrade: integrated new .NET software with existing baggage-handling control systems
- Mentored junior devs through pair programming and code reviews; TDD; Agile/Scrum
- Contributed to and modernized 20+ year old legacy C# codebase

**Software/Simulation Co-op — Sanctuary AI (Jan–May 2022, Vancouver BC)**
- Developed components of ROS-based humanoid robot tech stack in Python and C++
- Focus on multi-threaded physics simulation engine and asset generation stack (Isaac Sim / Omniverse)
- Created automated scripts and quantitative metrics for sensor visualization, object tracking, dexterous manipulation
- Collaborated with ML researchers, robotics, and controls teams on Sim-to-Real transfer

**Teaching Assistant — UBC Physics & Astronomy (Jan 2020–Apr 2021, Vancouver BC)**
- Supervised physics labs, marked lab work, gave constructive feedback to engineering students
- Facilitated transition to remote learning (Zoom, Microsoft Teams)
- 92% positive ratings in TA evaluations

**Embedded Systems Co-op — Voltsafe Inc. (Sep–Dec 2020, Vancouver BC)**
- Embedded C++ firmware for ESP32-based Bluetooth/WiFi-enabled engine block heater IoT commercial product
- Built Flask server + MySQL/SQL database + Python-based authentication/login backend (hosted on DigitalOcean)
- API development and unit testing in Postman
- Agile/Scrum; Bitbucket, Jira, Confluence for CI/CD and documentation

**Mechatronics Co-op — CARIS Lab, UBC Mech Eng (May–Aug 2019, Vancouver BC)**
- Python ML framework for real-time terrain classification for power-assist wheelchair users → IEEE publication
- Debugged hardware and Linux software on PR2 (ROS-based research robot)
- Developed Android app (CARIS-WHEELCHAIR) for collecting wheelchair IMU acceleration data for ML training

**Engineering Intern — Max Planck Institute MPSD (May–Dec 2018, Hamburg Germany)**
- Electron-gun imaging experimental work at Institute for Structure and Dynamics of Matter
- Designed CAD components for experimental systems; prototyped and tested circuits for ultra-fast applications
- Created Python-based web interface / UI (Servo-Serial-Interface) to control custom experimental equipment via microcontrollers

## Projects

**BarPath App** (https://barpath.app) — published iOS & watchOS app
- Python ML pipeline (BarPathModel) for exercise classification + rep counting using IMU/accelerometer data
- Signal preprocessing, feature extraction, supervised model training
- MongoDB cloud backend for labeled data collection, model evaluation, and tuning

**TrashBot** (https://github.com/glynfinck/trashbot) — collaborative, sponsored by MistyWest
- Autonomous mobile robot on NVIDIA Jetson TX2; GPU-accelerated CNNs in PyTorch for real-time object detection/classification/localization
- ROS navigation stack with SLAM (depth-sensing camera) for localization, mapping, and goal-directed path planning

**CLIDAW** — Command-line Digital Audio Workstation (Rust)
- Unix philosophy: text-based composition, git version control
- Real-time audio engine; ADSR synthesis; multi-track playback; DSP

**Wheelchair Terrain Classification** (https://github.com/KeenanMcConkey/Wheelchair-Terrain-Classification)
- ML terrain classification for power-assist wheelchairs; Python, Jupyter, multi-point IMU sensors
- Published at IEEE EMBC 2020

**CALVIN Robot** — Eng Phys Autonomous Robot Competition
- 2-month competition; built autonomous Arduino robot from scratch via CAD, 3D printing, laser cutting
- PID-based path detection and navigation; custom motor-control circuits

**Explosion Simulator** — Full-stack physics simulation
- Lagrangian mechanics and computational fluid dynamics; web-based

**Wheelchair Data Acquisition App** (https://github.com/AustinKhorram/CARIS-WHEELCHAIR)
- Android app for collecting IMU acceleration data from wheelchair users for ML training (CARIS Lab)

## Job Applications Tracker

| Company | Role | Status | Resume File | Apply URL | Notes |
|---------|------|--------|-------------|-----------|-------|
| Nuro | Software Engineer (Routing) | Applied | `Resume_Nuro_Routing.md` | https://app.welcometothejungle.com/jobs/pNRzFnHl | AV, C++, routing |
| Plaid | Software Engineer | Applied | `Resume_Plaid_SWE.md` | https://jobs.lever.co/plaid/f456f4fa-a9f7-4673-892a-8943e3cfa3fe | Fintech backend |
| Orb | Fullstack SWE, Pricing Lifecycle | Applied | `Resume_Orb_FullStack.md` | https://jobs.ashbyhq.com/orb/20199cf9-8f79-4e26-bc9d-dd98b3008d59 | $170-220K, Python/TS/React/Kafka |
| Hive AI | Software Engineer, Backend | Applied | `Resume_HiveAI_SWE.md` | https://jobs.lever.co/hive/9461e715-9e58-4414-bc9b-13e449f92b08 | $120-180K, AI/ML APIs |
| Anara | Software Engineer, Backend | Resume ready | `Resume_Anara_Backend.md` | https://jobs.ashbyhq.com/anara/b8991553-d4c6-4c8c-8431-3aeb2ed4bfb2 | $150-200K+equity, YC, AI research |

### Tier 2 — Identified, Not Yet Applied
| Company | Role | URL | Notes |
|---------|------|-----|-------|
| Zoox | SWE, Ride & Fleet Services | https://jobs.lever.co/zoox | AV dispatch, Python/C++/Kafka, Foster City |
| Waymo | SWE Backend, Simulation | https://careers.withwaymo.com | $204-259K, C++, Mountain View, 5+ yrs preferred |

## Tailored Resumes Index

| File | Role | Company |
|------|------|---------|
| `Resume_Apple_CICD.md` | CI/CD Engineer | Apple |
| `Resume_Apple_FullStack.md` | Full Stack Engineer | Apple |
| `Resume_Medra_Robotics.md` | Robotics Engineer | Medra |
| `Resume_Nuro_Routing.md` | Software Engineer (Routing) | Nuro |
| `Resume_Plaid_SWE.md` | Software Engineer | Plaid |
| `Resume_Orb_FullStack.md` | Fullstack SWE | Orb |
| `Resume_HiveAI_SWE.md` | Software Engineer, Backend | Hive AI |
| `Resume_Anara_Backend.md` | Software Engineer, Backend | Anara |

## Repo Workflow

- **Custom resumes:** `custom_resumes/*.md` — tailored per job
- **PDF generation:** `python3 resume_tools/create_pdf.py <input.md> <output.pdf>` (run from repo root)
- **Styling:** `resume_tools/styles.py` — controls global font sizes, margins, spacing
- **Archive:** `resume_archive/` — historical resumes 2018–2026 for reference
- **Font override for overflow:** temporarily edit `FONT_SIZE_BODY` + `LEADING_BODY/BULLET` in styles.py, generate PDF, then restore. Default: 9.5pt / 11pt leading. For 3-4 lines over: use 9.0pt / 10.5pt.

## Job Search Process

1. **Search** — use WebSearch targeting: site:jobs.lever.co, site:jobs.ashbyhq.com, site:greenhouse.io; filter by SF, 2-4 years exp, Python/C++/backend; target AV, robotics, fintech, AI/ML companies
2. **Fetch JDs** — use WebFetch on direct job URLs to extract full description, stack, salary, requirements
3. **Curate** — present tiered shortlist (Tier 1 = strong match, Tier 2 = stretch/different location)
4. **Build resume** — create `custom_resumes/Resume_<Company>_<Role>.md`, generate PDF, open for review
5. **Fit check** — target full one page; if under ~90% full, add detail; if over, trim bullets or reduce font
6. **Track** — add to Job Applications Tracker above with status (Resume ready → Applied → Interview)
7. **Update status** — when user applies, update tracker status from "Resume ready" to "Applied"

## Resume Tailoring Guidelines

1. **Fill the full page** — resumes using ~80% of space need more detail added
2. **Always preserve chronological order (most recent first)** — never reorder roles for relevance
3. Use this file + `Resume.html` as source of truth; never fabricate content
4. Lead with most relevant role/skill for the target job; put skills section last
5. Teaching Assistant role → include for research/academic/education-adjacent roles
6. Publication → include for research, ML, medical device, or academic roles
7. Langara College → typically omitted (space); include for academic roles
8. **TrashBot** → routing/navigation/SLAM/graph for AV or robotics roles
9. **Sanctuary AI** → C++, ROS, physics sim, multi-threaded systems, Sim-to-Real, Isaac Sim/Omniverse
10. **Brock Solutions** → microservices, backend, cloud, CI/CD, real-time ops, cross-functional
11. **CLIDAW** → Rust, systems, real-time audio/DSP roles
12. **CALVIN / Explosion Simulator** → academic, physics simulation, embedded/hardware roles
13. **Voltsafe** → embedded C++, IoT, firmware; Flask+MySQL+DigitalOcean backend available
14. **Max Planck** → research, physics, instrumentation; web UI (Servo-Serial-Interface) detail available
