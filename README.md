# MA-202-Project

## Problem Statement

Electromagnetic radiation may be reflected or transmitted by ions or particles in the atmosphere in addition to being absorbed or transmitted. The redirection of electromagnetic radiation by suspended particles (molecules of some substance or on a small particle of matter) in the atmosphere is known as scattering. The nature and amount of scattering that occurs is determined by particle size and energy wavelength. Atmospheric light scattering is the very reason why the atmosphere manifests colour. The sunlight entering the atmosphere is scattered/ absorbed by air molecules and aerosol, and ozone layers. In this problem statement we will consider two types of scattering phenomena that have a major impact on incoming solar radiation, namely Rayleigh scattering (scattering by small particles such as air molecules) and Mie scattering (scattering by aerosols such as dust). Further, we will be calculating the intensity of light after scattering with respect to various factors such as, height from the ground surface, wavelength of incident light and angle of incidence (w.r.t. Earth), using Simpson’s and Trapezoidal model. This study is useful in space travel simulators and in the simulation of earth surveys (comparisons with observations from weather satellites and weather simulations). This project work may be useful for viewing the earth, and the sea floor, from space, taking into account contaminants (air molecules and aerosols) in the atmosphere as well as water molecules in the sea.

## Physical Model

![image](https://user-images.githubusercontent.com/59308544/207958153-fb2e2cde-a5a5-4534-aaf4-ad6c705c71d6.png)

We consider a parallel beam of sunlight along a direction vector L (see Figure 1) entering the earth’s atmosphere at point Pc. The incoming light from sun is considered to have a spectral intensity of I <sub>1</sub>(λ) These incoming light rays get scattered at different points inside the atmosphere with different intensities along different directions. We want to find the net scattered intensity that reaches the eyes of the observer at the viewpoint (P <sub>o</sub>). The ray of light reaching the viewpoint (P<sub>o</sub>) present along the direction vector V is the result of scattering of the incoming light at different points (P) on a line along the direction vector V. The line intersects the atmospheric boundary at points P<sub>a</sub> and P <sub>b</sub>. The points P <sub>b</sub> and P <sub>a</sub> are the first and last points of non-zero atmospheric density along V. The line segment P<sub>a</sub>P<sub>b</sub> is at an angle θ (scattering angle) from the incident beam of light.
