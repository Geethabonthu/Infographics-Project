import matplotlib.pyplot as plt
import pandas as pd
df_clean=pd.read_csv('IKEA_business_case_clean_data.csv')
def plot_demography_bar(ax, features, color):
    df_clean.groupby(features)['CustomerID'].count().sort_values().plot(ax=ax, kind='barh',\
              figsize=(10,8), fontsize=8, width=0.8, color=color, zorder=3)
    ax.set_title("Customer distribution by " + str(features), fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.legend(loc='upper left', bbox_to_anchor=(0.4, 0.3))
    ax.grid(color='w', zorder=0)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_facecolor('whitesmoke')

def plot_demography_pie(ax, features):
    df_clean[features].value_counts().plot.pie(ax=ax, textprops={'color':"w"}, pctdistance=0.7, subplots=True)
    ax.set_title(str(features) +' Percentage Distribution', fontsize=8)
    ax.legend(labels=df_clean[features].value_counts().index, loc="best", bbox_to_anchor=(0.3, 0.15))

# Create a 1x2 grid of subplots
fig, axs = plt.subplots(3, 3, figsize=(15,15),tight_layout={'w_pad': 6.0})

# Plot in the first subplot (axes[0])
plot_demography_bar(axs[0,0], 'Sex', 'rebeccapurple')

# Plot in the second subplot (axes[1])
plot_demography_pie(axs[1,0], 'Sex')

plot_demography_bar(axs[0,1], 'Age', 'navy')
plot_demography_pie(axs[1,1], 'Age')

plot_demography_bar(axs[0,2], 'Profession', 'mediumaquamarine')
plot_demography_pie(axs[1,2], 'Profession')
plt.suptitle('IKEA business case', fontsize=16)

fig.delaxes(axs[2, 0])
fig.delaxes(axs[2, 1])
fig.delaxes(axs[2, 2])
fig.text(0.1, 0,
'''All the visualization of distribution of IKEA business cases have been accomplished
with respect to the Customer ID in order to check the distribution of products. Whether
it is age, sex or profession, Customer ID acted as indicator in all the visualizations.
From the first visualization, it has beenfound that male customers are more engaged
with the services of the organization in comparison to females. Likewise, the second
bar graph depicts the age group 26 to 35 of customers who expand the maximum for the
services of IKEA business. Similarly, category 4 indicates the professional background
of people who consumed the service at maximum.
'''
, fontsize=9, fontweight='light', fontfamily='serif')
fig.text(0.8,0.001,'''The visual representation has
been performed by using two
methods:bar graph and pie
chart. The pie chart shed
light mainly on the quantity
of customers consuming the
services of IKEA business.
On the other hand, the bar
graph represents the data
values in a classified manner.
The visual representation
has been performed by using
two methods: bar graph and
pie chart. The pie chart shed
light mainly on the quantity
of customers consuming the
services of IKEA business.
On the other hand, the bar
graph represents the data
values in a classified
manner.''', fontsize=9, fontweight='light', fontfamily='serif')
plt.subplots_adjust(wspace=0.4, hspace=0.5)

fig.text(0.8, 0.95,
'''Student id: 22095828 
Name : Geetha Bonthu'''
, fontsize=11, fontweight='light', fontfamily='serif')


# plt.savefig('22095828.png')

plt.show()