#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rake-compiler
Version  : 0.9.5
Release  : 6
URL      : https://rubygems.org/downloads/rake-compiler-0.9.5.gem
Source0  : https://rubygems.org/downloads/rake-compiler-0.9.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-rake-compiler-bin
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
= What is rake-compiler?
rake-compiler is first and foremost a productivity tool for Ruby developers.
It's goal is to make the busy developer's life easier by simplifying the building
and packaging of Ruby extensions by simplifying code and reducing duplication.

%package bin
Summary: bin components for the rubygem-rake-compiler package.
Group: Binaries

%description bin
bin components for the rubygem-rake-compiler package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rake-compiler-0.9.5
gem spec %{SOURCE0} -l --ruby > rubygem-rake-compiler.gemspec

%build
gem build rubygem-rake-compiler.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rake-compiler-0.9.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/rake-compiler-0.9.5
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rake-compiler-0.9.5.gem
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/History.txt
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/appveyor.yml
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/bin/rake-compiler
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/cucumber.yml
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/compile.feature
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/cross-compile.feature
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/cross-package-multi.feature
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/cross-package.feature
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/java-compile.feature
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/java-no-native-compile.feature
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/java-package.feature
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/package.feature
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/step_definitions/compilation.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/step_definitions/cross_compilation.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/step_definitions/execution.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/step_definitions/folders.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/step_definitions/gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/step_definitions/java_compilation.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/support/env.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/support/file_template_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/support/generator_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/features/support/platform_extension_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/lib/rake/baseextensiontask.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/lib/rake/extensioncompiler.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/lib/rake/extensiontask.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/lib/rake/javaextensiontask.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/spec/lib/rake/extensiontask_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/spec/lib/rake/javaextensiontask_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/spec/spec.opts
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/spec/support/capture_output_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/tasks/bin/cross-ruby.rake
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/tasks/bootstrap.rake
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/tasks/common.rake
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/tasks/cucumber.rake
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/tasks/gem.rake
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/tasks/news.rake
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/tasks/release.rake
/usr/lib64/ruby/gems/2.3.0/gems/rake-compiler-0.9.5/tasks/rspec.rake
/usr/lib64/ruby/gems/2.3.0/specifications/rake-compiler-0.9.5.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/rake-compiler
