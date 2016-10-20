mkdir ~/bin
curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
PATH=${PATH}:~/bin

#Download the source code:
cd ..
mkdir yocto
cd yocto
repo init -u https://github.com/Freescale/fsl-community-bsp-platform -b krogoth
repo sync
source setup-environment imx6sx_sdb
cp ../../setup_yocto/linux-fslc-imx_4.1-1.0.x.bb ../sources/meta-fsl-arm/recipes-kernel/linux/linux-fslc-imx_4.1-1.0.x.bb
cp ../../../middleware/rpmsg-sysfs/rpmsg_sysfs_interface.patch ../sources/meta-fsl-arm/recipes-kernel/linux/linux-fslc-imx/rpmsg_sysfs_interface.patch
cp ../../setup_yocto/imx6sx/local.conf conf/local.conf

bitbake core-image-minimal-dev
