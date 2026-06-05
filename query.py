from rdflib import Graph

g = Graph()
g.parse("labour_market.ttl", format="ttl")

queries = {
    "Top 10 regions by Bestand": """
    PREFIX : <http://example.org/ams#>

    SELECT ?region (SUM(?bestand) AS ?totalBestand)
    WHERE {
      ?obs a :Observation ;
           :region ?r ;
           :bestand ?bestand .
      ?r :rgsName ?region .
    }
    GROUP BY ?region
    ORDER BY DESC(?totalBestand)
    LIMIT 10
    """,

    "Bestand by gender": """
    PREFIX : <http://example.org/ams#>

    SELECT ?gender (SUM(?bestand) AS ?totalBestand)
    WHERE {
      ?obs a :Observation ;
           :gender ?g ;
           :bestand ?bestand .
      ?g :label ?gender .
    }
    GROUP BY ?gender
    ORDER BY DESC(?totalBestand)
    """,

    "Eisenstadt by nationality": """
    PREFIX : <http://example.org/ams#>

    SELECT ?nationality (SUM(?bestand) AS ?totalBestand)
    WHERE {
      ?obs a :Observation ;
           :region ?r ;
           :nationality ?n ;
           :bestand ?bestand .
      ?r :rgsName "Eisenstadt" .
      ?n :label ?nationality .
    }
    GROUP BY ?nationality
    ORDER BY DESC(?totalBestand)
    """
}

for title, query in queries.items():
    print("\n===", title, "===")
    for row in g.query(query):
        print(row)