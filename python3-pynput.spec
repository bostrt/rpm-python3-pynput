%global debug_package %{nil}

Name:		python3-pynput
Version:	1.4.4
Release:	0%{?dist}
Summary:	Sends virtual input commands


License:	GPLv3
URL:		https://github.com/moses-palmer/pynput
Source0:	https://github.com/moses-palmer/pynput/archive/v%{version}.tar.gz

BuildRequires:	python3
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

