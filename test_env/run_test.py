from pprint import pprint
import subprocess
from collections import defaultdict
from httperfpy import Httperf, HttperfParser
import matplotlib.pyplot as plt
import json
from threading import Thread
import sys

measurements = defaultdict(lambda: {})
num_requests = 0

def get_pids():
    res = subprocess.check_output(
            "ps -u root -ae | grep uwsgi | grep -v grep",
            shell=True)
    processes = res.decode().strip().split('\n')
    processes = [x.strip() for x in processes]
    processes = [x.split(' ')[0] for x in processes]
    processes = [int(x) for x in processes]
    return processes

def get_stat(pid, stat):
    res = subprocess.check_output(
            "cat /proc/{}/smaps | grep {}".format(pid, stat),
            shell=True
    ).decode().strip().split('\n')
    res = [int(x.strip().split(' ')[-2]) for x in res]
    return sum(res)

def measure_pid(pid):
    shared_memory = get_stat(pid, "Shared_Clean") + get_stat(pid, "Shared_Dirty")
    private_memory = get_stat(pid, "Private_Clean") + get_stat(pid, "Private_Dirty")

    global num_requests
    measurements[pid][num_requests] = {
            'shared': shared_memory,
            'private': private_memory,
            'total': shared_memory + private_memory,
    }

def measure_all_pids():
    for pid in get_pids():
        try:
            measure_pid(pid)
        except:
            print "Couldn't get measurement for {} at {}".format(pid, num_requests)

def test_load(requests=50):
    global num_requests
    num_requests += requests * 2

    def attach_load():
        perf = Httperf(server="localhost", port=4000,
                       num_conns=requests)
        httperf_result_string = perf.run()

        results = HttperfParser.parse(httperf_result_string)

    a = Thread(target=attach_load)
    b = Thread(target=attach_load)
    a.start()
    b.start()
    a.join()
    b.join()

def plot_results(measurements):
    fig, (shared, private) = plt.subplots(2, 1)

    Xs = []
    shared_Ys = []
    private_Ys = []
    for worker in measurements.values():
        for x, vals in worker.items():
            Xs.append(x)
            shared_Ys.append(vals['shared'])
            private_Ys.append(vals['private'])

    shared.scatter(Xs, shared_Ys)
    shared.set_xlabel("num_requests")
    shared.set_ylabel("memory (kb)")
    shared.set_title("Shared memory")
    shared.set_xlim(left=0)

    private.scatter(Xs, private_Ys)
    private.set_xlabel("num_requests")
    private.set_ylabel("memory (kb)")
    private.set_title("Nonshared memory")
    private.set_xlim(left=0)
    private.set_ylim(bottom=0)

    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    print sys.argv[1]
    for _ in range(50):
        measure_all_pids()
        test_load()
        print _

    measure_all_pids()
    pprint(dict(measurements))

    with open(sys.argv[1], 'w') as outfile:
        json.dump(measurements, outfile)

    plot_results(measurements)
