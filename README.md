# Attractor-Reconstruction-Project

This is my project on attractor reconstruction under assistant professor Sagar Chakraborty of India Institute of Technology Kanpur(IITK) in second year summers.

#### DYNAMICAL SYSTEMS AND CHAOS:
Firstly, I watched videos of online introductory course on dynamical system and chaos taught by Dr. Steven Strogatz of cornell university and set of four video lectures by Dr. Sagar Chakraborty on fractals and chaos on youtube.<br />
The link to the course:<br />
[http://www.infocobuild.com/education/audio-video-courses/mechanical-engineering/mae5790-spring2014-cornell.html](http://www.infocobuild.com/education/audio-video-courses/mechanical-engineering/mae5790-spring2014-cornell.html)<br />

#### Attractor Reconstruction:
After completing the course, I started exploring attractor reconstruction field through research papers and books.<br />
I reffered following papers:<br />
- [http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/Chakraborty_manuscript.pdf](http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/Chakraborty_manuscript.pdf)
- [http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/2012_Cecconi_etal_AJP.pdf](http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/2012_Cecconi_etal_AJP.pdf)
- [http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/embedelogy.pdf](http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/embedelogy.pdf)<br />
Third paper in the above list involved a lot of advanced maths that was beyond my reach. This paper was helpful as I got introduced to some powerful theorems in dynamical systems.<br /> 

I reffered following books:<br />
- Non-linear dynamics and chaos by steven strogatz.<br />
- An exploration of dynamical systems and chaos by John Argyris and Maria Hasse.

#### Implementation:
The above mentioned material gave me a flavour of attractor reconstruction methods. 
I implemented following algorithms:<br />
I implemented all the algorithms for the time series of lorenz system and coding was done in python.<br />
1. Grassberger Procaccia algorithm: I used this algorithm to find correlation dimension of lorenz attractor from time series.<br />
Scholarpedia link of the algorithm :[http://www.scholarpedia.org/article/Grassberger-Procaccia_algorithm](http://www.scholarpedia.org/article/Grassberger-Procaccia_algorithm)
To increase the computation speed, I reffered the following paper:
[http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/1990_Grassberger_PLA.pdf](http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/1990_Grassberger_PLA.pdf)  
2. Lyapunov Exponents: I implemented an algorithm to find all the lyapunov exponents from the differential equations of Lorenz system.<br />
Algorithm used: I used the algorithm given in the book "An exploration of dynamical systems and chaos by John Argyris and Maria Hasse" under the heading "Numerical Calculations of Lyapunov Exponents".
3.False-Nearest neighbors: I used FNN to find the embedding dimension.<br />
Link of the paper:[http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/PhysRevA.45.3403.pdf](http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/PhysRevA.45.3403.pdf
To improve time complexity, I also implemented Kd-Trees)<br />
kd-Trees theory and implementation:[http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/assignment-3-kdtree.pdf](http://home.iitk.ac.in/~gsubham/Attractor_Reconstruction_Project/assignment-3-kdtree.pdf)<br />

Currently, I am working on phase space reconstruction of non-invertible maps(Unsolved Problem).



