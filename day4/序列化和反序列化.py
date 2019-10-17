# Author:haha

import json
data={'a':1,'b':2}
j_str=json.dumps(data)
print(j_str)
j_json=json.loads(j_str)
print(j_json['a'])

with open('./test.txt','w') as f:
    json.dump(data,f)
with open('./test.txt','r') as f1:
    data_j=json.load(f1)
print(data_j['b'])


import pickle
data={'a':1,'b':2}
p_str=pickle.dumps(data)
print(p_str)
p_json=pickle.loads(p_str)
print(p_json['a'])

with open('./test.txt','wb') as f:
    pickle.dump(data,f)
with open('./test.txt','rb') as f1:
    data_j=pickle.load(f1)
print(data_j['b'])