# SPARQL Query Results

Triple count: **4.584.323**

## 1_structure_sample

```sparql
PREFIX : <http://example.org/ams#>

SELECT ?obs ?region ?gender ?nationality ?bestand
WHERE {
  ?obs a :Observation ;
       :region ?r ;
       :gender ?g ;
       :nationality ?n ;
       :bestand ?bestand .

  ?r :rgsName ?region .
  ?g :label ?gender .
  ?n :label ?nationality .
}
LIMIT 10
```

| region | gender | nationality | bestand |
| --- | --- | --- | --- |
| Eisenstadt | Frauen | Ausländer_innen | 15
| Eisenstadt | Frauen | Ausländer_innen | 7 |
| Eisenstadt | Frauen | Ausländer_innen | 11
| Eisenstadt | Frauen | Ausländer_innen | 2 |
| Eisenstadt | Frauen | Inländer_innen | 2 |
| Eisenstadt | Frauen | Inländer_innen | 52 |
| Eisenstadt | Frauen | Inländer_innen | 63 |
| Eisenstadt | Frauen | Inländer_innen | 25
| Eisenstadt | Frauen | Inländer_innen | 3 |
| Eisenstadt | Frauen | Ausländer_innen | 2 |

## 2_top_regions_2019_01_31

```sparql
PREFIX : <http://example.org/ams#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?region (SUM(?bestand) AS ?total)
WHERE {
  ?obs a :Observation ;
       :date "2019-01-31"^^xsd:date ;
       :region ?r ;
       :bestand ?bestand .

  ?r :rgsName ?region .
}
GROUP BY ?region
ORDER BY DESC(?total)
LIMIT 10
```

| region | total |
| --- | --- |
| Wien Favoritenstraße | 17828 |
| Wien Dresdner Straße | 14981 |
| Wien Schönbrunner Straße | 14003 |
| Wien Huttengasse | 14002 |
| Graz-West und Umgebung | 13487 |
| Wien Schloßhofer Straße | 11491 |
| Linz neu | 10476 |
| Wien-Wagramer Straße | 10376 |
| Salzburg | 8951 |
| Wien Hauffgasse | 8421 |

## 3_gender_nationality_2019_01_31

```sparql
PREFIX : <http://example.org/ams#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?gender ?nationality (SUM(?bestand) AS ?total)
WHERE {
  ?obs a :Observation ;
       :date "2019-01-31"^^xsd:date ;
       :gender ?g ;
       :nationality ?n ;
       :bestand ?bestand .

  ?g :label ?gender .
  ?n :label ?nationality .
}
GROUP BY ?gender ?nationality
ORDER BY DESC(?total)
```

| gender | nationality | total |
| --- | --- | --- |
| Männer | Inländer_innen | 154131 |
| Frauen | Inländer_innen | 96444 |
| Männer | Ausländer_innen | 72900 |
| Frauen | Ausländer_innen | 44504 |

## 4_time_trend

```sparql
PREFIX : <http://example.org/ams#>

SELECT ?date (SUM(?bestand) AS ?total)
WHERE {
  ?obs a :Observation ;
       :date ?date ;
       :bestand ?bestand .
}
GROUP BY ?date
ORDER BY ?date
```

| date | total |
| --- | --- |
| 2019-01-31 | 367979 |
| 2019-02-28 | 343400 |
| 2019-03-31 | 304411 |
| 2019-04-30 | 296275 |
| 2019-05-31 | 278948 |
| 2019-06-30 | 264520 |
| 2019-07-31 | 271777 |
| 2019-08-31 | 279171 |
| 2019-09-30 | 272098 |
| 2019-10-31 | 288033 |
| 2019-11-30 | 299527 |
| 2019-12-31 | 349795 |
| 2020-01-31 | 355335 |
| 2020-02-29 | 333987 |
| 2020-03-31 | 504345 |
| 2020-04-30 | 522253 |
| 2020-05-31 | 473300 |
| 2020-06-30 | 414766 |
| 2020-07-31 | 383951 |
| 2020-08-31 | 371893 |
| 2020-09-30 | 346907 |
| 2020-10-31 | 358396 |
| 2020-11-30 | 390858 |
| 2020-12-31 | 459682 |
| 2021-01-31 | 468330 |
| 2021-02-28 | 436982 |
| 2021-03-31 | 381038 |
| 2021-04-30 | 355382 |
| 2021-05-31 | 316960 |
| 2021-06-30 | 288862 |
| 2021-07-31 | 282685 |
| 2021-08-31 | 286277 |
| 2021-09-30 | 269250 |
| 2021-10-31 | 269514 |
| 2021-11-30 | 289340 |
| 2021-12-31 | 336276 |
| 2022-01-31 | 332956 |
| 2022-02-28 | 302697 |
| 2022-03-31 | 261917 |
| 2022-04-30 | 254755 |
| 2022-05-31 | 237818 |
| 2022-06-30 | 228908 |
| 2022-07-31 | 235487 |
| 2022-08-31 | 249019 |
| 2022-09-30 | 237409 |
| 2022-10-31 | 249314 |
| 2022-11-30 | 257513 |
| 2022-12-31 | 309653 |
| 2023-01-31 | 317131 |
| 2023-02-28 | 294071 |
| 2023-03-31 | 259440 |
| 2023-04-30 | 258652 |
| 2023-05-31 | 248037 |
| 2023-06-30 | 239301 |
| 2023-07-31 | 250227 |
| 2023-08-31 | 261298 |
| 2023-09-30 | 251844 |
| 2023-10-31 | 264232 |
| 2023-11-30 | 275710 |
| 2023-12-31 | 329328 |
| 2024-01-31 | 343828 |
| 2024-02-29 | 321655 |
| 2024-03-31 | 291468 |
| 2024-04-30 | 287559 |
| 2024-05-31 | 272997 |
| 2024-06-30 | 264018 |
| 2024-07-31 | 274957 |
| 2024-08-31 | 287458 |
| 2024-09-30 | 279730 |
| 2024-10-31 | 293301 |
| 2024-11-30 | 304372 |
| 2024-12-31 | 352873 |
| 2025-01-31 | 365746 |
| 2025-02-28 | 347424 |
| 2025-03-31 | 316347 |
| 2025-04-30 | 311838 |
| 2025-05-31 | 296140 |
| 2025-06-30 | 288545 |
| 2025-07-31 | 289968 |
| 2025-08-31 | 301421 |
| 2025-09-30 | 299180 |
| 2025-10-31 | 310509 |
| 2025-11-30 | 320351 |
| 2025-12-31 | 363006 |
| 2026-01-31 | 379771 |
| 2026-02-28 | 357518 |

