import matplotlib as plt


def save_vectorgraphic(fig, filename):
    fig.savefig(format='eps', fname=filename)
