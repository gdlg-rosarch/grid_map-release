# Script generated with Bloom
pkgdesc="ROS - ROS interface for the grid map library to manage two-dimensional grid maps with multiple data layers."
url='http://github.com/ethz-asl/grid_map'

pkgname='ros-kinetic-grid-map-ros'
pkgver='1.6.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-grid-map-core'
'ros-kinetic-grid-map-cv'
'ros-kinetic-grid-map-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-rosbag'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
)

depends=('ros-kinetic-cv-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-grid-map-core'
'ros-kinetic-grid-map-cv'
'ros-kinetic-grid-map-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-rosbag'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=grid_map_ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/grid_map_ros $srcdir/grid_map_ros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

