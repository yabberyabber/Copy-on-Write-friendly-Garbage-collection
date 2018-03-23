import subprocess

def do_test(n):
    print "make start && sleep 10 && httperf --port=4000 --num-conns={} > 4m_with_{}kreq_8g.httperf".format(n, n // 1000)

    subprocess.check_output(
        "make start && sleep 10 && httperf --port=4000 --num-conns={} > 4m_with_{}kreq_8g.httperf".format(n, n // 1000),
        shell=True)

for n in [5000, 10000, 15000, 20000]:
    do_test(n)
