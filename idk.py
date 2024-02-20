import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Function to calculate reflection and refraction angles
def calculate_angles(incident_angles, glass_refractive_index):
    if isinstance(incident_angles, (int, float)):
        incident_angles = [incident_angles]
    reflection_angles, refraction_angles = [], []
    for incident_angle in incident_angles:
        if incident_angle <= np.arcsin(1 / glass_refractive_index):
            refraction_angle = np.arcsin(np.sin(incident_angle) / glass_refractive_index)
        else:
            refraction_angle = np.pi / 2 - np.arcsin(np.sin(np.pi / 2 - incident_angle) * glass_refractive_index)
        reflection_angle = np.pi - incident_angle
        reflection_angles.append(reflection_angle)
        refraction_angles.append(refraction_angle)
    return reflection_angles, refraction_angles

# Function to plot 3D light rays
def plot_3d_light_rays(incident_angles, reflection_angles, refraction_angles, incident_color, reflected_color, refracted_color):
    fig = go.Figure()
    for incident_angle, reflection_angle, refraction_angle in zip(incident_angles, reflection_angles, refraction_angles):
        # Incident ray
        fig.add_trace(go.Scatter3d(
            x=[0, np.cos(incident_angle)],
            y=[0, np.sin(incident_angle)],
            z=[0, 0],
            mode='lines',
            name=f'Incident Ray {np.rad2deg(incident_angle):.1f}°',
            line=dict(color=incident_color, width=5),
            hoverinfo='name'
        ))

        # Reflected ray
        fig.add_trace(go.Scatter3d(
            x=[0, -np.cos(reflection_angle)],
            y=[0, np.sin(reflection_angle)],
            z=[0, 0],
            mode='lines',
            name=f'Reflected Ray {np.rad2deg(reflection_angle):.1f}°',
            line=dict(color=reflected_color, width=5),
            hoverinfo='name'
        ))

        # Refracted ray
        fig.add_trace(go.Scatter3d(
            x=[0, np.cos(refraction_angle)],
            y=[0, -np.sin(refraction_angle)],
            z=[0, 0],
            mode='lines',
            name=f'Refracted Ray {np.rad2deg(refraction_angle):.1f}°',
            line=dict(color=refracted_color, width=5),
            hoverinfo='name'
        ))

    fig.update_layout(
        title="Reflection and Refraction of Light",
        scene=dict(
            xaxis=dict(title='x'),
            yaxis=dict(title='y'),
            zaxis=dict(title='z'),
            aspectmode='cube'
        )
    )

    st.plotly_chart(fig)

def main():
    st.title("Optics Simulation")

    # User inputs (in the sidebar)
    with st.sidebar:
        st.subheader("Simulation Parameters")
        incident_angle_deg = st.slider("Incident Angle (degrees)", min_value=0, max_value=90, value=[45], step=1)
        glass_refractive_index = st.slider("Glass Refractive Index", min_value=1.0, max_value=2.0, value=1.5, step=0.1)
        incident_color = st.color_picker("Incident Ray Color", "#1f77b4")
        reflected_color = st.color_picker("Reflected Ray Color", "#ff7f0e")
        refracted_color = st.color_picker("Refracted Ray Color", "#2ca02c")

    # Convert incident angle from degrees to radians
    incident_angles = np.deg2rad(incident_angle_deg)

    # Calculate reflection and refraction angles
    reflection_angles, refraction_angles = calculate_angles(incident_angles, glass_refractive_index)

    # Plot 3D light rays with custom colors and annotations
    plot_3d_light_rays(incident_angles, reflection_angles, refraction_angles, incident_color, reflected_color, refracted_color)

if __name__ == "__main__":
    main()
