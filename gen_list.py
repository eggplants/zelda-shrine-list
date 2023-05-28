#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import itertools


# In[2]:


URL = "https://game8.jp/zelda-totk/526438"


# In[3]:


df_tables = pandas.read_html(URL)


# In[4]:


table_idxs = (5, 7, 8, 9, 10, 11, 12, 13, 14, 15)
area_names = ("始まりの空島",) + tuple(
    itertools.chain.from_iterable([r for r in df_tables[6].values])
)[:-1] + ("空島",)
assert len(table_idxs) == len(area_names)


# In[5]:


shrine_dic: dict[str, str] = {}
for table_idx, area_name in zip(table_idxs, area_names, strict=True):
    shrine_dic[area_name] = [n for n in df_tables[table_idx]["祠/試練名"]]
shrine_count = sum(map(len, shrine_dic.values()))


# In[6]:


md_f = open("zelda_shrine_list.md", "w")

md_f.write("# ゼルダ ティアキン 祠一覧\n\n")
md_f.write(f"全 {shrine_count} 箇所\n\n")

for area_name, shrine_names in shrine_dic.items():
    md_f.write(f"## {area_name}\n\n")
    md_f.write(f"全 {len(shrine_names)} 箇所\n\n")

    for shrine_name in shrine_names:
        md_f.write(f"- [ ] {shrine_name}\n")
    md_f.write(f"\n---\n\n")

md_f.write(f"引用: <{URL}>\n")

md_f.close()

