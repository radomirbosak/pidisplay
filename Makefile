.PHONY: run deploy

deploy:
	ansible-playbook playbooks/deploy.yaml -i hosts.ini

deploy_script:
	ansible-playbook playbooks/deploy.yaml -i hosts.ini --tags script

run:
	ansible-playbook playbooks/run.yaml -i hosts.ini
