Name:           ros-kinetic-grid-map-visualization
Version:        1.5.2
Release:        0%{?dist}
Summary:        ROS grid_map_visualization package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/ethz-asl/grid_map
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-grid-map-core
Requires:       ros-kinetic-grid-map-msgs
Requires:       ros-kinetic-grid-map-ros
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-grid-map-core
BuildRequires:  ros-kinetic-grid-map-msgs
BuildRequires:  ros-kinetic-grid-map-ros
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-visualization-msgs

%description
Configurable tool to visualize grid maps in RViz.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jul 25 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.2-0
- Autogenerated by Bloom

* Tue Jul 25 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.1-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.0-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.2-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.1-1
- Autogenerated by Bloom

* Sun Oct 23 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.1-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.0-0
- Autogenerated by Bloom

* Tue May 10 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.3.3-0
- Autogenerated by Bloom

* Tue May 10 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.3.1-1
- Autogenerated by Bloom

* Tue May 10 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.3.1-0
- Autogenerated by Bloom

