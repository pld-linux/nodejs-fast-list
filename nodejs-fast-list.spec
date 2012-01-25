%define		pkg	fast-list
Summary:	A fast linked list
Name:		nodejs-%{pkg}
Version:	1.0.2
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/fast-list
Source0:	http://registry.npmjs.org/fast-list/-/%{pkg}-%{version}.tgz
# Source0-md5:	a0b5d56e6d24aecf328f1d40069b532b
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast linked list. (good for queues, stacks, etc.)

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
