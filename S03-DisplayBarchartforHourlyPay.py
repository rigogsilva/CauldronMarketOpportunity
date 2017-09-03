import cauldron as cd
import pandas as pd 
import plotly.graph_objs as go

#get values from shared value epc
mg = cd.shared.mg 

cd.display.markdown(
    """
    ### South America's Internet and Mobile Penetration Growth
    
    You can see below that the Internet and mobile penetration in South America has grown from 280 million to 365 million in 4 years.

    """
)

internet = go.Scatter(x=list(mg['Year']),
                  y=list(mg['Internet Users']),
                  name='Internet Users',
                  marker=dict(color='#A2D5F2'))

mobile = go.Scatter(x=list(mg['Year']),
                    y=list(mg['Mobile Users']),
                    name='Mobile Users',
                    marker=dict(color='#ffcdd2'))

data=[internet, mobile]

cd.display.plotly(
    data, 
    go.Layout(
        title='South America\'s Mobile Growth'
    )
)

