import streamlit as st

st.title("About the Model")

image_url = "https://espresso-works.com/cdn/shop/articles/espresso-works-blog-coffee-101-robusta-coffee-1_1081x.jpg?v=1681280369"

# Text to display
text = "Much of the coffee grown in the Philippines (about 85%) is the lower quality Robusta that is largely used to produce instant coffee."

# Create a container
container = st.beta_container()

# Display text in the container
container.write(text)

# Display image to the right of the text
container.image(image_url, caption="Robusta Coffee Beans", use_column_width=True)