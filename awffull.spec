Summary: Web server log analysis program
Name: awffull
Version: 3.10.2
Release: 3%{?dist}
License: GPL-2.0-or-later
URL: http://www.stedee.id.au/awffull
ExclusiveArch: x86_64 aarch64

%if 0%{?suse_version}
%global libpng_devel_pkg libpng16-devel
%global db_devel_pkg libdb-4_8-devel
%else
%global libpng_devel_pkg libpng-devel
%global db_devel_pkg db4-devel
%endif

# Upstream is abandoned; original site is dead; no surviving archive found
Source0: http://www.stedee.id.au/files/awffull-%{version}.tar.gz

BuildRequires: zlib-devel, %{libpng_devel_pkg}, %{db_devel_pkg}, gd-devel, pcre-devel

%description
AWFFull is a Web server log analysis program, forked from Webalizer. It
adds a number of new features and improvements, such as extended frontpage
history, resizable graphs, and a few more pie charts.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc ChangeLog INSTALL README TODO
%doc %{_mandir}/man1/awffull.1*
%doc %{_mandir}/man5/awffull.conf.5*
%{_bindir}/awffull

%changelog
* Sat Jul 05 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.10.2-3
- Multi-distro pass: guard libpng-devel/db4-devel via %%global for openSUSE/SLES
  (libpng16-devel, libdb-4_8-devel); zlib-devel, gd-devel, pcre-devel unchanged
  (same name across distros); pcre-devel left unguarded on SUSE since PCRE1
  is not packaged there and swapping to pcre2-devel would be an API change,
  not a naming guard

* Thu Jul 03 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.10.2-3
- Rename Source: to Source0:; add comment noting upstream is dead/no archive
- GPL-2.0-or-later SPDX; ExclusiveArch: x86_64 aarch64
- %%autosetup -p1; %%make_build; %%make_install; %%license

* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.10.2-3
- Modernize spec for AlmaLinux 10: remove BuildRoot, %%clean, %%defattr, Group tag

* Tue Oct 03 2017 Nux <rpm@li.nux.ro> - 3.10.2-2
- build for EL7

* Thu Jan  1 2009 Dries Verachtert <dries@ulyssis.org> - 3.10.2-1 - 7981/dag
- Updated to release 3.10.2.

* Wed Nov 26 2008 Dries Verachtert <dries@ulyssis.org> - 3.10.1-1
- Updated to release 3.10.1.

* Thu Nov 20 2008 Dries Verachtert <dries@ulyssis.org> - 3.9.1-1
- Updated to release 3.9.1.

* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 3.8.2-1
- Updated to release 3.8.2.

* Tue May 08 2007 Dries Verachtert <dries@ulyssis.org> - 3.7.4-1
- Updated to release 3.7.4.

* Tue Jan 23 2007 Dries Verachtert <dries@ulyssis.org> - 3.7.2-1
- Updated to release 3.7.2.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.7.1-1
- Updated to release 3.7.1.

* Sun Jun 04 2006 Dries Verachtert <dries@ulyssis.org> - 3.4.3-1
- Updated to release 3.4.3.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 3.4.1-1
- Updated to release 3.4.1.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.3.1-1
- Updated to release 3.3.1.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 3.02-1
- Updated to release 3.02.

* Tue Dec 13 2005 Dries Verachtert <dries@ulyssis.org> - 3.01-1
- Initial package.
