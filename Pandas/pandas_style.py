import pandas as pd
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 5, 5)})
df = pd.concat([df, pd.DataFrame(np.random.randn(5, 2), columns=list('BC'))],
               axis=1)
print("Original array:")
print(df)
def color_negative_blue(val):
    color = 'blue' if val < 0 else 'red'
    return 'color: %s' % color
print("\nNegative numbers blue and positive numbers red:")
df.style.applymap(color_negative_blue)
