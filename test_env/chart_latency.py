import matplotlib.pyplot as plt
import sys
import json
from matplotlib2tikz import save as tikz_save

Xs = [5, 10, 15, 20]
standard_conn = [190.8, 269.2, 97.7, 103.2]
patched_conn = [67.9, 148.7, 188.8, 190.9]

fig, ax = plt.subplots()

bar_standard = ax.bar([x/5 + 0.15 for x in Xs], standard_conn, 0.35, color='r')
bar_patched = ax.bar([x/5 + 0.5 for x in Xs], patched_conn, 0.35, color='b')

ax.set_ylabel('Requests/sec (more is better)')
ax.set_xlabel('Number of Requests')
ax.set_title('Latency by number of requests')
ax.legend((bar_standard, bar_patched), ('Standard GC', 'Patched GC'))
ax.set_xticks([x/5 + 0.5 for x in Xs])
ax.set_xticklabels([str(x) + 'k' for x in Xs])

fig.tight_layout()
fig.savefig('chart_latency.pdf')
fig.savefig('chart_latency.pgf')
plt.show()
