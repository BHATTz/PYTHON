# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd 
# df = pd.DataFrame([['A',10,20,10,26],['B',20,25,15,21],['C',12,15,19,6],['D',10,18,11,19]],columns=['team','round 1','round 2','round 3','round 4'])
# print(df)
# df.plot(x='team',kind='bar',stacked=True,title='stacked bar graph by data frame')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.DataFrame([['A',10,20,10,26],['B',20,25,15,21],['C',12,15,19,6],['D',10,18,11,19]],
                columns=['Team','Round 1','Round 2','Round 3','Round 4'])
print(df)
df.plot(x='Team',kind='bar',stacked=True,
        title='Stacked Bar Graph by dataframe')