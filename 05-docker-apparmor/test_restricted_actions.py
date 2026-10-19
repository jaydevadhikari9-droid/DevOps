import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    detach=True,
    name="apparmor-restriction-test"
)

try:
    for command in [
        ["sh", "-c", "cat /etc/passwd"],
        ["sh", "-c", "/bin/bash"]
    ]:
        result = container.exec_run(command)
        print("Command:", " ".join(command))
        print("Exit code:", result.exit_code)
        print("Output:", result.output.decode(errors="replace"))
finally:
    container.stop()
    container.remove()
