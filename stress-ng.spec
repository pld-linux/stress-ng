Summary:	Stress test a computer system in various ways
Name:		stress-ng
Version:	0.11.17
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://kernel.ubuntu.com/~cking/tarballs/stress-ng/%{name}-%{version}.tar.xz
# Source0-md5:	7b89157c838f2bb4bdeba8f46e3c56ae
URL:		https://kernel.ubuntu.com/~cking/stress-ng/
BuildRequires:	attr-devel
BuildRequires:	judy-devel
BuildRequires:	keyutils-devel
BuildRequires:	libaio-devel
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

%prep
%setup -q

%build
export CFLAGS="%{rpmcppflags} %{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make}

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
%doc README example-jobs
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
