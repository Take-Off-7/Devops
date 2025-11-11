import sys


def stderr_logging():
    sys.stderr.write('stderr output being produced')

def stdout_logging():
    sys.stdout.write('stdout output being produced')


def test_verify_stderr(capsys):
    stderr_logging()
    out, err = capsys.readouterr()
    assert out == ''
    assert err == 'stderr output being produced'

def test_verify_stdout(capsys):
    stdout_logging()
    out, err =  capsys.readouterr()
    assert out == 'stdout output being produced'
    assert err == ''
