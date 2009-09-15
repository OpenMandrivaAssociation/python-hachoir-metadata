%define module_name hachoir-metadata

Summary:	Python library to read metadata file format for the hachoir framework
Name: 		python-%{module_name}
Version: 	1.2.1
Release: 	%mkrel 2
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://hachoir.org/wiki/hachoir-metadata
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
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%dir %{py_puresitedir}/hachoir_metadata
