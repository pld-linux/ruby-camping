Summary:	A tiny web framework
Summary(pl):	Ma³y szkielet aplikacji WWW
Name:		ruby-camping
Version:	1.5
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/13596/camping-%{version}.tar.gz
# Source0-md5:	883ac455a6e214d8205e5834bf3f1baa
#Patch0:		%{name}-nogems.patch
URL:		http://code.whytheluckystiff.net/camping/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-markaby
Requires:	ruby-metaid
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camping is a tiny web framework, less than 4k, basically a Rails
microcosm.

%description -l pl
Camping to ma³y szkielet aplikacji WWW, mniejszy ni¿ 4k, zasadniczo
okrojony Rails.

%prep
%setup -q -n camping-%{version}
#%patch0 -p1
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
