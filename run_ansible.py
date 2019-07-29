import subprocess
import time


def run_ansible(choice):

    if choice == "1":
        print("Moodle")
        proc = subprocess.Popen(["ansible-playbook", "ansible-templates/ansible_moodle/moodle-playbook.yml", "-i", "ansible-templates/ansible_moodle/inventory.txt"], stdout=subprocess.PIPE, universal_newlines=True)
        print("Ansible running...creating instance...")
        for line in iter(proc.stdout.readline, ''):
            time.sleep(0.2)
            yield line.rstrip() + '<br/>\n'

    if choice == "2":
        print("Wordpress")
        proc = subprocess.Popen(["ansible-playbook", "ansible-templates/ansible_wordpress/wp-playbook.yml", "-i", "ansible-templates/ansible_wordpress/inventory.txt"], stdout=subprocess.PIPE, universal_newlines=True)
        print("Ansible running...creating instance...")
        for line in iter(proc.stdout.readline, ''):
            time.sleep(0.2)
            yield line.rstrip() + '<br/>\n'
