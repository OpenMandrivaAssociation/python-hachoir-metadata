%define module_name hachoir-metadata

Summary:	Python library to read metadata file format for the hachoir framework
Name: 		python-%{module_name}
Version: 	1.3.3
Release: 	3
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group: 		Development/Python
URL: 		http://bitbucket.org/haypo/hachoir/wiki/Home
BuildArch:	noarch
Requires:	python-hachoir-core
Requires:	python-hachoir-parser
%{py_requires -d}
BuildRequires:	python-setuptools

%description
hachoir-metadata is tool to extract metadata from multimedia files 
(sound, video, archives, etc).

%prep
%setup -q -n %{module_name}-%{version}

%build
python setup.py build 

%install
python setup.py install --root=%{buildroot} --disable-qt

%files
%doc AUTHORS COPYING README 
%{py_sitedir}/hachoir_metadata
%{py_sitedir}/hachoir_metadata-%{version}-py%{py_ver}.egg-info
%{_bindir}/hachoir-metadata
%{_bindir}/hachoir-metadata-qt
%{_bindir}/hachoir-metadata-gtk


%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1.3.3-2mdv2011.0
+ Revision: 594040
- rebuild

* Sun Sep 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-1mdv2011.0
+ Revision: 577761
- new version

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 1.3.2-1mdv2010.1
+ Revision: 500768
- new version, with missing file for the qt interface
- update to 1.3.1
- disable qt interface, as some files are missing from tarball

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2010.0
+ Revision: 442157
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 320022
- rebuild with python 2.6
- clean spec
- new release 1.2.1

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 242412
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Jérôme Soyer <saispo@mandriva.org> 1.0-1mdv2008.0
+ Revision: 52869
- New release 1.0

* Sun Jun 17 2007 Michael Scherer <misc@mandriva.org> 0.10.0-1mdv2008.0
+ Revision: 40534
- fix url and description

  + Jérôme Soyer <saispo@mandriva.org>
    - Import python-hachoir-metadata

