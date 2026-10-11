# -*- coding: utf-8 -*-
"""国货美妆品牌健康度分析（2026H1）—— 图表复现脚本
数据：data/beauty_financials_2026h1.csv（A股iFinD实测；港股公开报道口径）
黑猫投诉数据：黑猫投诉官方《2026上半年美妆投诉数据报告》(2026-07-16)
"""
import numpy as np, pandas as pd, matplotlib.pyplot as plt

df = pd.read_csv('data/beauty_financials_2026h1.csv')
fig, axes = plt.subplots(2, 2, figsize=(14, 9))

# 图1 剪刀差
ax = axes[0, 0]; d = df.dropna(subset=['剪刀差pp']); x = np.arange(len(d))
ax.bar(x-0.2, d['营收YoY%'], 0.4, label='营收YoY', color='#9ecae1')
ax.bar(x+0.2, d['销售费用YoY%'], 0.4, label='销售费用YoY', color='#d45087')
ax.axhline(0, color='#333', lw=.8)
ax.set_xticks(x); ax.set_xticklabels(d['公司'], rotation=25, ha='right', fontsize=9)
ax.set_title('剪刀差：营收增速 vs 销售费用增速（2026H1）'); ax.legend(); ax.grid(alpha=.3, axis='y')

# 图2 销售费用率
ax = axes[0, 1]; d2 = df.dropna(subset=['销售费用率26%']).sort_values('销售费用率26%')
colors = ['#d45087' if v > 55 else '#f4a7c3' if v > 48 else '#9ecae1' for v in d2['销售费用率26%']]
ax.barh(d2['公司'], d2['销售费用率26%'], color=colors)
for i, v in enumerate(d2['销售费用率26%']): ax.text(v+0.5, i, f'{v}%', va='center', fontsize=9)
ax.set_title('销售费用率（2026H1，%）'); ax.grid(alpha=.3, axis='x')

# 图3 黑猫投诉量
ax = axes[1, 0]
brands = ['韩束', '雅诗兰黛', '丝芙兰', '珀莱雅', '巴黎欧莱雅']; cnt = [4574, 306, 230, 207, 182]
bars = ax.bar(brands, cnt, color=['#c92a2a'] + ['#9ecae1']*4)
for b, v in zip(bars, cnt): ax.text(b.get_x()+b.get_width()/2, v+60, str(v), ha='center')
ax.set_title('黑猫投诉2026H1美妆投诉量TOP5（行业约1万件）'); ax.grid(alpha=.3, axis='y')

# 图4 回复率
ax = axes[1, 1]
bars = ax.bar(['珀莱雅', '丝芙兰/欧莱雅/雅诗兰黛', '韩束'], [99.03, 93, 0.17],
              color=['#2b8a3e', '#74c69d', '#c92a2a'])
for b, v in zip(bars, [99.03, 93, 0.17]): ax.text(b.get_x()+b.get_width()/2, v+2, f'{v}%', ha='center')
ax.set_ylim(0, 110); ax.set_title('投诉回复率对比（2026H1）'); ax.grid(alpha=.3, axis='y')

plt.tight_layout(); plt.savefig('figures/beauty_health_2026H1.png', dpi=110)
print('done')
