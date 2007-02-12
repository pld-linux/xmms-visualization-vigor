Summary:	XMMS visualization plugin which displays dancing Vigor
Summary(pl.UTF-8):   Wtyczka wizualizacji dla XMMS-a wyświetlająca tańczącego Vigora
Name:		xmms-visualization-vigor
Version:	0.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/vigor/xmms-vigor-%{version}.tar.gz
# Source0-md5:	a4ddb8bdfdffb32f7b060973f4318a85
URL:		http://vigor.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.4
Requires:	gtk+ >= 1.2.2
Requires:	xmms >= 1.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS visualization plugin which displays dancing Vigor.

%description -l pl.UTF-8
Wtyczka wizualizacji dla XMMS-a wyświetlająca tańczącego Vigora.

%prep
%setup -q -n xmms-vigor-%{version}

%build
cp -f /usr/share/automake/config.* .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_visualization_plugindir}

rm -f $RPM_BUILD_ROOT%{xmms_visualization_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{xmms_visualization_plugindir}/libvigor.so
%{_datadir}/xmms-vigor
