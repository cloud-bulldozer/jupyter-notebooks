#!/usr/bin/env python
# coding: utf-8

# - Install touchstone. get config file and import required modules

# In[55]:


get_ipython().system('pip3 install git+https://github.com/Ayesha279/benchmark-comparison.git@multiRecord_touchstone')
get_ipython().system('curl -LO https://raw.githubusercontent.com/Ayesha279/benchmark-comparison/multiRecord_touchstone/config/ocm-requests.json')
    
from touchstone.benchmarks.generic import Benchmark
from touchstone import decision_maker
from touchstone import databases
from tabulate import tabulate
from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt


# - Set touchstone paramters

# In[84]:


uuid="aeed6306-b7e1-11eb-b313-e86a640406b2"
uuid2="1bf34d07-b3ef-4f57-a612-234c3f2d4ba1"
database="elasticsearch"
es_index = "ocm-requests"
es_url="https://search-perfscale-dev-chmf5l4sh66lvxbnadi4bznl3a.us-west-2.es.amazonaws.com"
benchmark=Benchmark(open("ocm-requests.json"), database)


# - Connect to database - ElasticSearch

# In[77]:


database_instance = databases.grab(database, conn_url = es_url)


# Iterate the indexes from the config file and get timeseries results from each one of them

# In[85]:


document_list = []  
for compute in benchmark.compute_map['ocm-requests'] :
    print("Getting results")
    timeseries_result1 = database_instance.get_timeseries_results(uuid=uuid, 
                                                                 compute_map = compute,
                                                                 index = es_index,
                                                                 identifier="uuid"
                                                                )
    
df = pd.DataFrame(timeseries_result1)

for compute in benchmark.compute_map['ocm-requests'] :
    print("Getting results")
    timeseries_result2 = database_instance.get_timeseries_results(uuid=uuid2, 
                                                                 compute_map = compute,
                                                                 index = es_index,
                                                                 identifier="uuid"
                                                                )
dff = pd.DataFrame(timeseries_result2)


# In[ ]:





# - Plot results

# In[93]:


fig, axs = plt.subplots(2,figsize=(15, 10))
plt.title('Latency comparision')
plt.ylabel('Latency (ns)')
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.groupby(df["timestamp"].dt.second)["latency_ns"].mean().plot(rot=0, ax=axs[0])

plt.ylabel('Latency (nc)')
dff["timestamp"] = pd.to_datetime(dff["timestamp"])
dff.groupby(dff["timestamp"].dt.second)["latency_ns"].mean().plot(rot=0, ax=axs[1])


axs[0].title.set_text('UUID- aeed6306-b7e1-11eb-b313-e86a640406b2')
axs[1].title.set_text('UUID- 1bf34d07-b3ef-4f57-a612-234c3f2d4ba1')
fig.suptitle('Latency comparision', fontsize=16)


# In[118]:



Test1=df["latency_ns"].mean()
Test2=dff['latency_ns'].mean()

plotdata = pd.DataFrame(
    {"Latency_ns": [Test1, Test2]}, 
    index=["Test1", "Test2"])

plotdata.plot(kind="bar")
plt.title('Avrage Latency Comparision')
plt.ylabel('Latency (ns)')


# In[112]:



df["timestamp"] = pd.to_datetime(df["timestamp"])
x1 = df.groupby(df["timestamp"].dt.second)["latency_ns"]
print(x1)


# In[ ]:


fig, ax = plt.subplots(2, figsize=(10, 6))
ax[0].scatter(x = df1['VALUE'], y = df1['Bytes_in'], c = df1['code'], cmap='Spectral')
ax[0].set_xlabel("avrage latency")
ax[0].set_ylabel("Bytes_in")

ax[1].scatter(x = df1['VALUE'], y = df1['Bytes_out'], c = df1['code'], cmap='Spectral')
ax[1].set_xlabel("avrage latency")
ax[1].set_ylabel("Bytes_out")


plt.show()

