%global debug_package %{nil}

Name:		python3-pynput
Version:	1.7.1
Release:	1
Summary:	Sends virtual input commands


License:	GPLv3
URL:		https://github.com/moses-palmer/pynput
Source0:	https://github.com/moses-palmer/pynput/archive/v%{version}.tar.gz

BuildRequires:	python3-devel
Requires:       python3-xlib
Requires:       python3-six

%description
This library allows you to control and monitor input devices.
Currently, mouse and keyboard input and monitoring are supported.

%prep
%setup -q -n pynput-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc README.rst docs
%license COPYING
%{python3_sitelib}/pynput
%{python3_sitelib}/pynput-%{version}-py?.?.egg-info

%changelog
* Sun Nov 22 2020 Robert Bost <rbost@redhat.com> 1.7.1-1
- Updating to 1.7.1

* Wed Oct 16 2019 Robert Bost <bostrt@gmail.com> 1.4.4-3
- Configured GitHub webhook

* Wed Oct 16 2019 Robert Bost <bostrt@gmail.com> 1.4.4-2
- Adding README (bostrt@gmail.com)

* Tue Oct 15 2019 Robert Bost <bostrt@gmail.com> 1.4.4-1
- removing unneeded files (bostrt@gmail.com)


