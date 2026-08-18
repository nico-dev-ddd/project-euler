"""Build the GitHub Pages landing page and coverage badge from the pytest-cov report."""

import json
from pathlib import Path

SITE_DIR = Path("site")


def couverture_en_pourcentage() -> int:
    totals = json.loads((SITE_DIR / "coverage.json").read_text())["totals"]
    return round(totals["percent_covered"])


def couleur_badge(pourcentage: int) -> str:
    if pourcentage >= 90:
        return "brightgreen"
    if pourcentage >= 75:
        return "green"
    if pourcentage >= 50:
        return "yellow"
    return "red"


def ecrire_badge(pourcentage: int) -> None:
    badge = {
        "schemaVersion": 1,
        "label": "coverage",
        "message": f"{pourcentage}%",
        "color": couleur_badge(pourcentage),
    }
    (SITE_DIR / "badge.json").write_text(json.dumps(badge))


def ecrire_page_accueil(pourcentage: int) -> None:
    (SITE_DIR / "index.html").write_text(f"""<!doctype html>
<html lang="fr">
<head><meta charset="utf-8"><title>project-euler — rapports</title></head>
<body>
  <h1>project-euler</h1>
  <p>Couverture de tests : <strong>{pourcentage}%</strong></p>
  <ul>
    <li><a href="report.html">Rapport de tests</a></li>
    <li><a href="coverage/index.html">Rapport de couverture</a></li>
  </ul>
</body>
</html>
""")


if __name__ == "__main__":
    pourcentage = couverture_en_pourcentage()
    ecrire_badge(pourcentage)
    ecrire_page_accueil(pourcentage)
