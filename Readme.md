# Red Eye
### Preparation

Social Media Analysis based profiling system is a profiling system that profiles users, persons based on their intersts, relationships, activities, and public infos on their social media accounts, in the age of data it's essential to know how to use the public and allowed data in order to enhance our industries, a company which use this concept is called Data-Driven-Company, one of operations that appears specially in marketing and hr levels is called Data-Based-Profiling which means to label a user with special attributes that represent some domain specific characteristic, where this profiling happens based on other activites or inputs about the user / person.

## Table of Content

<ul>
    <li>
        <a href="#installation" style="font-size: medium">Installation</a>
    </li>
        <li>
        <a href="#usage" style="font-size: medium">Usage</a>
    </li>
        <li>
        <a href="#tech-stack" style="font-size: medium">Tech Stack</a>
    </li>
</ul>

## Installation

## Usage
pipelines and models are accessable to use via a Command Line Interface
- Put the folder path the project exist at in the Enviroment System Variable / or use it directly from the folder
- Run the file <strong>main.py</strong> to enter the CLI
<p>These are the available commands:</p>
<div style="width:100%">
    <table>
        <tr style="font-size:16px">
            <th>Command</th>
            <th>Parameters</th>
            <th>Usage</th>
        </tr>
        <tr>
            <td class="command">Hello</td>
            <td>Hello</td>
            <td>Hello</td>
        </tr>
    </table>
</div>

<style>
    .command{
        font-weight: bold;
        font-size: 15px;
    }
    table{
        margin-top:100px;margin-bottom:100px; width:90%
    }
    th{
        text-align: center;
    }
    td{
        text-align:center;
    }
</style>


---

## 3. System Flow

1. **Data Ingestion**
   - Collect raw datasets from **Facebook**, **Last.fm**, and other social networks.
   - Store them in `data/storage/raw`.

2. **Data Preprocessing**
   - Clean and normalize user IDs, event IDs, and relationships.
   - Prepare datasets for graph ingestion in `src/preprocessing`.

3. **Graph Construction**
   - Load nodes and relationships into **Neo4j**:
     - `(User)-[:ATTENDED]->(Event)`
     - `(User)-[:FRIENDS_WITH]->(User)` (optional)
   - Additional metadata from `infoExtra` can enrich the graph.

4. **Feature Computation**
   - Node-level metrics: degree, centrality.
   - Edge-level metrics: similarity, co-attendance.
   - Tools: **NetworkX**, **GDS**.

5. **Graph Analytics & Profiling**
   - Community detection: `gds.louvain`
   - Node similarity: `gds.nodeSimilarity`
   - Embeddings: `gds.fastRP`
   - Predictive profiling: scikit-learn / TensorFlow models.

6. **Evaluation & Monitoring**
   - Validate profiling accuracy.
   - Log pipeline and model performance in `logs/logs_records`.
   - Monitor pipelines and analytics via `monitoring`.

7. **Interface**
   - CLI (`main.py`) or API (`api`) for:
     - Querying profiles
     - Running analyses
     - Generating reports

---

## 4. Tech Stack

| Component | Purpose |
|-----------|---------|
| **Neo4j** | Graph database for nodes, edges, and graph algorithms |
| **Python** (NumPy, Pandas, Matplotlib, seaborn) | Data preprocessing, analysis, visualization |
| **NetworkX** | Offline graph computations |
| **Scikit-learn & TensorFlow** | ML models for user profiling and embeddings |
| **CLI / API** | User interface for running commands and fetching results |

---

## 5. Conceptual Diagram

Raw Social Data (Facebook / Last.fm)<br>
│<br>
▼<br>
Preprocessing (src/preprocessing)<br>
│<br>
▼<br>
Graph Construction (Neo4j)<br>
│<br>
▼<br>
Feature Computation & Analytics (GDS / NetworkX)<br>
│<br>
▼<br>
Profiling & ML Models (src/models)<br>
│<br>
▼<br>
Evaluation & Monitoring (logs / monitoring)<br>
│<br>
▼<br>
CLI / API / Reports (notebooks / api)


## 6. Key Architectural Principles

- **Separation of Concerns** — independent modules for ingestion, preprocessing, modeling, and monitoring.
- **Graph-centric design** — optimized for social network analytics using Neo4j and GDS.
- **Data-driven profiling** — user labels and insights derived from activity and relationships.
- **Extensible & modular** — easy to add datasets, models, or analytics pipelines.
- **Notebook-friendly** — supports exploratory analysis and reporting in Jupyter.


<br>

## Data & Resources

    1. Online Social Networks Dataset ("https://athinagroup.eng.uci.edu/projects/online-social-networks/online-social-networks-dataset")
        - Facebook Egonet Samples
        - Last.fm Multigraph
        - Facebook Social Graph – MHRW & UNI
        - Facebook Social Graph – Breadth First Search
        - Facebook Weighted Random Walks
