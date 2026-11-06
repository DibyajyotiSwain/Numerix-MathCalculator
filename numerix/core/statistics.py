import numpy as np
import pandas as pd
def describe(values):
    a=np.asarray(values,dtype=float)
    if a.size==0 or not np.isfinite(a).all(): raise ValueError("Enter finite numeric values")
    s=pd.Series(a)
    return {"Count":int(s.count()),"Mean":float(s.mean()),"Median":float(s.median()),"Minimum":float(s.min()),"Maximum":float(s.max()),"Sample standard deviation":float(s.std(ddof=1)) if len(a)>1 else 0.0,"Sample variance":float(s.var(ddof=1)) if len(a)>1 else 0.0}
