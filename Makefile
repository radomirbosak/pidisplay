.PHONY: run deploy

deploy:
	ansible-playbook playbooks/deploy.yaml -i hosts.ini

run:
	ansible-playbook playbooks/run.yaml -i hosts.ini
