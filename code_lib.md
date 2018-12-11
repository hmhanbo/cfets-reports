#### 给图加text
```python
 for x, y in zip(x, net_buy):
     if y >= 0:
         plt.text(x, y+0.1, y, ha='center', va='bottom')
     else:
        plt.text(x, y-0.1, y, ha='center', va='top')
```

```python
axes[0].set_xticklabels(d1.index, rotation=40, fontproperties=font_set)
```