from rdflib import Graph

g = Graph()
g.parse("labour_market.ttl", format="ttl")

print("Triples:", len(g))

q = """
PREFIX : <https://w3id.org/ams-labour-market#>

SELECT ?region ?bestand
WHERE {
    ?obs a :Observation ;
         :region ?r ;
         :bestand ?bestand .

    ?r :rgsName ?region .
}
LIMIT 10
"""

for row in g.query(q):
    print(row)