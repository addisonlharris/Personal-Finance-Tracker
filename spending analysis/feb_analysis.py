import pandas as pd
import plotly.express as px

# Get Feb data
feb_df = pd.read_csv('spending data/febuary_spending.csv')

# Calculate total spending by category
category_spending = feb_df.groupby('Product')['Price'].sum().sort_values(ascending=True)


# Calculate total spending
total_spending = feb_df['Price'].sum()

# Create bar chart
fig = px.bar(
    x=category_spending.values,
    y=category_spending.index,
    orientation='h',
    title='Feb 2024 - Spending by Category',
    labels={'x': 'Total Spending ($)', 'y': 'Category'}
)

# Update layout for better readability
fig.update_layout(
    plot_bgcolor='white',
    showlegend=False,
    height=600,  # Make it taller to accommodate all categories
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis=dict(
        range=[0, total_spending],  # Extend x-axis to total spending
        tickformat='$,.0f'  # Format x-axis ticks as dollars
    )
)

# Add dollar signs and format numbers
fig.update_traces(
    texttemplate='$%{x:.2f}',
    textposition='outside'
)

# Add a vertical line and annotation for total spending
fig.add_vline(
    x=total_spending, 
    line_dash="dash", 
    line_color="red",
    annotation_text=f"Total: ${total_spending:,.2f}",
    annotation_position="top left"
)

fig.show()