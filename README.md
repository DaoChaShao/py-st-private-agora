<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---
PrivAgora is a decentralised personal data marketplace that empowers individuals to share, sell, or purchase synthetic
personal data safely. Users can generate data in categories like social media, short video, mobile payment, health &
fitness, and maps & navigation. Buyers can then compose anonymised datasets based on specific queries — all without
compromising privacy or relying on external servers. Processing happens entirely locally.

**PRIVACY NOTICE**
---
This application may require inputting personal information or private data to generate customised suggestions,
recommendations, and necessary results. However, please rest assured that the application does **NOT** collect, store,
or transmit your personal information. All processing occurs locally in the browser or runtime environment, and **NO**
data is sent to any external server or third-party service. The entire codebase is open and transparent — you are
welcome to review the code [here](./) at any time to verify how your data is handled.

**RELATED RESEARCH & DESIGN INSPIRATION**
---
PrivAgora’s architecture is deeply inspired by recent advances in **Private Data Query Systems (PDQS)** and the
development of data marketplaces under **differential privacy** constraints. In particular, the design draws directly
from the paper [_“Integrated Private Data Trading Systems for Data
Marketplaces”_](https://ebooks.iospress.nl/doi/10.3233/FAIA230420) (You can get the PDF by
clicking [here](https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA230420))by **Weidong Li et al.**, which outlines a
theoretical framework for balancing **privacy**, **accuracy**, and **incentives** in data trading scenarios.
This work has been instrumental in shaping PrivAgora’s **pricing mechanism**, **incentive design**, and
**privacy-preserving workflow**.

Moreover, **Ms. Weidong Li** is the scientific and technical advisor for the PrivAgora sandbox application. Her
expertise
has guided the implementation of key components in the demo, ensuring **conceptual fidelity** to the original PDQS
vision while adapting it to a more **applied and interactive context**.

Ms. Weidong Li’s PDQS framework addresses the core challenge of **balancing data usability and privacy protection** in
private marketplaces. Traditional systems often decouple **procurement** (which data to buy) from **query** (what
insights to generate), leading to **excessive noise addition** and reduced accuracy. By contrast, her **integrated
approach** simultaneously determines:

- the **data owners** to purchase from,
- the level of **privacy budget** allocated, and
- the **query mechanism**,

resulting in more accurate outcomes under the same budget.

PrivAgora follows the same **high-level architecture** — involving **dataset valuation**,
**budget-aware data selection**, and **structured query output** — but diverges in two critical ways:

1. **Synthetic Data Focus**:  
   Due to the lack of readily available real-world datasets, PrivAgora operates on **simulated data**. This approach
   enables the development and testing of **pricing and utility models** under controlled conditions, while maintaining
   the overall workflow and structure of real private data query systems.

2. **Design Prototype for Transparent Budget Allocation**:  
   While Ms. Weidong Li’s work focuses on **neural and greedy optimisation strategies** to maximise utility under
   privacy constraints, PrivAgora emphasises **user-facing budget flows** and **incentive transparency**, echoing ideas
   from **ECAI 2023** on **simultaneous selection and noise calibration** to ensure **incentive compatibility** and
   **feasibility**.

By grounding its structure in **trusted research** while **relaxing privacy constraints**, PrivAgora serves as a
**sandbox prototype** — simulating the **economics and workflows** of PDQS systems, and paving the way for future
deployments that may integrate **real private data** under rigorous privacy guarantees.

**FEATURES**
---

- Data Categories (as interactive sections):
    - Social Media: likes, comments, shares, watch durations, etc.
    - Short Video: video types, interaction history.
    - Mobile Payment: devices, methods, transaction volume/frequency.
    - Health & Fitness: workouts, steps, calories, heart rates.
    - Maps & Navigation: travel habits, distances, commutes.
- Key Capabilities
    - 🧪 Generate synthetic data for each category configurable by quantity and duration.
    - 💾 Insert and manage synthetic data in SQLite.
    - 📂 Flatten nested JSON content for detailed viewing.
    - 💸 Simulate data trading: set budget → use knapsack solver → select optimal data subset by price.
    - 📊 Visualise selected records with interactive data‑editor tables.
    - 📈 Analyse traded data via LLM-based Markdown reports.

**HOW TO USE**
---

1. Data Generation & Viewing

- Navigate to "Database Creation & Management" page → "Create Database".
- Then, navigate to "Data Generate, Display & Insert" page → choose category → “Generate & Display Data” → view
  flattened content → "Insert Data" to the database.

2. Database Management

- You can delete the database on the Database Creation & Management page.
- You can view all data on the Database Creation & Management page.
- You can view the category data on the Data Generate, Display & Insert page.

3. Data Trading Simulator

- Navigate to the "Data Trade" page.
- Select a category with existing data in SQLite to view the data description.
- Set your budget and Trade.
- Visual metrics and selection tables are rendered to show spending, item count, and selected flattened data.

4. Analysis via LLM

- After trading, select a category and choose Analyse Data.
- Provide your OpenAI or DeepSeek API key.
- Specify language (e.g. English, Chinese).
- The LLM returns structured Markdown analysis: patterns, trends, user profiles, etc.

**QUICK START**
---

1. Clone the repository to your local machine.
2. Install the required dependencies with the command `pip install -r requirements.txt`.
3. Run the application with the command `streamlit run main.py`.
4. You can also try the application by visiting the following
   link: [![Static Badge](https://img.shields.io/badge/Open%20in%20Streamlit-Daochashao-red?style=for-the-badge&logo=streamlit&labelColor=white)](https://smartcs.streamlit.app/)

**LICENCE**
---
This application is licensed under the [BSD-3-Clause License](LICENSE). You can click the link to read the licence.

**CREATING THE CHANGELOG**
---
This guide outlines the steps to automatically generate and maintain a project changelog using git-changelog.

1. Install the required dependencies with the command `pip install git-changelog`.
2. Run the command `pip show git-changelog` or `pip show git-changelog | grep Version` to check whether the changelog
   package has been installed and its version.
3. Prepare the configuration file of `pyproject.toml` at the root of the file.
4. The changelog style is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
5. Run the command `git-changelog`, creating the `Changelog.md` file.
6. Add the file `Changelog.md` to version control with the command `git add Changelog.md` or using the UI interface.
7. Run the command `git-changelog --output CHANGELOG.md` committing the changes and updating the changelog.
8. Push the changes to the remote repository with the command `git push origin main` or using the UI interface.

**USING STREAMLIT & STREAMLIT CLOUD**
---

1. Install NiceGUI with the command `pip install streamlit`.
2. Run the command `pip show streamlit` or `pip show streamlit | grep Version` to check whether the package has been
   installed and its version.