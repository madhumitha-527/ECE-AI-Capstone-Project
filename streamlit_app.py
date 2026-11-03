import streamlit as st, pandas as pd, json
from pathlib import Path
st.set_page_config(page_title='ECE AI Capstone Explorer',layout='wide')
root=Path(__file__).resolve().parent
folders=sorted(root.glob('Project_*'))
choice=st.selectbox('Choose a capstone project',[f.name for f in folders])
folder=root/choice
cfg=json.loads((folder/'project.json').read_text())
st.title(cfg['title']); st.write(cfg['objective'])
st.info(cfg['dataset_note'])
df=pd.read_csv(folder/'data'/'dataset.csv')
st.subheader('Dataset preview'); st.dataframe(df.head(30),use_container_width=True)
st.subheader('Feature and target details')
st.write('Features:',', '.join(cfg['features'])); st.write('Target:',cfg['target'])
metrics=folder/'results'/'metrics.json'
if metrics.exists(): st.json(json.loads(metrics.read_text()))
else: st.warning('Run python train.py inside this project folder to generate evaluation results.')
