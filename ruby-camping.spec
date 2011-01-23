Summary:	A tiny web framework
Summary(pl.UTF-8):	Mały szkielet aplikacji WWW
Name:		ruby-camping
Version:	1.5.180
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://code.whytheluckystiff.net/gems/camping-%{version}.gem
# Source0-md5:	2bc00721072aa11846e3d90a5e5f5383
URL:		http://code.whytheluckystiff.net/camping/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.3.1
Requires:	ruby-ActiveSupport
Requires:	ruby-markaby
Requires:	ruby-metaid
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camping is a tiny web framework, less than 4k, basically a Rails
microcosm.

%description -l pl.UTF-8
Camping to mały szkielet aplikacji WWW, mniejszy niż 4k, zasadniczo
okrojony Rails.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
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

#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc rdoc
%doc examples
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/camping*
#%{ruby_ridir}/*
