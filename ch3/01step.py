import numpy as np

# ステップ関数
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
    

# numpy配列に対応
def step_function2(x):
    y = (x > 0) # bool配列
    return y.astype(int) # intにキャスト

print(step_function2(np.array([-1.5, 1.0, 10.3])))
