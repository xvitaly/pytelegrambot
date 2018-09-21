%global appname pytelegrambotapi
%global richname pyTelegramBotAPI

%global appsum Python Telegram bot API
%global appdesc A simple, but extensible Python implementation for the Telegram Bot API

Name: python-%{appname}
Version: 3.6.6
Release: 1%{?dist}
Summary: %{appsum}

License: GPLv2+
URL: https://github.com/eternnoir/%{richname}
Source0: %{url}/archive/%{version}.tar.gz#/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python3-devel

BuildRequires: python2dist(requests)
BuildRequires: python3dist(requests)
BuildRequires: python2dist(wheel)
BuildRequires: python3dist(wheel)
BuildRequires: python2dist(six)
BuildRequires: python3dist(six)

%description
%{appdesc}.

%package -n python2-%{appname}
Summary: %{appsum}
Requires: python2dist(requests)
Requires: python2dist(six)
%{?python_provide:%python_provide python2-%{appname}}

%description -n python2-%{appname}
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
Requires: python3dist(requests)
Requires: python3dist(six)
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{richname}-%{version} -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{appname}
%license LICENSE
%doc README.rst README.md
%{python2_sitelib}/*

%files -n python3-%{appname}
%license LICENSE
%doc README.rst README.md
%{python3_sitelib}/*

%changelog
* Fri Sep 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.6-1
- Updated to version 3.6.6.

* Sat Aug 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.5-1
- Updated to version 3.6.5.

* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.4-1
- Updated to version 3.6.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.3-3
- Fixed build under Python 3.7.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-2
- Rebuilt for Python 3.7

* Tue May 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.3-1
- Updated to version 3.6.3.

* Sat Mar 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.2-1
- Updated to version 3.6.2.

* Mon Mar 12 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.1-1
- Updated to version 3.6.1.

* Fri Mar 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.0-1
- Updated to version 3.6.0.

* Sat Feb 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.2-1
- Updated to version 3.5.2.

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.1-1
- Updated to version 3.5.1.

* Wed Aug 23 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-2
- Small SPEC fixes.

* Tue Aug 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-1
- Initial SPEC release.
