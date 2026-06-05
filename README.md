# Austrian Labour Market Knowledge Graph

This project creates a Knowledge Graph from Austrian labour market statistics.  
The original tabular CSV data is transformed into an RDF-based representation where each statistical record becomes an observation connected to semantic dimensions.

Instead of storing information only as rows:

```
Date | Region | Gender | Age Group | Nationality | BESTAND | ZUGANG | ABGANG
```

the Knowledge Graph represents the data as connected entities:

```
Observation
 ├── Date
 ├── AMS Region
 ├── Gender
 ├── Age Group
 ├── Nationality
 ├── Employment Commitment
 ├── Health Constraint
 └── Labour Market Measures
```

This enables semantic querying using SPARQL and easier integration with other datasets.

## Dataset

The original dataset is provided by the Austrian Open Government Data platform:

https://www.data.gv.at/katalog/datasets/cfe2ff7e9ad53c1ee053c630070ab111

The raw CSV file and generated Turtle file are not included in this repository due to file size limitations.

The generated graph contains:

```
4,584,323 RDF triples
```

The Turtle file can be regenerated using the provided conversion script.

---

## Repository Structure

```
.
├── convert_to_rdf.py
├── query.py
├── visualizer.py
├── kg_visualisation.html
├── query_results.md
├── Report.md
└── README.md
```

### File Description

#### `convert_to_rdf.py`

Transforms the original CSV dataset into an RDF/Turtle Knowledge Graph.

Responsibilities:
- reads the Windows-1252 encoded CSV
- creates Observation entities
- creates reusable dimension entities
- generates RDF triples
- outputs `labour_market.ttl`

---

#### `checker.py`

Utility script for validating the generated Knowledge Graph.

Features:
- loads the Turtle file using RDFLib
- checks that parsing works
- prints the number of generated triples
- allows quick SPARQL tests

---

#### `run_report_queries.py`

Executes the SPARQL queries used for analysis.

Example analyses:
- regional unemployment comparison
- demographic analysis by gender and nationality
- time-based labour market trends
- graph structure inspection

Outputs:

```
query_results.md
query_results.csv (omitted in repository)
```

---

#### `visualizer.py`

Creates an interactive Knowledge Graph visualisation.

The visualisation shows how observations are connected to semantic dimensions such as:

- AMS locations
- demographic groups
- time
- labour market attributes

---

#### `kg_visualisation.html`

Interactive HTML visualisation of a selected Knowledge Graph subgraph.

Can be opened directly in a browser.

---

#### `Report.md`

Contains the project report and explanation of how the implementation addresses the Knowledge Graph learning outcomes.
---

## Setup

Install dependencies:

```bash
pip install rdflib pyvis
```

Generate the Knowledge Graph:

```bash
python convert_to_rdf.py
```

Validate:

```bash
python checker.py
```

Run analysis queries:

```bash
python query.py
```

Generate visualisation:

```bash
python visualizer.py
```

---

## Notes

This Project was created as part of the Lecture "Knowledge Graphs" at TU Wien in June 2026.

The focus of this project is semantic integration and Knowledge Graph creation rather than machine learning-based link prediction.

The graph model allows flexible analysis over multiple dimensions that were previously only available as fixed CSV columns.
