
Name:           grep
Version:        3.9
Release:        1%{?dist}
Summary:        <short_description>

License:        <license>
URL:            <upstream_url>
Source0:        tarballs/grep/grep-3.9.tar.xz

BuildArch:      x86_64

BuildRequires:  <build_time_dependencies>
Requires:       <runtime_dependencies>

%description
<full_description>

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%license COPYING
%doc README
%{_bindir}/<binary_name>
%{_libdir}/lib<library_name>.so
%{_includedir}/<header_files>
%{_mandir}/man1/<man_page>.1*

%changelog
* <date> Your Name <your.email@example.com> - 3.9-1
- Initial package
