# ROS Virtual: Setup Inicial

Install Singularity

Select the singularity install file corresponding to the Ubuntu distribution you are using (either 16.04 or 18.04)

- Singularity for <a href= "https://courses.edx.org/assets/courseware/v1/4beeefd3ac34401321609d7697f9097f/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/singularity-container_2.6.1-1_amd64_ubuntu_xenial16.04.deb">Ubuntu 16.04</a>

- Singularity for <a href = "https://courses.edx.org/assets/courseware/v1/626dbd92c8dd641c5657f8d9ec43ead2/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/singularity-container_2.6.1-1_amd64_ubuntu_bionic18.04.deb"> Ubuntu 18.04</a>

For Ubuntu 19.04 or newer, singularity can be installed directly from the repositories:
> $ sudo apt-get install singularity-container

***Disclaimer: Using singularity install files for 19.04 or newer is not recommended as the course instructors have not sufficiently tested this. So, any support on this will be minimal.***

You can't install all of them!

# Download the Singularity image

Download the course singularity image from this link: <a href= "https://surfdrive.surf.nl/files/index.php/s/pp59nr2PLr2QGNg/download"> hrwros-09.simg </a> (note: this file is approximately 1.1 GB, so the download may take a while).

# Verify the image downloaded successfully

Now verify that the Singularity image downloaded successfully by following these steps.

In a regular terminal (ctrl+alt+t), run:

> $ md5sum $HOME/Downloads/hrwros-09.simg

If the image is ok, you should see the following output:

         cbb042949c0a3b797804ad9606dbaac8  $HOME/Downloads/hrwros-09.simg

If you see a different code, downloading the image file was most likely not successful. Please try downloading the image file again using the link in the Download the Singularity image section above.

If you receive an error message, follow these steps:

    Is the file located in your $HOME/Downloads directory? No? Please move the file to $HOME/Downloads.
    Is the filename exactly hrwros-09.simg? No? Please rename the file to hrwros-09.simg.

Finally: retry validating the image download.

Download the course starter installation script

You will also need a course starter installation file, that will create some necessary infrastructure inside your Ubuntu install.

<a href="https://courses.edx.org/assets/courseware/v1/7d7f9ae82dfbbf2be2ce126022e63811/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/install-hrwros-starter.sh"> install-hrwros-starter.sh (~1.4 kB)</a>

# Download the file to your $USER/Downloads folder

startup a new terminal with Ctrl+Alt+T and run the command:
> $ bash $HOME/Downloads/install-hrwros-starter.sh

Installing new software inside the Course Command Shell (CCS)

This image is read-only! So, if you try to implement solutions after googling your problems with 'sudo apt-get install ...', inside the Course Command Shell, it will not work. All necessary installs for this course have already been considered. So, you will never have to run 'sudo apt-get install ...' yourself, except for when you install Singularity.

# Afterall

Run the following commands in the CCS terminal: 

```
source /opt/ros/melodic/setup.bash
cd $HOME/hrwros_ws
catkin build
source $HOME/hrwros_ws/devel/setup.bash
```

# Context 

Topics covered:

- Nodes
- Topics
- Publisher
- Subscriber
- Services
- Actions
- & Launch Files.

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/JoanPedro/ROS-Ambient-Setup.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/JoanPedro/ROS-Ambient-Setup/compare" target="_blank">`https://github.com/JoanPedro/ROS-Projects/compare`</a>.

---

## FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

---

## Support

Reach out to me at one of the following places!

- Linkedin at <a href="www.linkedin.com/in/joan-pedro" target="_blank">`www.linkedin.com/in/joan-pedro`</a>


---
