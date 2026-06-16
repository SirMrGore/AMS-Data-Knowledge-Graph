import csv
import re

INPUT = "Gesamtuebersicht_AL_RGS.csv"
OUTPUT = "labour_market.ttl"

BASE_URI = "https://w3id.org/ams-labour-market#"


def clean(value):
    value = value.strip()
    value = value.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    value = value.replace("Ä", "Ae").replace("Ö", "Oe").replace("Ü", "Ue")
    value = value.replace("ß", "ss")
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    return value.strip("_")


with open(INPUT, encoding="cp1252") as f, open(OUTPUT, "w", encoding="utf-8") as out:
    reader = csv.DictReader(f, delimiter=";")

    out.write(f"@prefix : <{BASE_URI}> .\n")
    out.write("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n")

    for i, row in enumerate(reader, start=1):
        obs = f":obs_{i}"
        region = f":Region_{clean(row['RGSCode'])}"
        gender = f":Gender_{clean(row['Geschlecht'])}"
        age = f":AgeGroup_{clean(row['Altersgruppe'])}"
        nat = f":Nationality_{clean(row['Nationalitaet'])}"
        commitment = f":Commitment_{clean(row['Einstellzusage'])}"
        health = f":Health_{clean(row['ges_Vermittlungsein'])}"

        out.write(f"{obs} a :Observation ;\n")
        out.write(f'  :date "{row["Datum"]}"^^xsd:date ;\n')
        out.write(f"  :region {region} ;\n")
        out.write(f"  :gender {gender} ;\n")
        out.write(f"  :ageGroup {age} ;\n")
        out.write(f"  :nationality {nat} ;\n")
        out.write(f"  :employmentCommitment {commitment} ;\n")
        out.write(f"  :healthConstraint {health} ;\n")
        out.write(f'  :bestand "{row["BESTAND"]}"^^xsd:integer ;\n')
        out.write(f'  :zugang "{row["ZUGANG"]}"^^xsd:integer ;\n')
        out.write(f'  :abgang "{row["ABGANG"]}"^^xsd:integer .\n\n')

        out.write(
            f'{region} a :AMSRegion ; '
            f':rgsCode "{row["RGSCode"]}" ; '
            f':rgsName "{row["RGSName"]}" .\n'
        )
        out.write(f'{gender} a :Gender ; :label "{row["Geschlecht"]}" .\n')
        out.write(f'{age} a :AgeGroup ; :label "{row["Altersgruppe"]}" .\n')
        out.write(f'{nat} a :Nationality ; :label "{row["Nationalitaet"]}" .\n')
        out.write(f'{commitment} a :EmploymentCommitment ; :label "{row["Einstellzusage"]}" .\n')
        out.write(f'{health} a :HealthConstraint ; :label "{row["ges_Vermittlungsein"]}" .\n\n')

print(f"Done. Created {OUTPUT}")