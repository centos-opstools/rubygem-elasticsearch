# Generated from elasticsearch-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name elasticsearch

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: Ruby integrations for Elasticsearch
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/elasticsearch/elasticsearch-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
Requires: rubygem(elasticsearch-api) = 2.0.2
Requires: rubygem(elasticsearch-transport) = 2.0.2
# the following BuildRequires are development dependencies
# BuildRequires: rubygem(elasticsearch-extensions)
# BuildRequires: rubygem(ansi)
# BuildRequires: rubygem(shoulda-context)
# BuildRequires: rubygem(mocha)
# BuildRequires: rubygem(turn)
# BuildRequires: rubygem(yard)
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(ci_reporter) >= 1.9
# BuildRequires: rubygem(ci_reporter) < 2
# BuildRequires: rubygem(minitest) >= 4.0
# BuildRequires: rubygem(minitest) < 5
# BuildRequires: rubygem(ruby-prof)
# BuildRequires: rubygem(require-prof)
# BuildRequires: rubygem(simplecov)
# BuildRequires: rubygem(simplecov-rcov)
# BuildRequires: rubygem(cane)
# BuildRequires: rubygem(test-unit) >= 2
# BuildRequires: rubygem(test-unit) < 3
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby integrations for Elasticsearch (client, API, etc.).


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/elasticsearch.gemspec
%{gem_instdir}/test

%changelog
* Thu Jun 29 2017 Rich Megginson <rmeggins@redhat.com> - 2.0.2-1
- Bump to version 2.0.2

* Fri Sep 16 2016 Rich Megginson <rmeggins@redhat.com> - 1.0.18-1
- Bump to version 1.0.18

* Mon Mar 23 2015 Steve Traylen  <steve.traylen@cern.ch> - 1.0.8-1
- New upstream

* Thu Aug 07 2014 Steve Traylen  <steve.traylen@cern.ch> - 1.0.4-2
- Use correct time stamp for src file.

* Thu Jul 03 2014 Steve Traylen  <steve.traylen@cern.ch> - 1.0.4-1
- Initial package
