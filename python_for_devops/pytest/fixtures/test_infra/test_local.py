import testinfra


host = testinfra.get_host('local://')

node_file = host.file('/etc/os-release')
print(node_file.exists)
print(node_file.user)


nginx = host.package("nginx")
print(nginx.is_installed)

if nginx.is_installed:
    print(nginx.version)
else:
    print("nginx is not installed")


uptime = host.run("uptime")
print(uptime.stdout.strip())
print(uptime.rc)
