# -*- coding: utf-8 -*-
import os
import random
import uuid

def get_idle_port():
    pscmd = "netstat -ntl |grep -v Active| grep -v Proto|awk '{print $4}'|awk -F: '{print $NF}'"
    procs = os.popen(pscmd).read()
    procarr = procs.split("\n")
    tt= random.randint(10000,20000)
    if tt not in procarr:
        return tt
    else:
        return get_idle_port()


def guid():
    return str(uuid.uuid4()).replace('-', '')


def run_tuchuan_container(image_tag: str, config_filepath: str, service_filepath: str = None, name: str = None):
    import platform
    import subprocess
    cpu_arch: str = platform.machine()

    cmd_base = [
            'docker', 'run', '--rm', '-it',
            '--cap-add=NET_ADMIN',
            '-p', '22554:12554/tcp',
            '-p', '22883:1883/tcp',
            '-p', '22001-22004:12001-12004/tcp',
            '-v', '/etc/hosts:/etc/hosts',
            '-v', '/tmp:/tmp',
            '-v', '/dev:/dev',
            '-e', 'DEBUG_COLORS=false'
    ]

    if cpu_arch in ('x86', 'x86_64'):
        run_cmd = cmd_base[:]
        run_cmd.extend([
            '--device', '/dev/dri/renderD128:/dev/dri/renderD128',
            '-e', 'LIBVA_DRIVER_NAME=iHD'
        ])
    elif cpu_arch in ('aarch64', ):
        run_cmd = cmd_base[:]
        run_cmd.extend([
            '-e', '--runtime', 'nvidia',
            '-e', ' GST_PLUGIN_PATH=/usr/local/lib/aarch64-linux-gnu/gstreamer-1.0:/usr/lib/aarch64-linux-gnu/gstreamer-1.0'
        ])
    else:
        run_cmd = None

    if run_cmd is None:
        return None
    
    if name:
        run_cmd.extend(['--name', f'{name}'])

    run_cmd.extend(['-v', f'{config_filepath}:/kd_install/config/matrix-config.json'])
    if service_filepath is not None:
        run_cmd.extend(['-v', f'{service_filepath}:/workdir/dy-pm-tuchuan/dist/configs/tuchuan-services.json'])
    run_cmd.append(image_tag)
    
    print(" ".join(run_cmd))
    return subprocess.Popen(run_cmd)


if __name__ == '__main__':
    import sys
    print(sys.argv)
    image_tag = sys.argv[1]
    config_filepath = sys.argv[2]
    service_filepath = None
    if len(sys.argv) >= 4:
        service_filepath = sys.argv[3]
    run_tuchuan_container(image_tag, config_filepath, service_filepath)
    import time
    while True:
        time.sleep(1)
        pass
