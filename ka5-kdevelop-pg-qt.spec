%define		_state		stable
%define		qtver		5.5.1
%define		orgname		kdevelop-pg-qt

Summary:	The parser-generator from KDevplatform
Name:		ka5-kdevelop-pg-qt
Version:	2.2.2
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	https://download.kde.org/%{_state}/%{orgname}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	54e7c85ae921c8161dc8e5d8b39abf53
URL:		http://www.kdevelop.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	bison
BuildRequires:	cmake >= 2.8.0
BuildRequires:	flex
BuildRequires:	kf5-extra-cmake-modules >= 5.14.0
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdevelop-pg-qt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDevelop-PG-Qt is the parser-generator from KDevplatform. It is used
for some KDevelop-languagesupport-plugins (Ruby, PHP, Java...).

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdev-pg-qt
%{_includedir}/%{orgname}
%{_libdir}/cmake/KDevelop-PG-Qt
