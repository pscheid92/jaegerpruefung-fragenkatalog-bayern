# Bayerischer Jagdfragen-Katalog – JSON Edition

Eine **freie, maschinenlesbare** Umsetzung des amtlichen Fragenkatalogs für die **Bayerische Jägerprüfung** (Stand: August 2024). Ideal für Apps, Analysezwecke oder eigene Skripte: Alle sechs Sachgebiete liegen in einem einheitlichen JSON-Format vor.

## Inhalte

| Datei                | Beschreibung                                         |
|----------------------|------------------------------------------------------|
| `fragenkatalog.json` | Enthält alle **1332** Prüfungsfragen samt Antworten |
| `schema.json`        | JSON-Schema zur Validierung der Datenstruktur        |

## Quelle & rechtlicher Hinweis

Die Originaldokumente mit Fragen und Lösungen sind abrufbar über die [Website des Bayerischen Landesamts für Maß und Gewicht (BLM)](https://www.lmg.bayern.de/aufgaben_leistungen/jaegerpruefung/index.html) 

Herausgeber ist das **Bayerisches Staatsministerium für Wirtschaft, Landesentwicklung und Energie**.

> Die Inhalte sind gemäß § 5 Abs. 2 UrhG **gemeinfrei**, da es sich um amtlich veröffentlichte Werke handelt.  
> Die Quelle wird korrekt angegeben, der Inhalt sinngemäß wiedergegeben.

**Hinweis:** Diese Aufbereitung erfolgte mit größter Sorgfalt, es wird jedoch   keine Gewähr für Richtigkeit, Vollständigkeit oder Aktualität übernommen.

## Datenformat – Beispiel

```jsonc
{
  "sg": 3,          // Sachgebiet (1–6)
  "no": 56,         // Laufende Nummer innerhalb des Sachgebiets
  "topic": "3.56 Rechtliche Vorschriften",
  "question": "Welche Aussagen zu Drückjagden und Riegeljagden treffen zu?",
  "answers": [
    { "text": "Hunde dürfen freilaufend eingesetzt werden", "correct": true  },
    { "text": "Rotwild darf nicht erlegt werden",           "correct": false },
    { "text": "Rehwild darf nicht erlegt werden",           "correct": false },
    { "text": "Maximal 4 Treiber",                          "correct": true  }
  ]
}
```
