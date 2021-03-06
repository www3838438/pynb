import os

from fabric.api import local


def cells():
    int(10000 + 2345)


def sumup(N):
    N = int(N)
    int((N * (N + 1)) / 2)


def sum(a, b):
    a, b = int(a), int(b)
    int(a + b)


def markdown():
    '''
    # Title
    '''


def test_pynb_cells():
    cmd = 'pynb {} --disable-cache --export-ipynb -'
    output = local(cmd.format(os.path.realpath(__file__)), capture=True)
    assert '12345' in output


def test_pynb_sumup():
    cmd = 'pynb {}:sumup --param N=10000 --disable-cache --export-ipynb -'
    output = local(cmd.format(os.path.realpath(__file__)), capture=True)
    assert '50005000' in output


def test_pynb_sum():
    cmd = 'pynb {}:sum --param a=50000 --param b=4321 --disable-cache --export-ipynb -'
    output = local(cmd.format(os.path.realpath(__file__)), capture=True)
    assert '54321' in output


def test_pynb_export_ipynb(tmpdir):
    cmd = 'pynb {} --disable-cache --export-ipynb {}/test.ipynb'
    local(cmd.format(os.path.realpath(__file__), tmpdir))

    cmd = 'jupyter nbconvert --stdout --to notebook {}/test.ipynb'
    output = local(cmd.format(tmpdir), capture=True)
    assert '12345' in output


def test_pynb_export_html():
    cmd = 'pynb {}:markdown --disable-cache --export-html -'
    output = local(cmd.format(os.path.realpath(__file__)), capture=True)
    assert '<html>' in output
    assert '>Title<' in output


def test_export_pynb(tmpdir):
    test_pynb_export_ipynb(tmpdir)
    cmd = 'pynb --disable-cache --import-ipynb {}/test.ipynb --export-pynb - --no-exec'
    output = local(cmd.format(tmpdir), capture=True)
    assert 'def cells():' in output


def test_no_double_footer(tmpdir):
    test_pynb_export_ipynb(tmpdir)
    cmd = 'pynb --disable-cache --import-ipynb {}/test.ipynb --export-ipynb - --debug'
    output = local(cmd.format(tmpdir), capture=True)
    assert 'Footer cell already present' in output.stderr
