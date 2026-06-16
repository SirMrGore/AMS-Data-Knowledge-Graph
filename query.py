from rdflib import Graph, URIRef
import csv

TTL_FILE = "labour_market.ttl"
BASE_URI = "https://w3id.org/ams-labour-market#"

g = Graph()
g.parse(TTL_FILE, format="ttl")


def shorten(value):
    if isinstance(value, URIRef) and str(value).startswith(BASE_URI):
        return str(value).replace(BASE_URI, "")
    return str(value)


queries = {
    "1_structure_sample": f"""
PREFIX : <{BASE_URI}>

SELECT ?obs ?region ?gender ?nationality ?bestand
WHERE {{
  ?obs a :Observation ;
       :region ?r ;
       :gender ?g ;
       :nationality ?n ;
       :bestand ?bestand .

  ?r :rgsName ?region .
  ?g :label ?gender .
  ?n :label ?nationality .
}}
LIMIT 10
""",

    "2_top_regions_2019_01_31": f"""
PREFIX : <{BASE_URI}>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?region (SUM(?bestand) AS ?total)
WHERE {{
  ?obs a :Observation ;
       :date "2019-01-31"^^xsd:date ;
       :region ?r ;
       :bestand ?bestand .

  ?r :rgsName ?region .
}}
GROUP BY ?region
ORDER BY DESC(?total)
LIMIT 10
""",

    "3_gender_nationality_2019_01_31": f"""
PREFIX : <{BASE_URI}>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?gender ?nationality (SUM(?bestand) AS ?total)
WHERE {{
  ?obs a :Observation ;
       :date "2019-01-31"^^xsd:date ;
       :gender ?g ;
       :nationality ?n ;
       :bestand ?bestand .

  ?g :label ?gender .
  ?n :label ?nationality .
}}
GROUP BY ?gender ?nationality
ORDER BY DESC(?total)
""",

    "4_time_trend": f"""
PREFIX : <{BASE_URI}>

SELECT ?date (SUM(?bestand) AS ?total)
WHERE {{
  ?obs a :Observation ;
       :date ?date ;
       :bestand ?bestand .
}}
GROUP BY ?date
ORDER BY ?date
"""
}

with open("query_results.md", "w", encoding="utf-8") as md, \
     open("query_results.csv", "w", encoding="utf-8", newline="") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(["query_name", "columns", "values"])

    md.write("# SPARQL Query Results\n\n")
    md.write(f"Triple count: **{len(g):,}**\n\n")
    md.write(f"Namespace: `{BASE_URI}`\n\n")

    for name, query in queries.items():
        result = g.query(query)
        columns = [str(v) for v in result.vars]  # type: ignore

        md.write(f"## {name}\n\n")
        md.write("```sparql\n")
        md.write(query.strip())
        md.write("\n```\n\n")

        md.write("| " + " | ".join(columns) + " |\n")
        md.write("| " + " | ".join(["---"] * len(columns)) + " |\n")

        for row in result:
            values = [shorten(value) for value in row]  # type: ignore
            md.write("| " + " | ".join(values) + " |\n")
            writer.writerow([name, ", ".join(columns), " | ".join(values)])

        md.write("\n")
        