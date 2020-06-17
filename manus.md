# The physics of a laser
The laser is one of the most important tools advances in science. I mean, it's one of the most important tools to tease cats.


<img src="https://media1.tenor.com/images/2f0877e3615e63d0bf78a00cdf8d2273/tenor.gif?itemid=3454835"/>

In this video, I'll show you the physics of lasers, and simulate a working laser as well.

Consider helping me create more free physics material, by supporting with whatever you want on Patreon.

### Light and atom interaction
The whole processes of lasing relies on a special mechanic between the atom and the light. So let's examine an atom. For simplicity lets look at an atom with only one electron. And two states shown by the two electron orbitals. The atom as a nucleus as well.

<img src="./00_atom_reveal/atom/atom.gif"/>

Off course the picture of this atom is completely wrong, but it gets the physics right, because the distance here represent energy levels. The picture also get the physics right because the orbits or the circles represents states for the electron. The electron can ONLY exists where there is a state. To switch state the electron will do a quantum jump: that is, teleport to another state. But to teleport requires some energy. One way to get that is if the electron absorbs a photon. That's called **Stimulated Absorption**. Once the electron is then in a excited state, it will fall down after some random time depending on the half life of that state. The processes is called **Spontaneous Emission**, and it releases a photon in a random direction in this processes.
<img src="./01_atom_interaction/interaction/interaction.gif"/>

Any photon that interacts with the electron wont excite it. To excite the electron, to photon have to have the exact same energy as the energy difference between the two states. One example could be a excitation energy of 2.00 electron volts. The energy of a photon is perceived as color in our eyes - and 2.00 eV corresponds to red.
<img src="./02_correct_color/correct_color/correct_color.gif"/>

here is an example: a photon of incorrect energy 4,00 eV a violet color, flies into the electron. Nothing happens. A photon with 2 eV then flies into the electron and excites the electron. After some random time, the electron de-excites and sends out a 2 eV photon in a random direction.
<img src="./03_correct_color_interact/correct_color_int/correct_color_int.gif"/>

It turns out there is one more type of interaction: the **Stimulated emission**. This interaction happens when an excited electron, interacts with a photon of the same excitation energy. In the example below the electron is excited to a 2.00 eV sate. A 2.00 eV photons interacts with the electron. The interaction de-excites the electron and sends out another 2.00 eV photon.

<img src="./04_stim_em/stim_em/stim_em.gif"/>

The new photon generated from the interaction have some very important features: It has an identical phase, frequency, polarization, and direction to the photon that interacted with the electron.

Because the frequency is the same, the color or energy is the same for the two photon as well, the two photons are called monochromatic. the identical phase is called coherence.

**L. A. S. E. R** stands for Light amplification by *stimulated emission* of radiation. So lasers works by exploiting that interaction. Let me show you how.

But first, I am a physicist so I love to boil down to the absolute simplest system we can. And right now the nucleus and the circularize representation of states, doesn't do anything.. So instead of the previous system, let's just look at the two states:

<img src="./06_penergy_system0/Marker/Marker.gif"/>

And draw then on a energy diagram. Our electron can off course again only exists in these two levels. And can interact with a photon just as shown before.

<img src="./06_penergy_system0/main/main.gif"/>

### Optical cavity

Now I want to build an actual laser system. It's just a system that exploits *stimulated emission*. So first, I'll make a box called a optical cavity. I'll put a bunch of 2-level atoms in there as well. Remember, I represent an atom just with the two states an electron can be in.
