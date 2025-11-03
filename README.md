🍽️ CycleSync – Personalized Meal Planner for Menstrual Health
Overview

CycleSync is a full-stack wellness app that aligns nutrition and meal planning with menstrual cycle phases. The platform helps users track their cycles, generate tailored recipe recommendations, and organize grocery lists through AI-driven analysis and API integrations.

🌟 Features
✅ MVP

Menstrual Tracker: Record and visualize menstrual cycle timing.

Recipe Calendar: Schedule recommended meals according to each phase (Menstrual, Follicular, Ovulation, Luteal).

Shopping List Generator: Automatically create grocery lists based on selected recipes and cycle needs.

ChatGPT Wrapper: Generate explanations or nutritional insights via natural-language prompts.

Data Pipeline: Ingest, clean, and structure recipe and nutrition datasets (USDA FoodData Central, scraped websites).

🚀 Stretch Goals

Pantry Tracker: Identify available ingredients through image or manual input and match with recipes.

Bulk Recipe Import: Batch upload recipes to the database.

Google Calendar API Integration: Sync meal schedules with Google Calendar.

Cycle-Based Recommender System: Machine learning model to classify recipes by cycle phase.

🧠 Tech Stack
Layer	Tools & Frameworks
Frontend	TypeScript, Next.js, Tailwind CSS
Backend	Python (FastAPI / Flask), Railway Database
Data	Pandas, Scikit-learn, USDA FoodData Central API
Visualization	Matplotlib / Seaborn
Deployment	Vercel (Frontend), Railway (Backend)
🧩 Architecture

Data Ingestion: Collects and cleans nutrition and recipe data from APIs and scraped sources.

Feature Engineering: Tags recipes by nutritional profile and menstrual phase relevance.

Database Layer: Stores structured recipes, user preferences, and historical cycle data.

Recommender Engine: Suggests meals based on current phase + pantry + goals.

UI/UX: Presents cycle visualization, recipe calendar, and shopping list in an intuitive interface.

🗓 Project Schedule

Week 1–2: Research menstrual nutrition and collect data

Week 3: Database schema + API integration

Week 4: Build baseline deterministic recommender

Week 5: Frontend (UI/UX + React Calendar + shopping list)

Week 6: Integration testing + presentation polish

📚 Data Sources

USDA FoodData Central API

Recipe websites (web scraping)

User input (cycle length, pantry items, number of meals)
