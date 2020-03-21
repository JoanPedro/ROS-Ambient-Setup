# BIR-Concepts: Setup Inicial
- Initial Concepts.

Install Singularity

Select the singularity install file corresponding to the Ubuntu distribution you are using (either 16.04 or 18.04)

    Singularity for <a href= "https://courses.edx.org/assets/courseware/v1/4beeefd3ac34401321609d7697f9097f/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/singularity-container_2.6.1-1_amd64_ubuntu_xenial16.04.deb">Ubuntu 16.04</a>

    Singularity for <a href="https://courses.edx.org/assets/courseware/v1/626dbd92c8dd641c5657f8d9ec43ead2/asset-v1:DelftX+ROS1x+1T2020+type@asset+block/singularity-container_2.6.1-1_amd64_ubuntu_bionic18.04.deb">Ubuntu 18.04</a>
    For Ubuntu 19.04 or newer, singularity can be installed directly from the repositories:

    > $ sudo apt-get install singularity-container

   Disclaimer: Using singularity install files for 19.04 or newer is not recommended as the course instructors have not sufficiently tested this. So, any support on this will be minimal.

You can't install all of them!
Download the Singularity image

Download the course singularity image from this link: <a href= "https://surfdrive.surf.nl/files/index.php/s/pp59nr2PLr2QGNg/download"> hrwros-09.simg </a> (note: this file is approximately 1.1 GB, so the download may take a while).

Warning: Some students have reported this file getting renamed during or after download. Please confirm this file is called hrwros-09.simg and is placed in your Downloads folder.
Verify the image downloaded successfully

Now verify that the Singularity image downloaded successfully by following these steps.

In a regular terminal (ctrl+alt+t), run:

$ md5sum $HOME/Downloads/hrwros-09.simg

If the image is ok, you should see the following output:

         cbb042949c0a3b797804ad9606dbaac8  $HOME/Downloads/hrwros-09.simg

If you see a different code, downloading the image file was most likely not successful. Please try downloading the image file again using the link in the Download the Singularity image section above.

If you receive an error message, follow these steps:

    Is the file located in your $HOME/Downloads directory? No? Please move the file to $HOME/Downloads.
    Is the filename exactly hrwros-09.simg? No? Please rename the file to hrwros-09.simg.

Finally: retry validating the image download.

Download the course starter installation script

You will also need a course starter installation file, that will create some necessary infrastructure inside your Ubuntu install.

install-hrwros-starter.sh (~1.4 kB)

Download the file to your $USER/Downloads folder, startup a new terminal with Ctrl+Alt+T and run the command:

$ bash $HOME/Downloads/install-hrwros-starter.sh
Installing new software inside the Course Command Shell (CCS)

This image is read-only! So, if you try to implement solutions after googling your problems with 'sudo apt-get install ...', inside the Course Command Shell, it will not work. All necessary installs for this course have already been considered. So, you will never have to run 'sudo apt-get install ...' yourself, except for when you install Singularity in the Course Setup (Week 0).

Weekly contents

You can download the files corresponding to each week from the Weekly contents page.

Each week contents, may also include new version of files/packages from previous weeks, Always overwrite with newer ones to avoid errors.

Any changes or additional files you made, should be backed up before replacing with the new ones.

When you download the contents for a week, some files that you might see in the instruction videos are already provided. So just open them and see their contents. It is not necessary to create files that are already given to you.
