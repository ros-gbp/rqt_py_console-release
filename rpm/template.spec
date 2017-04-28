Name:           ros-jade-rqt-py-console
Version:        0.4.8
Release:        0%{?dist}
Summary:        ROS rqt_py_console package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_py_console
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-jade-python-qt-binding >= 0.2.19
Requires:       ros-jade-qt-gui
Requires:       ros-jade-qt-gui-py-common
Requires:       ros-jade-rospy
Requires:       ros-jade-rqt-gui
Requires:       ros-jade-rqt-gui-py
BuildRequires:  ros-jade-catkin

%description
rqt_py_console is a Python GUI plugin providing an interactive Python console.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Apr 28 2017 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.8-0
- Autogenerated by Bloom

