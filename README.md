# Attractor-Reconstruction-Project

This is my project on attractor reconstruction under assistant professor Sagar Chakraborty of India Institute of Technology Kanpur(IITK) in second year summers.

#### DYNAMICAL SYSTEMS AND CHAOS:
Firstly, I watched videos of online introductory course on dynamical system and chaos taught by Dr. Steven Strogatz of cornell university and set of four video lectures by Dr. Sagar Chakraborty on fractals and chaos on youtube.<br />
The link to the course:<br />
[http://www.infocobuild.com/education/audio-video-courses/mechanical-engineering/mae5790-spring2014-cornell.html](http://www.infocobuild.com/education/audio-video-courses/mechanical-engineering/mae5790-spring2014-cornell.html)<br />

#### Attractor Reconstruction:
After completing the course, I started exploring attractor reconstruction field through research papers and books.<br />
I reffered following papers:<br />
- [Chakraborty Manuscript](https://drive.google.com/open?id=1C4Yup8NSlQg8SuizavjMRp-W5__X0GVs)
- [Book](https://drive.google.com/open?id=1rubummHqziZCrNupAHKgT7LG9IIfpkfy)
- [Paper](https://drive.google.com/open?id=1huP_Vur24XMdBVkPNf63hHDVzo7K06QU)<br />
Third paper in the above list involved a lot of advanced maths that was beyond my reach. This paper was helpful as I got introduced to some powerful theorems in dynamical systems.<br /> 

I reffered following books:<br />
- Non-linear dynamics and chaos by steven strogatz.<br />
- An exploration of dynamical systems and chaos by John Argyris and Maria Hasse.

#### Implementation:
The above mentioned material gave me a flavour of attractor reconstruction methods. 
I implemented following algorithms:<br />
I implemented all the algorithms for the time series of lorenz system and coding was done in python.<br />
1. Grassberger Procaccia algorithm: I used this algorithm to find correlation dimension of lorenz attractor from time series.<br />
Scholarpedia link of the algorithm :[http://www.scholarpedia.org/article/Grassberger-Procaccia_algorithm](http://www.scholarpedia.org/article/Grassberger-Procaccia_algorithm)<br />

2. Lyapunov Exponents: I implemented an algorithm to find all the lyapunov exponents from the differential equations of Lorenz system.<br />
Algorithm used: I used the algorithm given in the book **"An exploration of dynamical systems and chaos by John Argyris and Maria Hasse"** under the heading **"Numerical Calculations of Lyapunov Exponents"**.<br /><br />
3.False-Nearest neighbors: I used FNN to find the embedding dimension.<br />
Link of the paper:<br />
[https://drive.google.com/open?id=1q139DEhQJiqqTZjwDVxcX3I1N3wfGWIW](https://drive.google.com/open?id=1q139DEhQJiqqTZjwDVxcX3I1N3wfGWIW)<br />
To improve time complexity, I also implemented Kd-Trees)<br />
kd-Trees theory and implementation:<br />
[Kd-trees](https://drive.google.com/open?id=1swoFBs9I-Jpm6BHvV4Wn1T2QWGEqGB49)<br />



