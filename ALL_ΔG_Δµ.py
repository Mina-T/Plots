import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2.6,0.0)
fig, ax = plt.subplots(3, 3, sharex=True, sharey=True)
#***************** g.Pt2
x0 = [-2.6, -3.641/2]
y0 = [0,0]
ax[0,0].plot(x0, y0, color='black', linewidth = 4.0)
ax[0,0].plot(x, -2*x-3.641,label='${\mathrm{Pt_2O_2}}$',linewidth=4.0, color="blue")
ax[0,0].plot(x, -3*x-5.023,label='${\mathrm{Pt_2O_3}}$', linewidth=4.0, color='c')
ax[0,0].plot(x, -4*x-5.806,label='${\mathrm{Pt_2O_4}}$', linewidth=4.0, color='green')
ax[0,0].axvspan(-0.71, 0.0, alpha=0.6, color='grey') # Bulk PtO2 
ax[0,0].axvspan(-0.48, 0.0, alpha=0.5, color='grey') # Bulk PtO
ax[0,0].text(-2.6, 1.5, '(a)', fontsize=26)
ax[0,0].legend(prop={"size":12}, loc="lower left")
#************************************* second x axis
ax2 = ax[0,0].twiny()
ax3 = ax[0,0].twiny()
# Make space on the top for the additional axes
fig.subplots_adjust(top=0.79)
# Move additional axes to free space on the top
ax2.spines["top"].set_position(("axes", 1.25))
ax3.spines["top"].set_position(("axes", 1.65))
# Set axes value
ax2.set_xticks([
-0.6013,
-0.4227,
-0.2442,
-0.0656
])

ax3.set_xticks([
-1.2660,
-0.9088,
-0.5517,
-0.1945
])
# Set up ticks and grid lines
ax2.tick_params(direction="in", which="major", colors='k', length = 10, width = 3)
ax3.tick_params(direction="in", which="major", colors='k', length = 10, width = 3)

ax2.set_xticklabels([
                     '$\mathregular{10^{-12}}$',
                     '$\mathregular{10^{-6}}$',
                     '$\mathregular{10^{0}}}$',
                     '$\mathregular{10^{+6}}$'],fontsize=12, color= 'k', rotation = 70)

ax3.set_xticklabels([
                     '$\mathregular{10^{-12}}$',
                     '$\mathregular{10^{-6}}$',
                     '$\mathregular{10^{0}}}$',
                     '$\mathregular{10^{+6}}$'],fontsize=12, color= 'k')
# Set axes limits
ax2.set_xlim(-2.6, 0.0)
ax3.set_xlim(-2.6, 0.0)
# Set axes colors and width
ax2.spines["top"].set_color('k')
ax2.text(-2,6,'T=300K', fontsize = 16)
# ax2.text(0.1,6,'${\mathrm{P_{O_2}}}$ (bar)', fontsize = 16)
ax3.spines["top"].set_color('k')
ax3.text(-2.1,12,'T=600K', fontsize = 16)
# ax3.text(-0.2,12,'${\mathrm{P_{O_2}}}$ (bar)', fontsize = 16)
for axis in ['top']:
    ax2.spines[axis].set_linewidth(4)
    ax3.spines[axis].set_linewidth(4)
#***************** g.Pt4
x01 = [-2.6, -4.309/2]
y01 = [0,0]
ax[0,1].plot(x01, y01, color='black', linewidth = 4.0)
ax[0,1].plot(x, -2*x-4.309, color='red',label='${\mathrm{Pt_4O_2}}$', linewidth=4.0 )
ax[0,1].plot(x, -4*x-8.154, color='blue',label='${\mathrm{Pt_4O_4}}$', linewidth=4.0 )
ax[0,1].plot(x, -6*x-8.720, color='c',label='${\mathrm{Pt_4O_6}}$',linewidth=4.0 )
ax[0,1].plot(x, -8*x-9.873, color='green',label='${\mathrm{Pt_4O_8}}$', linewidth=4.0 )
ax[0,1].axvspan(-0.71, 0.0, alpha=0.6, color='grey')
ax[0,1].axvspan(-0.48, 0.0, alpha=0.5, color='grey')
ax[0,1].text(-2.6, 1.5, '(b)', fontsize=26)

