import subprocess
import pytest


def get_part_entry_type(device):
    """
    Parses the ID_PART_ENTRY_TYPE from blkid output (in udev format).
    """
    stdout = subprocess.check_output(['blkid', '-p', '-o', 'udev', device])

    if isinstance(stdout, bytes):
        stdout = stdout.decode()

    for line in stdout.split('\n'):
        if 'ID_PART_ENTRY_TYPE=' in line:
            return line.split('=')[-1].strip()
    return ''


def test_parses_id_entry_type(monkeypatch):
    monkeypatch.setattr(
        'subprocess.check_output',
        lambda cmd: 'ID_PART_ENTRY_TYPE=aaaaa\n'
    )

    assert get_part_entry_type('/dev/sda') == 'aaaaa'
