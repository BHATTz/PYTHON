# import matplotlib.pyplot as plt
# import numpy as np
# xaxis = np.array([2,8])
# yaxis = np.array([4,9])
# plt.plot(xaxis,yaxis)
# plt.show()

# import plotly.graph_objects as go
# categories = ['processing cost','mechanical properties','chemical stability',
#              'thermal stability', 'device integration']
# fig = go.Figure()
# fig.add_trace(go.Scatterpolar(
#       r=[1, 5, 2, 2, 3],
#       theta=categories,
#       fill='toself',
#       name='Product A'
# ))
# fig.add_trace(go.Scatterpolar(
#       r=[4, 3, 2.5, 1, 2],
#       theta=categories,
#       fill='toself',
#       name='Product B'
# ))
# fig.update_layout(
#   polar=dict(
#     radialaxis=dict(
#       visible=True,
#       range=[0, 5]
#     )),
#   showlegend=False
# )
# fig.show()

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()