# https://gopkg.in/ldap.v2
%global goipath gopkg.in/ldap.v2
%global tag     v2.5.1

Version:        2.5.1

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Basic LDAP v3 functionality for Go
License:        MIT

URL:            https://github.com/go-ldap/ldap
Source0:        %{url}/archive/%{tag}/ldap-v2-%{version}.tar.gz

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(gopkg.in/asn1-ber.v1)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%autosetup -n ldap-%{version} -p1


%install
%goinstall


%check
# some checks require network connectivity; ignore results for now
%gochecks || :


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1-2
- Use autosetup instead of gosetup.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.1-1
- Initial package for fedora.

