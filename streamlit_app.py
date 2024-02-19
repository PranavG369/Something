import streamlit as st
from PIL import Image
import random


class Particle:
    def __init__(self, name, charge, mass, symbol, description, image_path, animation_path, discoverer, uses):
        self.name = name
        self.charge = charge
        self.mass = mass
        self.symbol = symbol
        self.description = description
        self.image_path = image_path
        self.animation_path = animation_path
        self.discoverer = discoverer
        self.uses = uses

# List of Particle objects
particles = [
    Particle(
        name="Electron",
        charge="-1",
        mass="9.109 × 10^-31 kg",
        symbol="e⁻",
        description="A subatomic particle with a negative elementary electric charge.",
        image_path="electron.jpg",
        animation_path="electrong.gif",
        discoverer="J.J. Thomson",
        uses="Used in electronics, cathode ray tubes, and various imaging techniques."
    ),
    Particle(
        name="Proton",
        charge="+1",
        mass="1.672 × 10^-27 kg",
        symbol="p⁺",
        description="A subatomic particle with a positive elementary electric charge, found in the nucleus of an atom.",
        image_path="proton.jpg",
        animation_path="protong.gif",
        discoverer="Ernest Rutherford",
        uses="Used in particle physics experiments, proton therapy for cancer treatment, and various industrial processes."
    ),
    Particle(
        name="Muon",
        charge="-1",
        mass="1.883 × 10^-28 kg",
        symbol="μ⁻",
        description="A subatomic particle similar to the electron but with a greater mass.",
        image_path="muon.jpg",
        animation_path="muong.gif",
        discoverer="Carl D. Anderson",
        uses="Used in particle physics research, cosmic ray studies, and muon tomography for imaging applications."
    ),
    Particle(
        name="Neutron",
        charge="0",
        mass="1.675 × 10^-27 kg",
        symbol="n",
        description="A subatomic particle with no net electric charge, found in the nucleus of an atom.",
        image_path="neutrong.jpg",
        animation_path="neutron.gif",
        discoverer="James Chadwick",
        uses="Used in nuclear reactors, neutron scattering experiments, and neutron radiography for materials testing."
    ),
    Particle(
        name="Photon",
        charge="0",
        mass="0",
        symbol="γ",
        description="A quantum of electromagnetic radiation, visible light, or X-rays.",
        image_path="photons.jpg",
        animation_path="photon.gif",
        discoverer="Albert Einstein",
        uses="Used in various imaging techniques, telecommunications, and photovoltaic cells for solar energy conversion."
    ),
    Particle(
        name="Neutrino",
        charge="0",
        mass="Very small (less than 1 eV/c²)",
        symbol="ν",
        description="An electrically neutral subatomic particle.",
        image_path="neutrino.jpg",
        animation_path="neutrinog.gif",
        discoverer="Wolfgang Pauli",
        uses="Used in neutrino detectors for astrophysics research, neutrino oscillation experiments, and as a probe for studying the early universe."
    ),
    Particle(
        name="Kaon",
        charge="0",
        mass="Unknown",
        symbol="K",
        description="A hypothetical particle proposed by Japanese physicist Shoichi Sakata in 1956.",
        image_path="kaon.jpg",
        animation_path="kaong.gif",
        discoverer="Shoichi Sakata",
        uses="The existence of Kuon would explain certain aspects of particle decay processes, but it has not been observed experimentally."
    ),
    Particle(
        name="Pion",
        charge="±1",
        mass="Unknown",
        symbol="π",
        description="A type of meson, composed of a quark and an antiquark, that mediates the strong nuclear force.",
        image_path="pion.jpg",
        animation_path="piong.gif",
        discoverer="Cecil Powell",
        uses="Studied in particle physics to understand the strong interaction between nucleons and the structure of atomic nuclei."
    ),
    Particle(
        name="Fermion",
        charge="Varies",
        mass="Varies",
        symbol="f",
        description="A particle that follows Fermi-Dirac statistics and obeys the Pauli exclusion principle.",
        image_path="fermion.jpg",
        animation_path="fermion.gif",
        discoverer="Enrico Fermi and Paul Dirac",
        uses="Fundamental building blocks of matter and play a central role in the structure of atoms and molecules."
    ),
    Particle(
        name="Quark",
        charge="Varies (1/3 or 2/3 of electron charge)",
        mass="Varies",
        symbol="q",
        description="Elementary particles that combine to form composite particles called hadrons, such as protons and neutrons.",
        image_path="quarks.png",
        animation_path="quark.gif",
        discoverer="Murray Gell-Mann and George Zweig",
        uses="Studied in particle physics to understand the strong force and the structure of matter at the smallest scales."
    ),
    Particle(
        name="Gluon",
        charge="0",
        mass="0",
        symbol="g",
        description="An elementary particle that mediates the strong force between quarks, binding them together to form hadrons.",
        image_path="gluon.jpg",
        animation_path="gluong.gif",
        discoverer="David J. Gross, Frank Wilczek, and Hugh David Politzer",
        uses="Responsible for the confinement of quarks within hadrons and the behavior of the strong nuclear force."
    ),
    Particle(
        name="W Boson",
        charge="±1",
        mass="80.379 ± 0.012 GeV/c²",
        symbol="W",
        description="An elementary particle that mediates the weak force, responsible for processes such as beta decay.",
        image_path="wboson.jpg",
        animation_path="wbosong.gif",
        discoverer="Carlo Rubbia and Simon van der Meer",
        uses="Studied in particle physics to understand the weak interaction and its role in particle decay processes."
    ),
    Particle(
        name="Z Boson",
        charge="0",
        mass="91.1876 ± 0.0021 GeV/c²",
        symbol="Z",
        description="An electrically neutral elementary particle that mediates the weak force.",
        image_path="zboson.png",
        animation_path="zbosong.gif",
        discoverer="Carlo Rubbia and Simon van der Meer",
        uses="Studied in particle physics to understand the electroweak interaction and the behavior of neutrinos."
    ),
    Particle(
        name="Higgs Boson",
        charge="0",
        mass="125.18 ± 0.16 GeV/c²",
        symbol="H",
        description="An elementary particle that imparts mass to other fundamental particles via the Higgs mechanism.",
        image_path="higgs.jpg",
        animation_path="higgsg.gif",
        discoverer="ATLAS and CMS collaborations",
        uses="The discovery of the Higgs boson confirmed the mechanism responsible for the mass of elementary particles."
    ),
    Particle(
        name="Lambda Baryon",
        charge="0",
        mass="1.115683 ± 0.000006 GeV/c²",
        symbol="Λ",
        description="A type of baryon composed of three quarks: up, down, and strange.",
        image_path="baryon.jpg",
        animation_path="lambda.gif",
        discoverer="G. D. Rochester and C. C. Butler",
        uses="Studied in particle physics to understand the behavior of quarks within baryons and the dynamics of the strong nuclear force."
    ),
    Particle(
        name="Sigma Baryon",
        charge="Varies",
        mass="Varies",
        symbol="Σ",
        description="A type of baryon composed of three quarks: up, down, and strange.",
        image_path="baryon.jpg",
        animation_path="sigma.gif",
        discoverer="O. Chamberlain, E. Segrè, C. Wiegand, and T. Ypsilantis",
        uses="Studied in particle physics to understand the structure of baryons and the behavior of quarks."
    ),
    Particle(
        name="Omega Baryon",
        charge="0",
        mass="1.67245 ± 0.00017 GeV/c²",
        symbol="Ω",
        description="A type of baryon composed of three strange quarks.",
        image_path="omega.jpeg",
        animation_path="omegag.gif",
        discoverer="G. D. Rochester and J. C. Butler",
        uses="Studied in particle physics to explore the properties of quarks and the role of strange quarks in baryon structure."
    )
    # Add more particles here as needed
]


