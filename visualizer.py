from rdflib import Graph
from pyvis.network import Network

TTL_FILE = "labour_market.ttl"
OUTPUT = "kg_visualisation.html"

g = Graph()
g.parse(TTL_FILE, format="ttl")

query = """
PREFIX : <http://example.org/ams#>

SELECT ?obs ?date ?region ?gender ?age ?nationality ?commitment ?health ?bestand ?zugang ?abgang
WHERE {
  ?obs a :Observation ;
       :date ?date ;
       :region ?r ;
       :gender ?g ;
       :ageGroup ?a ;
       :nationality ?n ;
       :employmentCommitment ?c ;
       :healthConstraint ?h ;
       :bestand ?bestand ;
       :zugang ?zugang ;
       :abgang ?abgang .

  ?r :rgsName ?region .
  ?g :label ?gender .
  ?a :label ?age .
  ?n :label ?nationality .
  ?c :label ?commitment .
  ?h :label ?health .

  FILTER(CONTAINS(?region, "Wien"))
}
LIMIT 20
"""

net = Network(
    height="800px",
    width="100%",
    directed=True,
    notebook=False
)

net.force_atlas_2based()

for row in g.query(query):
    obs, date, region, gender, age, nationality, commitment, health, bestand, zugang, abgang = row

    obs_id = str(obs).split("#")[-1]

    obs_label = f"{obs_id}\\nBESTAND: {bestand}\\nZUGANG: {zugang}\\nABGANG: {abgang}"

    net.add_node(obs_id, label=obs_label, shape="box", title="Observation")

    dimensions = {
        f"Date: {date}": "date",
        f"Region: {region}": "region",
        f"Gender: {gender}": "gender",
        f"Age: {age}": "age group",
        f"Nationality: {nationality}": "nationality",
        f"Commitment: {commitment}": "employment commitment",
        f"Health: {health}": "health constraint",
    }

    for node_label, edge_label in dimensions.items():
        net.add_node(node_label, label=node_label)
        net.add_edge(obs_id, node_label, label=edge_label)

net.write_html(OUTPUT, notebook=False, open_browser=False)

print(f"Created {OUTPUT}")