"""
Summarise the trading day.
"""

import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

# summarise trading day
# trading message frequency

def nasdaq_summ(message_type_counter):
    counter = pd.Series(message_type_counter).to_frame('# Trades')
    counter['Message Type'] = counter.index.map(message_labels.set_index('message_type').name.to_dict())
    counter = counter[['Message Type', '# Trades']].sort_values('# Trades', ascending=False)
    counter

    with pd.HDFStore(itch_store) as store:
        store.put('summary', counter)
    
    with pd.HDFStore(itch_store) as store:
        stocks = store['R'].loc[:, ['stock_locate', 'stock']]
        trades = store['P'].append(store['Q'].rename(columns={'cross_price': 'price'}), sort=False).merge(stocks)

    trades['value'] = trades.shares.mul(trades.price)
    trades['value_share'] = trades.value.div(trades.value.sum())

    trade_summary = trades.groupby('stock').value_share.sum().sort_values(ascending=False)
    trade_summary.iloc[:50].plot.bar(figsize=(14, 6), color='darkblue', title='Share of Traded Value')

    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    sns.despine()
    plt.tight_layout()
    plt.show() 