#************************************* second x axis
ax2 = ax[0,1].twiny()
ax3 = ax[0,1].twiny()

# Make space on the top for the additional axes
fig.subplots_adjust(top=0.79)

# Move additional axes to free space on the top
ax2.spines["top"].set_position(("axes", 1.25))
ax3.spines["top"].set_position(("axes", 1.65))

# Set axes value
ax2.set_xticks([
-0.6013,
-0.4227,
-0.2442,
-0.0656
])

ax3.set_xticks([
-1.2660,
-0.9088,
-0.5517,
-0.1945
])
# Set up ticks and grid lines
ax2.tick_params(direction="in", which="major", colors='k', length = 10, width = 3)
ax3.tick_params(direction="in", which="major", colors='k', length = 10, width = 3)

ax2.set_xticklabels([
                     '$\mathregular{10^{-12}}$',
                     '$\mathregular{10^{-6}}$',
                     '$\mathregular{10^{0}}}$',
                     '$\mathregular{10^{+6}}$'],fontsize=12, color= 'k', rotation = 70)

ax3.set_xticklabels([
                     '$\mathregular{10^{-12}}$',
                     '$\mathregular{10^{-6}}$',
                     '$\mathregular{10^{0}}}$',
                     '$\mathregular{10^{+6}}$'],fontsize=12, color= 'k')

# Set axes limits
ax2.set_xlim(-2.6, 0.0)
ax3.set_xlim(-2.6, 0.0)

# Set axes colors and width
ax2.spines["top"].set_color('k')
ax2.text(-2,6,'T=300K', fontsize = 16)
# ax2.text(0.1,6,'${\mathrm{P_{O_2}}}$ (bar)', fontsize = 16)


ax3.spines["top"].set_color('k')
ax3.text(-2.1,12,'T=600K', fontsize = 16)
# ax3.text(-0.2,12,'${\mathrm{P_{O_2}}}$ (bar)', fontsize = 16)

for axis in ['top']:
    ax2.spines[axis].set_linewidth(4)
    ax3.spines[axis].set_linewidth(4)
#***************** g.Pt6
x02 = [-2.6, -11.734/6]
y02 = [0,0]
ax[0,2].plot(x02, y02, color='black', linewidth = 4.0)
ax[0,2].plot(x, -3*x-5.467, color='red',label='${\mathrm{Pt_6O_3}}$', linewidth=4.0 )
ax[0,2].plot(x, -6*x-11.734, color='blue',label='${\mathrm{Pt_6O_6}}$', linewidth=4.0 )
ax[0,2].plot(x, -9*x-12.124,color='c',label='${\mathrm{Pt_6O_9}}$',linewidth=4.0 )
ax[0,2].plot(x, -12*x-13.046,color='green',label='${\mathrm{Pt_6O_{12}}}$',linewidth=4.0 )
ax[0,2].axvspan(-0.71, 0.0, alpha=0.6, color='grey')
ax[0,2].axvspan(-0.48, 0.0, alpha=0.5, color='grey')
ax[0,2].text(-2.6, 1.5, '(c)', fontsize=26)

#************************************* second x axis
ax2 = ax[0,2].twiny()
ax3 = ax[0,2].twiny()

# Make space on the top for the additional axes
fig.subplots_adjust(top=0.79)

# Move additional axes to free space on the top
ax2.spines["top"].set_position(("axes", 1.25))
ax3.spines["top"].set_position(("axes", 1.65))

# Set axes value
ax2.set_xticks([
-0.6013,
-0.4227,
-0.2442,
-0.0656
])

ax3.set_xticks([
-1.2660,
-0.9088,
-0.5517,
-0.1945
])
# Set up ticks and grid lines
ax2.tick_params(direction="in", which="major", colors='k', length = 10, width = 3)
ax3.tick_params(direction="in", which="major", colors='k', length = 10, width = 3)

ax2.set_xticklabels([
                     '$\mathregular{10^{-12}}$',
                     '$\mathregular{10^{-6}}$',
                     '$\mathregular{10^{0}}}$',
                     '$\mathregular{10^{+6}}$'],fontsize=12, color= 'k', rotation = 70)

