from src.euler_method import chemical_kinetics_one
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Reaction Kinetics Lab')
st.subheader('Explore the reaction kinetics using the explicit Euler method.')

col1, col2 = st.columns(2)
with col1:
    st.subheader("Initial conditions")
    a0 = st.number_input("Concentration A", min_value=0.0, value=1.0)
    b0 = st.number_input("Concentration B", min_value=0.0, value=1.0)
    x0 = st.number_input("Concentration X", min_value=0.0, value=0.0)

with col2:
    st.subheader("Simulation settings")
    k = st.number_input("Rate constant k", min_value=0.0, value=0.5)
    tf = st.number_input("Final time (s)", min_value=0.01, value=10.0)
    dt = st.number_input("Time step (s)", min_value=0.001, value=0.1)



if st.button("Run simulation"):
    results = chemical_kinetics_one(a0, b0, x0, k, tf, dt)

    t = results[:,0]
    x = results[:,1]
    a = results[:,2]
    b = results[:,3]

    df_A = pd.DataFrame({'Time':t, 'Concentration': a, 'Component': 'A'})
    df_B = pd.DataFrame({'Time':t, 'Concentration': b, 'Component': 'B'})
    df_C = pd.DataFrame({'Time':t, 'Concentration': x, 'Component': 'X'})

    df_animation = pd.concat([df_A, df_B, df_C], ignore_index = True)

    frames = []
    for time_instant in t:
        df_temp = df_animation[df_animation['Time'] <= time_instant].copy()
        df_temp['Time_Frame'] = round(time_instant,2)
        frames.append(df_temp)

    df_final = pd.concat(frames, ignore_index=True)

    fig = px.line(
        df_final,
        x="Time",
        y="Concentration",
        color="Component",
        animation_frame="Time_Frame", 
        color_discrete_map={
        "A": "#3498DB",
        "B": "#E74C3C",
        "X": "#2ECC71",
        }, 
        title="Concentrations Time Evolution",
        range_x=[t.min(), t.max()],                   
        range_y=[0, results[:,1:].max() * 1.1],
        template="plotly_dark",            
    )

    
    fig.update_layout(
        transition={"duration": 100},
        )



    fig.show()
    

#     fig = go.Figure(
#         data=[
#             go.Scatter(x=t[:1], y=a[:1], name="A", mode="lines"),
#             go.Scatter(x=t[:1], y=b[:1], name="B", mode="lines"),
#             go.Scatter(x=t[:1], y=x[:1], name="C", mode="lines"),
#         ],
#         frames=[
#             go.Frame(
#             data=[
#                 go.Scatter(x=t[:1], y=a[:1]),
#                 go.Scatter(x=t[:1], y=b[:1]),
#                 go.Scatter(x=t[:1], y=x[:1]),
#             ],
#             name=str(i)
#         )
#         for i in range(1, len(t)+1, max(1, len(t)//100))
#     ],

#     )
#     fig.update_layout(
#         title="Concentration vs. Time",
#         xaxis_title="Time (s)",
#         yaxis_title="Concentration (mol/L)",
#         updatemenus=[{
#             "type": "buttons",
#             "buttons"=[dict(label="Play",
#                           method="animate",
#                           args=[None])])]
#     st.plotly_chart(fig, use_container_width=True)
# #    df = pd.DataFrame(
# #        results[:, 1:],
# #        columns = ["X", "A", "B"],
# #        index = results[:, 0]
# #    )

# #    st.line_chart(df)

# #simulation_time = st.number_input("Add the simulation time in seconds")
# #st.write("the simulation time is ", simulation_time)