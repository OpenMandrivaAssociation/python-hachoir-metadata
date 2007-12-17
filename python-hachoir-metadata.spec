%define module_name hachoir-metadata

Summary:    Python library to read metadata file format for the hachoir framework
Name: 		python-%{module_name}
Version: 	1.0
Release: 	%mkrel 1
Source0: 	%{module_name}-%{version}.tar.bz2
License:	GPL
Group: 		Development/Python
Url: 		http://hachoir.org/wiki/hachoir-metadata
BuildArch:  noarch
Requires:   python-hachoir-core
Requires:   python-hachoir-parser
BuildRequires: python-devel
%description
hachoir-metadata is tool to extract metadata from multimedia files 
(sound, video, archives, etc).


%prep
%setup -q -n %{module_name}-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%dir %py_puresitedir/hachoir_metadata