ax3.set_xticklabels([
                     '$\mathregular{10^{-12}}$',
                     '$\mathregular{10^{-6}}$',
                     '$\mathregular{10^{0}}}$',
                     '$\mathregular{10^{+6}}$'],fontsize=12, color= 'k')

# Set axes limits
ax2.set_xlim(-2.6, 0.0)
ax3.set_xlim(-2.6, 0.0)

# Set axes colors and width
ax2.spines["top"].set_color('k')
ax2.text(-2,6,'T=300K', fontsize = 16)
ax2.text(0.1, 5, '${\mathrm{P_{O_2}}}$ (bar)', fontsize = 20, rotation = 270)


ax3.spines["top"].set_color('k')

ax3.text(-2.1,12,'T=600K', fontsize = 16)
# ax3.text(-0.2,12,'${\mathrm{P_{O_2}}}$ (bar)', fontsize = 16)

for axis in ['top']:
    ax2.spines[axis].set_linewidth(4)
    ax3.spines[axis].set_linewidth(4)
#***************** T.Pt2
x10 = [-2.6, -4.34/2]
y10 = [0,0]
ax[1,0].plot(x10, y10, color='black', linewidth = 4.0)
ax[1,0].plot(x,-2*x-4.34, color='blue',label='${\mathrm{Pt_2O_2}}$', linewidth=5.0 )
ax[1,0].plot(x,-4*x-5.68, color='green',label='${\mathrm{Pt_2O_4}}$', linewidth=5.0 )
ax[1,0].axvspan(-0.71, 0.0, alpha=0.6, color='grey')
ax[1,0].axvspan(-0.48, 0.0, alpha=0.5, color='grey')
ax[1,0].text(-2.6, 1.5, '(d)', fontsize=26)
#***************** T.Pt4
x11 = [-2.6, -2.620/2]
y11 = [0,0]
ax[1,1].plot(x11, y11, color='black', linewidth = 4.0)
ax[1,1].plot(x,-2*x-2.620, color='red',label='${\mathrm{Pt_4O_2}}$',  linewidth=5.0 )
ax[1,1].plot(x,-4*x-5.380, color='blue',label='${\mathrm{Pt_4O_4}}$', linewidth=5.0 )
ax[1,1].plot(x,-6*x-6.298,color='c',label='${\mathrm{Pt_4O_6}}$', linewidth=5.0 )
ax[1,1].plot(x,-8*x-8.356,color='green',label='${\mathrm{Pt_4O_8}}$', linewidth=5.0 )
ax[1,1].axvspan(-0.71, 0.0, alpha=0.6, color='grey')
ax[1,1].axvspan(-0.48, 0.0, alpha=0.5, color='grey')
ax[1,1].text(-2.6, 1.5, '(e)', fontsize=26)
#***************** T.Pt6
x12 = [-2.6, -9.424/6]
y12 = [0,0]
ax[1,2].plot(x12, y12, color='black', linewidth = 4.0)
ax[1,2].plot(x, -3*x-3.900, color='red',label='${\mathrm{Pt_6O_3}}$', linewidth=5.0 )#label='Pt6O3'
ax[1,2].plot(x, -6*x-9.424, color='blue',label='${\mathrm{Pt_6O_6}}$', linewidth=5.0 )#label='Pt6O6'
ax[1,2].plot(x, -9*x-10.196,color='c',label='${\mathrm{Pt_6O_9}}$',linewidth=5.0 )#label='Pt6O9'
ax[1,2].plot(x, -12*x-10.281,color='green',label='${\mathrm{Pt_6O_{12}}}$', linewidth=5.0 )#
ax[1,2].axvspan(-0.71, 0.0, alpha=0.6, color='grey')
ax[1,2].axvspan(-0.48, 0.0, alpha=0.5, color='grey')
ax[1,2].text(-2.6, 1.5, '(f)', fontsize=26)
#***************** C.Pt2
x20 = [-2.6, -3.093/2]
y20 = [0,0]
ax[2,0].plot(x20, y20, color='black', linewidth = 4.0, label = '${\mathrm{Pt_x}}$')
ax[2,0].plot(x, -2*x+13.093, color='red',label='${\mathrm{Pt_xO_{0.5x}}}$',  linewidth=5.0 )# entered just to use for legend label
ax[2,0].plot(x, -2*x-3.093, color='blue',label='${\mathrm{Pt_xO_{x}}}}$',  linewidth=5.0 )
ax[2,0].plot(x, -2*x+13.093, color='c',label='${\mathrm{Pt_xO_{1.5x}}}$',  linewidth=5.0 )# entered just to use for legend label
ax[2,0].plot(x, -4*x-5.121, color='green',label='${\mathrm{Pt_xO_{2x}}}$', linewidth=5.0 )
ax[2,0].axvspan(-0.71, 0.0, alpha=0.6, color='grey')
ax[2,0].axvspan(-0.48, 0.0, alpha=0.5, color='grey')
ax[2,0].text(-2.6, 1.5, '(g)', fontsize=26)


