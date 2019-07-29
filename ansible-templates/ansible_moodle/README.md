# Setup of Moodle with Ansible
followed the official moodle-docs on: https://docs.moodle.org/37/en/Step-by-step_Installation_Guide_for_Ubuntu#Step_3:_Install_Additional_Software


This Playbook will setup a complete wordpress server. It will use a letsencrypt certificate for secure connection and automatically add a cron job to renew itself every day at a given time.

Please fill out all necessary variables in host_vars.

# Moodle Version
v3.7.1

# Attention
currently certbot is set to --dry-run
