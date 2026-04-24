Summary: Web server log analysis program
Name: awffull
Version: 3.10.2
Release: 3%{?dist}
License: GPL
URL: http://www.stedee.id.au/awffull

Source: http://www.stedee.id.au/files/awffull-%{version}.tar.gz

BuildRequires: zlib-devel, libpng-devel, db4-devel, gd-devel, pcre-devel

%description
AWFFull is a Web server log analysis program, forked from Webalizer. It
adds a number of new features and improvements, such as extended frontpage
history, resizable graphs, and a few more pie charts.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall
%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/awffull.1*
%doc %{_mandir}/man5/awffull.conf.5*
%{_bindir}/awffull

%changelog
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
