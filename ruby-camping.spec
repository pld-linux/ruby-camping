Summary:	A tiny web framework
Name:		ruby-camping
Version:	1.4.2
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/10577/camping-%{version}.tar.gz
# Source0-md5:	57afd02521457c51e0244eca7f8f8228
Patch0:		%{name}-nogems.patch
URL:		http://code.whytheluckystiff.net/camping/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-ActiveRecord >= 1.14.0
Requires:	ruby-markaby
Requires:	ruby-metaid
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camping is a tiny web framework, less than 4k, basically a Rails microcosm.

%prep
%setup -q -n camping-%{version}
%patch0 -p1
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

# rdoc crashes on _why's craaazy code.
#rdoc --op rdoc lib
#rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

#cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc rdoc
%doc examples
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/camping*
#%{ruby_ridir}/*
