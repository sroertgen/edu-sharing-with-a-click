from ruamel.yaml import YAML

yaml = YAML()


def edit_yml(input):
    print(input)

# Pfad anpassen
    with open('ansible-templates/ansible_moodle/host_vars/web_server_template.yml') as fp:
        data = yaml.load(fp)
        print(data)
        print(input)
    for entry in data:
        data['ansible_host'] = input['ip1']
        data['ansible_user'] = input['uname']
        data['ansible_ssh_pass'] = input['upasswd']
        data['admin-mail'] = input['email']

    with open("ansible-templates/ansible_moodle/host_vars/web_server.yml", "w") as outfile:
        yaml.dump(data, outfile)
