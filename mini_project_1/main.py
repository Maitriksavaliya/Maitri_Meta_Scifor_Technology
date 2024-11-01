# importing necessary library
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime,timedelta
from matrix_calculator import calculation_matrix
from visualization import visual_graph


# streamlit dashboard app
class StockDashboardApp:
    def __init__(self):
        self.calc=calculation_matrix()
        self.visuals = visual_graph()

    def run(self):
        st.set_page_config(page_title="Stock Dashboard", layout="wide")

        st.sidebar.markdown("# Stock Dashboard")

        popular_ticker = ["AAPL", "GOOGL", "MSFT", "META", "NVDA"]
        new_ticker = st.sidebar.text_input("Input a new ticker:")
        if new_ticker:
            popular_ticker.append(new_ticker.upper())
            st.sidebar.success(f"Added {new_ticker.upper()} to the list")
        ticker = st.sidebar.selectbox("Select a ticker/tickers for comparision:", popular_ticker,index=0)

        st.title(f"{ticker}")

        period= ["1d","5d","1mo", "3mo", "6mo", "1y", "2y", "5y", "YTD", "max"]
        selected_time_range = st.sidebar.selectbox("Select period:", period, index=2)

        show_line_chart=st.sidebar.checkbox("line chart",value=True)
        show_area_chart=st.sidebar.checkbox("area chart",value=True)
        show_summary = st.sidebar.checkbox("Summary", value=True)
        show_moving_averages = st.sidebar.checkbox("Moving Averages", value=False)
        show_bollinger_bands = st.sidebar.checkbox("Bollinger Bands", value=False)
        show_rsi = st.sidebar.checkbox("Relative Strength Index (RSI)", value=False)
        show_macd = st.sidebar.checkbox("Moving Average Convergence Divergence (MACD)", value=False)
        show_atr = st.sidebar.checkbox("Average True Range (ATR)", value=False)
        show_comparision=st.sidebar.checkbox("compare stocks",value=False)

        # Load data from Yahoo Finance
        data = yf.download(ticker, period=selected_time_range)

        if data.empty:
            st.error("No data found for the selected ticker and time period.")
            return 

        # load data for comparing two ticker
        if show_comparision:
            comp_ticker=st.sidebar.multiselect("select tickers to compare:",popular_ticker,default=[ticker,'GOOGL'])
            if len(comp_ticker)>0:
                cdata=yf.download(comp_ticker,period=selected_time_range)
        
        # plot line chart for the ticker/comparision ticker
        if show_line_chart:
            if show_comparision:
                st.subheader(f'line chart for{comp_ticker}')
                st.line_chart(cdata['Adj Close'])
            else:
                st.subheader(f"{ticker} line chart") 
                st.line_chart(data['Adj Close'])

        # plot area chart for the ticker
        if show_area_chart:
            st.subheader(f'{ticker} area chart')
            st.area_chart(data['Adj Close'])


        # calc and Plot Moving Averages
        if show_moving_averages:
            data=self.calc.moving_averages(data)
            ma_fig = self.visuals.plot_moving_averages(data)
            st.plotly_chart(ma_fig)

        # calc and Plot Bollinger Bands
        if show_bollinger_bands:
            data = self.calc.bollinger_bands(data)
            bb_fig = self.visuals.plot_bollinger_bands(data)
            st.plotly_chart(bb_fig)

        # calc and Plot RSI
        if show_rsi:
            data = self.calc.rsi(data)
            rsi_fig = self.visuals.plot_rsi(data)
            st.plotly_chart(rsi_fig)

        # calc and Plot MACD
        if show_macd:
            data = self.calc.macd(data)
            macd_fig = self.visuals.plot_macd(data)
            st.plotly_chart(macd_fig)

        # calc and Plot ATR
        if show_atr:
            data = self.calc.atr(data)
            atr_fig = self.visuals.plot_atr(data)
            st.plotly_chart(atr_fig)
            
        # Summary data
        if show_summary:
            if show_comparision:
                st.subheader("Summary - comparision_ticker")
                st.write(cdata.describe())
            else:
                st.subheader("Summary - main Ticker")
                st.write(data.describe())
        
        # download data as CSV
        st.sidebar.markdown(f"### Download {ticker} Data")
        csv = data.to_csv()
        st.sidebar.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"{ticker}_data.csv",
            mime="text/csv"
        )


if __name__ == "__main__":
    app = StockDashboardApp()
    app.run()

