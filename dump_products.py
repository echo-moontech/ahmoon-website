# -*- coding: utf-8 -*-
import re
with open('index.html','r',encoding='utf-8') as f:
    c=f.read()
i=c.find('')
i=c.find('class="products"')
if i<0: i=c.find('id="products"')
print('Products section at:', i)
print(c[i:i+10000])
