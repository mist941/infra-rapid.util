import subprocess


def install_react(project_name: str):
    command = f"npm init vite@latest {project_name} -- --template"

    result = subprocess.run(
        command,
        shell=True,
        text=True,
        stdout=None,
        stderr=None,
    )

    print(result.stdout)
