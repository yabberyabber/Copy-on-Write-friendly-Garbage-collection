import matplotlib.pyplot as plt
import sys
import json
from matplotlib2tikz import save as tikz_save

def pid_to_color(pid):
    colors = ['r', 'g', 'b', 'k', 'c', 'purple']
    return colors[int(pid) % len(colors)]

def plot_results(measurements):
    fig, (shared, private) = plt.subplots(2, 1)

    Xs = []
    shared_Ys = []
    private_Ys = []
    for pid, worker in measurements.items():
        if pid in ["18622", "14655"]:
            continue
        for x, vals in worker.items():
            if x == "0":
                continue
            Xs.append(x)
            shared_Ys.append((vals['shared'] / 1000.0, pid_to_color(pid)))
            private_Ys.append((vals['private'] / 1000.0, pid_to_color(pid)))

    shared.scatter(Xs, [x[0] for x in shared_Ys], color=[x[1] for x in shared_Ys])
    shared.set_xlabel("Requests Served")
    shared.set_ylabel("Memory (Mb)")
    shared.set_title("Shared memory")
    shared.set_xlim(left=0, right=5000)
    shared.set_ylim(bottom=0, top=6000)
    shared.get_yaxis().get_major_formatter().set_useOffset(False)

    private.scatter(Xs, [x[0] for x in private_Ys], color=[x[1] for x in private_Ys])
    private.set_xlabel("Requests Served")
    private.set_ylabel("Memory (Mb)")
    private.set_title("Nonshared memory")
    private.set_xlim(left=0, right=5000)
    private.set_ylim(bottom=0, top=1400)

    fig.tight_layout()
    fig.savefig('standard_mem.pdf')
    fig.savefig('standard_mem.pgf')
    plt.show()

    """
    tikz_save('patched_mem.tikz',
              figureheight = '\\figureheight',
              figurewidth = '\\figurewidth')
    """

if __name__ == '__main__':
	with open(sys.argv[1]) as infile:
		data = json.load(infile)
		plot_results(data)
