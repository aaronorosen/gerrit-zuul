Gerrit-Zuul

A tool to easily orchestrate gerrit and zuul!

Install:
	sudo pip install -U -r requirements.txt

Usage:
	python gerrit-enqueue.py
	usage: Zuul/gerrit patch enqueuer [-h] [--zuul-port ZUUL_PORT]
												 [--gerrit-url GERRIT_URL]
												 [--gerrit-user GERRIT_USER]
												 [--gerrit-port GERRIT_PORT]
												 [--zuul-trigger ZUUL_TRIGGER]
												 [--zuul-pipeline ZUUL_PIPELINE]
												 project zuul_server
