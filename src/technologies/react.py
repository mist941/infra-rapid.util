import subprocess


def execute_command(command: str):
    subprocess.run(
        command,
        shell=True,
        text=True,
        stdout=None,
        stderr=None,
    )


def setup_react(project_name: str):
    command = f"npm init vite@latest {project_name} -- --template react-ts"

    execute_command(command)
