import streamlit as st

st.set_page_config(
    page_title="Proactive Financial Planning for Lung Cancer Patients through Machine Learning-based Cost Prediction",
    page_icon="👋",
)

st.title("Home Page")
st.image("app/artifactory/Home.png", caption='', use_column_width=True)

st.header("The Problem")
st.write("""Bangladesh is highly susceptible to flooding due to its unique geography and monsoon climate. Flooding leads to significant socio-economic and environmental consequences, causing the loss of lives, displacing communities, damaging infrastructure, and disrupting livelihoods. According to historical data from the Bangladesh Water Development Board (BWDB) and the Department of Disaster Management, flooding occurs annually during the monsoon season, affecting millions of people and causing substantial economic losses.

Current Year Statistics:

In the most recent year, the Department of Disaster Management and the Bangladesh Water Development Board (BWDB) reported alarming flood statistics that underscore the urgency of proactive flood management strategies. The monsoon season, which occurs annually, has once again brought a wave of floods that have profoundly impacted the nation:

Flood-Affected Population: During this year’s monsoon season, millions of residents have been affected by flooding, often being forced to evacuate their homes and seek temporary shelter. The flooding has disrupted the lives of families and communities across Bangladesh’s vast landscape.

Economic Losses: The economic toll of these floods is staggering. Essential infrastructure, including roads, bridges, and agricultural fields, has been inundated, resulting in significant damage and disruption. Preliminary estimates indicate substantial economic losses, further straining an already challenged economy.

Humanitarian Consequences: The floods have tragically led to the loss of lives, emphasizing the immediate need for accurate and timely flood prediction systems. Additionally, health and sanitation conditions have deteriorated in flood-affected areas, increasing the risk of waterborne diseases and other health-related challenges.

The recurring nature of these flood events underscores the necessity for innovative and data-driven solutions that can enhance flood prediction accuracy, mitigate risks, and support disaster response efforts. This project seeks to harness the power of timeseries rainfall data and Geographic Information System (GIS) insights to develop a robust flood prediction and waterbody forecasting model, enabling proactive measures to safeguard lives, protect assets, and bolster the nation’s resilience in the face of this ongoing challenge.""")

st.header("Want to know more?")
st.markdown("* [https://omdena.com/chapter-challenges/floodguard-integrating-rainfall-time-series-and-gis-data-for-flood-prediction-and-waterbody-forecasting-in-bangladesh/)")

st.sidebar.success("Select a page above.")