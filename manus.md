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

here is an example: a photon of incorrect energy 5.00 eV a violet color, flies into the electron. Nothing happens. A photon with 2 eV then flies into the electron and excites the electron. After some random time, the electron deexcites and sends out a 2 eV photon in a random direction.
<img src="./03_correct_color_interact/correct_color_int/correct_color_int.gif"/>

Did you have have these self glowing stars as a kid? How did it work?

<img src="stars.jpg"/>

The atoms in the plastic have been shined upon by white light before dark - off course white light have all visible colors. Some green light then got absorbed by the atom via stimulated emission. The excited state for this specific atom have a very long life-time, and the electron undergoes spontaneous emission hours later at night! This processes is called fluorescence.

<img src="./03_correct_color_interact/correct_color_int_long_half_life/correct_color_int_long_half_life.gif"/>


It turns out there is one more type of interaction between light and atoms: the **Stimulated emission**. This interaction happens when an excited electron, interacts with a photon of the same excitation energy. In the example below the electron is excited to a 2.00 eV sate. A 2.00 eV photons interacts with the electron. The interaction deexcites the electron and sends out another 2.00 eV photon.

<img src="./04_stim_em/stim_em/stim_em.gif"/>

The new photon generated from the interaction have some very important features: It has an identical phase, frequency, polarization, and direction to the photon that interacted with the electron.

Because the frequency is the same, the color or energy is the same for the two photon as well, the two photons are called monochromatic. the identical phase is called coherence.

**L. A. S. E. R** stands for Light amplification by *stimulated emission* of radiation. So lasers works by exploiting that interaction. Let me show you how.

But first, I'll need to show many atoms later so let me simplify and resize the representation of the atom and the photon.  I'll show the photon as a small arrow and the atom is a grey circle. The atom is red when it has an excited electron in the 2.00 eV state.

<img src="./06_penergy_system0/interact_example/interact_example.gif"/>

Off course we can also represent stimulated emission with the new representation

<img src="./06_penergy_system0/stim_em2/stim_em2.gif"/>

### Optical Cavity

the exploit the stimulated emission processes, let's make an optical cavity. It's a cylinder, with mirrors on the sides. When photons hit the mirrors they will change direction, but when they hit the other wall they will fly out of the system - I will just remove them from our drawing. Inside the cavity there will be what's called a "gain medium". It's some material that can do this stimulated emission for us - real world example could be a synthetic ruby crystal or Helium Neon gas.

The optical cavity will also have a optical pump - actually all around the optical cavity but I'll just draw it on the top. The pump is just a very strong flashing light source.

<img src="./07_cavity/cavity/cavity.gif"/>

 The pump can be tuned to send out the energy in the 2.00 eV red range - the energy needed to excite our atoms.

<img src="./07_cavity/cavity_abs_flash/cavity_abs_flash.gif"/>
That looks way too confusing..  So let's make a rule: Instead of drawing photons everywhere, since the radiation pressure from the pump is strong, each time the pump flashes, all atoms have a 50% chance of getting hit by a photon.  I'll put a few atoms in the cavity to show you. The pump flashes once, exciting all the atoms with 50% chance in the cavity. The atoms will then randomly spontaneously deexcite and send out a 2.00 eV photon.

<img src="./07_cavity/cavity_abs/cavity_abs.gif"/>

We are almost ready to produce a laser. Obviously there should be many more atoms in the cavity, to work as a gain medium. This is the idea of producing laser light is:

1. We will continuously excite the atoms with the pump.
2. Wait for one of the atoms to send out a photon parallel to the mirrors.
3.  Then the photon will bounce around and create more photons by stimulated emission.

Let me show you the idea, by placing a photon parallel to the mirrors and excite some atoms with the pump:

<img src="./07_cavity/cavity_gain_example/cavity_gain_example.gif"/>

Did you see, at one instance the photon got amplified to 3 photons? But it quickly got absorbed because the atoms wasn't excited.

So let's flash with the pump continuously to excite the atoms, it seems like we fixed the problem **but** we intrude a new problem: atoms that are still excited when the pump flashes again, will undergo stimulated emission with light from the pump. The photon from the pump comes from a random direction - so sadly the atoms will release two photons in a random direction - not something we want.

<img src="./07_cavity/cavity_gain_example_flash/cavity_gain_example_flash.gif"/>

we don't want that! *Instead we want the atoms to stay excited and wait for a parallel photon to interact with.*
So there is actually a huge problem with our setup. Can you see what it is? Let's me put in some more atoms and see what happens when we keep flashing:

<img src="./08_cavity_flash/cavity_flash/cavity_flash.gif"/>

It looks quite confusing, but what I want to show is: no matter what we do, we can't have more than 50% of the atoms in our cavity excited. Because say we are at a point in time where 50% are excited, when the pump flashes it will simply invert the atoms: all the atoms that weren't excited will absorb a photon. And all atoms that was excited will be hit with the pump causing stimulated emission and the atom will end up in the unexcited state. Here is the same animation with a plot of the percentage of atoms excited


<img src="./08_cavity_flash/cavity_flash_plot/cavity_flash_plot.gif"/>

So we are guaranteed no matter what we do, the atoms in the cavity will always be under 50% excited. It's a problem because then the photons when interacting with an atom will have over 50% chance of getting absorbed, and under 50% chance of getting amplified by stimulated emission, and so this system actually absorbs the photons instead of amplifying them. So what can we do? 

### 3 level atom
Well the fix is actually simple! We find an atom with 3 energy system available:
<img src="./09_atom_reveal_3/atom/atom.gif"/>

This atom has a higher energy state available, and could for example absorb the 5.00 eV UV-photon, if the energy difference between state 1 and state 3 is 5.00 eV.

<img src="./09_atom_reveal_3/correct_color_int/correct_color_int.gif"/>

The example showed the atom absorbed a uv light, going from state 1->3. then release a blue photon from state 3->2. and again this red light from state 2->1 as we have seen before. This process is called a photoluminescence, which you might know from UV parties.

<img src="uv.jpg">

The room is actually lighten up with UV rays, but our eyes can't see that frequency so the room appear dark. But if we have a 3-level atom material that will absorb the uv light at state 3, then spontaneously emit to level 2 and then 1. In our example, The 5.00 eV photon got absorbed, then released a 3.00 eV blue photon and then a 2.00 eV red photon. 3.00 eV and 2.00 eV is visible for our eyes, but 5.00 eV is not!

Another thing that we need for our atom to work as a laser gain material is it needs to have a "meta stable state". which is a state, where the atom can't deexcite without any interference. The reason has to do with quantum mechanics, so let's just take it as a fact. We will need an atom that can spontaneously emit from state 3->2, but the state 2 is a meta stable state. So once the electron is in state 2 it can't fall down to state 1 by it self. This is called forbidden by the section rules, if you want to learn more.

<img src="./09_atom_reveal_3/meta_stable/meta_stable.gif"/>

Furthermore, a good atom for a gain medium should have a short life-time in state 3 such that it will quickly de-excite to state 2.



Alright let's use the other representation again for the atom. This is what can happen, shown with the smaller represents:
- Absorption 1 -> 2
- Absorption 2 -> 3
- Absorption 1 -> 3
- Stimulated emission 2 -> 1
- Stimulated emission 3 -> 2
- Stimulated emission 3 -> 1
- spontaneously emssion 3 -> 2
- spontaneously emssion 2 -> 1
