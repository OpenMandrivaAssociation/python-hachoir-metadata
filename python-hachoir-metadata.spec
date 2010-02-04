%define module_name hachoir-metadata

Summary:	Python library to read metadata file format for the hachoir framework
Name: 		python-%{module_name}
Version: 	1.3.2
Release: 	%mkrel 1
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES --disable-qt

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%dir %{py_puresitedir}/hachoir_metadata
%{py_puresitedir}/hachoir_metadata/qt/
