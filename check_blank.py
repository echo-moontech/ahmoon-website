# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the products section
idx = content.find('class="products"')
if idx == -1:
    idx = content.find('id="products"')
print(f"Products section starts at index {idx}")

# Find products-grid
idx2 = content.find('<div class="products-grid"')
print(f"Products-grid at index {idx2}")

# Show the section structure around the grid
section = content[idx2:idx2+6000]

# Show cat-section and cat-anchor structure in order
for m in re.finditer(r'(cat-section[^>]*>|cat-anchor[^>]*>|product-card)', section):
    tag = m.group()
    if 'cat-section' in tag or 'cat-anchor' in tag:
        print(f"  [{m.start():6d}] {tag[:100]}")
    elif 'product-card' in tag:
        print(f"  [{m.start():6d}]  <-- product-card")

print("\n=== Full cat-section headers ===")
for m in re.finditer(r'<div class="cat-section-header">.*?</div>\s*</div>', section, re.DOTALL):
    text = m.group()[:200]
    print(text)
    print("---")
