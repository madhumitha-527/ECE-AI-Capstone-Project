
import argparse, json, os
from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (accuracy_score, precision_recall_fscore_support, classification_report,
 mean_absolute_error, mean_squared_error, r2_score, confusion_matrix, ConfusionMatrixDisplay)
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor, ExtraTreesClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import joblib
ROOT=Path(__file__).resolve().parent
CFG=json.loads((ROOT/'project.json').read_text())
def model_for(name, task):
    if name=='Random Forest': return RandomForestClassifier(n_estimators=250,random_state=42,class_weight='balanced') if task=='classification' else RandomForestRegressor(n_estimators=250,random_state=42)
    if name=='Gradient Boosting': return GradientBoostingClassifier(random_state=42) if task=='classification' else GradientBoostingRegressor(random_state=42)
    if name=='Extra Trees': return ExtraTreesClassifier(n_estimators=250,random_state=42,class_weight='balanced')
    if name=='Decision Tree': return DecisionTreeClassifier(max_depth=8,random_state=42,class_weight='balanced')
    if name=='SVM': return make_pipeline(StandardScaler(),SVC(C=2,kernel='rbf',class_weight='balanced'))
    if name=='Logistic Regression': return make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000,class_weight='balanced'))
    return LinearRegression()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rows',type=int,default=1600); ap.add_argument('--seed',type=int,default=42); args=ap.parse_args()
    df=pd.read_csv(ROOT/'data'/'dataset.csv')
    target=CFG['target']; X=df.drop(columns=[target]); y=df[target]
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=args.seed,stratify=y if CFG['task']=='classification' else None)
    results={}; best=None; bestscore=-1e99
    for name in CFG['models']:
        m=model_for(name,CFG['task']); m.fit(Xtr,ytr); pred=m.predict(Xte)
        if CFG['task']=='classification':
            score=accuracy_score(yte,pred); results[name]={'accuracy':score,'weighted_precision':precision_recall_fscore_support(yte,pred,average='weighted',zero_division=0)[0],'weighted_recall':precision_recall_fscore_support(yte,pred,average='weighted',zero_division=0)[1],'weighted_f1':precision_recall_fscore_support(yte,pred,average='weighted',zero_division=0)[2]}
        else:
            rmse=mean_squared_error(yte,pred)**.5; score=-rmse; results[name]={'MAE':mean_absolute_error(yte,pred),'RMSE':rmse,'R2':r2_score(yte,pred)}
        if score>bestscore: bestscore=score; best=(name,m,pred)
    name,m,pred=best; joblib.dump(m,ROOT/'models'/'best_model.joblib')
    (ROOT/'results'/'metrics.json').write_text(json.dumps({'selected_model':name,'metrics':results},indent=2))
    if CFG['task']=='classification':
        labels=sorted(pd.Series(yte).unique()); cm=confusion_matrix(yte,pred,labels=labels)
        ConfusionMatrixDisplay(cm,display_labels=labels).plot(xticks_rotation=30); plt.tight_layout(); plt.savefig(ROOT/'results'/'confusion_matrix.png',dpi=150); plt.close()
        (ROOT/'results'/'classification_report.txt').write_text(classification_report(yte,pred,zero_division=0))
    else:
        plt.figure(figsize=(7,5)); plt.scatter(yte,pred,s=12,alpha=.5); lo=min(yte.min(),pred.min()); hi=max(yte.max(),pred.max()); plt.plot([lo,hi],[lo,hi]); plt.xlabel('Actual'); plt.ylabel('Predicted'); plt.title(CFG['title']+' — Actual vs Predicted'); plt.tight_layout(); plt.savefig(ROOT/'results'/'actual_vs_predicted.png',dpi=150); plt.close()
    print(json.dumps({'project':CFG['title'],'selected_model':name,'metrics':results[name]},indent=2))
if __name__=='__main__': main()
