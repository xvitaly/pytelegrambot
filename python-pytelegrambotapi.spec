%global appname pytelegrambotapi
%global richname pyTelegramBotAPI

%global appsum Python Telegram bot API
%global appdesc A simple, but extensible Python implementation for the Telegram Bot API

Name: python-%{appname}
Version: 3.2.0
Release: 2%{?dist}
Summary: %{appsum}

License: GPLv2+
URL: https://github.com/eternnoir/%{richname}
Source0: %{url}/archive/%{version}.tar.gz#/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python3-devel
BuildRequires: python2dist(requests)
BuildRequires: python3dist(requests)

%description
%{appdesc}.

%package -n python2-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python2-%{appname}}

%description -n python2-%{appname}
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{richname}-%{version}

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
* Wed Aug 23 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-2
- Small SPEC fixes.

* Tue Aug 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-1
- Initial SPEC release.
