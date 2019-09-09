'''
This file writes the form entries from register.html
to the host_var files of the relevant ansible-file
'''

from ruamel.yaml import YAML

yaml = YAML()


def edit_yml(input, instance_choice, moodle_registration):
    print("running edit_yaml")
    print(f"Input is: {input}")
    print(f"instance_choice is : {instance_choice}")

    # Set right path to host_vars file depending on instance_choice
    if instance_choice == "moodle" or instance_choice == "wordpress":
        print(f"Choice was: {instance_choice}")
        if instance_choice == "moodle":
            instance = "moodle"
        elif instance_choice == "wordpress":
            instance = "wordpress"

        path_template = f"ansible-templates/ansible_{instance}/host_vars/web_server_template.yml"
        path_edited_file = f"ansible-templates/ansible_{instance}/host_vars/web_server.yml"

        with open(path_template) as fp:
            data = yaml.load(fp)
            print(data)
            print(input)
        for entry in data:
            data['ansible_host'] = input['ip1']
            data['ansible_user'] = input['uname1']
            data['ansible_ssh_pass'] = input['upasswd1']
            data['admin-mail'] = input['email']

        with open(path_edited_file, "w") as outfile:
            yaml.dump(data, outfile)

    elif instance_choice == "edusharing":
        print(f"Choice was: {instance_choice} and moodle_registration was {moodle_registration}")
        instance = "edu_sharing"

        path_template_edu_sharing = "ansible-templates/ansible_edu_sharing/host_vars/edu_sharing_host_template.yml"
        path_template_esrender = "ansible-templates/ansible_edu_sharing/host_vars/esrender_host_template.yml"

        path_edited_edu_sharing_file = "ansible-templates/ansible_edu_sharing/host_vars/edu_sharing_host.yml"
        path_edited_esrender_file = "ansible-templates/ansible_edu_sharing/host_vars/esrender_host.yml"

        # first edit edu_sharing_template
        with open(path_template_edu_sharing) as fp:
            data = yaml.load(fp)
            print(data)
            print(f" Input 1: {input}")
        for entry in data:
            data['ansible_host'] = input['ip1']
            data['ansible_user'] = input['uname1']
            data['ansible_ssh_pass'] = input['upasswd1']
            data['edu_sharing_base_domain'] = input['domain1']
            #data['admin-mail'] = input1['email']

        with open(path_edited_edu_sharing_file, "w") as outfile:
            yaml.dump(data, outfile)

        print("First editing done")

        # second edit esrender_template
        with open(path_template_esrender) as fp:
            data = yaml.load(fp)
            print(data)
            print(input)
        for entry in data:
            data['ansible_host'] = input['ip2']
            data['ansible_user'] = input['uname2']
            data['ansible_ssh_pass'] = input['upasswd2']
            #data['admin-mail'] = input['email']

        with open(path_edited_esrender_file, "w") as outfile:
            yaml.dump(data, outfile)
    
        if moodle_registration == 1:
            path_template_moodle_host = "ansible-templates/ansible_edu_sharing/host_vars/moodle_host_template.yml"
            path_edited_moodle_host_file = "ansible-templates/ansible_edu_sharing/host_vars/moodle_host.yml"

            # edit moodle host var file in edu_sharing
            with open(path_template_moodle_host) as fp:
                data = yaml.load(fp)
                print(data)
                print(input)
            for entry in data:
                data['ansible_host'] = input['moodle_ip']
                data['ansible_user'] = input['moodle_uname']
                data['ansible_ssh_pass'] = input['moodle_pw']
                data['moodle_base_domain'] = input['moodle_domain']
                #data['admin-mail'] = input['email']

            with open(path_edited_moodle_host_file, "w") as outfile:
                yaml.dump(data, outfile)

            path_template = "ansible-templates/ansible_moodle/host_vars/web_server_template.yml"
            path_edited_file = "ansible-templates/ansible_moodle/host_vars/web_server.yml"

            # edit moodle host var file in ansible_moodle
            with open(path_template) as fp:
                data = yaml.load(fp)
                print(data)
                print(input)
            for entry in data:
                data['ansible_host'] = input['moodle_ip']
                data['ansible_user'] = input['moodle_uname']
                data['ansible_ssh_pass'] = input['moodle_pw']
                data['moodle_base_domain'] = input['moodle_domain']
                data['edu_sharing_host'] = input['ip1']
                data['edu_sharing_base_domain'] = input['domain1']

            with open(path_edited_file, "w") as outfile:
                yaml.dump(data, outfile)
