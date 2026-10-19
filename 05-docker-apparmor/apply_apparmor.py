import docker

client = docker.from_env()

client.images.build(path=".", tag="flask-apparmor")

container = client.containers.run(
    "flask-apparmor",
    ports={"5000/tcp": 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True,
    name="apparmor-sdk-test"
)

try:
    info = client.api.inspect_container(container.id)
    print("Container started:", container.short_id)
    print("Security options:", info["HostConfig"]["SecurityOpt"])
    print("Reported AppArmor profile:", info.get("AppArmorProfile"))
finally:
    container.stop()
    container.remove()
