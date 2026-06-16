# Report: Analysis and Semantic Integration of Austrian Labour Market Data

Github Repository[https://github.com/SirMrGore/AMS-Data-Knowledge-Graph], containing README with database links.
data.gv[https://www.data.gv.at/katalog/datasets/cfe2ff7e9ad53c1ee053c630070ab111], containing original dataset.

## 1. Project Aim

This project transforms Austrian labour market statistics from a CSV table into an RDF Knowledge Graph.

The goal is not to build a machine learning system, but to show how highly structured labour market data can be represented semantically and queried across multiple dimensions.

The Knowledge Graph supports questions such as:

* Which AMS regions report the highest unemployment stock?
* How does unemployment differ by gender and nationality?
* How do values change over time?
* How are observations connected to regional and demographic dimensions?

Repository setup, file descriptions, and execution instructions are documented separately in `README.md`.

---

## 2. Dataset Context

The source dataset contains aggregated Austrian labour market statistics. Each row represents a statistical observation for a specific reporting date, AMS region, and demographic grouping.

A simplified row has the following structure:

```text
Date | AMS Region | Gender | Age Group | Nationality | Employment Commitment | Health Constraint | BESTAND | ZUGANG | ABGANG
```

The important point is that the dataset does **not** contain individual people. It contains aggregated statistical counts.

The measures used in this project are:

| Measure   | Meaning                               |
| --------- | ------------------------------------- |
| `BESTAND` | stock/count at a given reporting date |
| `ZUGANG`  | entries/inflows                       |
| `ABGANG`  | exits/outflows                        |

This distinction matters because `BESTAND` is a point-in-time value. Summing `BESTAND` over several months does not produce the number of unique unemployed people. It produces a cumulative sum of repeated monthly stock observations.

---

## 3. Knowledge Graph Modelling

The graph uses an observation-centred model.

Each CSV row is transformed into one `Observation` node. This observation is linked to semantic dimension nodes.

```text
Observation
 ├── date
 ├── region
 ├── gender
 ├── ageGroup
 ├── nationality
 ├── employmentCommitment
 ├── healthConstraint
 ├── bestand
 ├── zugang
 └── abgang
```

This design separates the measured event from the descriptive dimensions.

For example, instead of repeatedly storing the text value `Frauen` in many CSV rows, the Knowledge Graph creates a reusable gender entity. All relevant observations then point to the same entity.

This makes repeated values explicit graph nodes instead of isolated strings.

Example RDF structure:

```ttl
:obs_1 a :Observation ;
    :date "2019-01-31"^^xsd:date ;
    :region :Region_101 ;
    :gender :Gender_Frauen ;
    :ageGroup :AgeGroup_Erwachsene_25_bis_unter_50_Jahre ;
    :nationality :Nationality_Auslaender_innen ;
    :employmentCommitment :Commitment_A_Arbeitsaufnahme ;
    :healthConstraint :Health_ohne_gesundh_Vermeinschraenkung ;
    :bestand "15"^^xsd:integer ;
    :zugang "7"^^xsd:integer ;
    :abgang "4"^^xsd:integer .

:Region_101 a :AMSRegion ;
    :rgsCode "101" ;
    :rgsName "Eisenstadt" .
```

The generated graph contains:

```text
4,584,323 RDF triples
```

---

## 4. Graph Visualisation

The file `kg_visualisation.html` contains an interactive visualisation of a selected subgraph.

The visualisation is intentionally limited to a small sample, because the complete graph contains more than four million triples and would not be readable as a full network.

The visualisation shows the core modelling idea:

```text
Observation → Region
Observation → Gender
Observation → Age Group
Observation → Nationality
Observation → Date
```

The rectangular observation nodes represent former CSV rows. The surrounding nodes represent shared semantic dimensions.

This demonstrates the transformation from a flat table into a connected graph structure.

---

## 5. SPARQL Analysis

The full query outputs are stored in `query_results.md`.

This section summarises the purpose of the main queries used for analysis.

### 5.1 Structure Sample

The first query checks whether the RDF transformation worked correctly.

It returns observations together with their linked region, gender, nationality, and `BESTAND`.

---

### 5.2 Regional Comparison

The second query identifies the AMS regions with the highest unemployment stock for a fixed reporting date.

A fixed date is used because `BESTAND` is a stock value. Without a date filter, the query would sum repeated monthly snapshots and produce misleading totals.

Purpose:

> Compare regions by unemployment stock at one point in time.

This demonstrates how the graph can support regional labour market analysis.

---

### 5.3 Gender and Nationality Analysis

The third query groups observations by gender and nationality for a fixed reporting date.

Purpose:

> Analyse how unemployment stock differs across demographic groups.

This query demonstrates multi-dimensional analysis. It follows graph links from observations to gender and nationality entities, then aggregates the measure.

This is one of the main benefits of the Knowledge Graph structure: different dimensions can be combined flexibly without changing the underlying data model.

---

### 5.4 Time Trend

The fourth query aggregates `BESTAND` by reporting date.

Purpose:

> Analyse how unemployment stock changes over time.

This query uses time as an explicit graph dimension. It can be used to produce a time series for the full dataset or, with additional filters, for specific regions or demographic groups.

---

## 6. Interpretation

The results show that the Knowledge Graph can answer analytical questions across several dimensions:

* regional dimension: AMS office / region
* demographic dimension: gender, age group, nationality
* temporal dimension: reporting date
* measurement dimension: `BESTAND`, `ZUGANG`, `ABGANG`

The main analytical value is not that SPARQL replaces CSV processing completely. The value is that the relationships between dimensions become explicit and reusable.

For example, a CSV row only stores `Wien Favoritenstraße` as a text value. In the graph, this becomes a region entity that can be linked from many observations and potentially enriched later with external regional information.

---

## 7. Limitations

The project has several limitations.

First, the graph is based on aggregated data. It does not represent individuals, only statistical groups.

Second, the interpretation of `BESTAND` requires care. Since it is a stock value at a reporting date, summing it across time does not produce unique person counts.

Third, The current graph uses a custom vocabulary under https://w3id.org/ams-labour-market#; a future version could align the model with RDF Data Cube, SKOS, PROV-O and relevant Austrian administrative vocabularies.

Fourth, the visualisation only shows a sample subgraph. The complete graph is too large to visualise directly in a readable way.

Fifth, the project does not implement embeddings, link prediction, graph neural networks, or reasoning. The focus is Knowledge Graph creation and semantic querying.

---

## 8. Learning Outcomes

### Main Learning Outcomes

#### LO7: Creating a Knowledge Graph

I have created a Knowledge Graph from a real Austrian labour market dataset. Each CSV row is transformed into an RDF observation, and each observation is linked to reusable semantic dimensions.

Evidence:

* CSV to RDF transformation
* RDF/Turtle output
* 4,584,323 generated triples
* RDFLib validation
* SPARQL queries over the graph

#### LO9: Real-world Knowledge Graph Applications

The Knowledge Graph is applied to real labour market data and supports practical analysis questions about regions, demographic groups, and time trends.

Evidence:

* regional comparison query
* gender and nationality query
* time trend query
* interactive subgraph visualization

The gained information can easily be used by the relevant authorities to find hotspots or timescale trends.

---

### Basic Learning Outcomes

#### LO1: Knowledge Graph Embeddings

The project does not implement embeddings. However, the generated RDF graph could later be used as input for embedding-based methods such as TransE or similar models.

This learning outcome is only addressed at a basic conceptual level.

#### LO2: Logical Knowledge

The project uses RDF triples and typed entities. It does not implement advanced logical reasoning, but it does represent knowledge in subject-predicate-object form.

Example:

```ttl
:obs_1 a :Observation .
:obs_1 :region :Region_101 .
:Region_101 a :AMSRegion .
```

#### LO3: Graph Neural Networks

Graph Neural Networks are not implemented in this project. However, the project helped me understand where GNNs would fit in relation to a Knowledge Graph.

In the context of this project, an observation node is connected to dimensions such as region, gender, age group, nationality and date. A GNN could use these connections to learn vector representations of observations or regions. For example, regions that are connected to similar demographic and temporal unemployment patterns might receive similar learned representations. Such representations could then be used for tasks such as regional similarity analysis, anomaly detection, or predicting future labour market trends.

This differs from the implemented SPARQL analysis. SPARQL queries retrieve and aggregate explicitly stored facts, while a GNN would try to learn patterns from the graph structure and node features. In this project, the focus remains on constructing and querying the RDF Knowledge Graph. Therefore, LO3 is addressed conceptually rather than technically, but the graph structure created here could serve as a possible input for future GNN-based analysis.

#### LO4: Knowledge Graph Data Models

The project addresses data modelling directly by converting a flat table into an observation-centred graph model.

The main modelling decision is to separate observations from reusable dimensions. Instead of keeping values such as region, gender, age group and nationality only as repeated strings in the CSV, they are represented as connected graph entities. This reflects a basic Knowledge Graph data model, where facts are represented as nodes and relations rather than isolated table columns.

This also shows the difference between a tabular data model and a graph data model. The CSV is useful for storage and aggregation, while the RDF model makes the semantic relationships between observations and their dimensions explicit.

#### LO5: Knowledge Graph Architectures

The project implements a simple Knowledge Graph pipeline:

```text
CSV dataset
   ↓
Python conversion
   ↓
RDF/Turtle Knowledge Graph
   ↓
SPARQL queries
   ↓
query results and HTML visualisation
```

This demonstrates the basic architecture of a small Knowledge Graph application.

#### LO11: Knowledge Graph Services

The project provides basic Knowledge Graph services through query scripts and visualisation.

The graph can be queried for regional comparison, demographic analysis, and temporal trends.

#### LO12: Connections between Knowledge Graphs, Machine Learning, and AI

The project does not implement machine learning, but it creates structured graph data that could be used for later AI methods.

Possible future extensions include:

* graph embeddings
* regional similarity analysis
* link prediction
* integration with additional socio-economic datasets

---

### Learning Outcomes Not Included

#### LO6: Scalable Reasoning

Scalable reasoning is not part of this project. No rule-based inference or large-scale reasoning engine is implemented.

#### LO8: Evolving a Knowledge Graph

The graph is generated from a static dataset. Incremental updates are not implemented.

#### LO10: Financial Knowledge Graph Applications

The project is about labour market data, not financial Knowledge Graphs.

---

## 9. Conclusion

This project demonstrates how Austrian labour market statistics can be transformed from a flat CSV file into a semantic RDF Knowledge Graph.

The resulting graph makes the relationships between observations, regions, demographic categories, time, and labour market measures explicit.

The main contribution is the creation of an observation-centred Knowledge Graph that supports SPARQL-based regional, demographic, and temporal analysis.

The project focuses on Knowledge Graph creation and real-world application. More advanced techniques such as embeddings, reasoning, or graph neural networks are left as possible future extensions.