def main():
    st.markdown("<h1 style='text-align: center;'>🔬 ParticlePedia</h1>",
                unsafe_allow_html=True)


    # Option to explore a random particle
    if st.button("Explore Random Particle"):
        selected_particle = random.choice(particles)
        display_particle_details(selected_particle)

    # Dropdown to select a particle
    selected_particle = st.selectbox('Select a particle:', options=[""] + [particle.name for particle in particles])

    if selected_particle:
        particle = next((particle for particle in particles if particle.name == selected_particle), None)
        display_particle_details(particle)

def display_particle_details(particle):
    # Display details of the selected particle in columns
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Particle:** {particle.name}")
        st.info(f"**Charge:** {particle.charge}")
        st.info(f"**Mass:** {particle.mass}")
        st.info(f"**Symbol:** {particle.symbol}")

    with col2:
        st.info(f"**Description:** {particle.description}")
        st.info(f"**Discoverer:** {particle.discoverer}")
        st.info(f"**Uses:** {particle.uses}")

    # Display image of the selected particle
    with col1:
        image = Image.open(particle.image_path)
        st.image(image, caption=f"Image of {particle.name}", use_column_width=True)

    # Display animated GIF of the selected particle
    with col2:
        animation = open(particle.animation_path, 'rb').read()
        st.image(animation, caption=f"Animation of {particle.name}")

# Entry point of the application
if __name__ == '__main__':
    main()