#OR
# lines_labels = [ax[2,0].get_legend_handles_labels()]
# lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
# fig.legend(lines, labels, loc="upper center", ncol = 5, fontsize= 24)
#***************** C.Pt4
x21 = [-2.6, -3.917/2]
y21 = [0,0]
ax[2,1].plot(x21, y21, color='black', linewidth = 4.0)
ax[2,1].plot(x, -2*x-3.917, color='red',label='${\mathrm{Pt_4O_2}}$',  linewidth=5.0 )
ax[2,1].plot(x, -4*x-6.742, color='blue',label='${\mathrm{Pt_4O_4}}$', linewidth=5.0 )
ax[2,1].plot(x, -6*x-6.596,color='c',label='${\mathrm{Pt_4O_6}}$',linewidth=5.0 )
ax[2,1].plot(x, -8*x-8.424,color='green',label='${\mathrm{Pt_4O_8}}$', linewidth=5.0 )
ax[2,1].axvspan(-0.71, 0.0, alpha=0.6, color='grey')
ax[2,1].axvspan(-0.48, 0.0, alpha=0.5, color='grey')
ax[2,1].text(-2.6, 1.5, '(h)', fontsize=26)
ax[2,1].legend(prop={"size":12}, loc="lower left")
#***************** C.Pt6
x22 = [-2.6, -5.284/3]
y22 = [0,0]
ax[2,2].plot(x22, y22, color='black', linewidth = 4.0)
ax[2,2].plot(x, -3*x-5.284, color='red',label='${\mathrm{Pt_6O_3}}$',  linewidth=5.0 )
ax[2,2].plot(x, -6*x-9.644, color='blue',label='${\mathrm{Pt_6O_6}}$', linewidth=5.0 )
ax[2,2].plot(x, -9*x-9.877,color='c',label='${\mathrm{Pt_6O_9}}$',linewidth=5.0 )
ax[2,2].plot(x, -12*x-10.296,color='green',label='${\mathrm{Pt_6O_{12}}}$', linewidth=5.0 )
ax[2,2].axvspan(-0.71, 0.0, alpha=0.6, color='grey')
ax[2,2].axvspan(-0.48, 0.0, alpha=0.5, color='grey')
ax[2,2].text(-2.6, 1.5, '(i)', fontsize=26)
ax[2,2].legend(prop={"size":12}, loc="lower left")
#************************************************************************************
plt.xticks(np.arange(min(x), max(x)+1, 0.2))
plt.ylim(-14, 1)

for ax in ax.flat:
    ax.tick_params(axis='x', which='major', labelsize=20)
    ax.tick_params(axis='y', which='major', labelsize=18)
    ax.margins(0)
fig.add_subplot(1, 1, 1, frame_on=False) #encapsulate all the subplots in one
plt.tick_params(labelcolor="none", bottom=False, left=False) # hide gigger plot's ticks

axis_font = {'size':'30'}
plt.xlabel("${\mathrm{Δµ_O (eV)}}$",  **axis_font, labelpad=20)
plt.ylabel("ΔG (eV)",  **axis_font, labelpad=22)

plt.show()


