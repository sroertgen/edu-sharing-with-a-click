import yaml
import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase


class ResultCallback(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))


# Options = namedtuple('Options',
#                      ['connection',
#                       'remote_user',
#                       'ask_sudo_pass',
#                       'verbosity',
#                       'ack_pass',
#                       'module_path',
#                       'forks',
#                       'become',
#                       'become_method',
#                       'become_user',
#                       'check',
#                       'listhosts',
#                       'listtasks',
#                       'listtags',
#                       'syntax',
#                       'sudo_user',
#                       'sudo',
#                       'diff'])

Options = namedtuple('Options', ['connection', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])

loader = DataLoader()

# options = Options(connection='ssh',
#                   remote_user='cloud',
#                   ack_pass=None,
#                   sudo_user=None,
#                   forks=5,
#                   sudo=None,
#                   ask_sudo_pass=False,
#                   verbosity=5,
#                   module_path=None,
#                   become=None,
#                   become_method='sudo',
#                   become_user='root',
#                   check=False,
#                   diff=False,
#                   listhosts=None,
#                   listtasks=None,
#                   listtags=None,
#                   syntax=None)

options = Options(connection='ssh', forks=100, become=None, become_method='sudo', become_user='cloud', check=False,
                  diff=False)

passwords = {}

results_callback = ResultCallback()

inventory = InventoryManager(loader=loader, sources=['ansible-files/inventory.txt'])

variable_manager = VariableManager(loader=loader, inventory=inventory)

with open('ansible-files/main.yml') as f:
    data = yaml.load(f)

play_source1 = dict(
    name="Ping test",
    hosts='all',
    gather_facts='no',
    tasks=[
        dict(action=dict(module='shell', args='ls'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    ]
)

with open('ansible-files/playbook-pingtest.yml') as f:
    tasks_dict = dict(yaml.load(f))

play = Play().load(tasks_dict, variable_manager=variable_manager, loader=loader)

tqm = None
try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        # options=options,
        passwords=passwords,
        stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin
    )
    result = tqm.run(play)
finally:
    if tqm is not None:
        tqm.cleanup()
