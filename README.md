# Edu-Sharing with a Click

Diese FLASK-App bietet die Möglichkeit möglichst unkompliziert eine edu-sharing, Moodle oder Wordpress Instanz aufzusetzen.
Bei der edu-sharing Instanz kann wahlweise direkt eine Moodle-Instanz angeschlossen werden, die auf die Inhalte aus dem edu-sharing Repositorium zugreifen kann.

Diese App enstand während eines Hackathons des IT- und Sommercamps 2019 in Weimar das von dem Projekt JOINTLY (https://jointly.info) gehostet und durchgeführt wurde.

Die verwendeten Ansible-Skripte beruhen auf den Vorarbeiten der TIB Hannover (https://github.com/TIBHannover/edu-sharing-box, https://github.com/TIBHannover/moodle-box) und wurden lediglich leicht angepasst. Zusätzlich integriert wurde noch eine mögliche automatische Moodle-Integration mit dem aufgesetzten edu-sharing Repositorium.

## How to use

Die App kann selbst gehostet werden. Dazu am besten zunächst eine virtuelle Umgebung einrichten. Hier eine Anleitung für Unix oder MacOS Umgebungen:

- Vorraussetzungen:
  - python3 (https://docs.python-guide.org/starting/install3/osx/)
  - git (https://www.atlassian.com/git/tutorials/install-git)

- Gehe an einen beliebigen Ort Deiner Wahl, öffne das Terminal:

  ```bash
  git clone https://github.com/sroertgen/edu-sharing-with-a-click.git

  cd edu-sharing-with-a-click

  ```

- nun erstellen wir die virtuelle Umgebung:

  ```bash
  python -m venv flask-venv
  ```

- und aktivieren die Umgebung:

  ```bash
  source flask-venv/bin/activate
  ```

- dann installieren wir die notwendigen pip-Pakete mit Hilfe der requirements.txt:

  ```bash
  pip3 install -r requirements.txt
  ```

- anschließend reicht folgender Befehl aus, um die flask-app im Browser unter http://localhost:5000 aufrufbar zu machen:

  ```bash
  python3 flask_edu.py
  ```
