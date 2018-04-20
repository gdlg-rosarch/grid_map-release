# Script generated with Bloom
pkgdesc="ROS - Meta-package for the universal grid map library."
url='http://github.com/ethz-asl/grid_map'

pkgname='ros-lunar-grid-map'
pkgver='1.6.0_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-grid-map-core'
'ros-lunar-grid-map-cv'
'ros-lunar-grid-map-demos'
'ros-lunar-grid-map-filters'
'ros-lunar-grid-map-loader'
'ros-lunar-grid-map-msgs'
'ros-lunar-grid-map-ros'
'ros-lunar-grid-map-rviz-plugin'
'ros-lunar-grid-map-visualization'
)

conflicts=()
replaces=()

_dir=grid_map
source=()
md5sums=()

prepare() {
    cp -R $startdir/grid_map $srcdir/grid_map
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

