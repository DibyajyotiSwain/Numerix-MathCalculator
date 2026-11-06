import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
def fit(x,y):
    X=np.asarray(x,dtype=float).reshape(-1,1); Y=np.asarray(y,dtype=float)
    if len(X)!=len(Y) or len(X)<2: raise ValueError("Provide at least two paired observations")
    if not np.isfinite(X).all() or not np.isfinite(Y).all(): raise ValueError("Values must be finite")
    m=LinearRegression().fit(X,Y); p=m.predict(X)
    return {"slope":float(m.coef_[0]),"intercept":float(m.intercept_),"r2":float(r2_score(Y,p)),"rmse":float(np.sqrt(mean_squared_error(Y,p))),"x":X.ravel(),"y":Y,"predictions":p}
