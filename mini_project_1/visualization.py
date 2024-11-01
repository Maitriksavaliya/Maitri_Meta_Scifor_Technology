import plotly.graph_objects as go

class visual_graph:

    def plot_moving_averages(self, stock_data):
        ma_fig = go.Figure()
        for window in [50, 200]:
            ma_fig.add_trace(go.Scatter(
                x=stock_data.index,
                y=stock_data[f'SMA_{window}'],
                name=f'SMA {window}',
                mode='lines'
            ))
        ma_fig.update_layout(title="Moving Averages (MA)", xaxis_title="Date", yaxis_title="MA")
        return ma_fig

    def plot_bollinger_bands(self, stock_data):
        bb_fig = go.Figure()
        bb_fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Bollinger High'], fill=None, mode='lines', name='Bollinger High'))
        bb_fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], fill='tonexty', mode='lines', name='Close'))
        bb_fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Bollinger Low'], fill='tonexty', mode='lines', name='Bollinger Low'))
        bb_fig.update_layout(title="Boillinger_Bands(BB)", xaxis_title="Date")
        return bb_fig

    def plot_rsi(self, stock_data):
        rsi_fig = go.Figure()
        rsi_fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['RSI'], name='RSI'))
        rsi_fig.update_layout(title="Relative Strength Index (RSI)", xaxis_title="Date", yaxis_title="RSI")
        return rsi_fig

    def plot_macd(self, stock_data):
        macd_fig = go.Figure()
        macd_fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['MACD'], name='MACD Line'))
        macd_fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Signal_Line'], name='Signal Line'))
        macd_fig.update_layout(title="Moving Average Convergence Divergence (MACD)", xaxis_title="Date", yaxis_title="MACD")
        return macd_fig

    def plot_atr(self, stock_data):
        atr_fig = go.Figure()
        atr_fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['ATR'], name='ATR'))
        atr_fig.update_layout(title="Average True Range (ATR)", xaxis_title="Date", yaxis_title="ATR")
        return atr_fig