import json
from datetime import datetime

import pandas as pd
import streamlit as st
from kafka import KafkaConsumer
from streamlit_autorefresh import st_autorefresh

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SmartCityX - Live Urban Operations Dashboard",
    page_icon="🚦",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("🚦 SmartCityX – Live Urban Operations Dashboard")
st.caption(
    "Real-time monitoring powered by Kafka • PostgreSQL • Apache Kafka • Streamlit"
)

st_autorefresh(interval=2000, key="refresh")

# =====================================================
# SESSION STATE
# =====================================================

if "consumer" not in st.session_state:

    st.session_state.consumer = KafkaConsumer(
        "traffic_topic",
        "transport_topic",
        "rides_topic",
        "parking_topic",
        "emergency_topic",
        "pollution_topic",

        bootstrap_servers="localhost:9092",

        value_deserializer=lambda m: json.loads(
            m.decode("utf-8")
        ),

        auto_offset_reset="latest",
        enable_auto_commit=True,
        consumer_timeout_ms=1000
    )

if "latest" not in st.session_state:

    st.session_state.latest = {

        "traffic_topic": None,
        "transport_topic": None,
        "rides_topic": None,
        "parking_topic": None,
        "emergency_topic": None,
        "pollution_topic": None

    }

if "event_count" not in st.session_state:
    st.session_state.event_count = 0

consumer = st.session_state.consumer

# =====================================================
# READ KAFKA EVENTS
# =====================================================

for _ in range(100):

    packs = consumer.poll(timeout_ms=50)

    if not packs:
        break

    for _, msgs in packs.items():

        for msg in msgs:

            st.session_state.latest[msg.topic] = msg.value

            st.session_state.event_count += 1

latest = st.session_state.latest

# =====================================================
# TOP STATUS BAR
# =====================================================

now = datetime.now()

status_col, update_col, event_col, time_col = st.columns(4)

with status_col:
    st.metric(
        "🟢 Live Status",
        "ACTIVE"
    )

with update_col:
    st.metric(
        "🕒 Last Updated",
        now.strftime("%I:%M:%S %p")
    )

with event_col:
    st.metric(
        "📊 Total Events",
        st.session_state.event_count
    )

with time_col:
    st.metric(
        "📅 Date",
        now.strftime("%d %b %Y")
    )

st.divider()

# =====================================================
# PANEL FUNCTION
# =====================================================

def panel(title, topic):

    st.subheader(title)

    if latest[topic]:

        df = pd.DataFrame(

            latest[topic].items(),

            columns=[
                "Field",
                "Value"
            ]

        )

        st.table(df)

        alert = latest[topic].get("alert")

        if alert:

            text = alert.lower()

            if (
                "critical" in text
                or
                "accident" in text
            ):

                st.error(f"🔴 {alert}")

            elif (
                "warning" in text
                or
                "congestion" in text
                or
                "delay" in text
            ):

                st.warning(f"🟠 {alert}")

            else:

                st.info(f"🔵 {alert}")

        else:

            st.success("🟢 Normal")

    else:

        st.info(
            f"Waiting for {title} data..."
        )

# =====================================================
# DASHBOARD
# =====================================================

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    panel(
        "🚦 Traffic Monitoring",
        "traffic_topic"
    )

with row1_col2:
    panel(
        "🚌 Public Transport",
        "transport_topic"
    )

st.divider()

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    panel(
        "🚖 Ride Services",
        "rides_topic"
    )

with row2_col2:
    panel(
        "🅿 Parking Management",
        "parking_topic"
    )

st.divider()

row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    panel(
        "🚑 Emergency Response",
        "emergency_topic"
    )

with row3_col2:
    panel(
        "🌍 Environmental Monitoring",
        "pollution_topic"
    )

st.divider()

# =====================================================
# FOOTER STATUS
# =====================================================

st.success("🔄 Dashboard auto-refreshes every 2 seconds")

st.markdown("---")

footer_left, footer_center, footer_right = st.columns([2, 3, 2])

with footer_left:
    st.markdown("### 📡 Data Pipeline")
    st.write("CSV Datasets")
    st.write("PostgreSQL Warehouse")
    st.write("Apache Kafka")

with footer_center:
    st.markdown("### 🛠 Technologies")
    st.write(
        "Python • PostgreSQL • Apache Kafka • "
        "Apache Airflow • Streamlit • Power BI • Docker"
    )

with footer_right:
    st.markdown("### 🚀 Project")
    st.write("SmartCityX")
    st.write("Urban Mobility &")
    st.write("Public Operations Intelligence")

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;
                color:gray;
                font-size:15px;'>
    <b>SmartCityX – Live Urban Operations Intelligence Platform</b><br>
    Developed using Python, PostgreSQL, Apache Kafka, Apache Airflow,
    Streamlit, Docker and Power BI
    </div>
    """,
    unsafe_allow_html=True,
)