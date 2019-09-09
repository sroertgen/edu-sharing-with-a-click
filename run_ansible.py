import subprocess
import time

edu_sharing_created = 0

def run_ansible(choice, moodle_registration):
    print(f"Running Ansible with instance choice: {choice} and moodle_registration: {moodle_registration}")

    if choice == "moodle":
        print("Creating a Moodle instance")
        proc = subprocess.Popen(["ansible-playbook", "ansible-templates/ansible_moodle/moodle-playbook.yml", "-i", "ansible-templates/ansible_moodle/inventory.txt"], stdout=subprocess.PIPE, universal_newlines=True)
        print("Ansible running...creating moodle instance...")
        for line in iter(proc.stdout.readline, ''):
            time.sleep(0.2)
            yield line.rstrip() + '<br/>\n'

    if choice == "wordpress":
        print("Creating a Wordpress instance")
        proc = subprocess.Popen(["ansible-playbook", "ansible-templates/ansible_wordpress/wp-playbook.yml", "-i", "ansible-templates/ansible_wordpress/inventory.txt"], stdout=subprocess.PIPE, universal_newlines=True)
        print("Ansible running...creating wordpress instance...")
        for line in iter(proc.stdout.readline, ''):
            time.sleep(0.2)
            yield line.rstrip() + '<br/>\n'

    if choice == "edusharing":
        print("Creating an edu-sharing instance")
        proc = subprocess.Popen(["ansible-playbook", "ansible-templates/ansible_edu_sharing/edu-playbook.yml", "-i", "ansible-templates/ansible_edu_sharing/inventory-edu-sharing.txt"], stdout=subprocess.PIPE, universal_newlines=True)
        print("Ansible running...creating edusharing instance...")
        for line in iter(proc.stdout.readline, ''):
            time.sleep(0.2)
            yield line.rstrip() + '<br/>\n'
        edu_sharing_created = 1

        if moodle_registration == 1:
            print("Creating a Moodle instance for edu-sharing")
            proc = subprocess.Popen(["ansible-playbook", "ansible-templates/ansible_moodle/moodle-playbook.yml", "-i", "ansible-templates/ansible_moodle/inventory.txt"], stdout=subprocess.PIPE, universal_newlines=True)
            print("Ansible running...creating moodle instance with es-plugin...")
            for line in iter(proc.stdout.readline, ''):
                time.sleep(0.2)
                yield line.rstrip() + '<br/>\n'
    
            if edu_sharing_created == 1 and moodle_registration == 1:
                print("Creating an edu-sharing instance")
                proc = subprocess.Popen(["ansible-playbook", "ansible-templates/ansible_edu_sharing/edu-playbook-moodle.yml", "-i",
                                        "ansible-templates/ansible_edu_sharing/inventory-es-moodle.txt"], stdout=subprocess.PIPE, universal_newlines=True)
                print("Ansible running...registration of moodle in es instance...")
                for line in iter(proc.stdout.readline, ''):
                    time.sleep(0.2)
                    yield line.rstrip() + '<br/>\n'
