import streamlit as st
import pandas as pd

st.title("About the Model")

image_url = "https://espresso-works.com/cdn/shop/articles/espresso-works-blog-coffee-101-robusta-coffee-1_1081x.jpg?v=1681280369"

# Text to display
text = "Much of the coffee grown in the Philippines (about 85%) is the lower quality **Robusta** that is largely used to produce instant coffee. Robusta plantation are located in Bukidnon, Misamis Oriental, Sultan Kudarat, Bataan, Bohol, Cebu, Compostela Valley and Palawan and various other regions. The Nestle Company buys a large percentage of the harvest. Coffee was first brought to the Philippines by a Franciscan friar in 1749 and grew into a thriving industry. The coffee rust disease decimated crops at the end of the nineteenth century. Toward the end of the era of Spanish colonization the Philippines was a top coffee exporter but the coffee trade languished due to lack of support from the government, urbanization and other factors including previous global declines in coffee prices."

col1, col2 = st.columns([2, 2])

col1.write(text)

# Display image to the right of the text
col2.image(image_url, caption="Robusta Coffee Bean", use_column_width=True)


st.title("Definition of Terms")

data = {
    "Term": ["Rainfall (mm)", "ASurface Pressure (hPa)", "Dewpoint (°C)", "Relative Humidity (%)"],
    "Definition": ["sum of water falling from the atmosphere to the Earth's surface", 
                   "Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation.",
                    "temperature at which air becomes saturated with moisture, leading to condensation",
                    "Is a ratio, expressed in percent, of the amount of atmospheric moisture present relative to the amount that would be present if the air were saturated"],
}

df = pd.DataFrame(data)

# Display the DataFrame as a table
st.table(df)

