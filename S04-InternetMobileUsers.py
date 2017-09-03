import cauldron as cd
import plotly.graph_objs as go

# Get data from previous step
epc = cd.shared.epc 

# Display text. 
cd.display.markdown(
    """
    ### Brazil's Internet and Mobile Penetration

    Brazil has the highest Internet and mobile penetration in South America. It does not have the same amount of Internet users that the US had in 2010 (222 million), but it is growing.
    """
)

# Set x and y values for internet users and mobile users
country = go.Bar(x=list(epc['Country']),
                  y=list(epc['Internet Users']),
                  name='Internet Users',
                  marker=dict(color='#ffcdd2'))

internet = go.Bar(x=list(epc['Country']),
                y=list(epc['Mobile Users']),
                name='Mobile Users',
                marker=dict(color='#A2D5F2'))

# Set data value for country and internet. 
data = [country, internet]

# Display data 
cd.display.plotly(
    data, 
    go.Layout(
        title='South America\'s Internet and Mobile Users (2016)'
    )
)


