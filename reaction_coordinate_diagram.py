import matplotlib.pyplot as plt

class Reaction_diagram:
    def __init__(self, data: dict):
        self.labels = data['labels']
        self.energies = data['energies']
        self.steps = range(1, len(self.labels) +1)
        self.barriers = data['barriers']

    def draw_barrier(self, step, energy, label, barrier):
        if barrier:
            color = 'r'
        else:
            color = 'g'
        plt.hlines(y= energy, xmin= step - 0.199, xmax= step + 0.199, linewidth=4, color=color)
        plt.annotate(label, xy=(step, energy + 0.2))
        
    def connect_steps(self):
        for i in range(len(self.steps)-1):
            plt.plot([self.steps[i]+0.20, self.steps[i+1]-0.2], [self.energies[i], self.energies[i+1]],  ':b')

    def plot_reaction_diagram(self):
        fig = plt.figure(figsize=(10,5))
        for step, energy, label, barrier in zip(self.steps, self.energies, self.labels, self.barriers):
            self.draw_barrier(step, energy, label, barrier)
        self.connect_steps()
        plt.xticks([])
        axs = plt.gca()
        axs.spines['top'].set_visible(False)
        axs.spines['right'].set_visible(False)
        plt.yticks(fontsize = 13)
        plt.xlabel('Reaction coordinates ------->', fontsize = 16, labelpad=15)
        plt.ylabel('Energy (eV)', fontsize = 16, labelpad=15)
        plt.show()

