import pandas as pd
import numpy as np


chat_id = 1882360450 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy import stats
    res = stats.ks_2samp(i, j)
    if res.pvalue<=0.03: 
        answer=True
    else:
        answer=False

    return answer
    
