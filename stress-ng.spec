Summary:	Stress test a computer system in various ways
Name:		stress-ng
Version:	0.16.04
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://github.com/ColinIanKing/stress-ng/archive/refs/tags/V%{version}.tar.gz
# Source0-md5:	ee25a2cc526804fb305dc7b4c16a0b53
URL:		https://github.com/ColinIanKing/stress-ng/
BuildRequires:	apparmor-parser
BuildRequires:	apparmor-profiles
BuildRequires:	apparmor-profiles-abstractions
BuildRequires:	attr-devel
BuildRequires:	judy-devel
BuildRequires:	keyutils-devel
BuildRequires:	kmod-devel
BuildRequires:	libaio-devel
BuildRequires:	libapparmor-devel
BuildRequires:	libatomic
BuildRequires:	libbsd-devel
BuildRequires:	libcap-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libsctp-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stress test a computer system in various ways. It was designed to
exercise various physical subsystems of a computer as well as the
various operating system kernel interfaces.

%package -n bash-completion-%{name}
Summary:        Bash completion for stress-ng
Summary(pl.UTF-8):      Bashowe dopełnianie parametrów dla stress-ng
Group:          Applications/Shells
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion >= 2.0

%description -n bash-completion-%{name}
Bash completion for stress-ng.

%description -n bash-completion-%{name} -l pl.UTF-8
Bashowe dopełnianie parametrów dla stress-ng.

%prep
%setup -q

%build
export CFLAGS="%{rpmcppflags} %{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make} \
	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{bash_compdir}}

cp -a %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
cp -a bash-completion/%{name} $RPM_BUILD_ROOT%{bash_compdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md example-jobs
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/%{name}
