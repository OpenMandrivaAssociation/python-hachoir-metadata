%define module_name hachoir-metadata

Summary:	Python library to read metadata file format for the hachoir framework

Name: 		python-%{module_name}
Version: 	1.3.3
Release: 	4
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group: 		Development/Python
URL: 		https://bitbucket.org/haypo/hachoir/wiki/Home
BuildArch:	noarch
Requires:	python-hachoir-core
Requires:	python-hachoir-parser
BuildRequires:  python-devel
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
%{py_puresitedir}/hachoir_metadata
%{py_puresitedir}/hachoir_metadata-%{version}-py%{py_ver}.egg-info
%{_bindir}/hachoir-metadata
%{_bindir}/hachoir-metadata-qt
%{_bindir}/hachoir-metadata-gtk


